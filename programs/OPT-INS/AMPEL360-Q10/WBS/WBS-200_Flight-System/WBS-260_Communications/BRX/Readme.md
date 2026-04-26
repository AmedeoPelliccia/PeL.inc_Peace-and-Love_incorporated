# BRX — Business Rules Exchange: WBS-260 Communications (AMPEL360-Q10)

**Product:** AMPEL360-Q10 · **WBS:** WBS-260 Communications · **Accountable Q-Division:** Q-SPACE · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-260 — Communications` in the **AMPEL360-Q10** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-SPACE | Q-GROUND | Link budget (S-band, Ka-band) | → | PDF | Q-SPACE (A) |
| 2 | Q-SPACE | Q-HPC | Communications protocol ICD | ↔ | YAML | Q-SPACE (A) |
| 3 | Q-SPACE | Q-STRUCTURES | Antenna mechanical interface | ↔ | MD | Q-SPACE (A) |
| 4 | Q-SPACE | Q-DATAGOV | RF spectrum allocation plan | → | PDF | Q-SPACE (A) |

## BRX Governance Rules

1. **Single source of truth**: the producer WBS element owns and versions all data items listed here.
2. **ICD alignment**: every row maps to a named interface in the master ICD (WBS-100 deliverable).
3. **Change control**: changes to any exchange require a BRX revision + Q-Division sign-off (Accountable: Q-SPACE).
4. **Format compliance**: all S1000D DMs must pass BREX validation; YAML/JSON must conform to repo schema.
5. **Traceability**: each data item SHALL be traceable to an SRD requirement via the CSDB requirement link.

## Related

- [WBS Readme.md](../Readme.md)
- [Product BRX index](../../BRX/Readme.md)
- [Q-Divisions RACI Master](../../../../../organization/Q-Divisions/Readme.md)

**[FIN DEL DOCUMENTO]**
