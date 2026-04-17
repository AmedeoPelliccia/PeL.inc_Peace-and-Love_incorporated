# DTTA 200-10-00: Aeronaves de Combate de Quinta/Sexta Generación

> **Especificación Técnica — UTCS G3: Defence Technology Type Architecture**
> Versión 1.0 | GQAOA, INC.

---

## 1. Identificación

| Campo | Valor |
|-------|-------|
| Código UTCS | **200-10-00** |
| Dominio | G3: DTTA 200-299 |
| Categoría padre | 200-00-00: Plataformas de Combate Aéreas |
| Título | Aeronaves de Combate de Quinta/Sexta Generación |
| Nivel | Subcategoría principal |

---

## 2. Descripción General

Esta subcategoría agrupa las aeronaves de combate tripuladas (y opcionalmente no tripuladas en 6G) que incorporan las capacidades definitorias de la **quinta generación (5G)** y las emergentes de la **sexta generación (6G)**.

La clasificación generacional, aunque objeto de debate doctrinal, se basa en un **salto cualitativo en la integración de tecnologías** que operan como un *sistema de sistemas* (System of Systems, SoS), no como mejoras incrementales de una plataforma existente.

---

## 3. Quinta Generación — Características Definitorias

Las cinco capacidades que definen inequívocamente una aeronave de combate de quinta generación:

### 3.1 Stealth Integral

- Diseño de baja sección radar (RCS) concebido **desde la fase conceptual** — no como retrofit ni como kit añadido.
- Geometría de facetas, formas oblicuas y bordes alineados para minimizar retornos radar en bandas de amenaza primarias (X, Ku).
- Tratamientos **RAM (Radar Absorbent Material)** — materiales absorbentes de radar de capa fina y estructurales.
- Gestión de cavidades (toberas, entradas de aire, bodegas de armas) con bordes dentados (sawtooth), pantallas de radar y recubrimientos especializados.
- **RCS frontal típico**: 0.0001–0.01 m² (banda X), dependiente de la configuración de carga.

### 3.2 Supercrucero

- Vuelo **supersónico sostenido sin postcombustión** (afterburner) — típicamente Mach 1.2–1.6+.
- Ventajas operativas:
  - Reduce el tiempo de tránsito hacia el área de operaciones.
  - Amplía la zona de empleo y el sobre energético de los misiles lanzados.
  - Dificulta la intercepción por parte de defensas aéreas adversarias.
  - Reduce el consumo de combustible versus postcombustión.
- Requiere motores con alta relación empuje/peso y eficiencia suprasónica (bypass ratio optimizado).

### 3.3 Fusión Avanzada de Sensores

- Los datos de **múltiples sensores heterogéneos** se procesan y correlacionan automáticamente en una **imagen situacional unificada (Common Operational Picture, COP)**.
- Sensores integrados:
  - **Radar AESA** (Active Electronically Scanned Array) — detección >200 km, tracking simultáneo de múltiples blancos.
  - **IRST** (Infrared Search and Track) — detección pasiva, sin emisión electromagnética.
  - **ESM/ELINT** (Electronic Support Measures) — localización y clasificación de emisores hostiles.
  - **MAWS** (Missile Approach Warning System) — alerta de misiles 360°.
  - **Enlace de datos táctico** (Link 16, MADL) — fusión de datos entre plataformas.
- El piloto recibe una **presentación unificada** sin necesidad de identificar manualmente la fuente de cada dato.

### 3.4 Aviónica Altamente Integrada

- **Arquitectura abierta de misión** (MOSA — Modular Open Systems Approach) con capacidad de actualización por software.
- **OFP (Operational Flight Program)** — actualización del software de misión en bloques (Block upgrades) para incorporar nuevas capacidades sin modificar el hardware.
- Buses de datos de alta velocidad (Fibre Channel, Ethernet de aviónica) para interconexión de subsistemas.
- Procesadores de misión embarcados de alto rendimiento para fusión en tiempo real.

### 3.5 Agilidad Aerodinámica

