---
title: Size a Waterfall Pump by Total Dynamic Head, Never by "Max Head"
impact: HIGH
impactDescription: Max head is measured at zero flow; a pump rated 1.7 m delivers nothing useful at a 1.5 m lift
tags: water, pump, waterfall, head-loss, calculation
---

## Max head is a zero-flow number and is useless for sizing

```
TDH = static head + tubing friction + fitting losses
```

Match TDH against the pump's **flow-vs-head curve**, not its quoted max head.

1. **Static head** — vertical distance from water surface (pump inlet) to the highest discharge point. For a 160 cm enclosure with a 15-20 cm basin and the outlet 5-15 cm below the lid: **1.4-1.6 m**. The descending water is irrelevant to pump sizing in an open loop; only net static lift and friction in the pressurised line matter.
2. **Tubing friction** — scales roughly with the *square* of flow velocity and *inversely with the fifth power* of internal diameter (Darcy-Weisbach). Hobby rule of thumb: **0.3-1.0 m of head loss per 3 m of 12-16 mm ID tubing at 300-600 L/h.**
3. **Fitting losses** — **~0.1-0.3 m per elbow or tee**; check valves cost more; a spray bar or diffuser plate can add **0.3-0.5 m alone** because it is deliberately restrictive.

**Worked example (my calc)** — 1.5 m static, 2.5 m of 12 mm ID tube, 3 fittings, a spray bar, target 400-500 L/h:

```
static                 1.50 m
tubing 2.5 m x 0.25    0.60 m
3 fittings x 0.15      0.45 m
spray bar restriction  0.30 m
                     -------
TDH                    2.85 m
+20-30% fouling margin -> design to ~3.5 m TDH at 400-500 L/h
```

**Consequence:** pumps rated 1.3-1.7 m max head are undersized for a 1.5 m static lift plus losses, even though the number superficially looks adequate. Choose a pump whose max-head rating sits comfortably above the design TDH, then **throttle it with a ball valve or bypass tee** back to the water section to hit the target flow. The bypass also gives headroom as the intake sponge and tube interior foul with biofilm over months.

**Verified reference points:** Sicce Multi 800 = 800 L/h / 1.3 m; Multi 1300 = 1200 L/h / 1.7 m; Multi 2500 = 2500 L/h / 3.1 m; Multi 4000 = 3800 L/h / 3.1 m; Multi 5800 = 5760 L/h / 3.8 m.

**Tubing:** 12-16 mm ID is the practical range for 400-600 L/h. Undersizing to 9-10 mm ID to save space sharply increases friction head and can push the required pump up a full size.

**Sources:**
- https://www.sicce.com/en/products/multifunction-pumps/multi.html — verified flow/head figures
- https://tunze.com/Osmolator-3/3154.000

**Unverified:** Eheim compactON, Universal, and ProfiPump specs — manufacturer pages are JS-rendered and did not yield numeric specs. Confirm before buying.
