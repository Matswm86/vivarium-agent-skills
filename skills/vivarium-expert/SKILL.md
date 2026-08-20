---
name: vivarium-expert
description: "Use when designing, building, stocking, or troubleshooting any closed glass habitat and the living things in it. Triggers: paludarium, vivarium, terrarium, aquarium, riparium, bioactive enclosure; DIY tank construction (glass thickness, silicone, bracing, euro-brace, bulkheads, stands, floor loading); backgrounds and hardscape (PU foam, epoxy, cork, driftwood, rock, drainage layer, false bottom, substrate); climate control (heating, insulation, condensation, humidity, misting, fogging, ventilation, air exchange); lighting (PPFD, PAR, DLI, photoperiod, UVB, Ferguson zones, LED vs T5); water systems (waterfall, dripwall, pump head, filtration, turnover, cycling, RO, water parameters, pH, GH, KH, TDS); plants (species selection, dormancy, melt, invasive growth, biogeography, mounting); animals (dart frogs, tree frogs, geckos, bearded dragons, vampire crabs/Geosesarma, shrimp, nano fish, snails, isopods, springtails, clean-up crew) and mixed-species compatibility, stocking density, and quarantine. Also use for 'is X safe for my tank', 'will X eat Y', 'how thick should the glass be', 'why is my glass fogging', 'why won't plants grow at the bottom', and 'how many isopods do I need'."
license: MIT
metadata:
  author: mwm-ai
  version: "0.1.0"
  date: August 2026
  abstract: Sourced engineering, husbandry, and design reference for closed glass habitats. Covers structural glass, climate, lighting, water systems, plants, animals, and bioactive substrate biology across 52 single-topic rule files. Every load-bearing number carries a URL; the author's own arithmetic is labelled "(my calc)"; genuine gaps are written UNVERIFIED rather than filled with plausible invention. Includes explicit corrections to several widely repeated hobby claims that are wrong.
---

# Vivarium Expert

Sourced reference for building and stocking closed glass habitats — paludariums, vivariums, terrariums, and aquariums — and for keeping the plants and animals inside them alive.

## Core principles

**1. A number without a source is a guess. Say which one you are giving.**
This skill's reference files label every load-bearing figure with a URL, mark the author's own arithmetic `(my calc)`, and write `UNVERIFIED` where no source was found. Preserve that distinction when you answer. Never present a remembered figure as a sourced one.

**2. When sources conflict, show both and name the conflict.**
Several genuine disagreements exist in this literature — orchid PPFD (2-3x), succulent PPFD (an order of magnitude), whether silicone mildewcide leaches, whether boiling driftwood helps or harms, isopod seeding density (5x). Do not silently pick a winner.

**3. Check the failure before the feature.**
The four things that actually destroy builds, in order: the floor gives way, the glass fails, the animals cook or freeze, the sealant was not cured. Work down that list before discussing aesthetics.

**4. Compatibility questions need a source or a trial, never a vibe.**
"Will X eat Y" is the single most common question and the one most often answered from folklore. If no source exists, say so and propose a supervised trial with an escape plan — do not manufacture a confident verdict. See `references/fauna-geosesarma-compatibility.md` for how a precautionary guess was overturned by one real 10-month trial.

**5. Physics and biology only — no jurisdiction-specific law.**
Rules on keeping, importing, or trading animals vary by country and change often. This skill does not cover them. Point the reader at their national authority.

## The four failure classes, in order

| Priority | Category | Prefix | Why it is first |
|---|---|---|---|
| 1 | Life and animal safety | `safety-` | Floor loading, glass failure, UVB injury, escape |
| 2 | Glass engineering | `glass-` | Thickness, silicone, bracing, seams, drilling |
| 3 | Climate | `climate-` | Heat loss, heater type, humidity, ventilation, condensation |
| 4 | Lighting | `light-` | PPFD/DLI, PAR falloff, UVB delivery, photoperiod |
| 5 | Water systems | `water-` | Pump head, filtration, intake guards, algae |
| 6 | Animals | `fauna-` | Species data, compatibility, stocking |
| 7 | Plants | `flora-` | Selection, dormancy traps, invasive growth, biogeography |
| 8 | Bioactive substrate | `bioactive-` | Clean-up crew, seeding density, leaf litter |
| 9 | Hardscape and composition | `build-` | Backgrounds, wood, rock, layout, maturation |

## How to use

Read the individual rule files. Each is one topic, ~1-2 KB, so several load cheaply:

