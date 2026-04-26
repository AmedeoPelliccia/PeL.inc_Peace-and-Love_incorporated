# OPT-INS — Space SIM Framework Wrapper

> **OPT-INS** = **OPT-IN + S (Space SIM)**
>
> The trailing **S** is the Space SIM qualifier, **not** a plural.
> OPT-INS extends the base OPT-IN framework with space-simulation capability:
> orbital mechanics, vacuum/thermal, radiation, microgravity, RPO, reentry.

**Document ID:** AEROSPACEMODEL-OPT-INS-001 · **Status:** draft · **Updated:** 2026-04-25

---

## Products

Three top-level products, each with its own `OPT-IN_FRAMEWORK` instance and Work Breakdown Structure:

| Product | Type | Mission | Folder |
|---------|------|---------|--------|
| **AMPEL360-Q10** | Crewed shuttle-type spacecraft | Space travel / space tourism | [AMPEL360-Q10/](AMPEL360-Q10/Readme.md) |
| **GAIA** | Space stations and habitats | Orbital / deep-space human habitation | [GAIA/](GAIA/Readme.md) |
| **ROBBBO-T** | Unmanned platforms | COMMS · SAT · REPAIR · DEBRIS | [ROBBBO-T/](ROBBBO-T/Readme.md) |

---

## Directory Layout

```
programs/OPT-INS/
├── Readme.md                          ← this file
├── AMPEL360-Q10/
│   ├── Readme.md
│   ├── OPT-IN_FRAMEWORK/             ← OPT-IN axes O/P/T/I/N/S (space-scoped)
│   ├── WBS/                          ← Work Breakdown Structure
│   │   ├── WBS-100_System-Engineering/BRX/
│   │   ├── WBS-200_Flight-System/
│   │   │   ├── WBS-210_Structures-Mechanisms/BRX/
│   │   │   ├── WBS-220_Propulsion-OMS-RCS/BRX/
│   │   │   ├── WBS-230_Electrical-Power/BRX/
│   │   │   ├── WBS-240_Thermal-Control/BRX/
│   │   │   ├── WBS-250_Avionics-Software/BRX/
│   │   │   ├── WBS-260_Communications/BRX/
│   │   │   ├── WBS-270_GNC/BRX/
│   │   │   └── WBS-280_ECLSS/BRX/
│   │   ├── WBS-300_Ground-Segment/BRX/
│   │   ├── WBS-400_Launch-Services/BRX/
│   │   ├── WBS-500_Mission-Operations/BRX/
│   │   ├── WBS-600_IA-T/BRX/
│   │   └── WBS-700_Certification/BRX/
│   └── BRX/                          ← cross-WBS programme-level exchange
├── GAIA/
│   ├── Readme.md
│   ├── OPT-IN_FRAMEWORK/
│   ├── WBS/
│   │   ├── WBS-100_System-Engineering/BRX/
│   │   ├── WBS-200_Flight-System/
│   │   │   ├── WBS-210_Structures-Mechanisms/BRX/
│   │   │   ├── WBS-220_ECLSS/BRX/
│   │   │   ├── WBS-230_Electrical-Power/BRX/
│   │   │   ├── WBS-240_Thermal-Control/BRX/
│   │   │   ├── WBS-250_Avionics-Software/BRX/
│   │   │   ├── WBS-260_Communications/BRX/
│   │   │   └── WBS-270_Docking-Berthing/BRX/
│   │   ├── WBS-300_Ground-Segment/BRX/
│   │   ├── WBS-400_Launch-Services/BRX/
│   │   ├── WBS-500_Mission-Operations/BRX/
│   │   ├── WBS-600_IA-T/BRX/
│   │   └── WBS-700_Certification/BRX/
│   └── BRX/
└── ROBBBO-T/
    ├── Readme.md
    ├── OPT-IN_FRAMEWORK/
    ├── WBS/
    │   ├── WBS-100_System-Engineering/BRX/
    │   ├── WBS-200_Flight-System/
    │   │   ├── WBS-210_Structures-Mechanisms/BRX/
    │   │   ├── WBS-220_Propulsion-RCS/BRX/
    │   │   ├── WBS-230_Electrical-Power/BRX/
    │   │   ├── WBS-240_Thermal-Control/BRX/
    │   │   ├── WBS-250_Avionics-Software/BRX/
    │   │   ├── WBS-260_Communications/BRX/
    │   │   ├── WBS-270_GNC/BRX/
    │   │   └── WBS-280_Payload/BRX/
    │   ├── WBS-300_Ground-Segment/BRX/
    │   ├── WBS-400_Launch-Services/BRX/
    │   ├── WBS-500_Mission-Operations/BRX/
    │   ├── WBS-600_IA-T/BRX/
    │   └── WBS-700_Certification/BRX/
    └── BRX/
```

---

## Shared 6-Axis OPT-INS Topology (Spatial Chapter Set)

| Axis | Code | Spatial Chapter Set |
|------|------|---------------------|
| **O** | Organizations | Mission-equivalent (ECSS-M) — programme office, consortia, governance |
| **P** | Programs | Mission-equivalent (ECSS-M) — plans, schedules, budgets |
| **T** | Technologies / On-Board Systems | ECLSS, TPS, GNC, OMS/RCS, EVA, comms, power |
| **I** | Infrastructures | Launch, range, recovery, ground segment |
| **N** | Neural Networks | Ledger, DPP, governance |
| **S** | Space Simulations | Orbital mechanics, vacuum/thermal, radiation, microgravity, RPO, reentry |

---

## WBS Numbering Convention

| WBS Code | Domain |
|----------|--------|
| WBS-100 | System Engineering & Management |
| WBS-200 | Flight System (vehicle / platform / habitat) |
| WBS-2xx | Flight System sub-elements (see per-product WBS) |
| WBS-300 | Ground Segment |
| WBS-400 | Launch Services |
| WBS-500 | Mission Operations |
| WBS-600 | Integration, Assembly & Test (IA&T) |
| WBS-700 | Certification & Safety |

---

## BRX — Business Rules Exchange Repositories

Each `BRX/` folder is a **Business Rules Exchange repository** for the enclosing WBS element. It defines:

- **Parties**: which WBS elements, Q-Divisions, or external entities exchange data
- **Data items**: what information is exchanged (ICDs, datasets, models, approvals)
- **Direction**: producer → consumer
- **Format**: S1000D DM, YAML, JSON, PDF, HDF5, XML, etc.
- **Governance**: which Q-Division is Accountable (A) and which is Responsible (R)

> See the `Readme.md` inside each `BRX/` for the specific exchange rules.

---

## Related Documents

| Document | Path |
|----------|------|
| Q-Divisions Governance (RACI Master) | [organization/Q-Divisions/Readme.md](../../organization/Q-Divisions/Readme.md) |
| Q-SPACE Domain README | [organization/Q-Divisions/Q-SPACE/README.md](../../organization/Q-Divisions/Q-SPACE/README.md) |
| GAIA Space PRD | [programs/GAIA_SPACE-PRD/Readme.md](../GAIA_SPACE-PRD/Readme.md) |
| OPT-INS_FRAMEWORK | [OPT-INS_FRAMEWORK/Readme.md](../../OPT-INS_FRAMEWORK/Readme.md) |
| Programs Master Matrix (ALICES) | [programs/readme.md](../readme.md) |

**[FIN DEL DOCUMENTO]**
