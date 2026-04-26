# BRX — Business Rules Exchange: WBS-600 Integration, Assembly & Test (AMPEL360-Q10)

**Product:** AMPEL360-Q10 · **WBS:** WBS-600 Integration, Assembly & Test · **Accountable Q-Division:** Q-INDUSTRY · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-600 — Integration, Assembly & Test` in the **AMPEL360-Q10** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-INDUSTRY | Q-SCIRES | AIT plan and test procedures | → | MD | Q-INDUSTRY (A) |
| 2 | Q-INDUSTRY | All WBS leads | Interface verification reports | → | PDF | Q-INDUSTRY (A) |
| 3 | Q-INDUSTRY | Q-SCIRES | Acceptance test results | → | PDF | Q-INDUSTRY (A) |

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
