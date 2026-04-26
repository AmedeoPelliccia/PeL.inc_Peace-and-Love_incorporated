# BRX — Business Rules Exchange: WBS-250 Avionics & Software (AMPEL360-Q10)

**Product:** AMPEL360-Q10 · **WBS:** WBS-250 Avionics & Software · **Accountable Q-Division:** Q-HPC · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-250 — Avionics & Software` in the **AMPEL360-Q10** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-HPC | Q-SCIRES | Software Requirements Specification (SRS) | → | MD | Q-HPC (A) |
| 2 | Q-HPC | Q-SPACE | Data link protocol ICD | ↔ | YAML | Q-HPC (A) |
| 3 | Q-HPC | Q-MECHANICS | Thruster command interface | → | YAML | Q-HPC (A) |
| 4 | Q-HPC | Q-SCIRES | SW qualification test report (DO-178C) | → | PDF | Q-HPC (A) |
| 5 | Q-HPC | Q-DATAGOV | OBC telemetry schema | → | YAML | Q-HPC (A) |

## BRX Governance Rules

1. **Single source of truth**: the producer WBS element owns and versions all data items listed here.
2. **ICD alignment**: every row maps to a named interface in the master ICD (WBS-100 deliverable).
3. **Change control**: changes to any exchange require a BRX revision + Q-Division sign-off (Accountable: Q-HPC).
4. **Format compliance**: all S1000D DMs must pass BREX validation; YAML/JSON must conform to repo schema.
5. **Traceability**: each data item SHALL be traceable to an SRD requirement via the CSDB requirement link.

## Related

- [WBS Readme.md](../Readme.md)
- [Product BRX index](../../BRX/Readme.md)
- [Q-Divisions RACI Master](../../../../../organization/Q-Divisions/Readme.md)

**[FIN DEL DOCUMENTO]**
