# Analizador de Gastos de Capacitación

Aplicación de consola (CLI) desarrollada en Python para analizar los gastos de capacitación de un área corporativa. Realiza cálculos estadísticos, búsquedas de extremos, filtrados, ordenamientos manuales y evaluaciones presupuestarias sin depender de funciones integradas avanzadas.

---

## Objetivo de aprendizaje

Consolidar el **Principio 2: Control de flujo y estructuras de datos básicas**:
- Almacenamiento y manipulación de registros en una **lista de diccionarios**.
- Búsqueda manual de valores máximos y mínimos mediante iteración explicita.
- Algoritmos manuales de acumulación y conteos bajo condicionales restrictivas (`>` vs `>=`).
- Algoritmo de **ordenación manual (Bubble Sort)** preservando la inmutabilidad de la estructura original.
- Control defensivo contra divisiones por cero e interacción con listas vacías.

---

## Mapa de Principios de la Saga Python 2026

- [X] **Principio 1. Fundamentos del lenguaje Python**
- [X] **Principio 2. Control de flujo y estructuras de datos básicas**
- [ ] Principio 3. Funciones, parámetros y alcance de variables
- [ ] Principio 4. Manejo de errores y excepciones
- [ ] Principio 5. Comprensiones y código idiomático de Python
- [ ] Principio 6. Calidad del código y convenciones profesionales
- [ ] Principio 7. Programación Orientada a Objetos (POO)
- [ ] Principio 8. Complejidad algorítmica y análisis de eficiencia
- [ ] Principio 9. Módulos, paquetes y reutilización de código
- [ ] Principio 10. PIP, entornos virtuales y dependencias
- [ ] Principio 11. Aplicaciones CRUD y persistencia de datos
- [ ] Principio 12. Testing y validación automatizada
- [ ] Principio 13. Estadística computacional, simulación y programación dinámica
- [ ] Principio 14. Arquitectura de proyectos y distribución de paquetes
- [ ] Principio 15. Principios SOLID y patrones de diseño

---

## Funcionalidades principales

1. **Visualización completa:** Presentación de actividades en formato tabla de consola.
2. **Totales y Promedios:** Acumulación del costo total y costo promedio por actividad/participante.
3. **Conteos por umbrales:** Evaluación diferenciada de costos con condiciones estrictas (`> 500`) y no estrictas (`>= 500`).
4. **Búsqueda manual de extremos:** Determinación del registro más costoso y más económico sin usar `max()` ni `min()`.
5. **Filtrado dinámico:** Consulta por categoría o monto límite.
6. **Ordenamiento manual:** Ordenamiento ascendente y descendente sin modificar el listado original, omitiendo `sort()` y `sorted()`.
7. **Informe de presupuesto:** Evaluación del total comprometido frente a una base de S/ 3,000.00.
8. **Modo prueba lista vacía:** Opción para alternar el estado a lista vacía para verificar el comportamiento defensivo.

---

## Estructura del repositorio

```text
2026_10_P02_R03_analizador-gastos-capacitacion/
├── .gitignore
├── main.py
└── README.md