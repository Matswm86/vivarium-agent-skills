# vivarium-agent-skills

An [Agent Skill](https://code.claude.com/docs/en/skills) for building and stocking closed glass habitats — paludariums, vivariums, terrariums, and aquariums — and keeping the plants and animals inside them alive.

## Install

```bash
# as a skill
npx skills add <owner>/vivarium-agent-skills

# or as a Claude Code plugin
claude plugin marketplace add <owner>/vivarium-agent-skills
```

## What is in it

One skill, `vivarium-expert`, backed by 52 single-topic reference files across nine categories:

| Prefix | Covers |
|---|---|
| `safety-` | Floor loading, glass failure modes, UVB injury |
| `glass-` | Thickness calculation, silicone, bracing, seams, drilling |
| `climate-` | Heat loss, heater selection, humidity, ventilation, condensation |
| `light-` | PPFD/DLI, PAR falloff, UVB delivery, photoperiod |
| `water-` | Pump head, filtration, intake guards, algae trajectory |
| `fauna-` | Species data, mixed-species compatibility, stocking |
| `flora-` | Plant selection, dormancy traps, invasive growth, biogeography |
| `bioactive-` | Clean-up crew, seeding density, leaf litter |
| `build-` | Backgrounds, wood, rock, composition, maturation |

## Sourcing rules

1. **Every load-bearing number carries a URL.** A number without a source is a guess.
2. **The author's own arithmetic is labelled `(my calc)`** and never placed beside a citation as though the source produced it.
3. **Genuine gaps are written `UNVERIFIED`** rather than filled with plausible invention.
4. **When sources conflict, both are shown and the conflict is named.**
5. **No jurisdiction-specific law.** Rules on keeping, importing, and trading animals vary by country and change; this skill covers physics, biology, and construction only.

## Some things it corrects

- Inverse-square is the wrong falloff model for vivarium lighting — the measured exponent for an LED bar is ~1.2, not 2.0.
- The "10-15 air changes per hour" figure circulating for vivaria is an NIH laboratory rodent-room standard.
- The vinegar drop test does not reliably detect carbonate rock.
- "Neutral-cure silicone is the safe one" is backwards for structural glass seams.
- Not all *Geosesarma* are direct developers — *G. hednon* has planktotrophic larvae.

## Contributing

See [`skills/vivarium-expert/references/_contributing.md`](skills/vivarium-expert/references/_contributing.md). One rule per file, under ~2 KB, sourced.

## Licence

MIT. See [LICENSE](LICENSE).
