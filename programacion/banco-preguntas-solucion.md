# DI · Preguntas de práctica de la 1ª evaluación

Cien preguntas para practicar, con la respuesta correcta marcada y una breve explicación. Al final, unos apuntes explican con ejemplos los temas en los que se apoyan muchas respuestas.

- **Verdadero o falso** (1 punto): se marca V o F. Cada acierto suma 1 punto, cada error resta 0,5 y una pregunta en blanco vale 0. Los errores solo restan dentro de esta parte, que nunca baja de 0: no quitan puntos de unir pares ni del resto del examen. Conviene contestar aunque haya dudas: compensa en cuanto se acierta más de una de cada tres veces.
- **Unir pares** (1 punto): cada elemento de la izquierda va con uno de la derecha. La derecha tiene una opción de más, que no va con ninguno. Cada pareja bien unida vale 0,25, y las mal unidas no restan.

Algunas preguntas usan el código de otra y lo dicen con su número.

---

**1.** Cinco personas hacen una prueba de usabilidad con el ratón, y todas terminan sus tareas rápido y sin dudar. Eso demuestra que la aplicación también es accesible.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* La prueba mide la **usabilidad** para esas personas y con esa forma de usarla. La **accesibilidad** es que la pueda usar cualquiera, también quien solo usa el teclado o un lector de pantalla, y eso se comprueba aparte: solo con el teclado, con un lector de pantalla y revisando el contraste. *(Apunte 1.)*

**2.** Un formulario de alta guarda siempre bien los datos, pero cada alta exige seis clics y escribir la fecha a mano. Según la ISO 9241, lo que falla es la eficacia.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El objetivo se consigue, porque el registro queda bien guardado: es **eficaz**. Lo que falla es la **eficiencia**, porque cuesta demasiado esfuerzo. Con un `QDateEdit` y menos pasos se arreglaría. *(Apunte 1.)*

**3.** Une cada situación con el estándar o el nivel que corresponde.

| | Situación | | Estándar o nivel |
|---|---|---|---|
| 1 | La web de un ayuntamiento español tiene que ser accesible por ley | a | Nivel AAA de las WCAG |
| 2 | Se mide si la gente consigue dar de alta un registro, cuánto le cuesta y si se frustra | b | WCAG |
| 3 | El texto normal de los botones tiene que llegar al menos a un contraste de 4,5:1 | c | ISO 9241 |
| 4 | Se revisa la interfaz con cuatro principios: perceptible, operable, comprensible y robusto | d | EN 301 549 |
| | | e | Nivel AA de las WCAG |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **c** &nbsp;&nbsp;&nbsp; 3 → **e** &nbsp;&nbsp;&nbsp; 4 → **b**

*Por qué:* La **EN 301 549** es la norma europea con la que se exigen las WCAG, que en España se exigen al sector público por el Real Decreto 1112/2018. La **ISO 9241** define la usabilidad como eficacia, eficiencia y satisfacción. El 4,5:1 es el del **AA**, el nivel que se suele exigir; el AAA pide más. *(Apunte 1.)*

**4.** Un comprobador da 4,3:1 para el texto blanco de un botón verde. Como está muy cerca de 4,5:1, el botón cumple el nivel AA de las WCAG para el texto normal.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* 4,5:1 es un **mínimo**, y 4,3 no llega a él aunque esté cerca. Hay que oscurecer el verde hasta superarlo. *(Apunte 1.)*

**5.** Un texto con poco contraste solo es un problema para las personas con baja visión.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* También lo sufre cualquiera que mire la pantalla con **mucha luz**, por ejemplo al sol. Por eso el contraste mínimo (4,5:1 para el texto normal, en el nivel AA) se pide para todos los textos. *(Apunte 1.)*

**6.** Un botón «Eliminar» se ve rojo cuando está activado y rojo claro cuando está desactivado, y nada más cambia. Quien no distingue bien los colores puede no saber si se puede pulsar.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Depende **solo del color**: si solo cambia el tono, quien no distingue bien los colores no ve la diferencia. Conviene que cambie algo más, como el color del texto o el borde. *(Apunte 1.)*

**7.** Este código está bien: cada etiqueta tiene su propio atajo de teclado.

```python
formulario.addRow("&Título:", self.txtTitulo)
formulario.addRow("&Prioridad:", self.cmbPrioridad)
formulario.addRow("&Estado:", self.cmbEstado)
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* La `&` crea el atajo con la letra que va detrás: Alt+T, Alt+P y Alt+E son tres letras distintas, y cada una lleva a su campo, que es su *buddy*. Solo habría un problema si dos etiquetas usaran la misma letra, como `&Título` y `&Tipo`. *(Apunte 3.)*

**8.** Une cada mejora con a quién ayuda.

| | Mejora | | A quién ayuda |
|---|---|---|---|
| 1 | Nombre accesible (`setAccessibleName`) | a | A quien quiere llegar a un campo con Alt y una letra |
| 2 | Un marco en el control que tiene el foco | b | A quien usa el teclado, que así sabe dónde está |
| 3 | *Tooltip* con el nombre y el atajo | c | A quien no distingue bien los colores, que así puede leer el texto sobre el fondo |
| 4 | `&` en la etiqueta, con el campo como *buddy* | d | A quien usa un lector de pantalla, que así puede decir qué hace el control |
| | | e | A quien usa el ratón y no reconoce un botón que solo tiene un icono |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **b** &nbsp;&nbsp;&nbsp; 3 → **e** &nbsp;&nbsp;&nbsp; 4 → **a**

*(Apunte 3.)*

**9.** Si se quitara la segunda línea, Tab en la descripción pasaría el foco al control siguiente.

```python
self.txtDescripcion = QTextEdit()
self.txtDescripcion.setTabChangesFocus(True)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Sin ella, un `QTextEdit` **escribe un tabulador** en el texto: con Tab no se podría salir del campo, y quien usa solo el **teclado** se quedaría atascado. *(Apunte 3.)*

**10.** En un menú, asignar Ctrl+N a la orden que elimina el registro seleccionado respeta la heurística de coherencia y estándares.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* En cualquier programa, Ctrl+N es **Nuevo** (y Supr, eliminar): quien lo pulse esperando crear un registro, lo borra. Los atajos tienen que ser los **habituales**. *(Apunte 2.)*

**11.** Desactivar «Guardar» hasta que estén rellenos todos los campos obligatorios es un ejemplo de la heurística de prevención de errores.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* No se puede guardar un registro incompleto: es mejor **evitar el error** que avisar después. *(Apunte 2.)*

**12.** Une cada heurística de Nielsen con un ejemplo.

| | Heurística | | Ejemplo |
|---|---|---|---|
| 1 | Visibilidad del estado del sistema | a | Al añadir un registro, la barra de estado lo confirma |
| 2 | Control y libertad | b | Todos los diálogos tienen un botón «Cancelar» |
| 3 | Prevención de errores | c | «Eliminar» está desactivado si no hay ninguna fila seleccionada |
| 4 | Flexibilidad y eficiencia de uso | d | Los mensajes de error usan las palabras de quien usa la aplicación, no las del programa |
| | | e | Intro en el campo de texto hace lo mismo que el botón «Añadir», sin ir a él |

1 → **a** &nbsp;&nbsp;&nbsp; 2 → **b** &nbsp;&nbsp;&nbsp; 3 → **c** &nbsp;&nbsp;&nbsp; 4 → **e**

*(Apunte 2.)*

**13.** Si falla al guardar, una aplicación muestra «No se ha podido guardar: CHECK constraint failed: nota BETWEEN 1 AND 5». Es un buen mensaje, porque dice exactamente qué ha fallado.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Es **técnico, en inglés**, y **no dice qué hacer**: incumple **ayudar a reconocer y corregir errores**. Mejor: «La nota tiene que estar entre 1 y 5», y el detalle técnico aparte. *(Apunte 2.)*

**14.** Una evaluación heurística se hace con personas que no conocen la aplicación, que hacen tareas y piensan en voz alta.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Eso es una **prueba de usabilidad**. La **evaluación heurística** revisa la interfaz con las **heurísticas de Nielsen**. *(Apunte 2.)*

**15.** Ctrl+S añade un registro si no hay ninguno seleccionado y modifica el seleccionado si lo hay, y nada indica qué va a hacer. Esto incumple la visibilidad del estado del sistema.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Quien selecciona un registro para crear otro parecido **lo modifica sin saberlo**. Habría que mostrar el modo («Editando…») o separar las acciones de añadir y de modificar. *(Apunte 2.)*

**16.** Una aplicación de rehabilitación tiene que contar cuántas veces una persona levanta el brazo por encima del hombro. Basta con el reconocedor de gestos de la mano, porque la mano sube con el brazo.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El reconocedor de gestos dice **qué forma tiene la mano** a partir de sus 21 puntos, pero no sabe dónde está el **hombro**. Para saber si la muñeca está por encima del hombro hace falta el **modelo de postura**, con los 33 puntos del cuerpo. *(Apunte 21.)*

**17.** Ayer la aplicación funcionaba. Hoy, en una terminal nueva, `python main.py` dice que no encuentra el módulo `PySide6`. Lo más probable es que el entorno virtual no esté activado.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Sin activarlo, `python` es el del sistema, que no tiene PySide6. El **entorno virtual** **aísla** las librerías de cada proyecto: hay que activarlo en cada terminal nueva. *(Apunte 4.)*

**18.** Une cada línea con lo que hace.

| | Línea | | Qué hace |
|---|---|---|---|
| 1 | `app = QApplication()` | a | Ejecuta el constructor de la clase madre, que crea la parte de Qt del objeto |
| 2 | `ventana.show()` | b | Crea el objeto único que gestiona la pantalla y los eventos; va antes que cualquier ventana |
| 3 | `app.exec()` | c | Arranca el bucle de eventos, que reparte clics y teclas hasta que se cierra la última ventana |
| 4 | `super().__init__()` | d | Hace visible una ventana que ya existe |
| | | e | Crea la ventana, pero todavía no la muestra |

1 → **b** &nbsp;&nbsp;&nbsp; 2 → **d** &nbsp;&nbsp;&nbsp; 3 → **c** &nbsp;&nbsp;&nbsp; 4 → **a**

*(Apunte 5.)*

**19.** Si se quita `app.exec()`, la ventana se muestra y se queda abierta hasta que alguien la cierra.

```python
app = QApplication()
ventana = Ventana()
ventana.show()
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Sin el **bucle de eventos** no hay nada que espere: el programa llega al final y termina, y la ventana desaparece nada más mostrarse. `show()` solo hace visible la ventana. Lo que mantiene viva la aplicación, atendiendo clics y teclas, es `app.exec()`. *(Apunte 5.)*

**20.** Para contar sentadillas con el modelo de postura, se suma una sentadilla cada vez que una imagen de la cámara muestra la rodilla doblada.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Una sentadilla dura **muchas imágenes** con la rodilla doblada, así que cada una contaría decenas de veces. Hay que contar el **cambio de estado**: de pie, agachado y otra vez de pie. Es lo mismo que hace el detector de gestos, que solo emite cuando cambia el gesto confirmado (`_ultimo`). *(Apuntes 19 y 21.)*

**21.** Con este código, `bloquear()` desactiva el botón.

```python
def __init__(self):
    super().__init__()
    boton = QPushButton("Añadir")
    distribucion = QVBoxLayout(self)
    distribucion.addWidget(boton)

def bloquear(self):
    boton.setEnabled(False)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* `boton` es una **variable local** del `__init__`: solo existe mientras se ejecuta. En `bloquear` no existe, y da un `NameError`. Lo que se usa desde otros métodos se guarda en `self`, como `self.boton`. *(Apunte 5.)*

**22.** Une cada cosa que se quiere conseguir con cómo se hace en Qt.

| | Qué se quiere | | Cómo se hace |
|---|---|---|---|
| 1 | Hacer algo cuando se pulsa un botón | a | Sobrescribir `keyPressEvent` en la clase del componente |
| 2 | Preguntar «¿Salir sin guardar?» al cerrar la ventana | b | Declarar una `Signal` en el cuerpo de la clase y emitirla |
| 3 | Que un componente propio avise a la ventana de que ha cambiado | c | Conectar la señal `clicked` con un método |
| 4 | Que las flechas suban y bajen la nota de un selector | d | Conectar `closeEvent` con un método usando `connect` |
| | | e | Sobrescribir `closeEvent` en la clase de la ventana |

1 → **c** &nbsp;&nbsp;&nbsp; 2 → **e** &nbsp;&nbsp;&nbsp; 3 → **b** &nbsp;&nbsp;&nbsp; 4 → **a**

*Por qué:* Pulsar un botón llega como una **señal**, `clicked`, y se **conecta**. Cerrar la ventana y pulsar una tecla llegan como **eventos**, que se tratan **sobrescribiendo** el método de nombre fijo y no se conectan: por eso la d no vale. Un componente avisa a la ventana con una **señal propia**. *(Apuntes 6 y 15.)*

**23.** Esta línea está en el `__init__` de la ventana, y `anadir_fila` no devuelve nada. Con ella, `anadir_fila` se ejecuta cada vez que se pulsa el botón.

```python
self.boton.clicked.connect(self.anadir_fila())
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Con paréntesis, el método **se ejecuta una vez, al conectar**, y se intenta conectar lo que devuelve, `None`: `connect` da un `TypeError` y el programa termina antes de abrir la ventana. Se pasa **sin paréntesis**. *(Apunte 6.)*

**24.** Si por error se conecta dos veces el mismo slot con `clicked`, cada pulsación del botón lo ejecuta dos veces.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El slot se ejecuta una vez por cada **conexión**. A veces no se nota: si la primera llamada vacía el campo, una **validación** como `if texto:` frena la segunda. *(Apunte 6.)*

**25.** Se intenta arreglar el problema de las lambdas en un bucle con un valor por defecto. Al pulsar «Baja», la etiqueta muestra «Baja».

```python
for nombre in ["Baja", "Media", "Alta"]:
    boton = QPushButton(nombre)
    capa.addWidget(boton)
    boton.clicked.connect(lambda texto=nombre: self.etiqueta.setText(texto))
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El valor por defecto sí guarda «Baja», pero `clicked` **envía `checked`**, que vale `False`, y PySide6 lo pasa al primer parámetro. Entonces `texto` vale `False`, `setText(False)` da un `TypeError` y la etiqueta no cambia. Hace falta un primer parámetro que recoja `checked`: `lambda _=False, texto=nombre: …`. *(Apunte 7.)*

**26.** `keyPressEvent` y `closeEvent` se conectan con `connect`, igual que las señales.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Son **eventos**: Qt los manda al widget, que los trata en esos métodos de nombre fijo, **sobrescribiéndolos** en la clase. No se conectan. *(Apunte 6.)*

