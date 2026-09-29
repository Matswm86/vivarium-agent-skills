# vivarium-agent-skills

A sourced reference pack for building and stocking closed glass habitats, paludariums,
vivariums, terrariums and aquariums, and for keeping the plants and animals inside them
alive.

It is written as an [Agent Skill](https://code.claude.com/docs/en/skills), but there is
nothing model-specific in it. The content is 56 plain Markdown files plus one router
document. Any assistant that can read files can use it: Claude, Qwen, GPT, Gemini, a
local Llama or Mistral through Ollama, or your own harness. Nothing here calls an API,
imports an SDK, or assumes a particular tool surface.

## Using it

**Any agent that reads a folder.** Point it at `skills/vivarium-expert/`. Start with
`SKILL.md`, which is the router: it carries the sourcing rules and a category map telling
the agent which of the 56 reference files answers which kind of question. The agent reads
only the files it needs.

**Cursor, Continue, opencode, Aider, Cline, or any editor agent.** Drop the folder into
the project and add `skills/vivarium-expert/SKILL.md` to the context.

**A chat model with no file access.** Paste `SKILL.md` as the system prompt and paste the
one or two reference files the question touches. Each file is 1 to 8 KB and self-contained
on purpose, so this stays practical.

**Claude Code**, where the skill format comes from, loads it directly:

```bash
npx skills add Matswm86/vivarium-agent-skills
# or as a plugin
claude plugin marketplace add Matswm86/vivarium-agent-skills
```

**Your own harness.** `SKILL.md` frontmatter carries a `description` written as a trigger
list, so a router can match a user question against it without an LLM call. The body is
ordinary Markdown.

## What is in it

One skill, `vivarium-expert`, backed by 56 single-topic reference files across nine
categories:

| Prefix | Covers |
|---|---|
| `safety-` | Floor loading, glass failure modes, tempered glass and drilling, UVB injury |
| `glass-` | Thickness calculation, silicone, bracing, seams |
| `climate-` | Heat loss, heater selection, humidity, ventilation, condensation |
| `light-` | PPFD/DLI, PAR falloff, UVB delivery, photoperiod |
| `water-` | Pump head, filtration, intake guards, algae trajectory |
| `fauna-` | Species data, mixed-species compatibility, stocking |
| `flora-` | Plant selection, dormancy traps, invasive growth, biogeography |
| `bioactive-` | Clean-up crew, seeding density, leaf litter and sterilisation, predatory mites |
| `build-` | Backgrounds, wood, rock, composition, maturation |

## Sourcing rules

1. **Every number you would build or stock from carries a URL.** A number without a source
   is a guess, and guesses kill animals and crack glass.
2. **The author's own arithmetic is labelled `(my calc)`** and is never placed beside a
   citation as though the source produced it.
3. **Genuine gaps are written `UNVERIFIED`** rather than filled with plausible invention.
4. **When sources conflict, both are shown and the conflict is named.**
5. **No jurisdiction-specific law.** Rules on keeping, importing and trading animals vary
   by country and change; this pack covers physics, biology and construction only.

## Some things it corrects

- Inverse-square is the wrong falloff model for vivarium lighting: the measured exponent
  for an LED bar is about 1.2, not 2.0.
- The "10 to 15 air changes per hour" figure circulating for vivaria is an NIH laboratory
  rodent-room standard.
- The vinegar drop test does not reliably detect carbonate rock.
- "Neutral-cure silicone is the safe one" is backwards for structural glass seams.
- Not all *Geosesarma* are direct developers: *G. hednon* has planktotrophic larvae.

## Contributing

See [`skills/vivarium-expert/references/_contributing.md`](skills/vivarium-expert/references/_contributing.md).
One rule per file, under about 2 KB, sourced. `test/sanity.py` checks frontmatter,
filename prefixes, cross-links, sourcing discipline and scope; it is plain Python with no
dependencies, so it runs anywhere.

## Licence

MIT. See [LICENSE](LICENSE).
