# GAIA — Space Stations and Habitats

> **Product ID:** OPT-INS-GAIA · **Status:** draft · **Updated:** 2026-04-25
>
> GAIA is the space stations and habitats programme within the OPT-INS Space SIM wrapper.
> Mission: orbital and deep-space human habitation. Operates under GQAOA OPT-INS governance.

**ALICE:** ALICE-GAIA-HAB-01 | **BOB DT:** BOB-DT-GAIA-HAB-01 | **CHARLIE_T:** CHARLIE_T-GAIA-HAB-01

---

## Directory Layout

```
GAIA/
├── Readme.md               ← this file
├── OPT-IN_FRAMEWORK/       ← 6-axis OPT-INS topology (O/P/T/I/N/S)
├── WBS/
│   ├── Readme.md
│   ├── WBS-100_System-Engineering/BRX/Readme.md
│   ├── WBS-200_Flight-System/
│   │   ├── Readme.md
│   │   ├── BRX/Readme.md
│   │   ├── WBS-210_Structures-Mechanisms/BRX/Readme.md
│   │   ├── WBS-220_ECLSS/BRX/Readme.md
│   │   ├── WBS-230_Electrical-Power/BRX/Readme.md
│   │   ├── WBS-240_Thermal-Control/BRX/Readme.md
│   │   ├── WBS-250_Avionics-Software/BRX/Readme.md
│   │   ├── WBS-260_Communications/BRX/Readme.md
│   │   └── WBS-270_Docking-Berthing/BRX/Readme.md
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
| WBS-100 | System Engineering & Management | Q-SCIRES | SRD, ICD master, ECSS-M docs, risk register |
| WBS-200 | Flight System (Habitat Module) | Q-STRUCTURES | Module structure, pressurized volumes |
| WBS-210 | Structures & Mechanisms | Q-STRUCTURES | Primary pressure shell, berthing CBM/IDSS |
| WBS-220 | ECLSS | Q-GREENTECH | Closed-loop life support — air, water, waste |
| WBS-230 | Electrical Power | Q-GREENTECH | Solar arrays, batteries, power bus |
| WBS-240 | Thermal Control | Q-MECHANICS | Multi-layer insulation, radiators, ATCS |
| WBS-250 | Avionics & Software | Q-HPC | OBC, housekeeping, FDIR, ECSS-SW-80 |
| WBS-260 | Communications | Q-SPACE | S-band TT&C, Ka-band data relay, QKD |
| WBS-270 | Docking & Berthing | Q-MECHANICS | CBM/IDSS interface, AMPEL360-Q10 docking |
| WBS-300 | Ground Segment | Q-GROUND | MCC, data relay network |
| WBS-400 | Launch Services | Q-INDUSTRY | Launch vehicle interface, module stack |
| WBS-500 | Mission Operations | Q-GROUND | Crew scheduling, resupply logistics |
| WBS-600 | Integration, Assembly & Test | Q-INDUSTRY | Module AIT, on-orbit commissioning |
| WBS-700 | Certification & Safety | Q-SCIRES | Safety case, NASA/ESA/ECSS compliance |

---

## BRX — Programme-Level Business Rules Exchange

Top-level `BRX/` documents cross-programme exchange rules (GAIA ↔ AMPEL360-Q10 resupply, ROBBBO-T servicing).
See [BRX/Readme.md](BRX/Readme.md) for the master exchange index.

---

## Related Documents

| Document | Path |
|----------|------|
| OPT-INS Wrapper Index | [../Readme.md](../Readme.md) |
| GAIA Space PRD | [../../GAIA_SPACE-PRD/Readme.md](../../GAIA_SPACE-PRD/Readme.md) |
| Q-SPACE Domain README | [../../../organization/Q-Divisions/Q-SPACE/README.md](../../../organization/Q-Divisions/Q-SPACE/README.md) |
| Q-Divisions RACI Master | [../../../organization/Q-Divisions/Readme.md](../../../organization/Q-Divisions/Readme.md) |

**[FIN DEL DOCUMENTO]**
