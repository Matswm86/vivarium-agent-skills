---
title: Size Aquarium Glass by the Wisner Plate Method, With B = 5.05 N/mm2
impact: CRITICAL
impactDescription: Gets pane thickness right to within one stock size; the alternative is guessing
tags: glass, structural, calculation, aquarium, paludarium
---

## Size glass by the plate method

Panes holding water are flat rectangular plates, simply supported on four edges, under a triangular (hydrostatic) pressure. The hobby-standard closed form behind every aquarium glass calculator:

```
t = sqrt( beta * H^3 * 1e-5 / B )            thickness, mm
d = ( alpha * p * 1e-6 * H^4 ) / ( E * t^3 ) mid-span deflection, mm

H = water height (mm)      p = 10 * H (N/m2)      E = 69000 N/mm2
B = allowable bending stress = 19.2 / 3.8 = 5.05 N/mm2
alpha, beta = plate coefficients from L/H (see below)
```

**Plate coefficients by L/H** (pane horizontal span / water height):

| L/H | alpha side | beta side | alpha bottom | beta bottom |
|---|---|---|---|---|
| 0.5 | 0.0030 | 0.0850 | — | — |
| 0.666 | 0.0085 | 0.1156 | — | — |
| 1.0 | 0.0220 | 0.1600 | 0.0770 | 0.4530 |
| 1.5 | 0.0420 | 0.2600 | 0.0906 | 0.5172 |
| 2.0 | 0.0560 | 0.3200 | 0.1017 | 0.5688 |
| 2.5 | 0.0630 | 0.3500 | 0.1110 | 0.6102 |
| >= 3.0 | 0.0670 | 0.3700 | 0.1335 | 0.7134 |

**Why B is so low:** 19.2 N/mm2 is the modulus of rupture convention for annealed float; the 3.8 safety factor divides it down. Cross-checked against EN 572-1 / EN 16612, which give annealed float a characteristic bending strength of 45 MPa reduced to roughly 8 MPa for permanent loads. The hobby's 5.05 sits **below** the Eurocode permanent-load design value, so the method is conservative — correctly, because water load is permanent and annealed glass suffers static fatigue (subcritical crack growth) under sustained stress.

**Verify:** Reproduce the published worked example. A 3000 x 950 x 900 mm tank, beta = 0.37, B = 5.05: `t = sqrt(0.37 * 950^3 * 1e-5 / 5.05) = 25.06 mm`, deflection `0.067 * 9500 * 1e-6 * 950^4 / (69000 * 25.06^3) = 0.48 mm`. Both match the published values (my calc, formula verified). If your implementation does not reproduce these, it is wrong.

**Sources:**
- https://www.monsterfishkeepers.com/forums/threads/how-to-calculate-the-glass-thickness-for-your-aquarium.50760/ — formula, coefficients, 19.2 MPa and SF 3.8
- https://www.omnicalculator.com/other/aquarium-glass-thickness — same convention
- https://structville.com/design-of-glass-structures and https://www.saint-gobain-glass.co.uk/document/the-strength-of-glass/ — EN characteristic strength 45 MPa, permanent-load reduction
- https://reefcalcs.com/calculators/aquarium-glass-thickness/ — tempered ~4x annealed (~77.2 N/mm2)
