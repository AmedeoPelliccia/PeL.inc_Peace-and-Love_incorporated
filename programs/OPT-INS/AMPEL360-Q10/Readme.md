# AMPEL360-Q10 — Crewed Shuttle-Type Spacecraft

> **Product ID:** OPT-INS-AMPEL360-Q10 · **Status:** draft · **Updated:** 2026-04-25
>
> AMPEL360-Q10 is the crewed shuttle-type spacecraft within the OPT-INS Space SIM wrapper.
> Mission: space travel and space tourism. Operates under the GQAOA OPT-INS governance framework.

**ALICE:** ALICE-AMPEL360-Q10 | **BOB DT:** BOB-DT-AMPEL360-Q10 | **CHARLIE_T:** CHARLIE_T-AMPEL360-Q10

---

## Directory Layout

```
AMPEL360-Q10/
├── Readme.md               ← this file
├── OPT-IN_FRAMEWORK/       ← 6-axis OPT-INS topology (O/P/T/I/N/S)
├── WBS/                    ← Work Breakdown Structure
│   ├── Readme.md
│   ├── WBS-100_System-Engineering/
│   │   ├── Readme.md
│   │   └── BRX/Readme.md
│   ├── WBS-200_Flight-System/
│   │   ├── Readme.md
│   │   ├── BRX/Readme.md
│   │   ├── WBS-210_Structures-Mechanisms/BRX/Readme.md
│   │   ├── WBS-220_Propulsion-OMS-RCS/BRX/Readme.md
│   │   ├── WBS-230_Electrical-Power/BRX/Readme.md
│   │   ├── WBS-240_Thermal-Control/BRX/Readme.md
│   │   ├── WBS-250_Avionics-Software/BRX/Readme.md
│   │   ├── WBS-260_Communications/BRX/Readme.md
│   │   ├── WBS-270_GNC/BRX/Readme.md
│   │   └── WBS-280_ECLSS/BRX/Readme.md
│   ├── WBS-300_Ground-Segment/BRX/Readme.md
│   ├── WBS-400_Launch-Services/BRX/Readme.md
│   ├── WBS-500_Mission-Operations/BRX/Readme.md
│   ├── WBS-600_IA-T/BRX/Readme.md
│   └── WBS-700_Certification/BRX/Readme.md
└── BRX/Readme.md           ← cross-programme exchange index
```

---

## Work Breakdown Structure Summary

| WBS Code | Element | Q-Division Lead | Key Deliverables |
|----------|---------|-----------------|------------------|
| WBS-100 | System Engineering & Management | Q-SCIRES | SRD, ICD master, risk register, WBS dictionary |
| WBS-200 | Flight System | Q-STRUCTURES | Vehicle assembly, subsystem ICDs |
| WBS-210 | Structures & Mechanisms | Q-STRUCTURES | Primary structure, separation mechanisms |
| WBS-220 | Propulsion / OMS-RCS | Q-MECHANICS | Main engine + orbital/attitude thrusters |
| WBS-230 | Electrical Power | Q-GREENTECH | Solar arrays, batteries, power distribution |
| WBS-240 | Thermal Control | Q-MECHANICS | TPS, active/passive thermal regulation |
| WBS-250 | Avionics & Software | Q-HPC | OBC, FDIR, DO-178C/ECSS-SW-80 SW |
| WBS-260 | Communications | Q-SPACE | S-band TT&C, Ka-band data, QKD channel |
| WBS-270 | GNC | Q-HPC | Navigation algorithms, AOCS, rendezvous |
| WBS-280 | ECLSS | Q-GREENTECH | Air revitalization, water, fire detection |
| WBS-300 | Ground Segment | Q-GROUND | MCC, network, tracking stations |
| WBS-400 | Launch Services | Q-INDUSTRY | Launch vehicle interface, pad operations |
| WBS-500 | Mission Operations | Q-GROUND | Flight operations procedures, crew training |
| WBS-600 | Integration, Assembly & Test | Q-INDUSTRY | AIT procedures, test campaigns |
| WBS-700 | Certification & Safety | Q-SCIRES | Safety case, FAA 14 CFR 460, ECSS hazard |

---

## BRX — Programme-Level Business Rules Exchange

The top-level `BRX/` documents cross-programme and cross-Q-Division exchange rules for AMPEL360-Q10.
See [BRX/Readme.md](BRX/Readme.md) for the master exchange index.

---

## Related Documents

| Document | Path |
|----------|------|
| OPT-INS Wrapper Index | [../Readme.md](../Readme.md) |
| Q-SPACE Domain README | [../../../organization/Q-Divisions/Q-SPACE/README.md](../../../organization/Q-Divisions/Q-SPACE/README.md) |
| Q-Divisions RACI Master | [../../../organization/Q-Divisions/Readme.md](../../../organization/Q-Divisions/Readme.md) |

**[FIN DEL DOCUMENTO]**
