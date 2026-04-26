# BRX — Business Rules Exchange: WBS-400 Launch Services (ROBBBO-T)

**Product:** ROBBBO-T · **WBS:** WBS-400 Launch Services · **Accountable Q-Division:** Q-INDUSTRY · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-400 — Launch Services` in the **ROBBBO-T** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-INDUSTRY | Q-STRUCTURES | Rideshare / dispenser ICD | ↔ | MD | Q-INDUSTRY (A) |
| 2 | Q-INDUSTRY | Q-SCIRES | Launch campaign plan | → | PDF | Q-INDUSTRY (A) |
| 3 | Q-INDUSTRY | Q-GROUND | Range safety plan | → | PDF | Q-INDUSTRY (A) |

## BRX Governance Rules

1. **Single source of truth**: the producer WBS element owns and versions all data items listed here.
2. **ICD alignment**: every row maps to a named interface in the master ICD (WBS-100 deliverable).
3. **Change control**: changes to any exchange require a BRX revision + Q-Division sign-off (Accountable: Q-INDUSTRY).
4. **Format compliance**: all S1000D DMs must pass BREX validation; YAML/JSON must conform to repo schema.
5. **Traceability**: each data item SHALL be traceable to an SRD requirement via the CSDB requirement link.

## Related

- [WBS Readme.md](../Readme.md)
- [Product BRX index](../../BRX/Readme.md)
- [Q-Divisions RACI Master](../../../../../organization/Q-Divisions/Readme.md)

**[FIN DEL DOCUMENTO]**
