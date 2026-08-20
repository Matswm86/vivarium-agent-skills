---
title: Permanent Glass Fogging Is Arithmetic, Not a Build Fault — Raise the Surface Temperature
impact: HIGH
impactDescription: At 26 C / 90% RH every interior surface below 24.2 C condenses; a single pane in a 21 C room sits at ~22-23 C
tags: climate, condensation, humidity, insulation, dew-point
---

## Compute the dew point, then compare it to your glass

**Magnus-Tetens approximation** (a = 17.625, b = 243.04 C, valid -40 to +50 C, uncertainty +/-0.35 C):

```
alpha = ln(RH/100) + a*T/(b + T)
Td    = (b * alpha) / (a - alpha)
```

Dew point (my calc):

| Air temp | RH 70% | RH 80% | RH 90% | RH 95% | RH 100% |
|---|---|---|---|---|---|
| 24 C | **18.2** | — | — | — | 24.0 |
| 26 C | — | **22.3** | **24.2** | — | 26.0 |
| 28 C | — | — | **26.2** | **27.1** | 28.0 |

**Read that as an instruction.** At 26 C and 90% RH, every interior surface below 24.2 C condenses. Your room is 21 C. An uninsulated single pane with 21 C air on the outside sits around 22-23 C on its inner face. **It will fog, permanently, all winter.** That is not a fault in the build; it is arithmetic.

**The fix is to raise the inner surface temperature above the dew point. Everything else is a workaround.**

| Mitigation | Effect | Confidence |
|---|---|---|
| **50 mm XPS on rear, both sides, base** | U 5.7 -> 0.68 W/m2K (my calc); those panels stop condensing entirely and heat demand falls 55-75% | **Highest-value single action.** Physics solid; vivarium-specific citation UNVERIFIED |
| Double-glaze or laminate the front pane | U 5.7 -> 2.8 W/m2K; inner face runs much warmer on the one pane you must see through | Physics sourced; vivarium effectiveness UNVERIFIED |
| Keep the enclosure off exterior walls | Removes the cold-wall radiant sink | UNVERIFIED numerically, mechanism obvious |
| Small fan across the inner face of the viewing pane | Disrupts the boundary layer; standard practice | UNVERIFIED numerically |
| Room dehumidification | Lowers room dew point but does **not** raise the glass temperature — helps the room, not the pane | — |
| Heated glass / anti-fog film | **UNVERIFIED** — no product specs retrieved | — |

**Build order consequence: insulate three sides and the base BEFORE filling the enclosure.** Retrofitting XPS to a planted, watered, stocked tall paludarium is close to impossible.

**Sources:**
- https://www.omnicalculator.com/physics/dew-point — Magnus-Tetens
- https://www.theadvancedgroup.co.uk/double-glazing-u-values-explained