**27.** Si no hay ninguna fila seleccionada en la lista, `self.lista.selectedItems()[0]` devuelve `None`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* `selectedItems()` devuelve una **lista vacía**, que no tiene elemento `[0]`: da un **`IndexError`**. Por eso conviene desactivar «Eliminar» mientras no haya selección. *(Apunte 12.)*

**28.** Une cada dato de un formulario de reserva de aula con el control más adecuado.

| | Dato | | Control |
|---|---|---|---|
| 1 | El aula, una de seis | a | `QDateEdit` |
| 2 | La fecha | b | `QCheckBox` |
| 3 | El número de asistentes, de 1 a 30 | c | `QSpinBox` con `setRange(1, 30)` |
| 4 | Si hace falta proyector | d | `QComboBox` |
| | | e | `QLineEdit` |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **a** &nbsp;&nbsp;&nbsp; 3 → **c** &nbsp;&nbsp;&nbsp; 4 → **b**

*(Apunte 8.)*

**29.** Una aplicación de realidad aumentada usa un marcador impreso para saber dónde dibujar las instrucciones de montaje sobre una pieza. Si una mano tapa el marcador, la aplicación puede perder el sitio donde dibujarlas.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El **marcador** es la referencia que reconoce la cámara para colocar el dibujo **en el sitio correcto**: si no lo ve, no sabe dónde está la pieza. La realidad aumentada **sin marcadores** reconoce superficies, caras o manos, pero le pasa lo mismo si deja de verlas. *(Apunte 21.)*

**30.** Un botón que se añade a mano en el archivo generado por `pyside6-uic` se conserva al regenerarlo tras cambiar el diseño en Qt Designer.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* `pyside6-uic` **regenera el archivo entero** a partir del `.ui`, y lo escrito a mano se pierde. Los controles se añaden en Qt Designer, y la lógica va en la **clase propia** de la ventana. *(Apunte 8.)*

**31.** Con esta validación, un título de 101 letras con dos espacios detrás (103 caracteres) se rechaza por largo.

```python
titulo = self.txtTitulo.text().strip()
if not titulo:
    ...   # avisa y return
if len(titulo) > 100:
    ...   # avisa y return
self.accept()
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* `strip()` quita los dos espacios **antes de medir**, pero quedan 101 caracteres, más de 100, y se rechaza. `strip()` solo quita los espacios del principio y del final, nunca letras. *(Apunte 9.)*

**32.** Si «Aceptar» se conectara directamente con `self.accept`, sin validar, y el título fuera `"   "`, el `NOT NULL` de la columna `titulo` impediría guardarlo. `datos()` devuelve el título con `strip()`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Tras `strip()`, el título es `""`, un **texto vacío**, que no es `NULL`: se guardaría un registro sin título. Por eso `accepted` se conecta con `validar`. *(Apunte 9.)*

**33.** Después de cerrar un diálogo con «Aceptar», `dialogo.datos()` sigue devolviendo lo que se escribió.

```python
dialogo = Dialogo(self)
if not dialogo.exec():
    return
bd.insertar(*dialogo.datos())
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Cerrar el diálogo lo **oculta**, no lo destruye: el **objeto** existe mientras la variable `dialogo` lo guarda, con sus campos. *(Apunte 9.)*

**34.** Una aplicación hace todas sus consultas con esta función. Une cada síntoma con su causa.

```python
def ejecutar_sql(sql, valores=()):
    conexion = sqlite3.connect(RUTA)
    cursor = conexion.execute(sql, valores)
    filas = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return filas
```

| | Síntoma | | Causa |
|---|---|---|---|
| 1 | Lo añadido se ve en la lista, pero al volver a abrir la aplicación no está | a | Al buscar, el valor se pasa como `(texto)`, sin coma |
| 2 | Buscar «Error» da «Incorrect number of bindings supplied… there are 5 supplied» | b | El texto se pega en el SQL con `+`, en lugar de usar `?` |
| 3 | Buscar «O'Brien» da un error de sintaxis de SQL | c | Falta `AUTOINCREMENT` en la clave primaria |
| 4 | Con la tabla ordenada por título, «Eliminar» borra otro registro, sin ningún error | d | Alguien ha quitado `conexion.commit()` de la función |
| | | e | La fila de la vista se usa en el modelo sin `mapToSource` |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **a** &nbsp;&nbsp;&nbsp; 3 → **b** &nbsp;&nbsp;&nbsp; 4 → **e**

*Por qué:* Sin **`commit`**, los cambios se descartan al cerrar la conexión. `(texto)` sin coma no es una tupla, y `sqlite3` toma cada una de las 5 letras de «Error» como un valor. El apóstrofo de O'Brien **cierra la comilla** del SQL pegado: es el mismo hueco por el que entra la inyección SQL. Y la vista y el modelo numeran sus filas por separado. *(Apuntes 10, 11 y 13.)*

**35.** Una aplicación de realidad aumentada pone etiquetas de texto blanco, sin fondo, sobre la imagen de la cámara. Si en una prueba el texto contrasta bien con lo que se ve detrás, se leerá bien siempre.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* En la realidad aumentada, el fondo es la **imagen real**, y cambia: delante de una pared blanca o del cielo, el texto blanco no se lee. La etiqueta necesita su propio fondo o un borde, para ser **legible sobre cualquier fondo**, y no debe **tapar** lo importante. Es el contraste de la UD1 con un fondo que la aplicación no controla. *(Apuntes 1 y 21.)*

**36.** En la función de la pregunta 34, si `filas = cursor.fetchall()` se mueve a después de `conexion.close()`, `ejecutar_sql` sigue funcionando sin errores con los `INSERT`, porque no devuelven filas.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* `fetchall()` lee **a través de la conexión**, y ya está cerrada: da un error en todas las consultas, también con un `INSERT` (la fila llega a guardarse, porque el `commit` va antes, pero la función se interrumpe). *(Apunte 10.)*

**37.** `(id_registro,)`, con la coma, es una tupla de un elemento; `(texto)`, sin coma, no lo es.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Sin la coma, los paréntesis solo agrupan: `(texto)` es el propio texto. `sqlite3` lo tomaría como una **secuencia de caracteres**, un valor por letra, y daría un error si hay más letras que `?`. Los valores de una consulta van en una **tupla**, y la coma es lo que hace una tupla de un elemento. *(Apunte 11.)*

**38.** La tabla tiene los registros 1, 2, 3, 4 y 5, y se eliminan el 2 y el 5. Sin `AUTOINCREMENT`, el siguiente registro recibe el `id` 2, el primer hueco libre.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Sin `AUTOINCREMENT`, el `id` nuevo es **el mayor que existe más uno**. El mayor es el 4, así que recibe el **5**, que es el de un registro borrado. Los huecos de en medio no se rellenan. Con `AUTOINCREMENT` recibiría el **6**, porque nunca reutiliza un `id` que ya ha dado. *(Apunte 10.)*

**39.** La tabla `registros` tiene estas filas. Une cada consulta con su resultado.

| prioridad | estado |
|---|---|
| Alta | Pendiente |
| Baja | Pendiente |
| Alta | Resuelta |
| Media | En proceso |
| Alta | Pendiente |

| | Consulta | | Resultado (en cualquier orden) |
|---|---|---|---|
| 1 | `SELECT prioridad, COUNT(*) FROM registros GROUP BY prioridad` | a | Una sola fila: 3 |
| 2 | `SELECT prioridad, COUNT(*) FROM registros WHERE estado = 'Pendiente' GROUP BY prioridad` | b | Alta 3 · Baja 1 · Media 1 |
| 3 | `SELECT estado, COUNT(*) FROM registros GROUP BY estado` | c | Alta 2 · Baja 1 · Media 0 |
| 4 | `SELECT COUNT(*) FROM registros WHERE estado = 'Pendiente'` | d | En proceso 1 · Pendiente 3 · Resuelta 1 |
| | | e | Alta 2 · Baja 1 |

1 → **b** &nbsp;&nbsp;&nbsp; 2 → **e** &nbsp;&nbsp;&nbsp; 3 → **d** &nbsp;&nbsp;&nbsp; 4 → **a**

*Por qué:* `WHERE` se aplica **antes** de agrupar. En la 2, ninguna Media está pendiente, así que Media **no aparece**; no sale con un 0, y por eso la c no vale. Sin `GROUP BY`, `COUNT(*)` da una sola fila con el total. *(Apunte 10.)*

**40.** Si en este `UPDATE` el `id` se pusiera el primero en la tupla, se produciría un error.

```python
conexion.execute(
    """UPDATE registros
       SET titulo = ?, tipo = ?, prioridad = ?, estado = ?, descripcion = ?
       WHERE id = ?""",
    (titulo, tipo, prioridad, estado, descripcion, id_registro)
)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Los valores se **desplazan** y el `WHERE` busca `id = descripcion`: **no da error**, pero **ninguna fila** cumple la condición y no cambia nada. *(Apunte 11.)*

**41.** Una aplicación guarda lo que se escribe con `conexion.execute("INSERT INTO registros (texto) VALUES (?)", (texto,))`. Alguien escribe `x'); DELETE FROM registros; --`. Ese texto se guarda tal cual, como un registro más, y no se borra nada.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* En una **consulta parametrizada**, la orden y el dato viajan **por separado**: el texto se guarda como texto, con sus comillas y su punto y coma, y **nunca se ejecuta como SQL**. Si se pegara con `+` y se ejecutara con `executescript`, se borrarían todos los registros. *(Apunte 11.)*

**42.** Con esta consulta, escribir `admin' --` como nombre, y cualquier contraseña, permite entrar como `admin`.

```python
sql = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "' AND clave = '" + clave + "'"
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El `'` cierra el nombre y el **`--`** convierte en **comentario** la condición de la clave: basta con que exista `admin`. *(Apunte 11.)*

**43.** Con `RUTA = "datos.db"`, si se lanza `main.py` desde otra carpeta, la aplicación abre una base de datos distinta de la de siempre.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Es una **ruta relativa**: se busca en la **carpeta desde la que se lanza** el programa, y allí se crea una nueva y vacía. `Path(__file__).with_name("datos.db")` la pone junto al archivo de código. *(Apunte 10.)*

**44.** Añadir una columna nueva en `CREATE TABLE IF NOT EXISTS registros (…)` la añade también a una base de datos que ya existía.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* `IF NOT EXISTS` **no hace nada** si la tabla ya existe, aunque su definición haya cambiado. Hay que cambiar la tabla existente con `ALTER TABLE … ADD COLUMN`. *(Apunte 10.)*

**45.** Si se quitara `self.lista.clear()`, al añadir un registro se verían filas repetidas en la lista, pero en la base de datos no habría ningún registro repetido.

```python
def cargar_filas(self):
    self.lista.clear()
    for id_registro, texto in bd.obtener_registros():
        elemento = QListWidgetItem(texto)
        elemento.setData(Qt.ItemDataRole.UserRole, id_registro)
        self.lista.addItem(elemento)
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Las filas que ya estaban siguen, y debajo se cargan todas otra vez: la repetición está solo en la **vista**, no en los **datos**. *(Apunte 12.)*

**46.** Une cada cosa que hay que conseguir con lo que se hace en Model/View.

| | Qué hay que conseguir | | Qué se hace |
|---|---|---|---|
| 1 | Que un registro nuevo aparezca en la tabla | a | Pedir al proxy `mapToSource` con la fila seleccionada |
| 2 | Que la columna ID no se vea, sin quitarla de los datos | b | Borrar del modelo las filas que no coinciden con la búsqueda |
| 3 | Que solo se vean los registros que contienen el texto buscado | c | Añadir la fila al modelo |
| 4 | Saber qué registro hay detrás de la fila seleccionada, con la tabla ordenada | d | Darle al proxy el texto con `setFilterFixedString` |
| | | e | Ocultar la columna en la vista con `setColumnHidden` |

1 → **c** &nbsp;&nbsp;&nbsp; 2 → **e** &nbsp;&nbsp;&nbsp; 3 → **d** &nbsp;&nbsp;&nbsp; 4 → **a**

*Por qué:* El **modelo** guarda los datos, la **vista** los dibuja (y puede ocultar columnas) y el **proxy** filtra y ordena **sin tocarlos**. Por eso la b es un error: al borrar la búsqueda, las filas borradas ya no volverían. *(Apunte 13.)*

**47.** La vista oculta la columna ID, y el proxy busca solo en la columna Título (`setFilterKeyColumn(1)`). Al buscar «4», aparece la fila con ID 4, aunque su título no tenga ningún 4.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Con `setFilterKeyColumn(1)`, el proxy solo mira la columna 1 **del modelo**, la del título. Que la vista oculte o no la columna ID no cambia nada, porque eso es cosa de la vista. Con `setFilterKeyColumn(-1)`, el proxy buscaría en todas las columnas del modelo, también en la oculta, y entonces sí aparecería. *(Apunte 13.)*

**48.** Con la tabla ordenada por título a través de un proxy, la fila que se ve en primer lugar puede no ser la fila 0 del modelo.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El **proxy** ordena y filtra **solo en la vista**, y la vista y el modelo numeran sus filas por separado. Para pasar de una a otra se usa **`mapToSource`**. *(Apunte 13.)*

**49.** Si `busquedaCambiada` se conecta primero con `mostrar_resultados`, que cuenta las filas del proxy, y después con el filtro, la barra de estado cuenta las filas antes de aplicar la búsqueda nueva.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Una señal conectada con **varios slots** los ejecuta **en el orden en que se conectaron**. `mostrar_resultados` cuenta las filas cuando el proxy todavía tiene el filtro anterior, y el filtro nuevo se aplica después. El filtro tiene que conectarse primero. *(Apunte 14.)*

**50.** En el manual de usuario de una aplicación con buscador conviene explicar que el `Buscador` emite `busquedaCambiada` y que la tabla usa un `QSortFilterProxyModel`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El **manual de usuario** es para quien **usa** la aplicación: cómo buscar un registro, qué atajos hay y qué hacer si algo falla, con capturas. La API y la arquitectura son para quien **programa**, y van en el docstring y en la documentación técnica. *(Apuntes 16 y 21.)*

**51.** El manual de usuario explica también cómo se instala y cómo se abre la aplicación, y no solo cómo se hace cada tarea.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El manual es para quien **usa** la aplicación, y lo primero que necesita es tenerla en marcha: qué hace, cómo se instala y se abre, cómo se hace cada tarea paso a paso y qué hacer ante los problemas frecuentes. *(Apunte 21.)*

**52.** Une cada necesidad con la tecnología que la resuelve.

| | Necesidad | | Tecnología |
|---|---|---|---|
| 1 | Contar las repeticiones de un ejercicio de brazos | a | Reconocimiento de gestos de la mano |
| 2 | Escribir la descripción de un registro hablando, con las manos ocupadas | b | Realidad aumentada |
| 3 | Ver en la imagen de la cámara, sobre cada caja del almacén, qué contiene | c | Síntesis de voz |
| 4 | Pasar al registro siguiente con el pulgar arriba | d | Modelo de postura |
| | | e | Reconocimiento de voz, para dictar |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **e** &nbsp;&nbsp;&nbsp; 3 → **b** &nbsp;&nbsp;&nbsp; 4 → **a**

*Por qué:* Escribir hablando es **reconocimiento** de voz, de la voz al texto; la **síntesis** hace lo contrario. Los brazos necesitan los puntos del **cuerpo**, y el pulgar, los de la **mano**. Dibujar sobre la imagen real, en su sitio, es **realidad aumentada**. *(Apuntes 18 y 21.)*

**53.** Una aplicación tiene `main.py`, `ventana.py` (sin SQL) y `bd.py` (sin widgets). Si los datos pasaran a guardarse en un servidor, solo habría que cambiar `bd.py`.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Es la **separación de responsabilidades**: la ventana pide los datos a las mismas funciones y **no sabe dónde se guardan**. *(Apunte 12.)*

**54.** Al ejecutar la última línea, la nota cambia a 5.

```python
@dataclass
class Registro:
    nota: int