- **Empuje vectorial** — control de empuje multidireccional (pitch y yaw) para superagilidad.
- Altas relaciones empuje/peso (>1.0 en peso de combate).
- **Maniobrabilidad post-stall** — capacidad de maniobra controlada más allá del ángulo de pérdida.
- Diseño aerodinámico que combina inestabilidad inherente (para agilidad) con estabilidad controlada por FBW (Fly-By-Wire).

---

## 4. Quinta Generación — Plataformas Relevantes

| Plataforma | País | Estado | Notas Clave |
|------------|------|--------|-------------|
| **F-22A Raptor** | USA (Lockheed Martin) | Operativo (2005) | Primera 5G operativa. Superioridad aérea. Supercrucero Mach 1.5+. AN/APG-77 AESA. Empuje vectorial 2D (pitch). Producción finalizada (187 unidades). |
| **F-35A/B/C Lightning II** | USA (Lockheed Martin) + aliados | Operativo (2015/16/19) | Multi-rol por defecto. Mayor programa de producción 5G global (3.000+ planeados). AN/APG-81 AESA + EOTS + DAS. Tres variantes: CTOL/STOVL/CV. |
| **J-20 Mighty Dragon** | China (Chengdu) | Operativo (2017) | Interceptor/multi-rol. Bodegas grandes para misiles PL-15. Motor objetivo WS-15 para supercrucero. Dos variantes: J-20A (monoplaza), J-20S (biplaza). |
| **Su-57 Felon** | Rusia (Sukhoi/UAC) | Producción limitada (2020+) | Radar N036 Byelka AESA + sensores L-band en bordes de ataque de alas. Superagilidad con empuje vectorial 3D. Motor objetivo Izdeliye 30 (Saturn AL-51). |
| **KF-21 Boramae** | Corea del Sur (KAI) | En desarrollo/test (2022+) | Generación 4.5/5G transicional. Inicialmente sin bodegas internas completas (previstas Block 2/3). Radar AESA + IRST. |

---

## 5. Sexta Generación — Capacidades Emergentes

La sexta generación no tiene aún una definición consensuada, pero convergen las siguientes capacidades proyectadas:

### 5.1 Opcionalidad Tripulada

- Capacidad de operar **con o sin piloto a bordo**, adaptando el nivel de autonomía al tipo de misión y al nivel de riesgo.
- Transición fluida entre modos tripulado, remotamente pilotado y autónomo.

### 5.2 Teaming con Drones (CCA / Loyal Wingman)

- **Mando de enjambres de plataformas autónomas colaborativas** (UCAV / CCA — Collaborative Combat Aircraft) desde la aeronave líder.
- Los CCA actúan como **multiplicadores de masa** baratos: sensores avanzados, portadores de armas, señuelos, nodos EW.
- Comunicación líder-CCA mediante enlaces stealth (LPI/LPD).

### 5.3 Armas de Energía Dirigida (DEW)

- Integración de **láseres de estado sólido** (SSL) de alta energía (100+ kW) para:
  - Defensa propia contra misiles y drones.
  - Ataque de precisión contra sensores y sistemas ópticos.
  - Capacidad de "magazine infinito" (limitada solo por potencia eléctrica).
- Referencia cruzada: DTTA 208-10-00 (Armas de Energía Dirigida).

### 5.4 Motor de Ciclo Adaptativo (AETD/AETP)

- **Propulsión que alterna** entre alta eficiencia en crucero (bypass alto → mayor alcance) y alto empuje en combate (bypass bajo → mayor velocidad/aceleración).
- Programas de referencia:
  - **AETP** (Adaptive Engine Transition Program) — GE XA100, Pratt & Whitney XA101.
  - Incremento proyectado: +25% alcance, +10% empuje vs. turbofans convencionales.

### 5.5 Computación Embarcada de Próxima Generación

- **IA/ML a bordo** para:
  - Gestión autónoma de la misión (replanificación en tiempo real).
  - Guerra electrónica cognitiva (EW adaptativa basada en ML).
  - Toma de decisiones tácticas en tiempo real bajo condiciones de comunicación degradada.
