---
title: Do Not Use Inverse-Square for Vivarium Light Falloff — Real Exponent Is ~1.2
impact: HIGH
impactDescription: Inverse-square over-predicts the required fixture by ~100x and sells you a 600 W grow light you do not need
tags: light, PAR, PPFD, physics, tall-enclosure
---

## LED bars fall off like line sources, not point sources

**Wrong:**

```
I(d2) = I(d1) * (d1/d2)^2
10 cm -> 150 cm: (10/150)^2 = 0.00444
To land 30-50 umol/m2/s at the floor you would need 6,750-11,250 umol/m2/s
at 10 cm -- 5-8x full tropical noon sunlight, inside a glass box.
```

**Right:**

```
I ~ d^-n with n ~ 1.15-1.26 for an LED bar at vivarium distances
```

**Why:** Inverse-square is a *point-source, far-field* law. It holds only once measuring distance substantially exceeds the source's largest dimension. An 87 cm LED bar measured at 15-45 cm is deep in the **near field**, where a long line source falls off closer to 1/d and a large-area panel barely falls off at all.

**The empirical proof — Arcadia's published PAR table** (Apogee MQ-200, at 244.6 V / 49.9 Hz), the only vivarium brand publishing PAR:

| Distance | 15 W (290 mm) | 22 W (470 mm) | 34 W (570 mm) | 51 W (870 mm) |
|---|---|---|---|---|
| 100 mm | 661 | 660 | 843 | 859 |
| 150 mm | 448 | 448 | 561 | 591 |
| 300 mm | 146 | 155 | 226 | 242 |
| 375 mm | 87 | 108 | 160 | 187 |

Fitted exponent for the 51 W bar (my calc): 100→300 mm gives `n = ln(859/242)/ln(3) = 1.153`; 100→375 mm gives `1.154`; 150→375 mm gives `1.256`. **n ~ 1.15-1.26, not 2.0.** That is a factor-of-hundreds difference at 1.5 m, and it is the reason tall vivaria are lightable at all.

**Extrapolated to a 1.5 m drop** from 591 umol/m2/s at 150 mm (my calc; beyond the tested range, an estimate not a spec):

| Assumed n | PPFD at 1500 mm |
|---|---|
| 1.15 (measured near-field) | 42 — optimistic; falloff steepens past the bar's own length |
| 1.30 | 30 — realistic upper |
| 1.50 | 19 — realistic lower |
| 2.00 (pure inverse-square) | 5.9 — pessimistic, would apply to a genuine point source |

**Cross-check by total flux** (enclosed reflective box, `PPFD_avg = PPF * utilisation / footprint`), 1.05 m2 footprint:

| Fixture PPF | 40% util. | 60% | 80% |
|---|---|---|---|
| 50 umol/s | 19 | 29 | 38 |
| 100 | 38 | 57 | 76 |
| 200 | 76 | 114 | 152 |
| 300 | 114 | 171 | 229 |

**Verify:** Borrow or buy a PAR meter and measure at plant level. Do not convert LED lux to PPFD — no published conversion factor exists for white LED and spectra vary widely (UNVERIFIED).

**Sources:**
- https://www.arcadiareptile.com/jungledawn-ledbar/ — the measured PAR table

**Unverified:** The near-field/far-field transition threshold for this application has no vivarium-specific citation; it is standard photometric theory, confirmed here only by Arcadia's empirical data.
