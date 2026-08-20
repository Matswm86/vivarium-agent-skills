---
title: Orchid Light Figures Disagree 2-3x — Design to the Under-Lights Band
impact: MEDIUM
impactDescription: Greenhouse footcandle maxima over-light a vivarium by 2-3x and scorch the plants
tags: light, orchids, PPFD, conversion
---

## Greenhouse numbers do not transfer to a glass box

American Orchid Society footcandle maxima, converted (my calc, bracketed with the sunlight x0.200 and cool-white-fluorescent x0.146 factors):

| Genus | AOS max (fc) | PPFD @x0.200 | PPFD @x0.146 |
|---|---|---|---|
| Phalaenopsis, Paphiopedilum | 1,500 | 300 | 219 |
| Miltoniopsis, Zygopetalum | 2,500 | 500 | 365 |
| Cattleya | 3,000 | 600 | 438 |
| Dendrobium, Oncidium, Cymbidium | 5,000 | 1,000 | 730 |

**The caveat that matters:** those figures were developed for sunlit greenhouses under shade cloth. AOS's own growing-under-lights material and secondary sources give a much lower band — Phalaenopsis tolerates down to ~46 umol/m2/s, Dendrobium performs well at ~300.

**The literature genuinely disagrees by 2-3x here. For a vivarium, design to the lower under-lights band.**

**Footcandle conversion factors** (needed because orchid literature is still in footcandles):

| Source | fc -> PPFD | PPFD -> fc |
|---|---|---|
| Sunlight | 0.200 | 5.01 |
| Cool white fluorescent | 0.146 | 6.87 |
| Metal halide | 0.152 | 6.60 |
| HPS | 0.131 | 7.62 |

**No conversion factor exists for white LED.** LED spectra vary too widely. Do not convert LED lux to PPFD — measure with a PAR meter. UNVERIFIED and unfixable by arithmetic.

A comparable order-of-magnitude disagreement exists for succulents: one source gives 75-150 PPFD, another 250-1000 at 12-14 h (DLI 8-20). Unresolved.

**Sources:**
- https://www.aos.org/orchid-care/principles-of-light
- https://www.apogeeinstruments.com/conversion-ppfd-to-foot-candles/
- https://askgardening.com/succulent-light-needs/ — the succulent disagreement
