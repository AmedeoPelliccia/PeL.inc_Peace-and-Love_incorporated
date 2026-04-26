# Business Rules Exchange (BREX) — Programme Convention

This document defines the canonical layout and governance for **Business Rules
Exchanges (BREX)** that live inside each programme charter under `programs/`.

A BREX is the single source of truth for the rules a programme imposes on the
data it produces and consumes: naming, applicability, lifecycle gates,
schema contracts and approval workflow. The term is borrowed from the
S1000D *Business Rules Exchange* data module concept, but in this repository it
is generalised to cover **all** structured exchanges (CSDB, CAD, telemetry,
ledger, OPT‑INS, UTA, etc.) made by a programme with its peers.

---

## 1. Scope

Every programme directory under `programs/<PROGRAMME>/` MUST contain a `BREX/`
folder that scaffolds the rules and exchange contracts for that programme. The
scaffold provides predictable locations for:

* the human‑readable rule catalogue,
* the machine‑readable schemas / BREX data modules,
* the inbound and outbound exchange manifests with sibling programmes,
* the governance record (owner, version, approval state).

Sub‑programmes (e.g. `programs/AMPEL360/AMPEL360-BWB-Q100/`) inherit their
parent programme's BREX by default. They MAY add a local `BREX/` folder only to
**override or extend** the parent rules; otherwise they SHOULD reference the
parent.

---

## 2. Canonical Folder Layout

```
programs/<PROGRAMME>/BREX/
├── README.md              # Programme BREX overview, owner, version, status
├── rules/                 # Human‑readable rule catalogue (Markdown)
│   ├── README.md
│   ├── naming.md          # Naming, identifiers, UTCS / UTA mapping
│   ├── applicability.md   # ACT / PCT / CCT applicability model
│   └── governance.md      # Approval workflow, change control, signatories
├── exchanges/             # Per‑counterparty exchange contracts
│   ├── README.md
│   ├── inbound/           # Contracts for data this programme RECEIVES
│   │   └── .gitkeep
│   └── outbound/          # Contracts for data this programme PUBLISHES
│       └── .gitkeep
└── schemas/               # Machine‑readable contracts
    ├── README.md
    └── .gitkeep           # Place BREX DMs (.xml), JSON Schema, YAML, etc.
```

All folders MUST exist (use `.gitkeep` when empty) so that the structure stays
discoverable across programmes.

---

## 3. README.md Front‑Matter (per programme)

Each `programs/<PROGRAMME>/BREX/README.md` SHOULD provide at minimum:

| Field          | Description                                                       |
| -------------- | ----------------------------------------------------------------- |
| Programme      | Programme identifier (e.g. `AMPEL360`, `GAIA_SPACE-PRD`)          |
| BREX ID        | `BREX-<PROGRAMME>-vMAJOR.MINOR`                                   |
| Owner          | ORB function or Q‑Division responsible                            |
| Status         | `DRAFT` / `APPROVED` / `DEPRECATED`                               |
| Parent BREX    | Inherited BREX (or `n/a` for root programmes)                     |
| Counterparties | Programmes / infrastructures this programme exchanges data with   |
| Last review    | ISO‑8601 date of last governance review                           |

---

## 4. Exchanges

Each exchange contract is a single Markdown (or YAML) file inside
`exchanges/inbound/` or `exchanges/outbound/`, named:

```
<COUNTERPARTY>__<DOMAIN>__<DIRECTION>.md
```

For example: `GAIA_SPACE-PRD__telemetry__inbound.md`.

A contract states: counterparty, schema reference (in `../schemas/`), cadence,
transport, applicability filter, signatory, and revocation rules.

---

## 5. Relationship to Existing Frameworks

* **S1000D / CSDB** — Where a programme publishes S1000D content, the schemas
  in `schemas/` SHOULD include the canonical BREX data module
  (`DMC-…-022A-…xml`) and reference the CSDB `BREX/` folder defined in the
  OPT‑INS canonical leaf‑node pattern.
* **OPT‑INS / UTA** — Naming and applicability rules MUST be consistent with
  the OPT‑INS topology (O / P / T / I / N / S) and the UTA 1000‑chapter
  taxonomy (G1…G10).
* **ORB Functions** — Governance ownership lines up with the ORB function
  matrix in `organization/ORB/`.

---

## 6. Adding a New Programme

When a new programme charter is created under `programs/`, scaffold its BREX
by copying the canonical layout above. The minimum acceptable initial state is
`DRAFT` with empty `inbound/`, `outbound/` and `schemas/` placeholders.
