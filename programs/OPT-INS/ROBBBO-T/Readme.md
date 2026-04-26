# ROBBBO-T — Unmanned Platforms (COMMS · SAT · REPAIR · DEBRIS)

> **Product ID:** OPT-INS-ROBBBO-T · **Status:** draft · **Updated:** 2026-04-25
>
> ROBBBO-T is the unmanned platforms programme within the OPT-INS Space SIM wrapper.
> Mission: COMMS relay, satellite servicing, on-orbit REPAIR, and DEBRIS removal.
> Operates under GQAOA OPT-INS governance.

**ALICE:** ALICE-GAIA-SRV-01 | **BOB DT:** BOB-DT-GAIA-SRV-01 | **CHARLIE_T:** CHARLIE_T-GAIA-SRV-01

---

## Directory Layout

```
ROBBBO-T/
├── Readme.md               ← this file
├── OPT-IN_FRAMEWORK/       ← 6-axis OPT-INS topology (O/P/T/I/N/S)
├── WBS/
│   ├── Readme.md
│   ├── WBS-100_System-Engineering/BRX/Readme.md
│   ├── WBS-200_Flight-System/
│   │   ├── Readme.md
│   │   ├── BRX/Readme.md
│   │   ├── WBS-210_Structures-Mechanisms/BRX/Readme.md
│   │   ├── WBS-220_Propulsion-RCS/BRX/Readme.md
│   │   ├── WBS-230_Electrical-Power/BRX/Readme.md
│   │   ├── WBS-240_Thermal-Control/BRX/Readme.md
│   │   ├── WBS-250_Avionics-Software/BRX/Readme.md
│   │   ├── WBS-260_Communications/BRX/Readme.md
│   │   ├── WBS-270_GNC/BRX/Readme.md
│   │   └── WBS-280_Payload/BRX/Readme.md
│   ├── WBS-300_Ground-Segment/BRX/Readme.md
│   ├── WBS-400_Launch-Services/BRX/Readme.md
│   ├── WBS-500_Mission-Operations/BRX/Readme.md
│   ├── WBS-600_IA-T/BRX/Readme.md
│   └── WBS-700_Certification/BRX/Readme.md
└── BRX/Readme.md
```

---

## Work Breakdown Structure Summary

| WBS Code | Element | Q-Division Lead | Key Deliverables |
|----------|---------|-----------------|------------------|
| WBS-100 | System Engineering & Management | Q-SCIRES | ConOps, SRD, ICD master, mission analysis |
| WBS-200 | Flight System (Platform) | Q-STRUCTURES | Platform bus, deployable mechanisms |
| WBS-210 | Structures & Mechanisms | Q-STRUCTURES | Structural panels, robotic arm mount |
| WBS-220 | Propulsion / RCS | Q-MECHANICS | Hall-effect thruster or cold-gas RCS |
| WBS-230 | Electrical Power | Q-GREENTECH | Solar arrays, batteries, power bus |
| WBS-240 | Thermal Control | Q-MECHANICS | MLI, heat pipes, radiators |
| WBS-250 | Avionics & Software | Q-HPC | OBC, FDIR, autonomous operations SW |
| WBS-260 | Communications | Q-SPACE | S-band TT&C, inter-satellite link |
| WBS-270 | GNC | Q-HPC | Proximity operations, RPO, AOCS |
| WBS-280 | Payload | Q-MECHANICS | Robotic arm, COMMS repeater, de-orbit sail |
| WBS-300 | Ground Segment | Q-GROUND | Mission control, scheduling |
| WBS-400 | Launch Services | Q-INDUSTRY | Launch vehicle interface, rideshare |
| WBS-500 | Mission Operations | Q-GROUND | Autonomous operations oversight |
| WBS-600 | Integration, Assembly & Test | Q-INDUSTRY | AIT procedures, flat-sat campaigns |
| WBS-700 | Certification & Safety | Q-SCIRES | Space debris mitigation, safety case |

---

## BRX — Programme-Level Business Rules Exchange

Top-level `BRX/` documents cross-programme exchange rules (ROBBBO-T ↔ GAIA servicing, ↔ AMPEL360-Q10 COMMS relay).
See [BRX/Readme.md](BRX/Readme.md) for the master exchange index.

---

## Related Documents

| Document | Path |
|----------|------|
| OPT-INS Wrapper Index | [../Readme.md](../Readme.md) |
| Robbbo-T Robotics PRD | [../../Robbbo-T_Robotics_PRD/Readme.md](../../Robbbo-T_Robotics_PRD/Readme.md) |
| Q-SPACE Domain README | [../../../organization/Q-Divisions/Q-SPACE/README.md](../../../organization/Q-Divisions/Q-SPACE/README.md) |
| Q-Divisions RACI Master | [../../../organization/Q-Divisions/Readme.md](../../../organization/Q-Divisions/Readme.md) |

**[FIN DEL DOCUMENTO]**
