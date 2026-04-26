# BRX — Business Rules Exchange: WBS-200 Flight System (AMPEL360-Q10)

**Product:** AMPEL360-Q10 · **WBS:** WBS-200 Flight System · **Accountable Q-Division:** Q-STRUCTURES · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-200 — Flight System` in the **AMPEL360-Q10** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-STRUCTURES | Q-MECHANICS, Q-HPC | Flight system mass budget | ↔ | XLSX | Q-STRUCTURES (A) |
| 2 | Q-STRUCTURES | Q-SCIRES | Vehicle-level ICD | → | MD | Q-STRUCTURES (A) |
| 3 | Q-STRUCTURES | Q-INDUSTRY | Assembly drawing tree | → | PDF | Q-STRUCTURES (A) |

## BRX Governance Rules

1. **Single source of truth**: the producer WBS element owns and versions all data items listed here.
2. **ICD alignment**: every row maps to a named interface in the master ICD (WBS-100 deliverable).
3. **Change control**: changes to any exchange require a BRX revision + Q-Division sign-off (Accountable: Q-STRUCTURES).
4. **Format compliance**: all S1000D DMs must pass BREX validation; YAML/JSON must conform to repo schema.
5. **Traceability**: each data item SHALL be traceable to an SRD requirement via the CSDB requirement link.

## Related

- [WBS Readme.md](../Readme.md)
- [Product BRX index](../../BRX/Readme.md)
- [Q-Divisions RACI Master](../../../../../organization/Q-Divisions/Readme.md)

**[FIN DEL DOCUMENTO]**
