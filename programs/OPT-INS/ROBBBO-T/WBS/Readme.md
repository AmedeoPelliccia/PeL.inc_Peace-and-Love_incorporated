# WBS — ROBBBO-T Work Breakdown Structure

**Product:** ROBBBO-T (Unmanned Platforms) · **ID:** OPT-INS-ROBBBO-T-WBS · **Status:** draft

This directory defines the Work Breakdown Structure for the ROBBBO-T programme. Each WBS element contains:
- A `Readme.md` describing scope, deliverables, and accountable Q-Division
- A `BRX/` sub-directory with the **Business Rules Exchange** for that element

---

## WBS Hierarchy

```
WBS-100  System Engineering & Management
WBS-200  Flight System (Platform Bus)
  WBS-210  Structures & Mechanisms
  WBS-220  Propulsion / RCS
  WBS-230  Electrical Power
  WBS-240  Thermal Control
  WBS-250  Avionics & Software
  WBS-260  Communications
  WBS-270  GNC (Proximity Operations / RPO)
  WBS-280  Payload (Robotic arm / COMMS / de-orbit)
WBS-300  Ground Segment
WBS-400  Launch Services (rideshare / dedicated)
WBS-500  Mission Operations
WBS-600  Integration, Assembly & Test (IA&T)
WBS-700  Certification & Safety
```

---

## WBS Element Summary

| WBS | Element | Accountable Q-Division | BRX |
|-----|---------|------------------------|-----|
| 100 | System Engineering & Management | Q-SCIRES | [BRX](WBS-100_System-Engineering/BRX/Readme.md) |
| 200 | Flight System (Platform Bus) | Q-STRUCTURES | [BRX](WBS-200_Flight-System/BRX/Readme.md) |
| 210 | Structures & Mechanisms | Q-STRUCTURES | [BRX](WBS-200_Flight-System/WBS-210_Structures-Mechanisms/BRX/Readme.md) |
| 220 | Propulsion / RCS | Q-MECHANICS | [BRX](WBS-200_Flight-System/WBS-220_Propulsion-RCS/BRX/Readme.md) |
| 230 | Electrical Power | Q-GREENTECH | [BRX](WBS-200_Flight-System/WBS-230_Electrical-Power/BRX/Readme.md) |
| 240 | Thermal Control | Q-MECHANICS | [BRX](WBS-200_Flight-System/WBS-240_Thermal-Control/BRX/Readme.md) |
| 250 | Avionics & Software | Q-HPC | [BRX](WBS-200_Flight-System/WBS-250_Avionics-Software/BRX/Readme.md) |
| 260 | Communications | Q-SPACE | [BRX](WBS-200_Flight-System/WBS-260_Communications/BRX/Readme.md) |
| 270 | GNC / Proximity Ops | Q-HPC | [BRX](WBS-200_Flight-System/WBS-270_GNC/BRX/Readme.md) |
| 280 | Payload | Q-MECHANICS | [BRX](WBS-200_Flight-System/WBS-280_Payload/BRX/Readme.md) |
| 300 | Ground Segment | Q-GROUND | [BRX](WBS-300_Ground-Segment/BRX/Readme.md) |
| 400 | Launch Services | Q-INDUSTRY | [BRX](WBS-400_Launch-Services/BRX/Readme.md) |
| 500 | Mission Operations | Q-GROUND | [BRX](WBS-500_Mission-Operations/BRX/Readme.md) |
| 600 | Integration, Assembly & Test | Q-INDUSTRY | [BRX](WBS-600_IA-T/BRX/Readme.md) |
| 700 | Certification & Safety | Q-SCIRES | [BRX](WBS-700_Certification/BRX/Readme.md) |

---

## Cross-WBS BRX Index

The product-level exchange index is at [../BRX/Readme.md](../BRX/Readme.md).

**[FIN DEL DOCUMENTO]**
