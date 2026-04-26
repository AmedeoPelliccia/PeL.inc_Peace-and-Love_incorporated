# `rules/` — Human‑Readable Rule Catalogue

This folder holds the human‑readable rules that the programme imposes on the
data it produces and consumes. Each file is a Markdown rule sheet. The
machine‑readable counterparts (BREX data modules, JSON Schema, YAML schema)
live under `../schemas/`.

## Standard files

| File              | Purpose                                                        |
| ----------------- | -------------------------------------------------------------- |
| `naming.md`       | Identifier, file‑name, UTCS / UTA mapping rules                |
| `applicability.md`| ACT / PCT / CCT applicability model and product attributes     |
| `governance.md`   | Approval workflow, signatories, change‑control, revocation     |

Add additional rule sheets as needed (e.g. `security.md`, `units.md`,
`provenance.md`). Cross‑link them from the parent `BREX/README.md`.

> See [`programs/BREX-CONVENTION.md`](../../../BREX-CONVENTION.md) for the
> programme‑wide convention.
