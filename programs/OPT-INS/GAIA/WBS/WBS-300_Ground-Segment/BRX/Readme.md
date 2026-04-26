# BRX — Business Rules Exchange: WBS-300 Ground Segment (GAIA)

**Product:** GAIA · **WBS:** WBS-300 Ground Segment · **Accountable Q-Division:** Q-GROUND · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-300 — Ground Segment` in the **GAIA** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-SPACE | Q-GROUND | Tracking & relay network schedule | → | XML | Q-GROUND (A) |
| 2 | Q-GROUND | Q-HPC | Uplink command sequences | → | XML | Q-GROUND (A) |
| 3 | Q-GROUND | Q-SCIRES | MCC ops concept & crew support plan | → | MD | Q-GROUND (A) |

## BRX Governance Rules

1. **Single source of truth**: the producer WBS element owns and versions all data items listed here.
2. **ICD alignment**: every row maps to a named interface in the master ICD (WBS-100 deliverable).
3. **Change control**: changes to any exchange require a BRX revision + Q-Division sign-off (Accountable: Q-GROUND).
4. **Format compliance**: all S1000D DMs must pass BREX validation; YAML/JSON must conform to repo schema.
5. **Traceability**: each data item SHALL be traceable to an SRD requirement via the CSDB requirement link.

## Related

- [WBS Readme.md](../Readme.md)
- [Product BRX index](../../BRX/Readme.md)
- [Q-Divisions RACI Master](../../../../../organization/Q-Divisions/Readme.md)

**[FIN DEL DOCUMENTO]**
