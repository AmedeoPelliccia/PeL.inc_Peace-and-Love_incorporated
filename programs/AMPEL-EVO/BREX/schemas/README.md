# `schemas/` — Machine‑Readable Contracts

This folder holds the machine‑readable artefacts that back the rules in
`../rules/` and the exchange contracts in `../exchanges/`. Acceptable formats:

* S1000D BREX data modules (`DMC-…-022A-…xml`),
* JSON Schema (`*.schema.json`),
* YAML schema (`*.schema.yaml`),
* XSD, Avro, Protobuf or other contract formats as needed.

Each schema SHOULD declare its identifier, version and the rule sheet(s) it
implements. Exchange contracts under `../exchanges/` MUST reference a schema
file in this folder by relative path.

> See [`programs/BREX-CONVENTION.md`](../../../BREX-CONVENTION.md) for the
> programme‑wide convention.
