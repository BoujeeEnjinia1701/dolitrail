---
doc_id: DLT-PRB-001
title: DoliTrail problem statement
project: DoliTrail
doc_type: Problem statement
version: "0.2"
status: Draft
date: '2026-10-03'
author: Amish Chadha
license: CERN-OHL-S-2.0
revisions:
- version: "0.1"
  date: '2026-09-30'
  author: Amish Chadha
  change: Initial scaffold
- version: "0.2"
  date: '2026-10-03'
  author: Amish Chadha
  change: TRL 2 and 3 update; constraints worded as a value-engineering target, open questions settled (DLT-DDR-001), first co-design candidates, safety section
---

# DoliTrail problem statement

Where roads end, patients are carried, and the only equipment is a stretcher and the bearers' shoulders.

## The problem

Reports from Odisha, Madhya Pradesh, Meghalaya, Chhattisgarh and Jammu and Kashmir describe carries of 3 to 8 km on stretchers made from bamboo and cloth or on ambulance stretchers, over mud, snow, streams and forest trails ([ANI, 2026](https://aninews.in/news/national/general-news/pregnant-woman-carried-7-km-on-stretcher-due-to-no-road-connectivity-in-odishas-mayurbhanj20260823102717/); [The Tribune, 2021](https://www.tribuneindia.com/news/nation/madhya-pradesh-no-motorable-road-relatives-carry-pregnant-woman-on-makeshift-stretcher-for-8-km-287707); [The Tribune, 2022](https://www.tribuneindia.com/news/nation/pregnant-meghalaya-woman-taken-to-hospital-on-bamboo-stretcher-for-5-km-429099); [Gulf News, 2020](https://gulfnews.com/world/asia/india/india-video-of-a-pregnant-woman-who-was-taken-to-hospital-on-a-handmade-stretcher-has-gone-viral-1.1594298702634)). In Meghalaya, volunteers took turns to carry ([The Tribune, 2022](https://www.tribuneindia.com/news/nation/pregnant-meghalaya-woman-taken-to-hospital-on-bamboo-stretcher-for-5-km-429099)). Roads will come, as officials promise in these reports, but patients need to move now.

Wheeled litters exist for mountain rescue teams, and the preliminary IP screen found a litter wheel sold without a listed brake and an expired stretcher brake patent, but these fit purpose-built metal rescue litters, not a bamboo doli, and they cost more than a village can spend. The gap is a low-cost, clamp-on wheel with a brake and a harness that fits the stretcher a family has already built.

## Users and context

| User | Need | Context |
| --- | --- | --- |
| Family and neighbour bearers | Carry a patient further with less load on the shoulders and control on descents | Forest and hill trails of 3 to 8 km to the nearest road |
| Ambulance crews (108 and similar services) | A kit they can carry in the vehicle and fit on arrival at the road end | Calls to villages without motorable roads |
| Community health workers and village health committees | A ready kit kept in the village, simple to fit and maintain | Maternal care and emergencies |
| The patient | A steadier, safer ride with less jolting and less risk of being dropped | Women in labour, the injured and the elderly |

## Operating environment

- Narrow forest and hill trails, often under 1 m (3 ft) wide, with steps, roots, rocks and grades of 20 per cent or more (estimate).
- Monsoon mud, stream and river crossings, and snow in some regions.
- Carries of 3 to 8 km, by day or night.
- Dolis built from bamboo poles of varied diameter, with cloth, rope or a cot frame.

## Constraints

- Value-engineering target of USD 1,500 for the parts of one kit (a hypothetical control target, not a spending limit; STANDARDS section 18).
- Must clamp to bamboo poles of about 40 to 80 mm (1.6 to 3.1 in) diameter (estimate) without tools, or with one simple tool.
- Kit mass at or below 10 kg (22 lb) (target) so one person can carry it to the village (R7).
- Clamps fit on bare pole: where the bed is lashed or tied, the lashing is slid aside at the four clamp points (DLT-DDR-002).
- Built from bicycle parts, steel tube and webbing that can be sourced and repaired locally; hardware under CERN-OHL-S-2.0.
- Own clamp geometry and colours (see design-arounds).
- Published as an open engineering reference, not as certified medical or rescue equipment.

## Out of scope

- Motorised drive or power assist.
- A new stretcher or litter; DoliTrail adds to the existing doli.
- Medical care during transport.
- River crossings where the doli must be carried or ferried; the kit is lifted clear.

## Prior work

| Prior work | What it does | Gap for these users | Source |
| --- | --- | --- | --- |
| Cloth and bamboo village stretcher | Stretcher made by relatives from cloth and bamboo sticks and carried by hand | All weight on the bearers; no wheel or brake | [link](https://www.tribuneindia.com/news/nation/madhya-pradesh-no-motorable-road-relatives-carry-pregnant-woman-on-makeshift-stretcher-for-8-km-287707) |
| Hand-made dola | Hand-made carrying stretcher used by health workers over monsoon mud | Carried entirely by hand | [link](https://gulfnews.com/world/asia/india/india-video-of-a-pregnant-woman-who-was-taken-to-hospital-on-a-handmade-stretcher-has-gone-viral-1.1594298702634) |
| Ambulance stretcher carried on foot | Ambulance crew carries the vehicle stretcher to and from the village | Not made for trails; carried entirely by hand | [link](https://aninews.in/news/national/general-news/pregnant-woman-carried-7-km-on-stretcher-due-to-no-road-connectivity-in-odishas-mayurbhanj20260823102717/) |
| Army evacuation stretcher | Military evacuation team carries a patient on a stretcher through snow | Depends on a trained team; carried by hand | [link](https://www.tribuneindia.com/news/j-k/watch-army-men-carry-pregnant-woman-to-hospital-amid-heavy-snowfall-in-j-k-359452) |

## Co-design

A district health system or NGO running maternal health or emergency transport in a hill or forest district, together with community health workers who have carried dolis, to test fit on real stretchers and trails and to decide where kits are kept. First candidates to approach, in order (none approached yet, DLT-DDR-001): a district 108 ambulance operator in Mayurbhanj, Odisha, with its road-end crews; a maternal health NGO working with village health committees in the same block; a volunteer mountain rescue group for trail technique and the step and descent rules.

## Open questions, settled

The scaffold's open questions were settled under Amish's pre-approval of 2026-10-03 (DLT-DDR-001):

- **One wheel or two?** One, under the patient's hips. Two wheels would need a track wider than the doli on trails under 1 m wide; one wheel keeps the width to the doli's own (680 mm on the reference doli).
- **How much of a route can roll?** Unknown until trail surveys with the first partner; the calculations assume rolling on level ground and moderate grades and lifting at steps, rocks and water.
- **Where are kits kept?** First trial: in the ambulance, carried in by the crew, so the kit is maintained by a service. Village storage is a TRL 4 question for the partner.
- **Commercial wheeled litter kits.** Purpose-built litter wheels fit metal rescue litters, not bamboo poles, and cost more than the whole value-engineering target; DoliTrail does not compete with them (see Prior work).
- **Does a harness shift load safely?** The harness takes the pole ends in slings at the bearer's knuckle height; slings are adjustable for bearers of different heights. A fit trial with bearers is TRL 4 work.

## Safety

> **Safety:** DoliTrail carries a person who may be in labour, injured or unconscious, on steep and wet ground. It is an open engineering reference, not certified medical or rescue equipment. The main hazards are a runaway on a descent, the doli tipping sideways on its single wheel, a clamp slipping on wet bamboo, and bearers lifting too much at steps. Bearers keep hold of the poles at all times, lift and carry across water and down steps, and no patient is carried before the frame and wheel are proof-loaded (DLT-BLD-001, sections 5 and 6).
