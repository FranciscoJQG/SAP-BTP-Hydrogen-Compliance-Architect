# 🤝 Guía de Contribución

## Código de Conducta

Nos comprometemos a proporcionar un entorno acogedor e inclusivo para todos los colaboradores.

### Nuestros Compromisos
- ✅ Ser respetuosos y constructivos
- ✅ Aceptar crítica constructiva
- ✅ Enfocarnos en lo mejor para la comunidad
- ✅ Mantener confidencialidad de regulaciones internas

## Cómo Contribuir

### 1. Fork del Repositorio

```bash
# En GitHub:
# Click "Fork" en la esquina superior derecha
```

### 2. Clonar tu Fork

```bash
git clone https://github.com/YOUR_USERNAME/SAP-BTP-Hydrogen-Compliance-Architect.git
cd SAP-BTP-Hydrogen-Compliance-Architect
```

### 3. Crear Rama Feature

```bash
git checkout -b feature/mi-funcionalidad
# Ejemplos:
# - feature/validators-co2
# - bugfix/purity-calculation
# - docs/sap-integration
```

### 4. Hacer Cambios

```bash
# Editar archivos
# Asegurar que el código sigue el estilo del proyecto
```

### 5. Commit con Mensajes Claros

```bash
git commit -m "feat: Agregar validador de pureza ISO 14687

- Implementa verificación ISO 14687
- Valida ≥99.9% purity requirement
- Agrega test cases

Closes #123"
```

**Formato de commits**:
- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Documentación
- `style:` Formato, linting
- `refactor:` Refactorización
- `test:` Tests
- `chore:` Tareas administrativas

### 6. Push a tu Fork

```bash
git push origin feature/mi-funcionalidad
```

### 7. Crear Pull Request

1. Ir a tu fork en GitHub
2. Click en "Compare & pull request"
3. Completar plantilla de PR
4. Describir cambios claramente
5. Referenciar issues relacionados

### 8. Code Review

- Los maintainers revisarán tu PR
- Responder a comentarios constructivamente
- Hacer cambios solicitados si es necesario

## Estándares de Código

### Python Style Guide (PEP 8)

```python
# ✅ BIEN
def validate_rfnbo_compliance(batch_data: dict) -> bool:
    """Validar cumplimiento RFNBO del lote.
    
    Args:
        batch_data: Diccionario con datos del lote
        
    Returns:
        bool: True si cumple RFNBO
    """
    purity = batch_data.get("purity_percent")
    carbon = batch_data.get("carbon_footprint")
    
    return purity >= 99.9 and carbon <= 0.38

# ❌ MAL
def validate(b):
    return b['p'] >= 99.9 and b['c'] <= 0.38
```

### Docstrings

```python
def calculate_carbon_footprint(energy_mwh: float, source: str) -> float:
    """Calcular huella de carbono en gCO2eq/MJ.
    
    Calcula la huella de carbono según la fuente de energía
    y el estándar RFNBO UE 2023/2413.
    
    Args:
        energy_mwh: Energía en MWh
        source: Fuente ('renewable', 'grid', 'fossil')
        
    Returns:
        float: Huella de carbono en gCO2eq/MJ
        
    Raises:
        ValueError: Si source no es válido
        
    Example:
        >>> calculate_carbon_footprint(1000, 'renewable')
        0.38
    """
    # Implementación
    pass
```

### Type Hints

```python
from typing import Dict, List, Optional, Tuple

def process_batches(
    batches: List[Dict[str, float]],
    config: Optional[Dict[str, str]] = None
) -> Tuple[List[str], List[str]]:
    """Procesar múltiples lotes."""
    pass
```

## Estructura de Tests

```python
# tests/test_rfnbo_validator.py
import pytest
from src.validators.rfnbo_validator import RFNBOValidator

class TestRFNBOValidator:
    """Tests para RFNBOValidator."""
    
    @pytest.fixture
    def validator(self):
        """Crear instancia de validator."""
        return RFNBOValidator()
    
    def test_valid_rfnbo_compliance(self, validator):
        """Test: Lote que cumple RFNBO."""
        batch = {
            "facility_id": "PLANT-001",
            "purity_percent": 99.95,
            "carbon_footprint_gco2_per_mj": 0.35
        }
        assert validator.validate(batch)["valid"] is True
    
    def test_invalid_purity(self, validator):
        """Test: Pureza insuficiente."""
        batch = {
            "facility_id": "PLANT-001",
            "purity_percent": 99.5,  # < 99.9%
            "carbon_footprint_gco2_per_mj": 0.35
        }
        assert validator.validate(batch)["valid"] is False
    
    @pytest.mark.parametrize("purity", [99.0, 99.5, 99.8])
    def test_purity_threshold(self, validator, purity):
        """Test: Umbrales de pureza."""
        batch = {
            "facility_id": "PLANT-001",
            "purity_percent": purity,
            "carbon_footprint_gco2_per_mj": 0.35
        }
        assert validator.validate(batch)["valid"] is False
```

## Documentación

### Markdown Style

```markdown
# Título Principal

Texto introductorio clara y conciso.

## Subtítulo

### Subsubtítulo

- Punto 1
- Punto 2
  - Subpunto 2.1

**Negrita** para énfasis
_Cursiva_ para énfasis suave

```código
Código en bloque
```

[Link descriptivo](url)
```

## Reportar Bugs

### Plantilla de Issue

```markdown
**Descripción**
Descripción clara del bug.

**Pasos para reproducir**
1. Paso 1
2. Paso 2
3. Bug ocurre

**Comportamiento esperado**
Qué debería pasar

**Comportamiento actual**
Qué pasa en realidad

**Logs/Screenshots**
Adjuntar evidencia

**Entorno**
- OS: macOS 14
- Python: 3.11.2
- Rama: develop
```

## Solicitar Características

### Plantilla de Feature Request

```markdown
**Descripción**
Descripción clara de la característica solicitada

**Problema que resuelve**
Contexto del problema

**Solución propuesta**
Cómo implementarla

**Contexto adicional**
Información relevante
```

## Proceso de Release

1. Preparar changeset en CHANGELOG.md
2. Crear tag: `git tag v1.0.0`
3. Push tags: `git push origin --tags`
4. GitHub Actions genera release automáticamente

### Versionamiento Semántico

Seguimos [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH` (ej: 1.2.3)
- MAJOR: Cambios incompatibles
- MINOR: Nuevas funcionalidades compatibles
- PATCH: Fixes

## Reconocimiento

Todos los colaboradores serán:
- ✅ Listados en CONTRIBUTORS.md
- ✅ Mencionados en releases
- ✅ Reconocidos en README

---

**Gracias por contribuir! 🙏**

¿Preguntas? Abre una discussion en GitHub.

**Última actualización**: 2026-06-06
