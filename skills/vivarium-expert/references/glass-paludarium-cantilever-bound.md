---
title: A Tall Paludarium Pane Has No Waterline Brace — Use the Cantilever Bound
impact: CRITICAL
impactDescription: beta 0.37 silently assumes a top support the pane does not have; SF drops from 5.2 to 1.9
tags: glass, structural, paludarium, bracing
---

## The beta = 0.37 coefficient assumes a support you may not have

This is the single most dangerous silent assumption in aquarium glass sizing, and it bites paludariums specifically.

**Wrong:**

```
1500 x 1600 mm front pane, 400 mm water, L/H = 3.75 -> beta = 0.37
t = sqrt(0.37 * 400^3 * 1e-5 / 5.05) = 6.85 mm -> "8 mm is plenty"
```

**Right:**

```
No brace within 1200 mm of the waterline -> the pane is a propped-free
cantilever, beta = 1.0
t = sqrt(1.0 * 400^3 * 1e-5 / 5.05) = 11.26 mm -> 12 mm stock
```

**Why:** Back-analysis of the coefficient table (my calc): a simply-supported vertical strip under triangular load gives beta = 0.193; a **propped cantilever** — base rotationally restrained by the silicone joint, top edge propped by a brace — gives beta = 0.40. The table's saturated 0.37 matches the propped case, not pin-pin. In a normal aquarium that prop is the rim or euro-brace, which sits at the waterline. **In a paludarium the brace is at the top of the enclosure, a metre or more above the water.** The water column has nothing propping it.

Front pane, 1500 mm wide, at 400 mm water (my calc):

| t | sigma Case S | SF | sigma Case C (beta=1.0) | SF Case C |
|---|---|---|---|---|
| 8 mm | 3.70 MPa | 5.2 | 10.00 MPa | **1.9 — reject** |
| 10 mm | 2.37 MPa | 8.1 | 6.40 MPa | 3.0 |
| 12 mm | 1.64 MPa | 11.7 | 4.44 MPa | **4.3 — accept** |

**The structurally honest fix for a deep water column in a tall enclosure:** do not build it as one tall box. Build the water section as a braced sub-tank with a bonded glass ledge at roughly the waterline. That restores Case S and lets 10 mm work at SF 8.1.

**Verify:** Measure the vertical distance from your waterline to the nearest horizontal brace. If it exceeds roughly the water depth itself, you are in Case C. Size for beta = 1.0.

**Sources:**
- https://www.monsterfishkeepers.com/forums/threads/how-to-calculate-the-glass-thickness-for-your-aquarium.50760/ — the coefficient table being reinterpreted

**Unverified:** The beta = 1.0 cantilever bound and the propped-cantilever back-analysis are my own derivation from the closed-form triangular-load moment (M = w0*H^2/6, sigma = 6M/t^2), not a published aquarium figure. It is a bound, deliberately conservative.
