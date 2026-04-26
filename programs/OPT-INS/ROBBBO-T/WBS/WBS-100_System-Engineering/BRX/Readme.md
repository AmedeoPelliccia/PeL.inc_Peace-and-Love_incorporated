# BRX — Business Rules Exchange: WBS-100 System Engineering & Management (ROBBBO-T)

**Product:** ROBBBO-T · **WBS:** WBS-100 System Engineering & Management · **Accountable Q-Division:** Q-SCIRES · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-100 — System Engineering & Management` in the **ROBBBO-T** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-SCIRES | All Q-Divisions | SRD (System Requirements Document) | → | MD | Q-SCIRES (A) |
| 2 | Q-SCIRES | All WBS leads | ICD Master Register | → | MD | Q-SCIRES (A) |
| 3 | Q-SCIRES | Q-DATAGOV | CSDB document register | → | YAML | Q-SCIRES (A) |
| 4 | All WBS leads | Q-SCIRES | Risk register inputs | → | YAML | Q-SCIRES (A) |
| 5 | Q-SCIRES | ORB-PMO | Programme schedule | → | XML | Q-SCIRES (A) |

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
