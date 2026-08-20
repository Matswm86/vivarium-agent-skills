#!/usr/bin/env python3
"""Sanity checks for the vivarium-expert skill. Run: python3 test/sanity.py"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "vivarium-expert"
REFS = SKILL_DIR / "references"
VALID_PREFIXES = {
    "safety", "glass", "climate", "light",
    "water", "fauna", "flora", "bioactive", "build",
}
VALID_IMPACT = {"CRITICAL", "HIGH", "MEDIUM", "LOW"}
failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def frontmatter(path: Path) -> dict[str, str]:
    """Parse the flat top-level keys of a --- delimited YAML block."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path.name}: no frontmatter block")
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if line.startswith((" ", "\t")) or ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"')
    return fields


def check_marketplace() -> None:
    path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"marketplace.json unreadable: {exc}")
        return
    for key in ("name", "owner", "metadata", "plugins"):
        if key not in data:
            fail(f"marketplace.json: missing '{key}'")
    for plugin in data.get("plugins", []):
        for rel in plugin.get("skills", []):
            if not (ROOT / rel).is_dir():
                fail(f"marketplace.json: skills path '{rel}' does not exist")


def check_skill_md() -> None:
    path = SKILL_DIR / "SKILL.md"
    if not path.is_file():
        fail("SKILL.md missing")
        return
    fields = frontmatter(path)
    if fields.get("name") != "vivarium-expert":
        fail(f"SKILL.md: name is {fields.get('name')!r}, expected 'vivarium-expert'")
    if len(fields.get("description", "")) < 200:
        fail("SKILL.md: description too short to route reliably")
    if fields.get("license") != "MIT":
        fail("SKILL.md: license must be MIT for a public skill")
    size = path.stat().st_size
    if size > 16_000:
        fail(f"SKILL.md is {size} bytes; keep the router under 16 KB")


def check_references() -> None:
    rules = [p for p in sorted(REFS.glob("*.md")) if not p.name.startswith("_")]
    if len(rules) < 20:
        fail(f"only {len(rules)} rule files found")
    for path in rules:
        fields = frontmatter(path)
        prefix = path.name.split("-", 1)[0]
        if prefix not in VALID_PREFIXES:
            fail(f"{path.name}: prefix '{prefix}' not in _sections.md")
        for key in ("title", "impact", "impactDescription", "tags"):
            if not fields.get(key):
                fail(f"{path.name}: missing frontmatter '{key}'")
        impact = fields.get("impact", "")
        if impact and impact not in VALID_IMPACT:
            fail(f"{path.name}: impact '{impact}' not one of {sorted(VALID_IMPACT)}")
        size = path.stat().st_size
        if size > 8_000:
            fail(f"{path.name} is {size} bytes; split it")


def check_cross_links() -> None:
    """Every references/<file>.md mentioned anywhere must exist."""
    names = {p.name for p in REFS.glob("*.md")}
    pattern = re.compile(r"`?(?:references/)?(_?[a-z0-9-]+\.md)`?")
    for path in [SKILL_DIR / "SKILL.md", *REFS.glob("*.md")]:
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            if target.startswith("_") or target in {"README.md", "LICENSE.md"}:
                continue
            if target not in names:
                fail(f"{path.name}: dangling reference to '{target}'")


def check_sourcing_discipline() -> None:
    """Every rule file must cite a URL or explicitly declare it has none."""
    for path in REFS.glob("*.md"):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        if "http" not in text and "unverified" not in text.lower():
            fail(f"{path.name}: no source URL and no UNVERIFIED declaration")


def check_no_legal_scope() -> None:
    banned = re.compile(r"\b(?:CITES permit|import permit|is illegal to keep|banned in)\b", re.I)
    for path in REFS.glob("*.md"):
        if banned.search(path.read_text(encoding="utf-8")):
            fail(f"{path.name}: jurisdiction-specific legal claim; out of scope")


for check in (
    check_marketplace,
    check_skill_md,
    check_references,
    check_cross_links,
    check_sourcing_discipline,
    check_no_legal_scope,
):
    check()

rule_count = len([p for p in REFS.glob("*.md") if not p.name.startswith("_")])
if failures:
    print(f"FAIL ({len(failures)} problems, {rule_count} rule files)")
    for line in failures:
        print(f"  - {line}")
    sys.exit(1)
print(f"PASS - {rule_count} rule files, all frontmatter valid, all links resolve")