r = Registro(4)
r.nota = 5
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Sin `frozen=True`, el objeto se puede cambiar, y la nota pasa a 5. Con `@dataclass(frozen=True)` sería **inmutable** y la última línea daría un error. En los dos casos, `@dataclass` escribe el `__init__`, el `__repr__` y el `__eq__`. *(Apunte 12.)*

**55.** Para usar el componente `Buscador` en otra aplicación basta con conocer su API pública, sin cambiar `buscador.py`.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Es un **componente reutilizable**: sus **propiedades**, **señales** y **métodos públicos** son lo que se usa desde fuera, y el interior no importa. *(Apunte 15.)*

**56.** Desde la ventana, `self.buscador._caja.textChanged.connect(…)` es una buena forma de saber cuándo cambia la búsqueda, porque funciona.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El `_` indica que es **interno**: se salta la API pública y rompe la **encapsulación**. Si una versión nueva del componente cambia `_caja`, da un `AttributeError`; con `busquedaCambiada`, no se notaría. *(Apunte 15.)*

**57.** Une cada cosa que necesita la ventana con lo que usa del `Buscador`.

| | Qué necesita la ventana | | Qué usa |
|---|---|---|---|
| 1 | Enterarse de cada cambio en la búsqueda | a | `help(Buscador)` |
| 2 | Volver a poner, al abrirse, la última búsqueda guardada con `QSettings` | b | `buscador.limpiar()` |
| 3 | Vaciar la búsqueda desde una opción del menú | c | `buscador._caja.textChanged.connect(…)` |
| 4 | Consultar la API del componente sin abrir su código | d | `buscador.busquedaCambiada.connect(…)` |
| | | e | `buscador.texto = valor` |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **e** &nbsp;&nbsp;&nbsp; 3 → **b** &nbsp;&nbsp;&nbsp; 4 → **a**

*Por qué:* Desde fuera solo se usa la **API pública**, la señal, la propiedad y los métodos, documentada en el docstring que muestra `help()`. La c funciona hoy, pero usa un widget **interno**, `_caja`: rompe la encapsulación. *(Apunte 15.)*

**58.** Con este código, `buscador.busquedaCambiada.connect(…)` funciona.

```python
class Buscador(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.busquedaCambiada = Signal(str)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Una **señal** se declara **en el cuerpo de la clase**, fuera de los métodos: así Qt la convierte en una señal de cada objeto, con `connect` y `emit`. Declarada **dentro de `__init__`**, es un atributo normal, que no tiene `connect`, y da un `AttributeError`. *(Apunte 15.)*

**59.** El selector empieza con la nota a 0. Con este setter, `selector.nota = 8` emite `notaCambiada` con el valor 8.

```python
def _set_nota(self, valor):
    valor = max(0, min(5, valor))
    if valor == self._nota:
        return
    self._nota = valor
    self._dibujar()
    self.notaCambiada.emit(valor)

nota = Property(int, _get_nota, _set_nota, notify=notaCambiada)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Escribir en la **propiedad** ejecuta el **setter**, que **recorta** el valor antes que nada: `max(0, min(5, 8))` da 5. La nota queda en 5 y se emite **5**, no 8, así que quien escucha nunca recibe un valor fuera de 0 a 5. *(Apunte 15.)*

**60.** Con el setter de la pregunta 59 y la nota ya en 5, `selector.nota = 9` no emite `notaCambiada`.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El 9 se recorta a 5, que es **el valor que ya tenía**, y el setter termina con `return` antes de emitir. Solo se avisa cuando la nota **cambia de verdad**. *(Apunte 15.)*

**61.** Une cada ejemplo con el concepto que muestra.

| | Ejemplo | | Concepto |
|---|---|---|---|
| 1 | `SelectorNota` hereda de `QFrame` para aprovechar su marco | a | `notify` |
| 2 | El `Buscador` junta una etiqueta, una caja de texto y un botón | b | Encapsulación |
| 3 | `selector.nota = 4` ejecuta `_set_nota(4)` | c | Herencia |
| 4 | La señal que se indica en `Property(…, notify=…)` avisa de que la propiedad ha cambiado | d | Composición |
| | | e | `Property` |

1 → **c** &nbsp;&nbsp;&nbsp; 2 → **d** &nbsp;&nbsp;&nbsp; 3 → **e** &nbsp;&nbsp;&nbsp; 4 → **a**

*Por qué:* La herencia es **ser** un widget que ya existe y añadirle cosas; la composición, **juntar** varios. Una `Property` se usa como un atributo, pero ejecuta su getter y su setter, y `notify` dice qué señal avisa de sus cambios. *(Apunte 15.)*

**62.** Con este componente, al teclear «Error» con `qtbot.keyClicks`, `busquedaCambiada` se emite cinco veces.

```python
class Buscador(QWidget):
    busquedaCambiada = Signal(str)
    def __init__(self, parent=None, etiqueta="&Buscar:"):
        ...
        self._caja = QLineEdit()
        self._caja.textChanged.connect(self._al_cambiar_texto)
    def _al_cambiar_texto(self, texto):
        self.busquedaCambiada.emit(texto)
    def _set_texto(self, valor):
        self._caja.setText(valor)
    texto = Property(str, _get_texto, _set_texto, notify=busquedaCambiada)
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* `keyClicks` pulsa **tecla a tecla**, como una persona, y cada tecla cambia el texto: «E», «Er», «Err», «Erro» y «Error». *(Apunte 15.)*

**63.** Con el componente de la pregunta 62, `buscador.texto = "Error"` emite `busquedaCambiada`, aunque `_set_texto` no llame a `emit`.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Es una **cadena de señales**: `setText` cambia la caja, la caja emite `textChanged` y `_al_cambiar_texto` emite `busquedaCambiada`. *(Apunte 15.)*

**64.** Si el `keyPressEvent` de un componente no llamara a `super().keyPressEvent(evento)` con las teclas que no usa, esas teclas no llegarían a la ventana que lo contiene.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Con `super()`, la tecla que nadie usa se ignora y el **evento sube al widget padre**. Sin esa línea, el componente se queda con ella: por ejemplo, Intro no guardaría. *(Apunte 6.)*

**65.** Una ventana tiene dos selectores de cinco estrellas y un botón «Guardar». Si cada estrella pudiera recibir el foco, recorrer la ventana con Tab necesitaría 11 paradas en lugar de 3.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Serían 5 + 5 estrellas más «Guardar»: 11 paradas. Con `NoFocus` en las estrellas y el foco en cada selector, quedan 3, porque cada selector es **una sola pieza** para el **teclado** y el lector de pantalla, que se maneja con las flechas. *(Apunte 3.)*

**66.** El `Buscador` está colocado en Qt Designer con *Promote to*, y su constructor pasa a ser este. La aplicación no arranca.

```python
def __init__(self, etiqueta="&Buscar:", parent=None):
    super().__init__(parent)
    self._etiqueta = QLabel(etiqueta)
    ...
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* *Promote to* crea el componente **pasándole el padre como primer argumento**, `Buscador(self.centralwidget)`, y ahora ese padre llega en `etiqueta`. `QLabel(widget)` también es válido: crea una etiqueta **sin texto** cuyo padre es ese widget. La aplicación arranca, pero la etiqueta **sale vacía, sin ningún aviso**. Por eso `parent` va primero. *(Apunte 15.)*

**67.** Une cada tarea con lo que hay que hacer.

| | Tarea | | Qué se hace |
|---|---|---|---|
| 1 | Indicar que el paquete pasa a ser la versión 0.2.0 | a | `python -m build` |
| 2 | Generar el archivo que se reparte | b | Añadir PySide6 a `requirements.txt` |
| 3 | Usar el componente en otro proyecto | c | Cambiar `version` en `pyproject.toml` |
| 4 | Que al instalar el paquete se instale también PySide6 | d | `pip install` con la ruta del `.whl` |
| | | e | Añadir PySide6 a `dependencies`, en `pyproject.toml` |

1 → **c** &nbsp;&nbsp;&nbsp; 2 → **a** &nbsp;&nbsp;&nbsp; 3 → **d** &nbsp;&nbsp;&nbsp; 4 → **e**

*Por qué:* `pyproject.toml` describe el paquete, `python -m build` crea el `.whl` en `dist/` y `pip install` lo instala con sus **dependencias**. `requirements.txt` es de una **aplicación**, no del paquete: `pip` no lo lee al instalar el `.whl`. *(Apunte 16.)*

**68.** El paquete del buscador lleva solo el módulo `buscador` (`py-modules = ["buscador"]`). Si `buscador.py` hace `import bd`, con el `bd.py` de la aplicación, el paquete incluye también `bd.py`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Solo entra lo que dice `py-modules`: en otro proyecto, **no encuentra el módulo `bd`**. Un componente reutilizable **no depende de la aplicación**. *(Apunte 16.)*

**69.** `limpiar()` borra la caja del buscador. Esta prueba pasa.

```python
def test_limpiar(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    buscador.texto = "error"
    buscador.limpiar()
    assert buscador.texto == "error"
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Tras `limpiar()`, `texto` vale `""`: el **`assert`** es falso y la prueba falla. Debería comprobar `== ""`. *(Apunte 17.)*

**70.** Une cada comprobación con la herramienta que hace falta para ella.

| | Comprobación | | Herramienta |
|---|---|---|---|
| 1 | Que `error_titulo("")` devuelve un mensaje de error | a | `pytest.approx` |
| 2 | Que guardar una nota de 6 hace que la base de datos lance un `IntegrityError` | b | Una *fixture* con `tmp_path` |
| 3 | Que la media ponderada de unas notas da 3,7 | c | `assert`, sin nada más |
| 4 | Que al escribir en el buscador se emite `busquedaCambiada` | d | `pytest.raises` |
| | | e | `qtbot.waitSignal` |

1 → **c** &nbsp;&nbsp;&nbsp; 2 → **d** &nbsp;&nbsp;&nbsp; 3 → **a** &nbsp;&nbsp;&nbsp; 4 → **e**

*Por qué:* Los decimales se comparan con un margen (`approx`). Un error que **tiene que** producirse se espera con `raises`, y una señal, con `waitSignal`, que falla si no llega a tiempo. La *fixture* con `tmp_path` no comprueba nada: prepara una base de datos aparte para cada prueba. *(Apunte 17.)*

**71.** Con el `Buscador` de la pregunta 62, recién creado y con la caja vacía, esta prueba pasa.

```python
with qtbot.waitSignal(buscador.busquedaCambiada, timeout=1000):
    buscador.texto = ""
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El texto **no cambia**: la caja no emite `textChanged` ni se emite `busquedaCambiada`. **`waitSignal`** espera un segundo y falla por tiempo agotado. *(Apunte 17.)*

**72.** La clase `Registro` no comprueba nada, pero la tabla tiene `CHECK (… BETWEEN 1 AND 5)` en cada nota. Esta prueba pasa.

```python
def test_la_base_de_datos_no_acepta_notas_fuera_de_1_a_5():
    with pytest.raises(sqlite3.IntegrityError):
        almacen.guardar(Registro(6, 3, 5))
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El **`CHECK`** hace que la base de datos rechace el 6 con un `IntegrityError`, que es lo que espera **`pytest.raises`**. Sin el `CHECK`, se guardaría y la prueba fallaría. *(Apunte 17.)*

**73.** `media` divide entre `3` en lugar de entre `len(registros)`, y todas las pruebas pasan. Por tanto, `media` está bien.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Si las pruebas usan siempre **tres registros**, el error **no se nota**. Hay que **variar los datos** (uno, dos, ninguno): una prueba que pasa no demuestra que el código esté bien. *(Apunte 17.)*

**74.** Las pruebas usan la base de datos de verdad, que al principio está vacía. Una prueba guarda dos registros y comprueba que se leen exactamente esos dos: pasa la primera vez y falla la segunda.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* La primera vez se leen 2; la segunda ya están **los de la vez anterior** y se leen 4. Cada prueba tiene que estar **aislada** y empezar **desde cero**. *(Apunte 17.)*

**75.** Una media ponderada se compara con `pytest.approx(3.7)` y no con `== 3.7` porque los decimales se guardan de forma aproximada.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* En binario, `0.1 + 0.2` da `0.30000000000000004`. **`approx`** compara con un **margen** muy pequeño. *(Apunte 17.)*

**76.** Una ventana restaura con `QSettings` la última búsqueda, «Error», que coincide con 3 de sus 8 registros. `busquedaCambiada` está conectada primero con el filtro y después con `mostrar_resultados`, que cuenta las filas del proxy. Si `restaurar_estado()` se llama antes de cargar los registros, la barra de estado dice «0 registros» y la tabla también se queda vacía.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* La barra sí dice 0, porque se contó con el modelo aún vacío y nadie vuelve a contar. Pero la tabla muestra **3**: el proxy **guarda el filtro** y lo aplica a las filas que llegan después. El filtro es un estado y el recuento, una foto. Por eso el estado se restaura al final de `__init__`. *(Apunte 14.)*

**77.** Sacar la comprobación del título a una función sin widgets, `error_titulo(titulo)`, permite probar la regla sin abrir el diálogo.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Es la **separación de responsabilidades**: la lógica, fuera de la interfaz. Una **prueba unitaria** la comprueba rápido y aislada, sin un `QMessageBox` que espere un clic. *(Apunte 17.)*

**78.** Para reconocer tres signos de la lengua de signos que no están entre los gestos de un modelo ya entrenado, hay que entrenar un modelo propio.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Un **modelo ya entrenado** solo reconoce lo que decidió quien lo entrenó. Hay que entrenar uno **propio**, con muchos ejemplos de cada signo, por ejemplo con Teachable Machine. *(Apunte 18.)*

**79.** El detector acepta un gesto con una confianza mayor que 0,6. Une cada situación con el concepto que la describe.

| | Situación | | Concepto |
|---|---|---|---|
| 1 | El modelo da «Thumb_Up» con 0,58 | a | Modelo propio, con Teachable Machine |
| 2 | El 0,6 a partir del cual se acepta un gesto | b | Falso positivo |
| 3 | Mientras la mano pasa del puño a la victoria, el modelo ve un instante «Thumb_Up» | c | Confirmación durante varias imágenes seguidas |
| 4 | Hay que reconocer tres signos que el modelo no conoce | d | Umbral |
| | | e | Confianza |

1 → **e** &nbsp;&nbsp;&nbsp; 2 → **d** &nbsp;&nbsp;&nbsp; 3 → **b** &nbsp;&nbsp;&nbsp; 4 → **a**

*Por qué:* El 0,58 es la **confianza** del modelo, que no llega al **umbral**. Ver un gesto que nadie ha hecho es un **falso positivo**; la **confirmación** lo evita, pero no lo describe. Para signos nuevos hace falta un modelo **propio**. *(Apunte 19.)*

**80.** Para dictar las notas de los pacientes de un hospital, el reconocimiento de voz en el propio equipo protege más la privacidad que en la nube.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* La voz, con **datos de salud**, **no sale del ordenador**, y funciona sin conexión. En la nube puede acertar más, pero envía la voz fuera. *(Apunte 18.)*

**81.** Con este código, si el gesto más probable es `Thumb_Up` con 0,55, `gesto` vale `"Thumb_Up"`.

```python
gesto = None
if mejor.category_name != "None" and mejor.score > 0.6:
    gesto = mejor.category_name
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* 0,55 **no supera el umbral** de 0,6: `gesto` sigue siendo `None`. La aplicación solo acepta lo que supera el umbral de **confianza**. *(Apunte 19.)*