- Hardware: procesadores GPU/TPU embarcados con capacidad de inferencia de redes neuronales a bordo.
- Software: arquitecturas de misión actualizables OTA (Over-The-Air).

### 5.6 Conectividad Omnidireccional

- La plataforma actúa como un **nodo de la red de combate multidominio**:
  - **JADC2** (Joint All-Domain Command and Control) — USA.
  - **FCAS/SCAF** (Future Combat Air System) — Europa.
- Capacidad de recibir y transmitir datos a/desde: satélites, AWACS, UAS, fuerzas terrestres, buques, nodos cibernéticos.
- Enlaces de baja probabilidad de intercepción y detección (LPI/LPD).

---

## 6. Sexta Generación — Programas de Referencia

| Programa | Países | Estado | Notas Clave |
|----------|--------|--------|-------------|
| **NGAD** (Next Generation Air Dominance) | USA (USAF) | En desarrollo (secreto). Decisión de producción ~2024-2025. | Concepto: plataforma tripulada + familia de CCA (Increment 1). Diseño aún clasificado. Presupuesto bajo revisión por dilema coste vs. masa. |
| **GCAP** (Global Combat Air Programme) | UK / Italia / Japón | En desarrollo. IOC estimada ~2035. | Fusión de programas Tempest (UK) y F-X (Japón). Opcionalidad tripulada, motor de ciclo adaptativo (Rolls-Royce), CCA teaming. |
| **FCAS / SCAF** (Future Combat Air System) | Francia / Alemania / España | En desarrollo. Demonstrador ~2029, IOC ~2040. | Sistema de sistemas: NGF (Next Generation Fighter) + drones remotos + cloud de combate. Dassault (NGF), Airbus (drones/cloud), Indra (sensores). |

---

## 7. Subcategorías de 200-10-00

| Código | Título | Descripción |
|--------|--------|-------------|
| [**200-10-10**](./200-10-10-Multirole-Fighters.md) | Cazas Multi-rol (Stealth, Supercrucero, Fusión de Sensores) | Plataformas capaces de ejecutar misiones A/A y A/G en la misma salida |
| **200-10-20** | Bombarderos Estratégicos (Penetración, Capacidades Nucleares) | Plataformas de gran autonomía para ataque en profundidad estratégica |
| **200-10-30** | Aeronaves de Reconocimiento y Guerra Electrónica Avanzadas | Plataformas especializadas en ISR y denegación del espectro EM |

---

## 8. Implicaciones Operativas

### 8.1 Transición 5G → 6G

La transición generacional se centra en tres vectores:

1. **Integración hombre-máquina** — De piloto como operador a piloto como gestor de un equipo hombre-drones.
2. **Guerra colaborativa distribuida** — De plataformas individuales a enjambres coordinados con inteligencia distribuida.
3. **Dominancia de información** — La ventaja ya no es solo cinética; es la capacidad de **detectar primero, decidir primero, actuar primero** (OODA loop comprimido).

### 8.2 Dilema de Affordability

| Factor | 5ª Generación | 6ª Generación (proyección) |
|--------|---------------|---------------------------|
| Coste unitario | $80M–$150M+ | $200M–$300M+ (estimado) |
| Flota total | 100–3.000+ | Decenas a cientos |
| Compensación | — | CCA de $10M–$25M como multiplicadores de masa |
| Ratio previsto | — | 1 plataforma tripulada : 2-5 CCA |

### 8.3 Integración en JADC2/FCAS

Estas plataformas son **nodos clave de las arquitecturas de mando y control conjunto multidominio**, aportando:

- Sensores avanzados a la red de combate (radar AESA como sensor distribuido).
- Capacidad de designación de blancos desde fuentes externas (satélites, AWACS, UAS, fuerzas terrestres).
- Relé de comunicaciones en áreas contestadas donde los nodos terrestres están degradados.

---

## 9. Estado del Documento

| Campo | Valor |
|-------|-------|
| Versión | 1.0 |
| Estado | DRAFT |
| Clasificación UTCS | DTTA 200-10-00 |
| Data | 2026-04-17 |
