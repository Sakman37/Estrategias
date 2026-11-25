# Navegando mareas: rutas accesibles en un campus

Prototipo didáctico de navegación en una red peatonal pequeña. Implementa Dijkstra y tres políticas intercambiables: fastest, accessible y balanced. Usa solo Python 3.10+ y biblioteca estándar.

## Ejecutar
`python src/router.py`

## Probar
`python -m unittest discover -s tests -v`

## Reproducir resultados
`python scripts/benchmark.py`

La red y sus métricas son sintéticas para la actividad; no representan un campus real ni tráfico observado. `minutes` informa tiempo físico estimado acumulado; `score` es el costo de la política. `visited` cuenta nodos extraídos de la cola. Los tiempos de ejecución medidos dependen del equipo y no se usan como evidencia comparativa entre algoritmos.

## Estructura
- `src/router.py`: dominio, estrategias y algoritmo.
- `tests/`: pruebas funcionales.
- `scripts/benchmark.py`: medición reproducible y CSV.
- `docs/uml/`: fuentes Mermaid de los cuatro modelos solicitados.
- `evidence/`: resultados y gráfico.
- `INFORME.pdf`, `PRESENTACION.pptx`, `GUION_VIDEO.md`: entregables.

## Alcance
Es una demostración CLI offline, no un servicio de producción ni una aplicación móvil. Las rutas accesibles excluyen escaleras y penalizan pendientes/superficie rugosa según supuestos parametrizables. Debe validarse con usuarios y datos reales antes de uso operativo.
