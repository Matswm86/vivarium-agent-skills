---
title: Check Floor Loading Before Buying Glass, Not After
impact: CRITICAL
impactDescription: A filled 1.05 m2 paludarium reaches 5.0-7.4 kN/m2 against a ~2.0 kN/m2 nominal residential floor
tags: safety, structural, siting, paludarium
---

## Check floor loading before buying glass

A large paludarium is the heaviest object most people ever put in a house. The load is concentrated over a small footprint and it is permanent. This is the one mistake that cannot be fixed after the fact.

**Wrong:**

```
Buy the glass -> build the tank -> fill it -> wonder about the floor
```

**Right:**

```
Compute filled mass -> divide by footprint -> compare to the floor's rated
imposed load -> site over a load-bearing wall or get an engineer's assessment
-> THEN order glass
```

**Why:** Worked example for a 150 x 70 x 160 cm build over a 1.05 m2 footprint (my calc): filled mass is 480 / 580 / 731 kg at 150 / 250 / 400 mm water depth, giving **5.0 / 6.0 / 7.4 kN/m2**. Typical residential floors are designed around **1.5-2.0 kN/m2** imposed load. The tank is 3-5x over nominal. Water is 1000 kg/m3 and substrate, hardscape, and glass all add on top.

Concentration matters as much as total mass: the same 731 kg spread over a room is trivial, over 1 m2 it is not. Joist direction decides everything — a tank running **across** joists spreads load over several; one running **along** a single joist bay loads one member.

**Verify:** Weigh the design before you build it. Water volume in litres = L x W x H in cm / 1000, then 1 kg per litre. Add glass (2500 kg/m3), substrate (~600-900 kg/m3 wet), and rock (~2600 kg/m3). Divide by the footprint in m2. If the answer exceeds ~2.5 kN/m2, place the tank against a load-bearing wall with its long axis perpendicular to the joists, or have the floor assessed.

**Sources:**
- https://en.wikipedia.org/wiki/Properties_of_water — water density 1000 kg/m3

**Unverified:** The 1.5-2.0 kN/m2 residential figure is a widely used nominal value; the actual rating for any given floor depends on national building code, joist span, and age. Have it checked rather than assumed.
