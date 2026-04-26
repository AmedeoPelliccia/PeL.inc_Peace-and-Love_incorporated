# BRX — Business Rules Exchange: WBS-270 Guidance, Navigation & Control (AMPEL360-Q10)

**Product:** AMPEL360-Q10 · **WBS:** WBS-270 Guidance, Navigation & Control · **Accountable Q-Division:** Q-HPC · **Status:** draft

## Purpose

This repository defines the **Business Rules Exchange (BRX)** for `WBS-270 — Guidance, Navigation & Control` in the **AMPEL360-Q10** programme.
A BRX specifies the authoritative rules governing every data exchange crossing the boundary of this WBS element.

## Exchange Registry

| # | Producer | Consumer | Data Item | Direction | Format | Governance |
|---|----------|----------|-----------|-----------|--------|------------|
| 1 | Q-HPC | Q-SCIRES | GNC algorithm design document | → | MD | Q-HPC (A) |
| 2 | Q-HPC | Q-MECHANICS | Actuator command interface (thrusters/RWs) | → | YAML | Q-HPC (A) |
| 3 | Q-HPC | Q-SPACE | Navigation data feed (GNSS/star tracker) | ← | JSON | Q-HPC (A) |
| 4 | Q-HPC | Q-GROUND | RPO trajectory plan (GAIA rendezvous) | → | JSON | Q-HPC (A) |

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
