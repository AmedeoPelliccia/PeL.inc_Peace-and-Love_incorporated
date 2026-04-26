# BRX — Business Rules Exchange: WBS-220 Propulsion / OMS-RCS (AMPEL360-Q10)

**Product:** AMPEL360-Q10 · **WBS:** WBS-220 Propulsion / OMS-RCS · **Accountable Q-Division:** Q-MECHANICS · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-220 — Propulsion / OMS-RCS` in the **AMPEL360-Q10** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-MECHANICS | Q-STRUCTURES | Propulsion mass & envelope | → | XLSX | Q-MECHANICS (A) |
| 2 | Q-MECHANICS | Q-GREENTECH | Power demand profile (OMS burn) | → | XLSX | Q-MECHANICS (A) |
| 3 | Q-MECHANICS | Q-HPC | Thruster firing commands ICD | ↔ | YAML | Q-MECHANICS (A) |
| 4 | Q-MECHANICS | Q-SCIRES | Propellant & delta-V budget | → | PDF | Q-MECHANICS (A) |

## BRX Governance Rules

1. **Single source of truth**: the producer WBS element owns and versions all data items listed here.
2. **ICD alignment**: every row maps to a named interface in the master ICD (WBS-100 deliverable).
3. **Change control**: changes to any exchange require a BRX revision + Q-Division sign-off (Accountable: Q-MECHANICS).
4. **Format compliance**: all S1000D DMs must pass BREX validation; YAML/JSON must conform to repo schema.
5. **Traceability**: each data item SHALL be traceable to an SRD requirement via the CSDB requirement link.

## Related

- [WBS Readme.md](../Readme.md)
- [Product BRX index](../../BRX/Readme.md)
- [Q-Divisions RACI Master](../../../../../organization/Q-Divisions/Readme.md)

**[FIN DEL DOCUMENTO]**
