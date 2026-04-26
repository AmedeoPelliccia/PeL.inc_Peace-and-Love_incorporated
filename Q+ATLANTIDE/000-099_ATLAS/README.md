# 000-099 ATLAS — Aircraft Top-Level Architecture System

**Architecture Code:** ATLAS
**Master Range:** `000-099`
**Register:** ATLAS-1000 (subpart of Q+ATLANTIDE)
**Classification:** Standard

## Purpose

Aircraft top-level architecture band covering identification, ground handling, core aircraft systems, mechanical protection, avionics & APU, primary structures, traditional & alternative propulsion, and aircraft-type expansion.

## Sub-ranges (`XX0-XX9`)

| Subrange | Block | Primary Q-Division |
|---:|---|---|
| 000-009 | Información General y Servicio | Q-DATAGOV |
| 010-019 | Manejo en Tierra & Servicio | Q-GROUND |
| 020-029 | Sistemas Core de Aeronave | Q-AIR |
| 030-039 | Protección & Sistemas Mecánicos | Q-MECHANICS |
| 040-049 | Aviónica, Información & APU | Q-DATAGOV |
| 050-059 | Estructuras Primarias e Interfaces de Programa / Q-Division | Q-STRUCTURES |
| 060-079 | Propulsión Tradicional & Eco-Tech | Q-GREENTECH |
| 080-089 | Propulsión Alternativa & Cuántica | Q-GREENTECH |
| 090-099 | Tipos Específicos & Expansión | Q-HORIZON |

## Governance

Governed by the controlled baseline [`organization/Q+ATLANTIDE.md`](../../organization/Q+ATLANTIDE.md). Templates declared in this band must populate `architecture_band`, `architecture_code = ATLAS`, `q_division_owner` and `orb_function_support`. The **No-AAA Rule (N-004)** applies: do not use "AAA" — use "Programme / Q-Division Interface" instead. Subrange `050-059` shall use the title fragment **"Estructuras Primarias e Interfaces de Programa / Q-Division"** (N-005).
