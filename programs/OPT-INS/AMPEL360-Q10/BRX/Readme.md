# BRX — Business Rules Exchange: PROG-LEVEL Programme-Level Cross-WBS Exchange (AMPEL360-Q10)

**Product:** AMPEL360-Q10 · **WBS:** PROG-LEVEL Programme-Level Cross-WBS Exchange · **Accountable Q-Division:** Q-SCIRES · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `PROG-LEVEL — Programme-Level Cross-WBS Exchange` in the **AMPEL360-Q10** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-SCIRES (WBS-100) | All WBS leads | SRD baseline | → | MD | Q-SCIRES (A) |
| 2 | Q-STRUCTURES (WBS-200) | Q-SCIRES, Q-MECHANICS | Vehicle mass budget | ↔ | XLSX | Q-SCIRES (A) |
| 3 | Q-SPACE (WBS-260) | Q-GROUND (WBS-300) | COMMS link budget | → | PDF | Q-SCIRES (A) |
| 4 | Q-HPC (WBS-250) | Q-SCIRES | SW development plan | → | MD | Q-SCIRES (A) |
| 5 | Q-INDUSTRY (WBS-600) | Q-SCIRES | AIT test results | → | PDF | Q-SCIRES (A) |

## BRX Governance Rules

1. **Single source of truth**: the producer WBS element owns and versions all data items listed here.
2. **ICD alignment**: every row maps to a named interface in the master ICD (WBS-100 deliverable).
3. **Change control**: changes to any exchange require a BRX revision + Q-Division sign-off (Accountable: Q-SCIRES).
4. **Format compliance**: all S1000D DMs must pass BREX validation; YAML/JSON must conform to repo schema.
5. **Traceability**: each data item SHALL be traceable to an SRD requirement via the CSDB requirement link.

## Related

- [WBS Readme.md](../Readme.md)
- [Product BRX index](../../BRX/Readme.md)
- [Q-Divisions RACI Master](../../../../../organization/Q-Divisions/Readme.md)

**[FIN DEL DOCUMENTO]**
