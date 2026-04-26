# `exchanges/` — Per‑Counterparty Exchange Contracts

This folder holds one Markdown (or YAML) file per data exchange the programme
maintains with another programme, infrastructure or external party. Files are
split between:

* `inbound/`  — data **received** by this programme,
* `outbound/` — data **published** by this programme.

## File naming

```
<COUNTERPARTY>__<DOMAIN>__<DIRECTION>.md
```

Examples:

* `GAIA_SPACE-PRD__telemetry__inbound.md`
* `Robbbo-T_Robotics_PRD__manufacturing__outbound.md`

## Minimum content per contract

| Field           | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| Counterparty    | Programme / org identifier                                     |
| Direction       | `inbound` or `outbound`                                        |
| Schema          | Reference to a file under `../schemas/`                        |
| Cadence         | Frequency / trigger of the exchange                            |
| Transport       | Mechanism (Git, ledger, REST, MQTT, file drop, …)              |
| Applicability   | ACT / PCT / CCT filter that selects what is exchanged          |
| Signatory       | Approver on each side                                          |
| Revocation      | Conditions under which the contract is suspended or revoked    |

> See [`programs/BREX-CONVENTION.md`](../../../BREX-CONVENTION.md) for the
> programme‑wide convention.
