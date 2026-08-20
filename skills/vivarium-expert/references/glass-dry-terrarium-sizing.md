---
title: Size Dry Terrarium Glass by Longest Unsupported Edge, Not by Load
impact: HIGH
impactDescription: Substrate thrust is ~1/50th of water pressure; span and impact govern instead
tags: glass, structural, terrarium
---

## A dry terrarium is sized by span, not stress

Run the hydrostatic formula on a dry terrarium and it returns a meaningless answer, because the hydrostatic load is zero. What actually governs, in order:

1. **Self-weight and handling.** A 1700 x 600 mm pane in 6 mm float is floppy, flexes visibly when lifted, and is a laceration hazard if it fails during assembly.
2. **Substrate side-thrust — negligible.** For bark/soil at bulk density 600 kg/m3, 0.10 m deep, Ka ~ 0.33: base lateral pressure = 0.33 x 600 x 9.81 x 0.10 = **194 N/m2 = 0.00019 N/mm2** (my calc), roughly 1/50th of what a 400 mm water column exerts. It matters only for keeping substrate out of door tracks.
3. **Point impact.** A dropped basking lamp, a cat, a knee. Absent from the hydrostatic formula entirely, and the real reason terrarium glass is sized by span.
4. **Door and lid weight** hung off the front and top edges.

**Right — the trade table, by longest unsupported edge:**

| Longest unsupported edge | Float | Toughened (ESG) | Floor pane |
|---|---|---|---|
| <= 60 cm | 4 mm | 4 mm | 6 mm |
| <= 100 cm | 5 mm | 4 mm | 8 mm |
| <= 150 cm | 6 mm | 5 mm | 8 mm |
| <= 200 cm | **8 mm** | **6 mm** | **10 mm** |

The floor pane always takes one thickness step above the walls, because it carries substrate, water bowls, and the animal.

**Verify:** Measure the longest edge with no brace, mullion, or corner support along it. That single number picks the row.

**Sources:**
- https://www.terraristikshop.net/terrarium/terrarium-selbstbau/ — the span table and the floor-pane step rule
