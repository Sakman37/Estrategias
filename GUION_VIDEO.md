# Guion individual para el video

**Título:** Navegando mareas: rutas accesibles en un campus
**Estudiante:** completar nombre
**Enlace YouTube no listado:** pendiente de grabación y publicación
**Duración estimada:** 8 minutos (máximo permitido: 15 minutos)

## Texto para narrar

### 1. Presentación (0:00–0:40)
Hola. Soy [nombre] y presentaré la Actividad 6 de Arquitectura de Software, titulada “Navegando mareas”. En este trabajo diseñé e implementé un prototipo que busca rutas peatonales en un campus usando distintas preferencias de navegación.

### 2. Problema y alcance (0:40–1:40)
La ruta que toma menos minutos no siempre es adecuada para todas las personas. Puede incluir escaleras, pendientes o superficies irregulares. Por eso el prototipo ofrece tres opciones: ruta más rápida, ruta accesible y ruta equilibrada. El mapa y los tiempos son sintéticos y se usan solo para esta demostración.

### 3. Arquitectura y UML (1:40–3:20)
El campus se representa como un grafo. Cada tramo guarda un tiempo estimado, pendiente, superficie y si tiene escaleras. El motor Router aplica el algoritmo de Dijkstra para buscar el menor costo. El patrón Strategy separa el cálculo del costo en tres políticas intercambiables. En los diagramas UML muestro los componentes, las clases, la secuencia de consulta y el flujo de decisión.

### 4. Demostración del prototipo (3:20–5:40)
Ahora ejecuto `python src/router.py`. La salida muestra las rutas entre Entrada y Laboratorios para las tres políticas. La ruta rápida tarda [leer el valor que aparece] minutos y [indicar si usa escaleras]. La opción accesible evita escaleras y estima [leer el valor] minutos. La equilibrada combina tiempo y penalizaciones.

También puedo excluir un tramo cerrado. Para ello paso, por ejemplo, el cierre entre Plaza y Biblioteca a la consulta. El motor lo descarta y calcula una alternativa o informa que no hay ruta.

### 5. Pruebas y resultados (5:40–6:40)
Ejecuto `python -m unittest discover -s tests -v`. Las seis pruebas verifican una ruta válida, la exclusión de escaleras en la opción accesible, el efecto de cierres, el caso en que origen y destino coinciden, un nodo desconocido y la ausencia de ruta. El benchmark de mil consultas por política queda registrado en `evidence/benchmark.csv`. Sus tiempos dependen del computador y no deben extrapolarse a un campus real.

### 6. Conclusiones y límites (6:40–8:00)
El prototipo demuestra que puedo cambiar el criterio de navegación sin modificar el motor de búsqueda. Dijkstra funciona aquí porque los costos son no negativos. La principal limitación es que el mapa y los coeficientes son sintéticos. Antes de usarlo en un campus real, habría que levantar y verificar las rutas, validar las preferencias con personas usuarias y mantener actualizados los cierres. Gracias.

## Lista de publicación

1. Reemplazar [nombre] por el nombre del estudiante.
2. Grabar la presentación y mantenerla por debajo de 15 minutos.
3. Subirla a YouTube con visibilidad “No listado”.
4. Pegar el enlace real aquí y en el informe; después entregar informe, diapositivas, código y enlace en el LMS.