**82.** Con el código de la pregunta 81, si el resultado es `"None"` (la clase del modelo para una mano sin ningún gesto conocido) con 0,9, la aplicación lo toma como un gesto, porque supera el umbral.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* La condición descarta `"None"` **aunque el modelo esté muy seguro**: `gesto` vale `None`, «sin gesto». *(Apunte 19.)*

**83.** Con este código y `CONFIRMAR = 5`, la secuencia de imágenes 5 pulgares arriba, 6 sin gesto y 5 pulgares arriba emite `gestoDetectado` dos veces.

```python
def _procesar(self, gesto):
    if gesto == self._candidato:
        self._repeticiones += 1
    else:
        self._candidato, self._repeticiones = gesto, 1
    if self._repeticiones == self.CONFIRMAR:
        if gesto is not None and gesto != self._ultimo:
            self.gestoDetectado.emit(gesto)
        self._ultimo = gesto
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Las 6 imágenes sin gesto llegan a 5 y **confirman «sin gesto»**: `_ultimo` pasa a `None`, aunque no se emite nada. Así, el segundo pulgar es distinto del último y se emite. Con solo 2 imágenes sin gesto, `_ultimo` seguiría siendo el pulgar y se emitiría una sola vez. *(Apunte 19.)*

**84.** Con el código de la pregunta 83, la secuencia 6 pulgares arriba, 1 victoria y 6 pulgares arriba emite `gestoDetectado` dos veces.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El primer pulgar se confirma y se emite, y `_ultimo` pasa a ser el pulgar. La victoria **reinicia la cuenta**, pero dura una sola imagen y no se confirma: `_ultimo` sigue siendo el pulgar. El segundo pulgar llega a 5, pero es igual que el último y no se emite. Se emite una vez. *(Apunte 19.)*

**85.** Si `CONFIRMAR` pasa de 5 a 10 y la cámara se lee al mismo ritmo, hay que mantener un gesto más o menos el doble de tiempo para que cuente.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El tiempo depende del número de imágenes seguidas y del intervalo del temporizador: con el doble de imágenes, más o menos el doble de tiempo. Con una imagen cada 66 ms, entre la primera y la última imagen hay 4 intervalos con 5 (unos 0,26 s) y 9 con 10 (unos 0,59 s). Habrá menos falsos positivos, pero la aplicación responderá más lenta. *(Apunte 19.)*

**86.** Subir el umbral de confianza de 0,6 a 0,9 hace que, con poca luz, se reconozcan más gestos reales.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Al revés: con un umbral más alto hay menos falsos positivos, pero **más gestos reales sin reconocer**, sobre todo con poca luz. Ajustar el umbral es un **equilibrio**. *(Apunte 19.)*

**87.** Une cada elemento del código de las preguntas 83 y 92 con su papel.

| | Elemento | | Papel |
|---|---|---|---|
| 1 | `CONFIRMAR` | a | Evita que un gesto mantenido dispare la acción muchas veces |
| 2 | `_ultimo` | b | Lee una imagen de la cámara cada poco tiempo, sin bloquear la ventana |
| 3 | `gestoDetectado` | c | Desmarca la opción del menú si la cámara no se puede abrir |
| 4 | `setChecked(False)` | d | Señal con la que el detector avisa a la aplicación |
| | | e | Nº de imágenes seguidas que tiene que durar un gesto |

1 → **e** &nbsp;&nbsp;&nbsp; 2 → **a** &nbsp;&nbsp;&nbsp; 3 → **d** &nbsp;&nbsp;&nbsp; 4 → **c**

*(Apunte 19.)*

**88.** Leer la cámara con un bucle `while` que no para, en lugar de con un `QTimer`, deja la ventana sin responder.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El `while` **bloquea el bucle de eventos**. Con el **`QTimer`**, se lee una imagen cada poco tiempo y, entre una y otra, la ventana sigue atendiendo clics y teclas. *(Apunte 5.)*

**89.** El detector de gestos tiene que heredar de `QWidget` para tener señales propias.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* El detector **no se ve**: con **`QObject`** basta para tener señales propias y un `QTimer`. Si se crea con la ventana como **padre**, se destruye con ella. *(Apunte 20.)*

**90.** El mismo detector de gestos sirve en dos aplicaciones distintas porque solo detecta y avisa con una señal: el significado de cada gesto lo pone cada aplicación.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El detector **no sabe nada de la ventana**: cada aplicación conecta su señal con su propio slot. Es **desacoplamiento**, y por eso es **reutilizable**. *(Apunte 20.)*

**91.** En esta clase, si `super().__init__()` se moviera al final del constructor, la línea que crea el detector daría un error.

```python
class VentanaConGestos(VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.detector = gestos.DetectorGestos(self)
        self.accion_gestos = QAction("Gestos de la mano", self)
        self.ui.menuArchivo.insertAction(self.ui.actionSalir, self.accion_gestos)
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* `super().__init__()` crea la parte de Qt de la ventana y `self.ui`. Antes de esa línea, el detector no puede usar la ventana como padre: da un `RuntimeError`. *(Apunte 20.)*

**92.** Se marca la opción «Gestos de la mano», cuyo `toggled` está conectado con este método, y la cámara no se puede abrir. `activar_gestos` se ejecuta dos veces.

```python
def activar_gestos(self, activar):
    if not activar:
        self.detector.detener()
        self.ui.statusbar.showMessage("Gestos desactivados", 3000)
    elif self.detector.iniciar():
        self.ui.statusbar.showMessage("Gestos activados", 3000)
    else:
        self.accion_gestos.setChecked(False)
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* `setChecked(False)` desmarca la opción, y eso emite otra vez **`toggled`**, ahora con `False`: `activar_gestos` se ejecuta de nuevo y apaga el detector. *(Apunte 20.)*

**93.** Hay 5 filas a la vista y ninguna seleccionada. Con este método, `mover_seleccion(-1)` selecciona la última fila.

```python
def mover_seleccion(self, paso):
    filas = self.proxy.rowCount()
    if filas == 0:
        return
    actuales = self.ui.tabla.selectionModel().selectedRows()
    fila = actuales[0].row() + paso if actuales else 0
    self.ui.tabla.selectRow(max(0, min(fila, filas - 1)))
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* Sin selección, `actuales` es una lista vacía y `fila` vale **0**, sea cual sea el paso: selecciona la **primera**. Con selección, `max(0, min(fila, filas - 1))` recorta la fila para que nunca se salga de la tabla. *(Apunte 20.)*

**94.** Con `CATEGORIAS = ("docente", "materiales", "clases", "instalaciones")` y el foco en «materiales», cinco gestos de victoria seguidos dejan el foco en «clases».

```python
categoria = CATEGORIAS[(CATEGORIAS.index(categoria) + 1) % len(CATEGORIAS)]
```

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* Desde «materiales», la posición 1, pasa a «clases» (2), a «instalaciones» (3), a «docente» (0, porque (3 + 1) % 4 da 0), a «materiales» (1) y a «clases» (2). El **resto (`%`)** recorre la lista **en círculo**: cuatro pasos vuelven al mismo sitio. *(Apunte 20.)*

**95.** El selector es el de la pregunta 59, y su método público `limpiar()` hace `self.nota = 0`. Para dejar el selector sin nota, `selector._nota = 0` también redibuja las estrellas y avisa a la ventana, igual que `selector.limpiar()`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* `_nota` es **interno**: cambiarlo no redibuja las estrellas ni emite la señal, y la ventana no se entera. Hay que usar la **API pública**, `limpiar()`. *(Apunte 15.)*

**96.** Une cada pregunta que se hace una aplicación con lo que necesita para responderla.

| | Pregunta | | Lo que necesita |
|---|---|---|---|
| 1 | ¿Tiene la persona los brazos levantados? | a | Un marcador o una superficie reconocida en la imagen |
| 2 | ¿Es un pulgar arriba? | b | El ángulo entre la cadera, la rodilla y el tobillo |
| 3 | ¿Dónde se dibuja la etiqueta del objeto? | c | El texto que ha reconocido el modelo de voz |
| 4 | ¿Está la rodilla doblada? | d | La posición de las muñecas respecto a los hombros, con el modelo de postura |
| | | e | La forma de la mano, con sus 21 puntos |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **e** &nbsp;&nbsp;&nbsp; 3 → **a** &nbsp;&nbsp;&nbsp; 4 → **b**

*Por qué:* El modelo de postura da 33 puntos del cuerpo, con los que se comparan posiciones, como la muñeca y el hombro, o se calculan ángulos, como el de la rodilla. La forma de la mano la da el reconocedor de gestos. La realidad aumentada necesita una referencia en la imagen para dibujar en el sitio correcto. *(Apunte 21.)*

**97.** Una aplicación de escritorio que se maneje solo con gestos, sin teclado, es más accesible.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☒

*Por qué:* No todo el mundo puede hacer gestos, y el reconocimiento se equivoca: siempre tiene que haber una **alternativa**, y todo debe poder hacerse **con el teclado**. *(Apunte 18.)*

**98.** En un almacén ruidoso conviene usar órdenes de voz cortas, pocas y distintas entre sí, y pedir confirmación antes de eliminar.

**V** ☒ &nbsp;&nbsp;&nbsp; **F** ☐

*Por qué:* El **ruido** provoca errores de reconocimiento, y con pocas órdenes distintas es más fácil acertar. Antes de algo **irreversible**, se confirma diciendo cuál; si no entiende la respuesta, no hace nada. *(Apunte 18.)*

**99.** Une cada criterio de diseño de interfaces naturales con un ejemplo.

| | Criterio | | Ejemplo |
|---|---|---|---|
| 1 | Alternativa | a | Tras cada gesto, la barra de estado dice qué ha entendido la aplicación |
| 2 | Retroalimentación | b | Mantener el brazo levantado durante horas cansa |
| 3 | Privacidad | c | «¿Eliminar el registro "Exportar a CSV"? Di sí o no» |
| 4 | Confirmación | d | Todo lo que se hace con gestos se puede hacer también con el teclado |
| | | e | La cámara solo se enciende al marcar una opción del menú |

1 → **d** &nbsp;&nbsp;&nbsp; 2 → **a** &nbsp;&nbsp;&nbsp; 3 → **e** &nbsp;&nbsp;&nbsp; 4 → **c**

*(Apunte 18.)*

**100.** Une cada prueba con su tipo.

| | Prueba | | Tipo |
|---|---|---|---|
| 1 | Tras cambiar el orden de los parámetros del `Buscador`, se vuelven a pasar todas las pruebas | a | Unitaria |
| 2 | Se comprueba que `media([4, 2])` da 3, sin ventana ni base de datos | b | De integración |
| 3 | Se escribe un registro en la ventana y se comprueba que queda en la base de datos | c | De usabilidad |
| 4 | Una persona que no conoce la aplicación intenta añadir y eliminar un registro sin ayuda | d | De humo |
| | | e | De regresión |

1 → **e** &nbsp;&nbsp;&nbsp; 2 → **a** &nbsp;&nbsp;&nbsp; 3 → **b** &nbsp;&nbsp;&nbsp; 4 → **c**

*Por qué:* El tipo depende de **qué** se comprueba: una pieza sola (unitaria), varias piezas juntas (integración), que lo que funcionaba sigue funcionando tras un cambio (regresión) o que las personas consiguen usarla (usabilidad). *(Apunte 17.)*

---

## Apuntes para entender las respuestas

Estos apuntes explican, con ejemplos y paso a paso, los temas en los que se apoyan muchas respuestas. Cada respuesta indica su apunte. No hace falta memorizarlos: la idea es entender qué pasa y por qué, para poder razonarlo en cualquier caso parecido.

### 1. Usabilidad, accesibilidad y estándares

**Dos ideas distintas.** La **usabilidad** es que una aplicación sea fácil, eficiente y agradable de usar para quien la usa. La **accesibilidad** es que la pueda usar **cualquier persona**, también con una discapacidad: quien no ve bien la pantalla, quien no puede usar el ratón, quien no distingue algunos colores. Son cosas distintas: una aplicación puede ser muy cómoda con el ratón y, a la vez, imposible de usar solo con el teclado. Sería usable para unos y nada accesible para otros.

**La usabilidad según la ISO 9241.** Esta norma la divide en tres partes. En un formulario para dar de alta un registro:

| Parte | Qué significa | En el formulario |
|---|---|---|
| Eficacia | Conseguir el objetivo | El registro queda guardado, con sus datos bien |
| Eficiencia | Conseguirlo con poco esfuerzo y tiempo | Pocos pasos, atajos, controles que no dejan escribir mal |
| Satisfacción | Que usarla no frustre | Mensajes claros, nada que confunda |

**Por qué seguir estándares.** Lo que ya se conoce de otras aplicaciones funciona igual, y no hay que aprenderlo otra vez; hay menos errores; y en accesibilidad, a veces es **obligatorio**, por ejemplo en el sector público.

- **WCAG**: las pautas de accesibilidad del W3C, que también se usan como referencia en aplicaciones. Se organizan en cuatro principios: **perceptible** (se puede ver u oír), **operable** (se puede manejar, también con el teclado), **comprensible** y **robusto**. Tienen tres niveles: A, AA y AAA. El que se suele exigir es el **AA**.
- **EN 301 549**: la norma europea a través de la cual se exigen las WCAG. En España se exigen a las webs y aplicaciones del sector público, con el **Real Decreto 1112/2018**.
- **ISO 9241**: norma de ergonomía, con la definición de usabilidad de la tabla.

**El contraste.** Es una de las comprobaciones más habituales del principio perceptible. Se mide como una relación entre el color del texto y el del fondo: cuanto mayor, más se distinguen. El nivel AA pide **al menos 4,5:1** para el texto normal. El poco contraste lo sufren las personas con baja visión, pero también cualquiera que mire la pantalla con mucha luz, por ejemplo al sol: por eso el mínimo vale para todos los textos.

| Texto blanco sobre… | Contraste | ¿Cumple el AA? |
|---|---|---|
| azul | 4,85:1 | Sí |
| rojo | 4,0:1 | No: hay que oscurecer el rojo |

**No depender solo del color.** Si un botón activado y desactivado solo se distinguen por el tono, quien no distingue bien los colores no sabe si se puede pulsar. Conviene que cambie algo más: el color del texto, el borde, un icono.

### 2. Heurísticas de Nielsen y cómo se evalúa una interfaz

**Qué son.** Las **heurísticas de Nielsen** son diez principios generales para diseñar interfaces fáciles de usar. No son reglas exactas, sino preguntas para revisar una interfaz: «¿sabe la persona qué está pasando?», «¿puede deshacer?». Las que más se usan en este módulo, con un ejemplo de cada una:

| Heurística | Qué pide | Ejemplo |
|---|---|---|
| Visibilidad del estado del sistema | Que la aplicación diga qué está pasando | Al añadir un registro, la barra de estado lo confirma |
| Relación con el mundo real | Hablar el idioma de quien la usa, no el del programa | «La nota tiene que estar entre 1 y 5», no «CHECK constraint failed» |
| Control y libertad | Poder salir o deshacer sin consecuencias | Todos los diálogos tienen «Cancelar» |
| Coherencia y estándares | Que lo habitual funcione como siempre | Ctrl+N es «Nuevo», Ctrl+S guarda y Supr elimina, como en cualquier programa |
| Prevención de errores | Evitar el error mejor que avisar después | «Eliminar» desactivado si no hay nada seleccionado |
| Reconocer mejor que recordar | Que las opciones estén a la vista | Elegir de una lista desplegable en lugar de escribir el valor de memoria |
| Flexibilidad y eficiencia de uso | Atajos para quien tiene práctica | Intro en el campo de texto hace lo mismo que el botón |
| Ayudar a reconocer y corregir errores | Mensajes que digan qué pasa y qué hacer | «Escribe un título: es obligatorio» |

**Un ejemplo con varias a la vez.** Ctrl+S añade un registro si no hay ninguno seleccionado y modifica el seleccionado si lo hay, y nada lo indica. Quien selecciona un registro para crear otro parecido lo modifica sin saberlo. Incumple la **visibilidad del estado del sistema** (no sabe en qué modo está) y el **control y libertad** (no puede deshacer). Se arregla mostrando el modo («Editando…») o separando las acciones de añadir y modificar.

**Las convenciones también cuentan.** Los puntos suspensivos de una opción de menú, como «Pesos…», avisan de que **abre un diálogo** antes de hacer nada. Quien usa otras aplicaciones ya lo sabe: es coherencia.

**Dos formas de evaluar una interfaz.**

- La **evaluación heurística** la hace quien conoce las heurísticas: recorre la interfaz y, para cada problema, apunta qué heurística incumple y cómo se arreglaría.
- La **prueba de usabilidad** se hace con **personas que no conocen la aplicación**. Hacen tareas concretas sin ayuda («añade un registro y elimínalo») mientras **piensan en voz alta**, y se apunta si lo consiguen, cuánto tardan y dónde dudan. Descubre problemas que quien diseñó la aplicación no ve.

### 3. Usar una aplicación con el teclado y el lector de pantalla

**Por qué importa.** Hay personas que no pueden usar el ratón y personas que no ven la pantalla y usan un **lector de pantalla**, un programa que lee en voz alta lo que hay. Además, el teclado es más rápido para quien tiene práctica. Una aplicación accesible se tiene que poder usar entera con el teclado.

**Atajos con `&` y el *buddy*.**

```python
formulario.addRow("&Título:", self.txtTitulo)
formulario.addRow("T&ipo:", self.cmbTipo)
```

La `&` delante de una letra crea un **atajo**: Alt más esa letra. La letra sale subrayada. El ***buddy*** es el campo asociado a la etiqueta (`addRow` los une): el atajo lleva el foco a ese campo. Cada etiqueta necesita una letra distinta. Si las dos fueran `&Título` y `&Tipo`, las dos usarían Alt+T y el atajo no llevaría a un único campo; por eso la segunda usa la I.

**El foco y Tab.** El **foco** indica qué control recibe las teclas. Tab lo pasa al siguiente control, en un orden que sigue el de los controles en la ventana. Dos detalles:

- El control con el foco tiene que **verse** (un marco, un color): si no, quien usa el teclado no sabe dónde está.
- En un `QTextEdit`, Tab **escribe un tabulador** en el texto en lugar de pasar al siguiente control: quien usa solo el teclado no podría salir del campo. `setTabChangesFocus(True)` hace que Tab pase al siguiente.

**Componentes con piezas.** Un selector de cinco estrellas está hecho de cinco botones. Si cada estrella pudiera recibir el foco, una ventana con tres selectores tendría 15 paradas de Tab en lugar de 3. Por eso las estrellas llevan `setFocusPolicy(Qt.NoFocus)` y el componente entero, `Qt.StrongFocus`: para el teclado y para el lector de pantalla es **una sola pieza**, que se maneja con las flechas.

**Nombres para el lector de pantalla.** Un botón que solo muestra un icono, como una papelera, no tiene texto que leer. Le hace falta un **nombre accesible**, `setAccessibleName("Eliminar registro")`, para que el lector diga qué hace. Un ***tooltip***, `setToolTip("Eliminar (Supr)")`, ayuda además a quien usa el ratón y no reconoce el icono.

**Cómo se comprueba.** Usar la aplicación **solo con el teclado** (llegar a todo, en un orden lógico, viendo siempre el foco), probarla con un **lector de pantalla** y revisar el **contraste** de los textos.

### 4. Qt, PySide6 y el entorno virtual

**Qt y PySide6.** **Qt** es un framework, escrito en C++, para crear interfaces gráficas **multiplataforma**: el mismo programa funciona en Windows, Linux y macOS. Desde Python se usa a través de una librería que da acceso a sus clases:

- **PySide6**, la versión **oficial**, de The Qt Company, con licencia LGPL;
- **PyQt6**, de otra empresa, con licencia GPL o comercial.

Las dos tienen las mismas clases de Qt; lo que más las distingue es la licencia. **Tkinter** viene ya con Python y es más sencilla, pero no tiene un editor visual oficial como Qt Designer.

**El entorno virtual.** Es una carpeta del proyecto, normalmente `.venv`, con su propio Python y sus propias librerías. Sirve para que cada proyecto tenga las versiones que necesita sin mezclarse con los demás. Se crea una vez y se **activa** en cada terminal que se abre; se nota porque el indicador de la terminal empieza por `(.venv)`.

Un caso típico: ayer se instaló PySide6 y la aplicación funcionaba. Hoy, en una terminal nueva, `python main.py` dice que no encuentra el módulo `PySide6`. No se ha borrado nada: la terminal nueva no tiene el entorno activado, y `python` es el del sistema, que no tiene PySide6. Se activa el entorno y vuelve a funcionar.

**`requirements.txt`** lista las librerías del proyecto. Con `pip install -r requirements.txt`, otro equipo **reproduce** el mismo entorno.

### 5. Cómo arranca una aplicación con ventanas y por qué una ventana puede desaparecer

**La idea.** Un programa normal de Python se ejecuta de arriba abajo y termina. Una aplicación con ventanas no puede hacer eso: tiene que quedarse esperando a que alguien haga clic o escriba. Esa espera la hace el **bucle de eventos**.

```python
app = QApplication()
ventana = Ventana()
ventana.show()
app.exec()
print("Después")
```

Qué hace cada línea:

1. `QApplication()` crea el objeto que conecta el programa con el sistema: la pantalla, el ratón y el teclado. Solo hay uno, y tiene que existir **antes que cualquier ventana**. Si se crea una ventana antes, el programa se detiene con un error.
2. `Ventana()` crea la ventana en memoria, pero todavía no se ve.
3. `show()` la hace visible.
4. `app.exec()` arranca el **bucle de eventos**. A partir de aquí, el programa se queda dentro de esa línea: espera un evento (un clic, una tecla, el aviso de un temporizador), ejecuta el código que corresponde y vuelve a esperar. Solo sale cuando se cierra la última ventana.
5. Por eso `print("Después")` no se escribe hasta que se cierra la ventana.

Sin `app.exec()` no hay bucle: el programa llega al final y termina, y la ventana desaparece nada más mostrarse.

**Mientras se ejecuta un slot, el bucle está parado.** El bucle atiende los eventos de uno en uno. Mientras se ejecuta el código de un clic, no puede atender otro clic ni volver a dibujar la ventana. Si ese código tarda mucho, la ventana se queda congelada. Un `while True` que lee la cámara no termina nunca, así que la ventana deja de responder para siempre. La solución es un **`QTimer`**: cada pocos milisegundos emite una señal, su slot lee **una sola** imagen y termina, y entre una lectura y la siguiente el bucle sigue atendiendo la ventana.

**Guardar en `self` o en una variable local.** Lo que se crea en el `__init__` en una variable normal, **local**, solo existe mientras se ejecuta el `__init__`. Lo que se guarda en `self` queda guardado en la ventana y se puede usar desde sus otros métodos:

```python
def __init__(self):
    super().__init__()
    self.boton = QPushButton("Añadir")
    distribucion = QVBoxLayout(self)
    distribucion.addWidget(self.boton)

def bloquear(self):
    self.boton.setEnabled(False)
```

El botón va en `self.boton` porque otro método, `bloquear`, lo usa para desactivarlo. La distribución solo se usa dentro del `__init__`, así que basta una variable local. Si el botón se guardara en `boton`, sin `self`, `bloquear` no lo encontraría y daría un `NameError`.

**En una clase hija, `super().__init__()` va lo primero.** Una ventana propia hereda de `QWidget` o de otra ventana. `super().__init__()` ejecuta el constructor de la clase madre, que es quien crea de verdad el objeto de Qt y, en una ventana hecha con Qt Designer, `self.ui` con todos sus controles. Antes de esa línea, el objeto está a medio hacer: no se puede usar como padre de otro objeto (da un `RuntimeError`) y `self.ui` todavía no existe.

### 6. Señales, slots y eventos

**La idea.** Una **señal** es como un timbre, y un **slot**, lo que se hace al oírlo. El botón no sabe qué va a hacer la aplicación: solo avisa de que lo han pulsado. Es la ventana la que decide qué hacer, conectando ese aviso con uno de sus métodos. Así, el mismo botón sirve en cualquier aplicación: es el **desacoplamiento**.

```python
self.boton.clicked.connect(self.anadir_fila)
```

Se lee así: «cuando el botón emita `clicked`, ejecuta `anadir_fila`».

**Sin paréntesis.** `connect` necesita **la función misma**, para guardarla y llamarla más tarde, en cada clic. `self.anadir_fila` es la función; `self.anadir_fila()` es **llamarla ahora** y quedarse con lo que devuelve. Con paréntesis pasa esto:

1. `anadir_fila` se ejecuta una vez, en ese momento, sin que nadie haya pulsado nada.
2. Devuelve `None`, porque no tiene `return`.
3. `connect` recibe `None`, que no es una función, y da un `TypeError`. Como esto pasa en el `__init__`, la ventana ni siquiera llega a abrirse.

**Una señal, varios slots.** Una señal se puede conectar con varios slots, y al emitirse los ejecuta uno detrás de otro, **en el orden en que se conectaron**. En un buscador:

```python
self.buscador.busquedaCambiada.connect(self.proxy.setFilterFixedString)
self.buscador.busquedaCambiada.connect(self.mostrar_resultados)
```

Al escribir, primero se filtra la tabla y después `mostrar_resultados` cuenta las filas que quedan. Si se conectaran al revés, se contarían antes de filtrar, con el filtro anterior, y el número no coincidiría con lo que se ve. Por lo mismo, si un slot se conecta dos veces, se ejecuta dos veces en cada clic.

**Los eventos no se conectan.** Algunas cosas no llegan como señal, sino como **evento**: pulsar una tecla o cerrar la ventana. Qt llama directamente a un método del widget con un **nombre fijo**: `keyPressEvent` para las teclas y `closeEvent` para el cierre. Para cambiar lo que hacen, se escribe ese método en la clase (se **sobrescribe**); no hay nada que conectar.

```python
def keyPressEvent(self, evento):
    if evento.key() == Qt.Key_Right:
        self.subir_nota()
    else:
        super().keyPressEvent(evento)
```

Las teclas que el widget no usa se pasan a `super().keyPressEvent(evento)`. La clase madre no las usa y las deja pasar, y Qt las manda al **widget padre**, por ejemplo a la ventana. Así, Intro puede llegar a la ventana y guardar aunque el foco esté en un componente. Sin esa línea, el componente se quedaría con todas las teclas, también las que no usa.

### 7. Lambdas en un bucle y el argumento `checked`

**Qué es una lambda.** Es una función pequeña, sin nombre, escrita en una línea. Estas dos formas hacen lo mismo:

```python
def mostrar():
    self.etiqueta.setText("Baja")

lambda: self.etiqueta.setText("Baja")
```

En `connect` se usa para **envolver** una llamada que lleva un dato. `connect(self.etiqueta.setText("Baja"))` no sirve, porque ejecutaría `setText` en ese momento (apunte 6). La lambda envuelve la llamada para que espere al clic.

**El problema del bucle.**

```python
for nombre in ["Baja", "Media", "Alta"]:
    boton = QPushButton(nombre)
    boton.clicked.connect(lambda: self.etiqueta.setText(nombre))
```

Se esperaría que cada botón mostrara su texto, pero los tres muestran «Alta». La lambda **no copia** el valor de `nombre` al crearse: guarda **la variable** y la lee **al ejecutarse**, es decir, al pulsar el botón.

- Vuelta 1: se crea la lambda del botón «Baja»; `nombre` vale «Baja».
- Vuelta 2: se crea la lambda de «Media»; la **misma** variable `nombre` vale ahora «Media».
- Vuelta 3: se crea la lambda de «Alta»; `nombre` vale «Alta».
- El bucle termina y `nombre` se queda con «Alta».

Al pulsar cualquier botón, su lambda lee `nombre` en ese momento, y vale «Alta». Es como si las tres lambdas miraran la misma caja, y en la caja quedó lo último que se metió.

**Primer arreglo: un valor por defecto.** En Python, el valor por defecto de un parámetro se calcula **una sola vez, al crear la función**, no al llamarla:

```python
lambda texto=nombre: self.etiqueta.setText(texto)
```

Ahora cada lambda tiene su propio `texto`, que guarda el valor que tenía `nombre` en su vuelta: «Baja», «Media» o «Alta». Ya no depende de la variable del bucle.

**Pero aparece otro problema: `checked`.** La señal `clicked` **envía un dato** al emitirse: `checked`, que dice si el botón está marcado. Sirve para los botones que se quedan pulsados, como un interruptor; en un botón normal siempre vale `False`. PySide6 pasa a la lambda tantos datos de la señal como esta pueda recibir, empezando por el primer parámetro. Esta lambda tiene un parámetro, `texto`, así que `checked` entra ahí y **pisa** el valor por defecto: `texto` vale `False`, y `setText(False)` da un error, porque espera un texto.

**Arreglo completo: dos parámetros.**

```python
lambda _=False, texto=nombre: self.etiqueta.setText(texto)
```

El primer parámetro recoge `checked`; se llama `_` porque en Python ese nombre indica «aquí llega algo que no se va a usar». El segundo, `texto`, no recibe nada y conserva su valor por defecto.

| Lambda | Al pulsar «Baja» |
|---|---|
| `lambda: self.etiqueta.setText(nombre)` | Muestra «Alta»: lee `nombre` al pulsar |
| `lambda texto=nombre: self.etiqueta.setText(texto)` | `checked` pisa `texto`: error |
| `lambda _=False, texto=nombre: self.etiqueta.setText(texto)` | Muestra «Baja» |

### 8. Construir la interfaz: controles, layouts, Qt Designer y hojas de estilo

**Elegir el control según el dato.** Un buen control impide escribir un valor imposible, y así casi no hace falta validar: es **prevención de errores**.

| Dato | Control |
|---|---|
| Uno de varios valores fijos (un aula de seis) | `QComboBox`, lista desplegable |
| Una fecha | `QDateEdit` |
| Un número con límites (de 1 a 30) | `QSpinBox` con `setRange(1, 30)` |
| Sí o no | `QCheckBox` |
| Un texto corto | `QLineEdit` |
| Un texto largo | `QTextEdit` |

**Layouts.** Un layout coloca los controles solo y los recoloca al cambiar el tamaño de la ventana.

- `QVBoxLayout`: uno debajo de otro.
- `QHBoxLayout`: uno al lado de otro.
- `QFormLayout`: parejas de etiqueta y campo; `addRow` crea la etiqueta y la une al campo.
- Un layout puede ir **dentro de otro** con `addLayout`.
- `addStretch()` añade un **espacio elástico** que ocupa lo que sobra. Delante de dos botones en un `QHBoxLayout`, los empuja a la derecha.

```python
botones = QHBoxLayout()
botones.addStretch()
botones.addWidget(self.btnAceptar)
botones.addWidget(self.btnCancelar)
```

**Qt Designer y el código generado.** Qt Designer permite dibujar la ventana en lugar de escribirla:

1. El diseño se guarda en un archivo **`.ui`**.
2. **`pyside6-uic`** lo convierte en código Python: `pyside6-uic ventana.ui -o ui_ventana.py`.
3. La clase propia de la ventana llama a **`setupUi(self)`**, que crea los controles en `self.ui`.

Cada vez que se cambia el diseño, `pyside6-uic` **regenera el archivo entero**: lo que se hubiera escrito a mano en `ui_ventana.py` se pierde. Por eso los controles se añaden en Qt Designer y la **lógica** (los `connect` y los métodos) va en la clase propia, que no se regenera.

**Hojas de estilo (QSS).** Dicen el aspecto de los controles con **reglas** parecidas al CSS de las páginas web. Se aplican con `setStyleSheet`; en la ventana, valen para ella y para todo lo que contiene. Conviene tenerlas en un archivo aparte, separadas de la lógica.

```css
QPushButton { padding: 6px; }
#boton_eliminar { background-color: red; color: white; }
#boton_eliminar:disabled { background-color: lightcoral; }
```

- `QPushButton` se aplica a todos los botones.
- `#boton_eliminar` se aplica solo al control cuyo **`objectName`** es `boton_eliminar`. Ese nombre se le da con `setObjectName("boton_eliminar")`.
- `:disabled` es un **estado**: la regla solo vale cuando el control está desactivado.

### 9. Diálogos y validación

**Diálogos modales.** Un diálogo **modal** bloquea la ventana principal hasta que se cierra: no se puede tocar nada más.

```python
dialogo = Dialogo(self)
if not dialogo.exec():
    return
bd.insertar(*dialogo.datos())
```

- `exec()` muestra el diálogo y **espera** a que se cierre. Devuelve verdadero si se acepta y falso si se cancela.
- Cerrar el diálogo lo **oculta**, no lo destruye. El objeto sigue existiendo mientras la variable `dialogo` lo guarde, con sus campos y lo que se escribió en ellos. Por eso `dialogo.datos()` funciona después de cerrarlo.
- `datos()` devuelve una tupla con los valores. El `*` la **desempaqueta**: pasa cada valor como un argumento separado, en orden. `insertar(*("Hola", "Alta"))` es lo mismo que `insertar("Hola", "Alta")`.

**`strip()` antes de comprobar.** Lo que se escribe en un campo puede llevar espacios al principio o al final sin que se vean. `strip()` los quita:

| Se escribe | Tras `strip()` | Longitud |
|---|---|---|
| `"   "` | `""` | 0 |
| `"  hola  "` | `"hola"` | 4 |
| dos espacios, 99 letras y dos espacios | las 99 letras | 99 |

Por eso se aplica **antes** de comprobar si el campo está vacío o es demasiado largo: si no, un título de solo espacios pasaría por bueno, y uno con espacios de más se rechazaría por largo.

**Un texto vacío no es `NULL`.** `NULL` significa «no hay ningún dato». `""` es un dato: un texto que no tiene letras. Una columna `NOT NULL` frena el primero, pero **no el segundo**. Si un título de solo espacios llega a la base de datos, tras `strip()` es `""`, el `NOT NULL` no protesta y se guarda un registro sin título. Por eso los datos se validan en el código, antes de guardarlos.

**Validar en un diálogo.** «Aceptar» no se conecta directamente con `accept()`, que cerraría el diálogo siempre, sino con un método `validar`:

```python
def validar(self):
    titulo = self.txtTitulo.text().strip()
    if not titulo:
        QMessageBox.warning(self, "Falta el título", "Escribe un título: es obligatorio.")
        return
    self.accept()
```

Si falta algo, avisa y hace `return`, sin `accept()`: el diálogo **sigue abierto** con lo escrito, para corregirlo. Solo cuando todo está bien llama a `accept()`, que lo cierra como aceptado.

### 10. SQLite paso a paso

**La idea.** Trabajar con una base de datos se parece a trabajar con un documento: se abre, se hacen cambios, se guarda y se cierra. Esta función hace esos pasos para cualquier consulta:

```python
def ejecutar_sql(sql, valores=()):
    conexion = sqlite3.connect(RUTA)
    cursor = conexion.execute(sql, valores)
    filas = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return filas
```

1. **`connect`** abre la base de datos, que es un archivo. Si el archivo no existe, lo crea vacío.
2. **`execute`** ejecuta la consulta y devuelve un **cursor**. El cursor es como un marcador que señala los resultados, pero **todavía no los ha leído**.
3. **`fetchall()`** lee todos los resultados y los devuelve como una lista de tuplas, una por fila. Los lee **a través de la conexión**, así que tiene que ir **antes de cerrarla**. Si se pone después de `close()`, da un error con cualquier consulta, también con un `INSERT`.
4. **`commit()`** confirma los cambios: es el «guardar» del documento. Sin él, al cerrar la conexión los cambios **se descartan**, como al cerrar un documento sin guardar. La aplicación parece funcionar, pero al volver a abrirla no hay nada.
5. **`close()`** cierra la conexión.

Como todas las consultas pasan por esta función, esos pasos se escriben una sola vez.

**`CREATE TABLE IF NOT EXISTS`.** La tabla se crea al arrancar la aplicación. Sin `IF NOT EXISTS`, la segunda vez daría un error, porque la tabla ya existe. Con él, solo se crea la primera vez. Pero ojo: si la tabla ya existe, **no hace nada, aunque su definición haya cambiado**. Si se añade una columna en el `CREATE TABLE`, en un equipo nuevo funciona, pero en uno que ya tenía la base de datos la columna no existe y las consultas que la usan fallan. Una tabla existente se cambia con `ALTER TABLE … ADD COLUMN`.

**`AUTOINCREMENT`.** Con `id INTEGER PRIMARY KEY`, la base de datos pone sola el `id` de cada fila nueva: el siguiente al mayor que existe. Con `AUTOINCREMENT`, además, **nunca reutiliza** un `id` borrado. Con los registros 1, 2 y 3, si se borra el 3:

- con `AUTOINCREMENT`, el siguiente es el **4**;
- sin él, el siguiente es otra vez el **3**.

Importa porque, si algo guardaba todavía el `id` 3 (una lista sin recargar, otro programa), con el 3 reutilizado apuntaría a un registro distinto.

**Rutas relativas.** Con `RUTA = "datos.db"`, el archivo se busca en la **carpeta desde la que se lanza** el programa, no en la carpeta del código. Si se lanza desde la carpeta del proyecto, encuentra los datos. Si se lanza desde otra carpeta, no encuentra el archivo, `connect` crea uno nuevo y vacío, y parece que los datos se han perdido. `Path(__file__).with_name("datos.db")` usa la ruta del propio archivo de código (`__file__`) y pone la base de datos siempre a su lado.

**Contar por grupos.** `GROUP BY` junta las filas que tienen el mismo valor en una columna y permite calcular algo de cada grupo:

```sql
SELECT prioridad, COUNT(*) AS total
FROM registros
WHERE estado = 'Pendiente'
GROUP BY prioridad
ORDER BY total DESC
```

1. `WHERE` se queda con las filas pendientes, **antes** de agrupar.
2. `GROUP BY prioridad` hace un grupo por cada prioridad.
3. `COUNT(*)` cuenta las filas de cada grupo, y `AS total` da nombre a esa columna.
4. `ORDER BY total DESC` ordena de más a menos.

Con las filas (Alta, Pendiente), (Media, Pendiente), (Baja, En proceso), (Media, Pendiente), el resultado es Media 2 y Alta 1. Baja no sale: no tiene ninguna pendiente.

### 11. Los valores de una consulta y la inyección SQL

**La idea.** Una consulta tiene dos partes: la **orden** (el SQL) y los **datos** (lo que escribe quien usa la aplicación). Mientras vayan separados, no hay problema. Si se mezclan, los datos pueden convertirse en órdenes.

**Los `?` y la tupla.** Cada `?` es un hueco que se rellena con un valor de la tupla, **por orden**: el primer `?` con el primer valor, el segundo con el segundo, y así.

```python
conexion.execute(
    "UPDATE registros SET titulo = ?, estado = ? WHERE id = ?",
    (titulo, estado, id_registro)
)
```

Si se pone el `id` el primero, `(id_registro, titulo, estado)`, todo se desplaza: el título recibe el `id`, el estado recibe el título y el `WHERE` busca `id = estado`. SQLite no da ningún error al comparar un número con un texto: simplemente ninguna fila cumple la condición y **no se cambia nada**, en silencio.

Los valores van siempre en una **tupla**, aunque sea uno solo. `(id_registro,)`, con la coma, es una tupla de un elemento. `(texto)`, sin coma, **no es una tupla**: los paréntesis solo agrupan y queda el texto tal cual. `sqlite3` lo tomaría como una secuencia de letras, un valor por letra, y daría un error porque hay más valores que huecos.

**La inyección SQL.** Aparece cuando lo que se escribe se **pega** dentro del SQL:

```python
conexion.executescript("INSERT INTO registros (texto) VALUES ('" + texto + "')")
```

Con un texto normal, como `Comprar pan`, queda `INSERT INTO registros (texto) VALUES ('Comprar pan')`, y funciona. Pero si alguien escribe `x'); DELETE FROM registros; --`, queda:

```sql
INSERT INTO registros (texto) VALUES ('x'); DELETE FROM registros; --')
```

1. `'x'` y `);` cierran el `INSERT`: se guarda un registro con el texto «x».
2. `DELETE FROM registros;` es una **orden nueva**, que borra todos los registros. La tabla sigue existiendo, vacía; `DROP TABLE` la borraría.
3. `--` empieza un **comentario**: el `')` que añadía el programa detrás deja de contar y no da error.

`executescript` ejecuta varias sentencias seguidas. `execute` solo admite una, pero el comentario basta para hacer daño. Un formulario de acceso que pega el nombre:

```sql
SELECT * FROM usuarios WHERE nombre = 'admin' --' AND clave = '…'
```

Con el nombre `admin' --`, el `'` cierra el nombre y todo lo que va detrás de `--`, incluida la comprobación de la clave, es un comentario. Se entra como `admin` con cualquier contraseña.

No hace falta mala intención para que falle: un nombre con apóstrofo, como `O'Brien`, cierra la comilla antes de tiempo y la consulta da un error de sintaxis.

**La solución: una consulta parametrizada.**

```python
conexion.execute("INSERT INTO registros (texto) VALUES (?)", (texto,))
```

La orden y el dato viajan **por separado**: `sqlite3` recibe el SQL con su hueco y, aparte, el valor. El valor se guarda tal cual, como texto, aunque contenga comillas, punto y coma o guiones: **nunca se ejecuta como SQL**. El formulario de acceso buscaría a alguien llamado literalmente `admin' --`, y no lo hay.

### 12. Organizar la aplicación: capas, lista recargada y dataclass

**Cada archivo, una responsabilidad.** Una aplicación sencilla se reparte así:

| Archivo | Responsabilidad | Qué no hace |
|---|---|---|
| `main.py` | El arranque: crea la aplicación y la ventana | — |
| `ventana.py` | La interfaz: controles, señales y lo que se ve | No escribe SQL |
| `bd.py` | Los datos: guardar y leer | No sabe nada de widgets |

Es la **separación de responsabilidades**. La ventana pide los datos a funciones de `bd.py` y **no sabe dónde se guardan**. Si mañana se guardaran en un servidor, solo cambiaría `bd.py`. Escribir SQL en la ventana rompe esta separación.

**El flujo al pulsar «Añadir».**

```python
self.boton_anadir.clicked.connect(self.anadir_fila)

def anadir_fila(self):
    texto = self.campo.text().strip()
    if texto:
        bd.insertar(texto)
        self.cargar_filas()
        self.campo.clear()
```

1. El botón emite `clicked` y se ejecuta el slot `anadir_fila`.
2. Lee el texto y lo valida: si está vacío, no hace nada.
3. Pide a `bd.py` que lo **guarde**.
4. **Recarga** la lista entera desde la base de datos y vacía el campo.

**Por qué se recarga la lista.** El `id` de cada registro lo pone **la base de datos** al guardarlo. Recargando, la fila nueva aparece con su `id`, y la lista muestra siempre lo que de verdad hay guardado.

```python
def cargar_filas(self):
    self.lista.clear()
    for id_registro, texto in bd.obtener_registros():
        elemento = QListWidgetItem(texto)
        elemento.setData(Qt.ItemDataRole.UserRole, id_registro)
        self.lista.addItem(elemento)
```

- `clear()` vacía la lista antes de volver a llenarla. Sin él, las filas que ya estaban seguirían y debajo se cargarían todas otra vez: se verían repetidas, aunque en la base de datos no hay nada repetido. La repetición estaría solo en la **vista**.
- Cada fila guarda su `id` con `setData` en un **rol** que no se ve, `UserRole`; el texto va en el rol que se ve. Para eliminar, se recupera con `data(UserRole)`. El texto no sirve, porque puede haber dos registros con el mismo texto: hace falta el **identificador único**, la clave primaria.

**Sin selección, lista vacía.** `selectedItems()` devuelve la lista de filas seleccionadas. Si no hay ninguna, es una lista vacía, y `selectedItems()[0]` da un **`IndexError`**: una lista vacía no tiene elemento 0. Por eso el botón «Eliminar» se desactiva mientras no haya selección (**prevención de errores**).

**Un modelo para los cálculos.** Si la aplicación calcula algo (medias, notas ponderadas), esos cálculos van en una capa aparte, sin widgets ni SQL. Así se pueden **probar** sin abrir ninguna ventana (apunte 17).

**`@dataclass`.** Escribe por nosotros, a partir de los atributos declarados, el `__init__`, el `__repr__` y el `__eq__` de una clase de datos. Con `frozen=True`, el objeto es **inmutable**: después de crearlo, cambiar un atributo da un error.

```python
@dataclass(frozen=True)
class Registro:
    nota: int

r = Registro(4)
r.nota = 5
```

La última línea da un error.

### 13. Proxy, filtros y `mapToSource`

**La idea.** En Model/View, los datos y lo que se ve están separados en piezas:

```
modelo  ──►  proxy  ──►  vista (la tabla)
(datos)     (filtra y    (dibuja lo que
             ordena)      le da el proxy)
```

- El **modelo** guarda **todos** los datos.
- La **vista** solo **dibuja** filas y gestiona la selección. No guarda datos.
- El **proxy** se pone en medio. La vista no mira el modelo, sino el proxy, y el proxy le enseña una versión **filtrada u ordenada** del modelo, **sin cambiarlo**. Es como unas gafas: los datos son los mismos y lo que cambia es cómo se ven.

```python
proxy = QSortFilterProxyModel()
proxy.setSourceModel(modelo)
tabla.setModel(proxy)
```

**Filtrar.** Cada vez que cambia el texto del filtro, el proxy recorre las filas **del modelo** y deja pasar solo las que lo contienen. Las demás no se borran: siguen en el modelo, pero la vista no las recibe. De ahí salen dos consecuencias:

- Si la vista **oculta** una columna, por ejemplo el ID, la columna sigue en el modelo y el proxy **sigue buscando en ella**. Al buscar «4», aparece la fila con ID 4, aunque no se vea ningún 4.
- Si un dato no está en el modelo, sino solo en la base de datos, como una descripción larga, el proxy **no puede encontrarlo**.
- `setFilterKeyColumn` dice en qué columna **del modelo** se busca: `-1`, en todas; `1`, solo en la columna 1. Lo que oculte la vista no cambia nada.

**Ordenar.** Al pulsar la cabecera de una columna, el proxy reordena lo que enseña. El modelo sigue en el orden en que se cargó.

**Dos numeraciones de filas.** Como el proxy filtra y reordena, la vista y el modelo **numeran sus filas por separado**. Con cinco registros cargados por orden de `id`, filtrados por «Pendiente» y ordenados por título:

| Fila del modelo | `id` | Título | Estado |
|---|---|---|---|
| 0 | 1 | Botón no responde | Pendiente |
| 1 | 2 | Exportar a CSV | Pendiente |
| 2 | 3 | Mejorar contraste | En proceso |
| 3 | 4 | Fallo al abrir | Resuelta |
| 4 | 5 | Ordenar por fecha | Pendiente |

| Fila de la vista | `id` | Título | Fila del modelo |
|---|---|---|---|
| 0 | 1 | Botón no responde | 0 |
| 1 | 2 | Exportar a CSV | 1 |
| 2 | 5 | Ordenar por fecha | **4** |

Se elige «Ordenar por fecha» y se pulsa «Eliminar». La selección dice «fila 2», pero es la fila 2 **de la vista**. Si se lee la fila 2 del modelo, se obtiene el `id` 3, y se borra «Mejorar contraste», que ni siquiera se ve, **sin ningún error**. Hay que traducir la fila con **`mapToSource`**:

```python
indice_vista = tabla.selectionModel().selectedRows()[0]
fila = proxy.mapToSource(indice_vista).row()
```

El proxy sabe qué fila del modelo hay detrás de cada fila que enseña, y `mapToSource` se lo pregunta: aquí devuelve la 4, el `id` 5.

**Por qué el fallo no se ve al probar.** Sin filtro y sin ordenar, las dos numeraciones coinciden (0 con 0, 1 con 1…), y el código sin `mapToSource` funciona por casualidad. El fallo solo aparece al filtrar u ordenar. Por eso conviene probar así: buscar algo, ordenar por una columna y entonces eliminar.

### 14. Restaurar el estado al final

**La situación.** Una ventana guarda con `QSettings`, al cerrarse, la última búsqueda: «Error», que coincide con 2 de sus 5 registros. Al abrirse, `restaurar_estado()` vuelve a escribir «Error» en el buscador, que emite `busquedaCambiada`. Esa señal está conectada, por este orden, con el filtro del proxy y con `mostrar_resultados`, que escribe en la barra de estado cuántas filas hay (apunte 6).

**Si se restaura antes de cargar los datos:**

```python
self.restaurar_estado()
self.cargar_registros()
```

1. `restaurar_estado()` escribe «Error» y se emite `busquedaCambiada`.
2. El proxy **guarda el filtro** «Error». El modelo todavía está vacío, así que no hay nada que filtrar.
3. `mostrar_resultados` pregunta al proxy cuántas filas hay: **0**. La barra dice «0 registros con «Error»».
4. `cargar_registros()` mete los 5 registros en el modelo.
5. El proxy **sigue teniendo el filtro** y lo aplica a las filas que llegan: deja pasar 2. La tabla muestra 2.
6. Nadie vuelve a contar: la señal del buscador ya se emitió en el paso 1, y cargar datos no la emite.

El resultado es contradictorio: la tabla muestra 2 filas y la barra dice 0. La diferencia está en que el **filtro** es un **estado** que el proxy conserva y aplica siempre, también a lo que llega después, mientras que el **recuento** es una foto tomada en un momento, el paso 3, cuando aún no había nada.

**Si se restaura al final:**

```python
self.cargar_registros()
self.restaurar_estado()
```

Primero se cargan los 5 registros; después se escribe «Error», el proxy filtra y quedan 2, y `mostrar_resultados` cuenta 2. La tabla y la barra coinciden. Por eso el estado guardado se restaura **al final de `__init__`**: con la ventana montada y los datos cargados, todo lo que reacciona a la restauración ve la aplicación completa.

### 15. Componentes: API pública, propiedades y señales propias

**La idea.** Un componente reutilizable, como un selector de estrellas o un buscador, se usa como una caja con mandos, sin mirar dentro. Esos mandos son su **API pública**:

- **propiedades**: valores que se leen y se cambian, como la nota (`selector.nota`);
- **señales**: avisos de que algo ha cambiado, como `notaCambiada`;
- **métodos**: acciones, como `limpiar()`.

Lo de dentro, con nombres que empiezan por `_`, es **interno**: quien usa el componente no debe tocarlo, porque puede cambiar en otra versión.

**Herencia o composición.** Un componente se crea de dos formas, que a menudo se combinan:

- por **herencia**, cuando un widget de Qt ya hace casi lo que hace falta y se le añaden cosas: el selector **es un** `QFrame`, y aprovecha su marco;
- por **composición**, cuando se **juntan varios widgets** en uno: el buscador junta una etiqueta, una caja de texto y un botón; el selector, cinco botones de estrella y una etiqueta.

Los widgets internos se guardan con `_` delante, porque no forman parte de la API.

```python
class Selector(QFrame):
    notaCambiada = Signal(int)

    def _get_nota(self):
        return self._nota

    def _set_nota(self, valor):
        valor = max(0, min(5, valor))
        if valor == self._nota:
            return
        self._nota = valor
        self._dibujar()
        self.notaCambiada.emit(valor)

    nota = Property(int, _get_nota, _set_nota, notify=notaCambiada)
```

**La señal se declara en el cuerpo de la clase.** `notaCambiada = Signal(int)` va fuera de los métodos. Al crear la clase, Qt la convierte en una señal de verdad de cada objeto, con `connect` y `emit`. Si se escribiera dentro de `__init__` (`self.notaCambiada = Signal(int)`), sería un atributo normal, sin `connect`, y conectarla daría un `AttributeError`.

**Una propiedad parece un atributo, pero ejecuta código.** `selector.nota = 9` no guarda el 9 directamente: ejecuta el **setter**, `_set_nota(9)`, y leer `selector.nota` ejecuta el getter. Así el componente controla cada cambio. Paso a paso, empezando con la nota a 0:

| Se escribe | Qué hace el setter | Se emite |
|---|---|---|
| `selector.nota = 9` | Recorta: `min(5, 9)` da 5. Cambia, redibuja y avisa | 5 |
| `selector.nota = 3` | Está entre 0 y 5. Cambia, redibuja y avisa | 3 |
| `selector.nota = 3` | Ya valía 3: termina con `return` antes de avisar | nada |

Solo se avisa **cuando cambia**, para no disparar trabajo inútil en quien escucha.

**Usar la API, no lo interno.** `selector._nota = 0` cambia el dato interno sin pasar por el setter: no se redibujan las estrellas ni se emite la señal, y la ventana no se entera. `selector.limpiar()`, que hace `self.nota = 0`, sí pasa por el setter, y todo queda coherente.

**Una cadena de señales.** Un buscador tiene dentro una caja de texto, `_caja`, y reenvía sus cambios con su propia señal:

```python
self._caja.textChanged.connect(self._al_cambiar_texto)

def _al_cambiar_texto(self, texto):
    self.busquedaCambiada.emit(texto)

def _set_texto(self, valor):
    self._caja.setText(valor)
```

`buscador.texto = "Error"` no llama a `emit`, pero la señal llega igual, en cadena: el setter hace `setText` en la caja, la caja emite `textChanged` porque su texto ha cambiado, y `_al_cambiar_texto` emite `busquedaCambiada`. De ahí salen dos consecuencias:

- Si el texto **no cambia** (la caja ya estaba vacía y se escribe `""`), la caja no emite nada y no llega ninguna señal.
- Teclear «Error» tecla a tecla, como hace una persona o `qtbot.keyClicks`, cambia el texto cinco veces: «E», «Er», «Err», «Erro» y «Error». Son cinco señales.

**El orden de los parámetros.** Qt Designer crea los componentes colocados con *Promote to* pasándoles **el padre como primer argumento**: `Buscador(self.centralwidget)`. Por eso `parent` tiene que ser el primer parámetro del constructor. Si fuera otro, el padre llegaría donde no toca, sin ningún error, y el componente se vería mal.

### 16. Documentar y empaquetar un componente

**Documentar.** El **docstring**, el texto entre `"""` justo debajo de `class`, explica qué hace el componente, su API y un ejemplo de uso. Es lo que muestra `help(Buscador)`. Va dirigido a quien programa; el **manual de usuario**, en cambio, es para quien usa la aplicación, sin código.

**Empaquetar.** Para usar un componente en otros proyectos sin copiar el archivo a mano, se convierte en un **paquete**:

```toml
[project]
name = "buscador-dam"
version = "0.1.0"
dependencies = ["PySide6-Essentials"]

[tool.setuptools]
py-modules = ["buscador"]
```

1. **`pyproject.toml`** describe el paquete: el nombre, la versión, las **dependencias** y qué módulos lleva.
2. **`python -m build`** crea el paquete, un archivo **`.whl`**, en la carpeta `dist/`.
3. En otro proyecto, **`pip install`** con la ruta del `.whl` lo instala, y además instala sus dependencias.

No hay que confundirlo con `requirements.txt`, que lista las librerías de una **aplicación** para reproducir su entorno.

**Solo entra lo que se dice.** En el paquete va únicamente lo que indica `py-modules`, aquí `buscador`. Si `buscador.py` hiciera `import bd` para usar el `bd.py` de la aplicación, en otro proyecto daría un error: ese módulo no va en el paquete. Un componente reutilizable **no depende de la aplicación**. Si la aplicación quiere guardar algo del componente, conecta su señal o lee su propiedad.

### 17. Pruebas que no engañan

**La idea.** Una prueba es un ejemplo de uso con su resultado esperado: «con estos datos, la media tiene que dar 3». El `assert` lo comprueba, y si no se cumple, la prueba falla. Pero que una prueba **pase no demuestra** que el código esté bien: solo que funciona **con esos datos**.

**Variar los datos.** Una función `media` divide por error entre 3, en lugar de entre el número de datos:

```python
def media(notas):
    return sum(notas) / 3
```

Si todas las pruebas usan tres notas, dividir entre 3 o entre `len(notas)` da lo mismo, y todas pasan. Con dos notas, 4 y 2, la media es 3,0, pero la función da 2,0. Hay que probar con datos distintos: uno, dos, ninguno, los valores límite.

**Cada prueba, aislada.** Una prueba tiene que dar lo mismo cada vez que se repite, sin depender de lo que dejaron otras. Si las pruebas usan la base de datos real, una prueba que guarda dos registros y comprueba que hay dos pasa la primera vez y falla la segunda, porque ya están los de la vez anterior y hay cuatro. Además, mezcla datos de prueba con los de verdad. Una *fixture* con `tmp_path` da a cada prueba una base de datos nueva, en una carpeta temporal que se borra al terminar.

**Comparar decimales.** El ordenador guarda los decimales en binario, y muchos no se pueden guardar exactos: `0.1 + 0.2` da `0.30000000000000004`. Por eso `== 0.3` fallaría aunque la cuenta esté bien. `pytest.approx(0.3)` compara admitiendo un margen muy pequeño.

**Comprobar que algo se rechaza.** A veces lo correcto es que el código **dé un error**, como al guardar una nota de 6 en una columna con `CHECK (nota BETWEEN 1 AND 5)`. `with pytest.raises(sqlite3.IntegrityError):` da la prueba por buena solo si el código de dentro lanza ese error; si no lo lanza, la prueba falla.

**Cómo encuentra pytest las pruebas.** Ejecuta las funciones cuyo nombre empieza por `test_`, en los archivos que se llaman `test_*.py`.

**Probar widgets con `qtbot`.** pytest-qt añade `qtbot`, que maneja los widgets como una persona: `qtbot.keyClicks` escribe tecla a tecla, `qtbot.keyClick` pulsa una tecla y `qtbot.waitSignal` espera a que llegue una señal; si no llega a tiempo, la prueba falla.

**Sacar las reglas de la interfaz.** Una validación dentro de un diálogo es difícil de probar: si falla, abre un `QMessageBox` que espera un clic. Si la regla se saca a una función sin widgets, como `error_titulo(titulo)`, que devuelve el mensaje de error o un texto vacío, se prueba en un instante y el diálogo solo la usa. Es la separación de responsabilidades.

**Tipos de prueba.**

| Prueba | Qué comprueba | Ejemplo |
|---|---|---|
| Unitaria | Una pieza sola | La función de la media, sin ventana ni base de datos |
| De integración | Varias piezas juntas | Pulsar teclas en la ventana y comprobar que el dato llega a la base de datos |
| De regresión | Que lo que funcionaba sigue funcionando tras un cambio | Volver a pasar todas las pruebas tras cambiar un componente |
| De humo | Lo mínimo, rápido: ¿arranca y abre la ventana? | Abrir la aplicación y ver la tabla |
| De aceptación | Que hace lo que pidió quien la encargó | Recorrer con esa persona sus tareas reales |
| De usabilidad | Que las personas consiguen usarla | Personas que no la conocen hacen tareas (apunte 2) |

### 18. Interfaces naturales: reconocer, decidir dónde y diseñar bien

**Qué son.** Una **interfaz natural** usa formas de comunicarse propias de las personas, en lugar del teclado y el ratón: la voz, los gestos, el tacto, la mirada, el cuerpo. Ventajas: manos libres, accesibilidad para quien no puede usar teclado o ratón, rapidez en algunas tareas. Límites: el reconocimiento se equivoca, depende del ruido o de la luz, cansa y plantea problemas de **privacidad**, porque usa la cámara o el micrófono.

**Cada tecnología, lo suyo.**

| Tecnología | Qué hace |
|---|---|
| Reconocimiento de voz | Convierte lo que se dice en texto: para **dictar** o para dar **órdenes** (unas pocas frases fijas) |
| Síntesis de voz | Convierte un texto en voz; es la base de los lectores de pantalla |
| Reconocimiento de gestos | Identifica la forma de la mano en la imagen de la cámara |
| Modelo de postura | Localiza puntos del cuerpo, como la cadera, la rodilla y el tobillo |
| Realidad aumentada | Superpone información sobre la imagen real, en el sitio correcto |

Con los puntos del cuerpo se pueden calcular ángulos: el de la rodilla dice si alguien está de pie o agachado, y contar «bajar y volver a subir» cuenta sentadillas. En realidad aumentada, los **marcadores** (códigos impresos que la cámara reconoce) indican dónde dibujar y hacen el resultado más fiable.

**Un modelo ya entrenado o uno propio.** Un **modelo ya entrenado** solo reconoce lo que decidió quien lo entrenó: un modelo de gestos generales no conoce los signos de una lengua de signos. Para eso hay que entrenar uno **propio**, por ejemplo con **Teachable Machine**: se graban ejemplos de cada clase con la cámara o el micrófono, y la web entrena el modelo, que después se exporta para usarlo en una aplicación.

**En el equipo o en la nube.** El reconocimiento puede hacerse en el propio ordenador o en un servidor de Internet. En la nube suele acertar más, pero **envía los datos fuera**. En el equipo, la voz o la imagen **no salen del ordenador** y funciona sin conexión. Con datos sensibles, como los de salud, pesa más la privacidad.

**Criterios de diseño.**

- **Para quién y para qué**: un gesto o una orden de voz se añade cuando ayuda a alguien en una situación concreta (manos ocupadas, manos sucias), no por ser moderno.
- **Alternativa**: nunca es la única forma de usar la aplicación. Todo tiene que poder hacerse también con el teclado, porque el reconocimiento falla y no todo el mundo puede hacer gestos o hablar.
- **Pocas órdenes, distintas y cómodas**: con ruido, órdenes de voz cortas y que no se parezcan; gestos que no cansen (horas con el brazo levantado agotan).
- **Retroalimentación**: decir qué se ha entendido (en la barra de estado o en voz alta), para que la persona sepa si ha llegado bien.
- **Confirmación** antes de algo irreversible: «¿Eliminar el registro "Exportar a CSV"? Di sí o no». Si no se entiende la respuesta, no se hace nada.
- **Privacidad**: la cámara o el micrófono se encienden solo cuando se pide, y con aviso de que están activos.

### 19. Reconocer gestos: confianza, umbral y confirmación

**La idea.** El modelo que reconoce gestos no está seguro de nada: para cada imagen **estima** cuál es el gesto más probable y da una **confianza**, un número de 0 a 1 que dice lo seguro que está. La aplicación decide qué hacer con esa estimación.

**El umbral.** La aplicación solo acepta el gesto si la confianza supera un **umbral**, por ejemplo 0,6:

```python
gesto = None
if mejor.category_name != "None" and mejor.score > 0.6:
    gesto = mejor.category_name
```

- `Thumb_Up` con 0,55 no supera 0,6: no cuenta.
- `"None"` es la clase del modelo para una mano sin ningún gesto conocido. Se descarta siempre, aunque venga con 0,9: el modelo está muy seguro de que **no** hay gesto.

Elegir el umbral es un **equilibrio**. Un umbral alto acepta solo lo muy seguro: hay menos **falsos positivos** (gestos que nadie ha hecho), pero más gestos reales sin reconocer, sobre todo con poca luz. Un umbral bajo hace lo contrario.

**La confirmación.** Al pasar de un gesto a otro, la mano pasa por posiciones intermedias, y el modelo puede ver un instante un gesto que nadie ha hecho. Por eso un gesto solo cuenta si se repite `CONFIRMAR` imágenes **seguidas**:

```python
def _procesar(self, gesto):
    if gesto == self._candidato:
        self._repeticiones += 1
    else:
        self._candidato, self._repeticiones = gesto, 1
    if self._repeticiones == self.CONFIRMAR:
        if gesto is not None and gesto != self._ultimo:
            self.gestoDetectado.emit(gesto)
        self._ultimo = gesto
```

- `_candidato` es el gesto que se está contando, y `_repeticiones`, cuántas imágenes seguidas lleva. Si llega uno distinto, la cuenta **vuelve a empezar** desde 1.
- Al llegar a `CONFIRMAR`, el gesto queda confirmado. Se emite solo si es un gesto (no `None`) y **distinto del último confirmado**, `_ultimo`. Así, mantener el pulgar arriba no dispara la acción una y otra vez.
- «Sin gesto» (`None`) también se confirma: cambia `_ultimo` a `None`, aunque no se emite nada. Así, bajar la mano un rato permite repetir el mismo gesto.

Con `CONFIRMAR = 5` (U es pulgar arriba; V, victoria; «–», sin gesto):

| Secuencia | Qué pasa | Emisiones |
|---|---|---|
| 5 U, 2 «–», 5 U | Los 5 U se confirman y se emiten. Las 2 «–» no llegan a 5, así que `_ultimo` sigue siendo U, y el segundo pulgar, igual que el último, no se emite | 1 |
| 5 U, 5 «–», 5 U | Las 5 «–» confirman «sin gesto» y `_ultimo` pasa a `None`: el segundo pulgar es distinto del último y se emite | 2 |
| 4 U, 1 V, 4 U | La V corta la cuenta del pulgar y los 4 U siguientes empiezan desde 1: ningún gesto llega a 5 | 0 |

El tiempo mínimo que hay que mantener un gesto depende de `CONFIRMAR` y del intervalo del temporizador que lee la cámara: con 5 imágenes, una cada 66 ms, entre la primera y la quinta hay 4 intervalos, unos 0,26 s. Un `CONFIRMAR` mayor da menos falsos positivos, pero la aplicación responde más lenta.

### 20. La ventana con gestos: detector, herencia, acción marcable y tabla

**Un detector que no se ve.** El detector de gestos lee la cámara con un `QTimer` (apunte 5) y avisa con señales: `gestoDetectado(str)` y `error(str)`. No es un widget, porque no se ve: hereda de **`QObject`**, que basta para tener señales propias y un temporizador. Se crea con la ventana como **padre**, `DetectorGestos(self)`, así que se destruye con ella. La cámara no es de Qt, y hay que soltarla a mano al cerrar la ventana, en `closeEvent`.

**Reutilizable porque solo avisa.** El detector no sabe nada de la ventana: detecta el gesto y emite la señal. El significado lo pone cada aplicación en el slot que conecta: en una, el pulgar arriba pasa a la fila siguiente de una tabla; en otra, suma una estrella. Es **desacoplamiento** (apunte 6). Y conviene que cada gesto haga lo mismo que una tecla que ya existía, como una flecha: es coherencia.

**La ventana con gestos hereda de la ventana normal.**

```python
class VentanaConGestos(VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.detector = gestos.DetectorGestos(self)
```

Se **reutiliza** la ventana entera por herencia y se le añaden los gestos **sin tocar** la original. `super().__init__()` va lo primero (apunte 5): crea la ventana, su diseño y sus conexiones. Si fuera al final, el detector usaría como padre una ventana aún no creada y daría un `RuntimeError`.

**Una opción marcable para encender la cámara.** Los gestos se activan con una opción marcable del menú, no están siempre encendidos: por **privacidad**, la cámara solo se enciende cuando se pide, y los gestos son un atajo opcional.

**Cuando la cámara no se abre: una señal que se vuelve a emitir desde su propio slot.** Cuando el código cambia el estado de un control, el control emite **la misma señal** que si lo hubiera cambiado una persona. Si eso pasa dentro del slot de esa señal, el slot se vuelve a ejecutar.

Una opción marcable del menú, «Gestos de la mano», tiene su señal `toggled` conectada con este método, que recibe `True` al marcarla y `False` al desmarcarla:

```python
def activar_gestos(self, activar):
    if not activar:
        self.detector.detener()
        self.ui.statusbar.showMessage("Gestos desactivados", 3000)
    elif self.detector.iniciar():
        self.ui.statusbar.showMessage("Gestos activados", 3000)
    else:
        self.accion_gestos.setChecked(False)
```

Se marca la opción, pero la cámara no se puede abrir:

1. Al marcarla, `toggled` se emite con `True` y empieza la **primera** ejecución de `activar_gestos`.
2. `iniciar()` intenta abrir la cámara, no puede y devuelve `False`. Se entra en el `else`.
3. `setChecked(False)` desmarca la opción. Para Qt, la opción ha cambiado, así que emite otra vez `toggled`, ahora con `False`.
4. Empieza la **segunda** ejecución: `activar` es `False`, se entra en el primer `if`, se apaga el detector y la barra dice «Gestos desactivados».

Al final, la opción queda sin marcar, de acuerdo con la cámara apagada: el menú no engaña sobre lo que pasa (**visibilidad del estado del sistema**). Funciona bien, pero hay que tenerlo en cuenta al escribir el slot: tiene que hacer lo correcto en las dos llamadas.

**Moverse por la tabla sin salirse.**

```python
def mover_seleccion(self, paso):
    filas = self.proxy.rowCount()
    if filas == 0:
        return
    actuales = self.ui.tabla.selectionModel().selectedRows()
    fila = actuales[0].row() + paso if actuales else 0
    self.ui.tabla.selectRow(max(0, min(fila, filas - 1)))
```

- `self.proxy.rowCount()` cuenta las filas **visibles**, las que deja pasar el filtro (apunte 13). Si no hay ninguna, no hace nada.
- Sin selección, empieza por la fila 0, sea cual sea el paso.
- `max(0, min(fila, filas - 1))` **recorta** la fila entre la primera y la última. Con 5 filas (0 a 4) y la 4 seleccionada, un paso de +1 da 5, y `min(5, 4)` la deja en 4: la selección no se sale de la tabla.

**Recorrer una lista en círculo.** Para pasar a la siguiente categoría y, tras la última, volver a la primera, se usa el **resto** de la división:

```python
CATEGORIAS = ("docente", "materiales", "clases")
siguiente = CATEGORIAS[(CATEGORIAS.index(actual) + 1) % len(CATEGORIAS)]
```

Desde «clases», la posición 2: (2 + 1) % 3 da 0, y vuelve a «docente». Tres pasos seguidos desde «docente» vuelven a «docente».

### 21. El cuerpo, la realidad aumentada y el manual de usuario

**El modelo de postura.** Localiza 33 puntos del cuerpo: hombros, codos, muñecas, caderas, rodillas, tobillos… Con ellos se **comparan posiciones** (si la muñeca está por encima del hombro, el brazo está levantado) o se **calculan ángulos** (el de la rodilla, entre la cadera, la rodilla y el tobillo, dice si alguien está de pie o agachado). El reconocedor de gestos, en cambio, solo mira la mano: sabe qué forma tiene, pero no dónde está respecto al cuerpo.

**Contar repeticiones es contar cambios.** Una sentadilla dura muchas imágenes con la rodilla doblada. Si se sumara una por imagen, una sola sentadilla contaría decenas de veces. Se cuenta el **cambio de estado**: de pie, agachado y otra vez de pie es una repetición. Es la misma idea que `_ultimo` en el detector de gestos (apunte 19): se actúa cuando cambia el estado confirmado, no mientras dura.

**La realidad aumentada.** Dibuja sobre la imagen real, en el sitio correcto. Para saber dónde, necesita una **referencia** en la imagen: un **marcador** impreso, o una superficie, una cara o una mano que reconoce. Si la cámara deja de verla, porque la tapa una mano o sale de la imagen, no sabe dónde dibujar. Tiene dos criterios propios:

- lo que se dibuja **no debe tapar** la información real importante;
- tiene que ser **legible sobre cualquier fondo**. El fondo es la imagen real y cambia: un texto blanco sin fondo se pierde delante de una pared blanca. Se le pone un fondo o un borde, que es el contraste del apunte 1.

**El manual de usuario y la documentación técnica.** Están escritos para personas distintas:

| | Manual de usuario | Documentación técnica (docstring, README) |
|---|---|---|
| Para quién | Quien usa la aplicación | Quien la programa o la mantiene |
| Qué cuenta | Qué hace la aplicación, cómo se instala y se abre, cómo se hace cada tarea, paso a paso y con capturas; los atajos; qué hacer ante los problemas frecuentes | La API de los componentes, la estructura de los datos y cómo está organizado el código |
| Ejemplo | «Para buscar un registro, escribe en Buscar (Alt+B)» | «`busquedaCambiada(str)` se emite cada vez que cambia el texto» |

La **información persistente**, como la base de datos y los ajustes de `QSettings`, se documenta con su estructura: qué tablas y campos hay, de qué tipo son y qué valores admiten.