```
references/_sections.md                          category map and impact levels
references/safety-floor-loading.md
references/glass-paludarium-cantilever-bound.md
references/fauna-geosesarma-compatibility.md
```

Each rule file contains: the failure it prevents, wrong-versus-right, the mechanism with numbers, a verification the reader can actually run, sources with URLs, and an explicit `Unverified` section where applicable.

## Corrections this skill makes to common hobby advice

These are the claims most often repeated and wrong. Each has its own file.

- **"Neutral-cure silicone is the animal-safe one."** Backwards for structural glass seams — acetoxy is both the stronger glass bond and the aquarium standard. The hazard is fungicide additives in sanitary grades, not the cure chemistry. -> `glass-silicone-chemistry.md`
- **"The mildewcide killed my fish."** Almost certainly the uncured sealant did. Every cure protocol is really one rule: full cure before water and animals. -> `build-what-actually-kills-livestock-is-uncured.md`
- **"Light falls off as inverse-square."** An LED bar at vivarium distances falls off at d^-1.2, not d^-2 — a factor-of-hundreds difference at 1.5 m, and the reason tall enclosures are lightable at all. -> `light-inverse-square-is-wrong.md`
- **"Vivariums need 10-15 air changes per hour."** That is the NIH laboratory rodent-room standard. Applied to a high-humidity paludarium it would evaporate ~7 L/day into the room. -> `climate-ventilation-no-sizing-rule-exists.md`
- **"The vinegar drop test tells you if a rock is inert."** Vinegar is too weak to fizz on carbonate from a drop. Immerse overnight, retest with dilute HCl, then soak in RO water for 2-4 weeks and measure KH. -> `build-rock-carbonate-test.md`
- **"Dragon stone raises hardness."** Ohko is an argillaceous clay rock, classified inert by three independent sources. -> `build-rock-carbonate-test.md`
- **"All Geosesarma breed in freshwater."** *G. hednon* has planktotrophic larvae. Larval mode is species-specific. -> `fauna-geosesarma-larval-mode-is-species-specific.md`
- **"Vampire crabs will eat your shrimp."** A 10-month trial with 50+ crabs and 2 adult cherry shrimp ended with both shrimp alive and full-grown. Adults survive; juveniles get cropped; slow fish do not. -> `fauna-geosesarma-compatibility.md`
- **"Boil driftwood before use."** One detailed source argues boiling softens the wood and shortens its life. Long weighted soak plus mechanical anchoring is the low-risk path. -> `build-wood-selection-and-prep.md`
- **"Some PU foams contain fungicide."** No manufacturer TDS declares one. The documented biocide issue is in silicones. -> `build-what-actually-kills-livestock-is-uncured.md`
- **"Cluttered means too many plants."** Dutch-style tanks are 80%+ covered and read as lush. Clutter is missing dominance hierarchy. -> `build-composition-hierarchy.md`

## Known gaps in the literature

State these as gaps rather than filling them:

- **No published vent-area sizing rule for vivaria exists.** Not cm2 per litre, not percent of footprint. The only numeric rule found anywhere is a 2/3-glass, 1/3-screen lid, derived in a humid US climate.
- **No controlled photometric study of vivarium lid PAR transmission.** All lid-loss figures are hobbyist measurements with uncalibrated meters.
- **No tropical-plant VPD table.** Every published VPD target is cannabis-specific.
- **No paludarium-specific bioload or stocking-density guidance** for any footprint.
- **No reptile-specific plant-toxicity database was reachable.** All available ratings are a mammalian (ASPCA dog/cat/horse) proxy.
- **No dose-response data for UVB in amphibians.** The Ferguson zone framework covers lizards and snakes; the dart-frog assignment is keeper extrapolation.
- **No account of Geosesarma predating frogs, in either direction.**

## References

- https://www.jzar.org/jzar/article/view/150 — Baines et al. 2016, the UV-Tool
- https://onlinelibrary.wiley.com/doi/10.1002/zoo.21806 — Baines et al. 2023, UVB-LED spectral risks
- http://www.uvguide.co.uk/fluorescenttubemeshtests.htm — mesh and reflector UVB transmission
- https://www.arcadiareptile.com/jungledawn-ledbar/ — the only vivarium brand publishing measured PAR
- https://www.apogeeinstruments.com/conversion-ppfd-to-foot-candles/ — DLI formula, footcandle conversions
- https://aquariumscience.org/ — silicone, rock buffering, wood, water mould
- https://www.seriouslyfish.com/ — fish species parameters
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6614171/ — Shy & Ng 2019, Geosesarma larval development
