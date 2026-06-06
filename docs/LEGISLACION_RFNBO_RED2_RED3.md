# 📋 Marco Regulatorio RFNBO - RED II/III (UE 2023/2413)

## 1. Introducción: ¿Qué es el Hidrógeno Verde Certificado RFNBO?

**RFNBO** (Renewable Fuels of Non-Biological Origin) es la categoría técnico-legal que define el **hidrógeno de origen renovable** producido mediante electrólisis de agua, alimentada exclusivamente por energía eléctrica de **fuentes renovables certificadas**.

### Fundamento Legal
- **Directiva RED III (UE 2023/2413):** Enmienda la Directiva RED II estableciendo requisitos de descarbonización en transporte e industria
- **Reglamento delegado (UE) 2023/1185:** Define los criterios técnicos para la producción y certificación de RFNBO
- **Reglamento delegado (UE) 2023/2514:** Especifica métodos de cálculo de la huella de carbono

---

## 2. Criterios Técnicos de Conformidad RFNBO

### 2.1 Balance Energético Temporal (Energy-to-Mass)

El requisito fundamental: **la energía eléctrica renovable suministrada DEBE ser igual o superior al consumo del electrolizador**.

\`\`\`
┌─────────────────────────────────────────────────────┐
│ VALIDACIÓN CRÍTICA: MWh_RENOVABLE ≥ MWh_CONSUMO    │
└─────────────────────────────────────────────────────┘
\`\`\`

| Parámetro | Símbolo | Unidad | Requisito | Norma |
|-----------|---------|--------|-----------|-------|
| Energía renovable disponible | MWh_PPA | MWh | ≥ MWh_consumo | RED III Art. 25.2 |
| Energía consumida electrolizador | MWh_ELEC | MWh | ≤ MWh_PPA | RED III Art. 25.2 |
| Diferencia temporal máxima | ΔT | Horas | ≤ 1 mes (30 días) | RED III Anexo V.2 |
| Correlación geográfica | Nodo_RED | Zona | Misma zona o adyacente | RED III Art. 25.3 |

**Fórmula de Cálculo:**
\`\`\`
RFNBO_CONFORME = (MWh_PPA ≥ MWh_ELEC) AND (ΔT ≤ 30 días) AND (Nodo_RENOVABLE == Nodo_CONSUMO)
\`\`\`

**Implementación en SAP:**
\`\`\`json
{
  "Z_ENERGY_BALANCE": "MWh_PPA >= MWh_ELEC",
  "Z_MWH_RENOVABLE": 12.5,
  "Z_MWH_CONSUMO": 10.120,
  "Z_CONFORMIDAD_ENERGETICA": "PASS"
}
\`\`\`

---

### 2.2 Análisis Químico: Pureza del Hidrógeno (ISO 14687)

El hidrógeno debe cumplir la **norma ISO 14687-2:2019** para combustible de calidad.

| Impureza | Símbolo | Límite Máx. | Peligro si se Supera | Método Prueba |
|----------|---------|-------------|----------------------|---------------|
| **Pureza Total** | %H₂ | ≥ 99.9 % | Fragilización del acero (Art. 15 RD 809) | ISO 14687-2 §5.1 |
| Oxígeno | O₂ | 5 ppm | Combustión espontánea | ISO 14687-2 §5.2 |
| Nitrógeno | N₂ | 100 ppm | Reducción poder calorífico | ISO 14687-2 §5.3 |
| Dióxido carbono | CO₂ | 2 ppm | Corrosión acelerada en válvulas | ISO 14687-2 §5.4 |
| Monóxido carbono | CO | 0.2 ppm | Envenenamiento catalizadores | ISO 14687-2 §5.5 |
| Agua | H₂O | 3 ppm | Corrosión bajo tensión (CUT) | ISO 14687-2 §5.6 |
| Azufre | S | 0.004 ppm | Envenenamiento fuel-cell | ISO 14687-2 §5.7 |

**Degradación automática de lote en SAP MM si:**
\`\`\`python
if PUREZA_H2 < 99.9:
    estado_lote = "B"  # Restringido
    regla_VCH1 = "BLOCKED"  # Bloquea despacho
    razon_bloqueo = "ISO 14687 INCUMPLIMIENTO"
\`\`\`

---

## 3. Huella de Carbono (Criterio de Descarbonización)

### 3.1 Cálculo de Emisiones CO₂eq

**Hidrógeno Verde Certificado RFNBO:**
\`\`\`
Huella = 0.38 gCO2eq/MJ (máximo permitido)
\`\`\`

**Comparación con alternativas:**
- ✅ Hidrógeno Verde (RFNBO): **0.38 gCO2eq/MJ**
- ❌ Hidrógeno Gris (Reforma SMR): **13.80 gCO2eq/MJ** (36x más emisiones)
- ❌ Hidrógeno Marrón (Carbón): **27.50 gCO2eq/MJ** (72x más emisiones)

### 3.2 Método de Cálculo (Reglamento delegado 2023/2514)

\`\`\`
CF_TOTAL = (E_RENOVABLE × FE_RED + Σ OTRAS_EMISIONES) / Energía_H2_Producida

donde:
- E_RENOVABLE: Energía consumida del electrolizador (MWh)
- FE_RED: Factor de emisión de la red (gCO2eq/MWh) = 50 gCO2eq/MWh (objetivo UE 2030)
- OTRAS_EMISIONES: Transporte, almacenamiento (<0.05 gCO2eq/MJ)
- Energía_H2_Producida: Contenido energético del H₂ (33.33 MWh/t)
\`\`\`

---

## 4. Certificación y Trazabilidad Digital

### 4.1 Números de Certificado RFNBO

Formato estandarizado para garantizar la trazabilidad:

\`\`\`
EU-RFNBO-YYYYMMDDHH-FACILITYID
        │       │  │    └─ Identificador planta (ELEC01)
        │       │  └────── Hora de corte (00-23)
        │       └───────── Fecha (20250606)
        └───────────────── Prefijo UE RFNBO
\`\`\`

**Ejemplo válido:**
\`\`\`
EU-RFNBO-20250606-14-ELEC01
\`\`\`

---

## 5. Checklist de Conformidad para Cumplimiento

\`\`\`
☐ Energy Balance (MWh_renovable ≥ MWh_consumo en 30 días)
☐ Pureza ISO 14687 (≥ 99.9%)
☐ Huella carbono (≤ 0.38 gCO2eq/MJ)
☐ Correlación temporal (ΔT ≤ 1 mes)
☐ Correlación geográfica (misma zona RED)
☐ Número certificado EU-RFNBO generado
☐ Documento de conformidad digital (DPP)
☐ Trazabilidad inmutable SAP MM
☐ Bloqueo automático en VCH1 si falla
☐ Auditoría registrada en AUSP
\`\`\`

---

**Documento Versión:** 1.0  
**Fecha:** Junio 2025  
**Clasificación:** Normativa Técnica SAP
