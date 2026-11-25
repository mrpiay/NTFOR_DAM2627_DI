# 1ª evaluación · DI

[← Programación](README.md)

Cómo se calcula la nota de la 1ª evaluación, qué contenidos entran en los exámenes y planificación semanal. La planificación empieza el 2 de noviembre; lo que ya evaluó Julia (exámenes y tareas de Teams) está en la fila «Antes del 2 nov».

**En este documento:** [Cómo se evalúa](#cómo-se-evalúa-de-dónde-sale-la-nota) · [Qué entra en los exámenes](#qué-entra-en-los-exámenes) · [Rúbricas](#rúbricas) · [Planificación semanal](#planificación-semanal) · [Notas](#notas)

## Cómo se evalúa: de dónde sale la nota

Porcentajes sobre la nota de la evaluación: entre todas las partes suman 100 %.

| Parte | Peso | Qué incluye |
|---|---|---|
| **P** · exámenes parciales | 40 % | Lo evaluado por Julia: «TRABAJO UD1» (Julia) 5,4 %, «Bloc Notas» (Julia) 3,5 %, «Wireframe» (Julia) 1 %, «Accesibilidad» (Julia) 0,5 %<br>P1 · mié 2 dic: 29,7 % |
| **A** · actividades guiadas | 20 % | 3 actividades, 6,7 % cada una. Nivel de implementación (50 %) y de comprensión (50 %) |
| **F** · examen final | 30 % | jue 10 dic |
| **R** · autoevaluación | 10 % | Una sola, la semana del examen final: una tarea de Teams con la [plantilla de autoevaluación](autoevaluacion-1a.xlsx) |
| **C** · cuestionarios | — | 3 cuestionarios. No tienen nota propia, pero su entrega es obligatoria: sin todos ellos entregados, la R es un 0 |

## Qué entra en los exámenes

Los porcentajes de esta sección no son partes de la nota: dicen cuánto pesa cada unidad y cada contenido **dentro de los exámenes**. Con ellos se reparte el 40 % de los exámenes parciales (P) entre lo que evaluó Julia y el examen parcial, y valen igual para el examen final (F), que pregunta todas las unidades: los contenidos con más porcentaje tienen preguntas que valen más. Cada porcentaje es la suma de los pesos de sus criterios de evaluación en la programación oficial. Las actividades guiadas (A) y la autoevaluación (R) cuentan aparte, como se indica en «Cómo se evalúa».

### UD1 · Diseño de interfaces, experiencia de usuario y accesibilidad

Pesa un 20,1 % en los exámenes (12 % del módulo).

| Contenido | Peso en la unidad |
|---|---|
| Estándares de usabilidad y accesibilidad | 15 % |
| Menús, acciones, distribución y elección de controles | 48 % |
| Aspecto y mensajes | 23 % |
| Pruebas de usabilidad y accesibilidad | 14 % |

### UD2 · Desarrollo de interfaces gráficas con PySide6 y Qt Designer

Pesa un 33,4 % en los exámenes (20 % del módulo).

| Contenido | Peso en la unidad |
|---|---|
| Herramientas y librerías; importancia de los estándares | 8 % |
| Qt Designer, propiedades, código generado, datos y la aplicación completa | 66 % |
| Acciones asociadas a eventos | 12 % |
| Menús, acciones, aspecto y mensajes | 14 % |

### UD3 · Creación de componentes visuales reutilizables

Pesa un 21,7 % en los exámenes (13 % del módulo).

| Contenido | Peso en la unidad |
|---|---|
| Componente reutilizable: propiedades, señales, pruebas, persistencia, documentación y empaquetado | 100 % |

### UD4 · Interfaces naturales y multimodales

Pesa un 24,8 % en los exámenes (26 % del módulo; en la 1ª evaluación cuenta un 14,8 %, lo que se da).

| Contenido | Peso en la unidad |
|---|---|
| Tipos de interfaces naturales y herramientas de aprendizaje automático | 18 % |
| Reconocimiento de voz y gestos de la mano | 35 % |
| Detección del cuerpo y realidad aumentada | 35 % |
| Información persistente, manual de usuario, pruebas de integración y de regresión | 12 % |

## Rúbricas

Cómo se califica cada parte de la evaluación.

### Exámenes parciales (P) y examen final (F)

En papel. Cada pregunta indica los puntos que vale: los contenidos con más porcentaje tienen preguntas que valen más. La rúbrica de cada examen se publica aquí antes del examen.

### Actividades guiadas (A)

Se califican una vez terminadas, por su **nivel de implementación y comprensión**, y cómo depende del tipo de actividad:

- **Proyecto de progresión continuada** (un mismo proyecto que avanza de una actividad a la siguiente): se califica **hasta dónde se ha implementado la solución final del proyecto**, no cada actividad por separado. Todas sus actividades tienen la misma nota.
- **Actividad independiente:** se califica su propio resultado.

La nota tiene dos mitades:

- **Implementación (50 %):** con el proyecto propio, en el ordenador, se muestran, por orden, las comprobaciones de las tablas de abajo: 12 por proyecto o actividad, 3 en cada nivel (del 1, lo más básico, al 4). Cada comprobación que sale bien suma por sí misma, aunque falle alguna de un nivel anterior: la nota de implementación es las que salen bien entre 12, por 10.
- **Comprensión (50 %):** cuánto se sabe explicar. Se hacen 4 preguntas sobre el diseño y la arquitectura, una por nivel, sobre lo que se muestra en ese nivel; se hacen las cuatro aunque no se haya alcanzado el nivel. Cada respuesta bien dada vale 2,5. De qué trata cada pregunta, en las tablas de abajo.

#### A1–A3 · Proyecto «Mejora tu BugTracker»

Proyecto de progresión continuada: A1, A2 y A3 tienen la misma nota, la del proyecto entero.

**Implementación** (12 comprobaciones; cada una que sale bien suma 10/12)

| Nivel | Muestra que… |
|---|---|
| **1** | • se maneja sin ratón, con el tabulador y los atajos<br>• las acciones Nueva, Guardar, Eliminar y Salir están en el menú y en la barra de herramientas<br>• el diálogo «Nueva incidencia» no deja aceptar con el título vacío |
| **2** | • el `Buscador` filtra la tabla al escribir<br>• `python -m pytest` pasa sus pruebas<br>• la ventana recuerda su tamaño y la última búsqueda al cerrarla y volver a abrirla |
| **3** | • la barra de estado muestra el recuento de incidencias por estado<br>• el `Buscador` está colocado en Qt Designer (se ve en *Object Inspector*)<br>• `python gestos.py` reconoce los gestos |
| **4** | • con «Gestos con la cámara» (Ctrl+G) se enciende la cámara<br>• el pulgar arriba y abajo recorren la tabla<br>• la palma abierta limpia el formulario |

**Comprensión** (una pregunta por nivel; se hacen las cuatro)

| Nivel | La pregunta trata sobre… |
|---|---|
| 1 | Qué es el *buddy* de una etiqueta |
| 2 | La API del `Buscador` y cómo se comunica con la ventana |
| 3 | Qué hace *Promote to* |
| 4 | Cómo llega un gesto de la cámara a la tabla |

| Comprensión | Nota |
|---|---|
| Las 4 preguntas, bien respondidas | 10 |
| 3 preguntas | 7,5 |
| 2 preguntas | 5 |
| 1 pregunta | 2,5 |
| Ninguna | 0 |

La nota es la media de las dos. El mínimo de 4 se aplica a la media de las actividades de la evaluación.

### Cuestionarios (C) y autoevaluación (R)

Hay un cuestionario cada semana en la que se facilitan apuntes o actividades guiadas nuevas, con preguntas sobre ellos. Su entrega es obligatoria, hasta el lunes siguiente a su semana, salvo que se indique otra fecha (ver las notas de la [1ª evaluación](#cómo-se-evalúa-de-dónde-sale-la-nota)). No tienen nota propia, pero son un requisito de la autoevaluación: sin todos los cuestionarios entregados, la autoevaluación (R) es un 0.

La autoevaluación (R) se hace una sola vez, la semana del examen final, con la [plantilla de autoevaluación](autoevaluacion-1a.xlsx) en una tarea de Teams. Forma el 10 % de la nota. La mitad es la hoja completa: un nivel en cada tema, un tipo de fallo donde corresponde y una frecuencia en cada hábito de estudio. La otra mitad es la reflexión final, si es concreta: nombra los temas o los hábitos que más fallan y qué se va a hacer, en concreto, para mejorarlos. Requisito: tener entregados todos los cuestionarios (C); si falta alguno, la R es un 0. Lo marcado en cada tema y en cada hábito no cambia la nota.

## Planificación semanal

| Semana | Qué se trabaja | Cómo se evalúa | Exámenes |
|---|---|---|---|
| Antes del 2 nov<br>[repaso Julia](../repaso-julia/apuntes) | Lo evaluado por Julia | «TRABAJO UD1» (Julia) (5,4 %), «Bloc Notas» (Julia) (3,5 %), «Wireframe» (Julia) (1 %), «Accesibilidad» (Julia) (0,5 %) | — |
| [2–6 nov](../2026_11_02-06)<br>[apuntes](../2026_11_02-06/apuntes) · [actividades](../2026_11_02-06/actividades) | UD1 · Estándares de usabilidad y accesibilidad<br>UD1 · Menús, acciones, distribución y elección de controles<br>UD1 · Aspecto y mensajes<br>UD1 · Pruebas de usabilidad y accesibilidad<br>UD2 · Herramientas y librerías; importancia de los estándares<br>UD2 · Qt Designer, propiedades, código generado, datos y la aplicación completa<br>UD2 · Acciones asociadas a eventos<br>UD2 · Menús, acciones, aspecto y mensajes | A1 (6,7 %), C1 | — |
| [9–13 nov](../2026_11_09-13)<br>[apuntes](../2026_11_09-13/apuntes) · [actividades](../2026_11_09-13/actividades) | UD1 · Pruebas de usabilidad y accesibilidad<br>UD3 · Componente reutilizable: propiedades, señales, pruebas, persistencia, documentación y empaquetado<br>UD4 · Interfaces naturales: reflexión (paso 8 del BugTracker) | A2 (6,7 %), C2 | — |
| [16–20 nov](../2026_11_16-20)<br>[apuntes](../2026_11_16-20/apuntes) · [actividades](../2026_11_16-20/actividades) | UD2 · Datos: contar las incidencias por estado con SQL (GROUP BY) y mostrarlo en la ventana<br>UD3 · El componente en Qt Designer (Promote to)<br>UD4 · Tipos de interfaces naturales y herramientas de aprendizaje automático: la teoría<br>UD4 · Gestos de la mano en el BugTracker (MediaPipe); la voz, en teoría<br>UD4 · Detección del cuerpo y realidad aumentada: la teoría<br>UD4 · Manual de usuario y pruebas de integración y de regresión: la teoría | A3 (6,7 %), C3 | — |
| [23–27 nov](../2026_11_23-27)<br>[actividades](../2026_11_23-27/actividades) | Repaso y consolidación: ValoraDI, explorada; MiniDI, la primera aplicación hecha desde cero, línea a línea; y TodoDI, que la convierte paso a paso en una lista de tareas (un botón, la lista, SQLite, eliminar, una hoja de estilo y la inyección SQL) | — | — |
| 30 nov–4 dic | Repaso (mar 1 y jue 3) | — | **P1** (29,7 %), mié 2 dic |
| 7–11 dic | Repaso (mié 9) | R (10 %) | **F** (30 %), jue 10 dic |
| 14–18 dic | UD5 · Generación de informes | Cierre de la 1ª evaluación · jue 17 | — |

## Notas

- **Cuestionarios (C).** Hay uno cada semana en la que se facilitan apuntes o actividades guiadas nuevas, con preguntas sobre ellos. Su entrega es obligatoria, hasta el lunes siguiente a su semana, salvo que se indique otra fecha (ver las notas). No tienen nota propia, pero sin todos los cuestionarios entregados, la autoevaluación (R) es un 0.
- **Autoevaluación (R).** La R es de reflexión. Una sola, la semana del examen final, en una tarea de Teams: la [plantilla de autoevaluación](autoevaluacion-1a.xlsx), que cada estudiante rellena en su propia copia. Por cada tema de cada unidad, el nivel de comprensión y el tipo de fallo principal; la frecuencia de 15 hábitos de estudio, y una reflexión general sobre qué hacer para mejorar en la 2ª evaluación. Forma el 10 % de autoevaluación del apartado 6.1 de la programación oficial. La mitad de su nota es la hoja completa; la otra mitad, la reflexión, si es concreta. Requisito: tener entregados todos los cuestionarios (C); si falta alguno, la R es un 0. Lo marcado en cada tema y en cada hábito no cambia la nota.
- **Exámenes escritos** (parciales, **P**, y final, **F**). Son en papel e incluyen preguntas similares a las de los cuestionarios. Cada pregunta indica los puntos que vale: los contenidos con más porcentaje tienen preguntas que valen más.
- **Actividades guiadas (A).** Se califican, una vez terminadas, por su nivel de implementación y comprensión, al 50 %. Si son partes de un proyecto de progresión continuada, se califica hasta dónde se ha implementado la solución final del proyecto, con la misma nota para todas; si son independientes, cada una por su resultado. Implementación: 12 comprobaciones ordenadas en 4 niveles; cada una que sale bien suma 10/12. Comprensión: 4 preguntas sobre el diseño y la arquitectura, una por nivel (2,5 cada una); qué pide cada nivel, en las [rúbricas](#rúbricas). Detalle, en las [rúbricas](#rúbricas). El mínimo de 4 se aplica a la media de las actividades de la evaluación.
- El C1 se entrega junto con el C2, el lunes 16 de noviembre.
- De la UD4, en la 1ª evaluación se da en teoría lo que se puede entender sin programarlo (tipos de interfaces naturales, herramientas, voz y gestos, cuerpo y realidad aumentada, manual de usuario y pruebas de integración y de regresión), con un caso práctico, un gesto de la mano en el BugTracker; las preguntas del examen sobre estos temas son de conceptos y criterio, no de código. La interfaz natural integrada en la aplicación (el trabajo final de la UD4) se aplaza al final del curso; la UD4 cuenta en la 1ª evaluación con el 57 % de su peso.
- En DI no hubo exámenes antes del 2 de noviembre. Las tareas de Teams cuentan para los contenidos que trabajan (fila «Antes del 2 nov» de la planificación semanal).
- «SQLite» se entregó en 3 de 13 casos: sus contenidos entran en la P1 para todo el grupo y, para quien la entregó, en esos contenidos cuenta la nota más alta entre la tarea y la P1.
- La semana del 23 al 27, de repaso y consolidación: se explora ValoraDI y, por primera vez, se construye una aplicación desde cero y paso a paso, entendiendo cada línea: MiniDI, una ventana vacía, y TodoDI, que la convierte en una lista de tareas en seis pasos (un botón, la lista, guardar en SQLite, eliminar, los colores con una hoja de estilo y un experimento de inyección SQL). Sin nota ni cuestionario.
- El examen parcial pregunta todo lo de la 1ª evaluación que no evaluó Julia, aunque sea de forma breve. Lo que ya evaluó Julia (fila «Antes del 2 nov» de la planificación semanal) cuenta con esa nota; si no se hizo ese examen o no se entregó esa tarea, en esa parte se obtiene un 5. El examen final pregunta toda la evaluación.
- Mínimo de 4 en cada examen parcial, en la media de las actividades guiadas y en el final para aplicar la media (apartado 6.1 de la programación oficial).
