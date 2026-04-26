# BREX — AMPEL360

Business Rules Exchange scaffold for the **AMPEL360** programme (atmospheric &
space platforms: Q100, Q250, PLUS, PLUSPLUS, XWLRGA, AC‑MACH, C‑MAX).

| Field          | Value                                                    |
| -------------- | -------------------------------------------------------- |
| Programme      | AMPEL360                                                 |
| BREX ID        | `BREX-AMPEL360-v0.1`                                     |
| Owner          | _to be assigned_                                         |
| Status         | `DRAFT`                                                  |
| Parent BREX    | n/a                                                      |
| Counterparties | AMPEL‑EVO, GAIA_SPACE-PRD, Robbbo‑T, QUANTUM             |
| Last review    | _pending_                                                |

Sub‑programmes (`AMPEL360-BWB-Q100`, `AMPEL360-BWB-Q250`, …) inherit this BREX
by default and MAY add a local `BREX/` only to override or extend it.

## Layout

* [`rules/`](./rules/) — naming, applicability, governance rule sheets
* [`exchanges/`](./exchanges/) — inbound / outbound exchange contracts
* [`schemas/`](./schemas/) — machine‑readable contracts (BREX DMs, JSON / YAML schemas)

> See the programme‑wide convention in
> [`../../BREX-CONVENTION.md`](../../BREX-CONVENTION.md).
