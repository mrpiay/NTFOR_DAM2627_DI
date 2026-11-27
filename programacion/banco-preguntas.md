# DI · Preguntas de práctica de la 1ª evaluación

Cien preguntas para practicar, sin las respuestas.

- **Verdadero o falso** (1 punto): se marca V o F. Cada acierto suma 1 punto, cada error resta 0,5 y una pregunta en blanco vale 0. Los errores solo restan dentro de esta parte, que nunca baja de 0: no quitan puntos de unir pares ni del resto del examen. Conviene contestar aunque haya dudas: compensa en cuanto se acierta más de una de cada tres veces.
- **Unir pares** (1 punto): cada elemento de la izquierda va con uno de la derecha. La derecha tiene una opción de más, que no va con ninguno. Cada pareja bien unida vale 0,25, y las mal unidas no restan.

Algunas preguntas usan el código de otra y lo dicen con su número.

---

**1.** Cinco personas hacen una prueba de usabilidad con el ratón, y todas terminan sus tareas rápido y sin dudar. Eso demuestra que la aplicación también es accesible.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**2.** Un formulario de alta guarda siempre bien los datos, pero cada alta exige seis clics y escribir la fecha a mano. Según la ISO 9241, lo que falla es la eficacia.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**3.** Une cada situación con el estándar o el nivel que corresponde.

| | Situación | | Estándar o nivel |
|---|---|---|---|
| 1 | La web de un ayuntamiento español tiene que ser accesible por ley | a | Nivel AAA de las WCAG |
| 2 | Se mide si la gente consigue dar de alta un registro, cuánto le cuesta y si se frustra | b | WCAG |
| 3 | El texto normal de los botones tiene que llegar al menos a un contraste de 4,5:1 | c | ISO 9241 |
| 4 | Se revisa la interfaz con cuatro principios: perceptible, operable, comprensible y robusto | d | EN 301 549 |
| | | e | Nivel AA de las WCAG |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**4.** Un comprobador da 4,3:1 para el texto blanco de un botón verde. Como está muy cerca de 4,5:1, el botón cumple el nivel AA de las WCAG para el texto normal.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**5.** Un texto con poco contraste solo es un problema para las personas con baja visión.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**6.** Un botón «Eliminar» se ve rojo cuando está activado y rojo claro cuando está desactivado, y nada más cambia. Quien no distingue bien los colores puede no saber si se puede pulsar.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**7.** Este código está bien: cada etiqueta tiene su propio atajo de teclado.

```python
formulario.addRow("&Título:", self.txtTitulo)
formulario.addRow("&Prioridad:", self.cmbPrioridad)
formulario.addRow("&Estado:", self.cmbEstado)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**8.** Une cada mejora con a quién ayuda.

| | Mejora | | A quién ayuda |
|---|---|---|---|
| 1 | Nombre accesible (`setAccessibleName`) | a | A quien quiere llegar a un campo con Alt y una letra |
| 2 | Un marco en el control que tiene el foco | b | A quien usa el teclado, que así sabe dónde está |
| 3 | *Tooltip* con el nombre y el atajo | c | A quien no distingue bien los colores, que así puede leer el texto sobre el fondo |
| 4 | `&` en la etiqueta, con el campo como *buddy* | d | A quien usa un lector de pantalla, que así puede decir qué hace el control |
| | | e | A quien usa el ratón y no reconoce un botón que solo tiene un icono |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**9.** Si se quitara la segunda línea, Tab en la descripción pasaría el foco al control siguiente.

```python
self.txtDescripcion = QTextEdit()
self.txtDescripcion.setTabChangesFocus(True)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**10.** En un menú, asignar Ctrl+N a la orden que elimina el registro seleccionado respeta la heurística de coherencia y estándares.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**11.** Desactivar «Guardar» hasta que estén rellenos todos los campos obligatorios es un ejemplo de la heurística de prevención de errores.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**12.** Une cada heurística de Nielsen con un ejemplo.

| | Heurística | | Ejemplo |
|---|---|---|---|
| 1 | Visibilidad del estado del sistema | a | Al añadir un registro, la barra de estado lo confirma |
| 2 | Control y libertad | b | Todos los diálogos tienen un botón «Cancelar» |
| 3 | Prevención de errores | c | «Eliminar» está desactivado si no hay ninguna fila seleccionada |
| 4 | Flexibilidad y eficiencia de uso | d | Los mensajes de error usan las palabras de quien usa la aplicación, no las del programa |
| | | e | Intro en el campo de texto hace lo mismo que el botón «Añadir», sin ir a él |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**13.** Si falla al guardar, una aplicación muestra «No se ha podido guardar: CHECK constraint failed: nota BETWEEN 1 AND 5». Es un buen mensaje, porque dice exactamente qué ha fallado.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**14.** Una evaluación heurística se hace con personas que no conocen la aplicación, que hacen tareas y piensan en voz alta.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**15.** Ctrl+S añade un registro si no hay ninguno seleccionado y modifica el seleccionado si lo hay, y nada indica qué va a hacer. Esto incumple la visibilidad del estado del sistema.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**16.** Una aplicación de rehabilitación tiene que contar cuántas veces una persona levanta el brazo por encima del hombro. Basta con el reconocedor de gestos de la mano, porque la mano sube con el brazo.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**17.** Ayer la aplicación funcionaba. Hoy, en una terminal nueva, `python main.py` dice que no encuentra el módulo `PySide6`. Lo más probable es que el entorno virtual no esté activado.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**18.** Une cada línea con lo que hace.

| | Línea | | Qué hace |
|---|---|---|---|
| 1 | `app = QApplication()` | a | Ejecuta el constructor de la clase madre, que crea la parte de Qt del objeto |
| 2 | `ventana.show()` | b | Crea el objeto único que gestiona la pantalla y los eventos; va antes que cualquier ventana |
| 3 | `app.exec()` | c | Arranca el bucle de eventos, que reparte clics y teclas hasta que se cierra la última ventana |
| 4 | `super().__init__()` | d | Hace visible una ventana que ya existe |
| | | e | Crea la ventana, pero todavía no la muestra |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**19.** Si se quita `app.exec()`, la ventana se muestra y se queda abierta hasta que alguien la cierra.

```python
app = QApplication()
ventana = Ventana()
ventana.show()
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**20.** Para contar sentadillas con el modelo de postura, se suma una sentadilla cada vez que una imagen de la cámara muestra la rodilla doblada.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

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

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**22.** Une cada cosa que se quiere conseguir con cómo se hace en Qt.

| | Qué se quiere | | Cómo se hace |
|---|---|---|---|
| 1 | Hacer algo cuando se pulsa un botón | a | Sobrescribir `keyPressEvent` en la clase del componente |
| 2 | Preguntar «¿Salir sin guardar?» al cerrar la ventana | b | Declarar una `Signal` en el cuerpo de la clase y emitirla |
| 3 | Que un componente propio avise a la ventana de que ha cambiado | c | Conectar la señal `clicked` con un método |
| 4 | Que las flechas suban y bajen la nota de un selector | d | Conectar `closeEvent` con un método usando `connect` |
| | | e | Sobrescribir `closeEvent` en la clase de la ventana |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**23.** Esta línea está en el `__init__` de la ventana, y `anadir_fila` no devuelve nada. Con ella, `anadir_fila` se ejecuta cada vez que se pulsa el botón.

```python
self.boton.clicked.connect(self.anadir_fila())
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**24.** Si por error se conecta dos veces el mismo slot con `clicked`, cada pulsación del botón lo ejecuta dos veces.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**25.** Se intenta arreglar el problema de las lambdas en un bucle con un valor por defecto. Al pulsar «Baja», la etiqueta muestra «Baja».

```python
for nombre in ["Baja", "Media", "Alta"]:
    boton = QPushButton(nombre)
    capa.addWidget(boton)
    boton.clicked.connect(lambda texto=nombre: self.etiqueta.setText(texto))
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**26.** `keyPressEvent` y `closeEvent` se conectan con `connect`, igual que las señales.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**27.** Si no hay ninguna fila seleccionada en la lista, `self.lista.selectedItems()[0]` devuelve `None`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**28.** Une cada dato de un formulario de reserva de aula con el control más adecuado.

| | Dato | | Control |
|---|---|---|---|
| 1 | El aula, una de seis | a | `QDateEdit` |
| 2 | La fecha | b | `QCheckBox` |
| 3 | El número de asistentes, de 1 a 30 | c | `QSpinBox` con `setRange(1, 30)` |
| 4 | Si hace falta proyector | d | `QComboBox` |
| | | e | `QLineEdit` |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**29.** Una aplicación de realidad aumentada usa un marcador impreso para saber dónde dibujar las instrucciones de montaje sobre una pieza. Si una mano tapa el marcador, la aplicación puede perder el sitio donde dibujarlas.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**30.** Un botón que se añade a mano en el archivo generado por `pyside6-uic` se conserva al regenerarlo tras cambiar el diseño en Qt Designer.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**31.** Con esta validación, un título de 101 letras con dos espacios detrás (103 caracteres) se rechaza por largo.

```python
titulo = self.txtTitulo.text().strip()
if not titulo:
    ...   # avisa y return
if len(titulo) > 100:
    ...   # avisa y return
self.accept()
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**32.** Si «Aceptar» se conectara directamente con `self.accept`, sin validar, y el título fuera `"   "`, el `NOT NULL` de la columna `titulo` impediría guardarlo. `datos()` devuelve el título con `strip()`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**33.** Después de cerrar un diálogo con «Aceptar», `dialogo.datos()` sigue devolviendo lo que se escribió.

```python
dialogo = Dialogo(self)
if not dialogo.exec():
    return
bd.insertar(*dialogo.datos())
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

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

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**35.** Una aplicación de realidad aumentada pone etiquetas de texto blanco, sin fondo, sobre la imagen de la cámara. Si en una prueba el texto contrasta bien con lo que se ve detrás, se leerá bien siempre.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**36.** En la función de la pregunta 34, si `filas = cursor.fetchall()` se mueve a después de `conexion.close()`, `ejecutar_sql` sigue funcionando sin errores con los `INSERT`, porque no devuelven filas.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**37.** `(id_registro,)`, con la coma, es una tupla de un elemento; `(texto)`, sin coma, no lo es.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**38.** La tabla tiene los registros 1, 2, 3, 4 y 5, y se eliminan el 2 y el 5. Sin `AUTOINCREMENT`, el siguiente registro recibe el `id` 2, el primer hueco libre.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

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

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**40.** Si en este `UPDATE` el `id` se pusiera el primero en la tupla, se produciría un error.

```python
conexion.execute(
    """UPDATE registros
       SET titulo = ?, tipo = ?, prioridad = ?, estado = ?, descripcion = ?
       WHERE id = ?""",
    (titulo, tipo, prioridad, estado, descripcion, id_registro)
)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**41.** Una aplicación guarda lo que se escribe con `conexion.execute("INSERT INTO registros (texto) VALUES (?)", (texto,))`. Alguien escribe `x'); DELETE FROM registros; --`. Ese texto se guarda tal cual, como un registro más, y no se borra nada.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**42.** Con esta consulta, escribir `admin' --` como nombre, y cualquier contraseña, permite entrar como `admin`.

```python
sql = "SELECT * FROM usuarios WHERE nombre = '" + nombre + "' AND clave = '" + clave + "'"
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**43.** Con `RUTA = "datos.db"`, si se lanza `main.py` desde otra carpeta, la aplicación abre una base de datos distinta de la de siempre.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**44.** Añadir una columna nueva en `CREATE TABLE IF NOT EXISTS registros (…)` la añade también a una base de datos que ya existía.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**45.** Si se quitara `self.lista.clear()`, al añadir un registro se verían filas repetidas en la lista, pero en la base de datos no habría ningún registro repetido.

```python
def cargar_filas(self):
    self.lista.clear()
    for id_registro, texto in bd.obtener_registros():
        elemento = QListWidgetItem(texto)
        elemento.setData(Qt.ItemDataRole.UserRole, id_registro)
        self.lista.addItem(elemento)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**46.** Une cada cosa que hay que conseguir con lo que se hace en Model/View.

| | Qué hay que conseguir | | Qué se hace |
|---|---|---|---|
| 1 | Que un registro nuevo aparezca en la tabla | a | Pedir al proxy `mapToSource` con la fila seleccionada |
| 2 | Que la columna ID no se vea, sin quitarla de los datos | b | Borrar del modelo las filas que no coinciden con la búsqueda |
| 3 | Que solo se vean los registros que contienen el texto buscado | c | Añadir la fila al modelo |
| 4 | Saber qué registro hay detrás de la fila seleccionada, con la tabla ordenada | d | Darle al proxy el texto con `setFilterFixedString` |
| | | e | Ocultar la columna en la vista con `setColumnHidden` |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**47.** La vista oculta la columna ID, y el proxy busca solo en la columna Título (`setFilterKeyColumn(1)`). Al buscar «4», aparece la fila con ID 4, aunque su título no tenga ningún 4.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**48.** Con la tabla ordenada por título a través de un proxy, la fila que se ve en primer lugar puede no ser la fila 0 del modelo.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**49.** Si `busquedaCambiada` se conecta primero con `mostrar_resultados`, que cuenta las filas del proxy, y después con el filtro, la barra de estado cuenta las filas antes de aplicar la búsqueda nueva.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**50.** En el manual de usuario de una aplicación con buscador conviene explicar que el `Buscador` emite `busquedaCambiada` y que la tabla usa un `QSortFilterProxyModel`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**51.** El manual de usuario explica también cómo se instala y cómo se abre la aplicación, y no solo cómo se hace cada tarea.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**52.** Une cada necesidad con la tecnología que la resuelve.

| | Necesidad | | Tecnología |
|---|---|---|---|
| 1 | Contar las repeticiones de un ejercicio de brazos | a | Reconocimiento de gestos de la mano |
| 2 | Escribir la descripción de un registro hablando, con las manos ocupadas | b | Realidad aumentada |
| 3 | Ver en la imagen de la cámara, sobre cada caja del almacén, qué contiene | c | Síntesis de voz |
| 4 | Pasar al registro siguiente con el pulgar arriba | d | Modelo de postura |
| | | e | Reconocimiento de voz, para dictar |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**53.** Una aplicación tiene `main.py`, `ventana.py` (sin SQL) y `bd.py` (sin widgets). Si los datos pasaran a guardarse en un servidor, solo habría que cambiar `bd.py`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**54.** Al ejecutar la última línea, la nota cambia a 5.

```python
@dataclass
class Registro:
    nota: int

r = Registro(4)
r.nota = 5
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**55.** Para usar el componente `Buscador` en otra aplicación basta con conocer su API pública, sin cambiar `buscador.py`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**56.** Desde la ventana, `self.buscador._caja.textChanged.connect(…)` es una buena forma de saber cuándo cambia la búsqueda, porque funciona.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**57.** Une cada cosa que necesita la ventana con lo que usa del `Buscador`.

| | Qué necesita la ventana | | Qué usa |
|---|---|---|---|
| 1 | Enterarse de cada cambio en la búsqueda | a | `help(Buscador)` |
| 2 | Volver a poner, al abrirse, la última búsqueda guardada con `QSettings` | b | `buscador.limpiar()` |
| 3 | Vaciar la búsqueda desde una opción del menú | c | `buscador._caja.textChanged.connect(…)` |
| 4 | Consultar la API del componente sin abrir su código | d | `buscador.busquedaCambiada.connect(…)` |
| | | e | `buscador.texto = valor` |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**58.** Con este código, `buscador.busquedaCambiada.connect(…)` funciona.

```python
class Buscador(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.busquedaCambiada = Signal(str)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

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

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**60.** Con el setter de la pregunta 59 y la nota ya en 5, `selector.nota = 9` no emite `notaCambiada`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**61.** Une cada ejemplo con el concepto que muestra.

| | Ejemplo | | Concepto |
|---|---|---|---|
| 1 | `SelectorNota` hereda de `QFrame` para aprovechar su marco | a | `notify` |
| 2 | El `Buscador` junta una etiqueta, una caja de texto y un botón | b | Encapsulación |
| 3 | `selector.nota = 4` ejecuta `_set_nota(4)` | c | Herencia |
| 4 | La señal que se indica en `Property(…, notify=…)` avisa de que la propiedad ha cambiado | d | Composición |
| | | e | `Property` |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

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

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**63.** Con el componente de la pregunta 62, `buscador.texto = "Error"` emite `busquedaCambiada`, aunque `_set_texto` no llame a `emit`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**64.** Si el `keyPressEvent` de un componente no llamara a `super().keyPressEvent(evento)` con las teclas que no usa, esas teclas no llegarían a la ventana que lo contiene.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**65.** Una ventana tiene dos selectores de cinco estrellas y un botón «Guardar». Si cada estrella pudiera recibir el foco, recorrer la ventana con Tab necesitaría 11 paradas en lugar de 3.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**66.** El `Buscador` está colocado en Qt Designer con *Promote to*, y su constructor pasa a ser este. La aplicación no arranca.

```python
def __init__(self, etiqueta="&Buscar:", parent=None):
    super().__init__(parent)
    self._etiqueta = QLabel(etiqueta)
    ...
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**67.** Une cada tarea con lo que hay que hacer.

| | Tarea | | Qué se hace |
|---|---|---|---|
| 1 | Indicar que el paquete pasa a ser la versión 0.2.0 | a | `python -m build` |
| 2 | Generar el archivo que se reparte | b | Añadir PySide6 a `requirements.txt` |
| 3 | Usar el componente en otro proyecto | c | Cambiar `version` en `pyproject.toml` |
| 4 | Que al instalar el paquete se instale también PySide6 | d | `pip install` con la ruta del `.whl` |
| | | e | Añadir PySide6 a `dependencies`, en `pyproject.toml` |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**68.** El paquete del buscador lleva solo el módulo `buscador` (`py-modules = ["buscador"]`). Si `buscador.py` hace `import bd`, con el `bd.py` de la aplicación, el paquete incluye también `bd.py`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**69.** `limpiar()` borra la caja del buscador. Esta prueba pasa.

```python
def test_limpiar(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    buscador.texto = "error"
    buscador.limpiar()
    assert buscador.texto == "error"
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**70.** Une cada comprobación con la herramienta que hace falta para ella.

| | Comprobación | | Herramienta |
|---|---|---|---|
| 1 | Que `error_titulo("")` devuelve un mensaje de error | a | `pytest.approx` |
| 2 | Que guardar una nota de 6 hace que la base de datos lance un `IntegrityError` | b | Una *fixture* con `tmp_path` |
| 3 | Que la media ponderada de unas notas da 3,7 | c | `assert`, sin nada más |
| 4 | Que al escribir en el buscador se emite `busquedaCambiada` | d | `pytest.raises` |
| | | e | `qtbot.waitSignal` |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**71.** Con el `Buscador` de la pregunta 62, recién creado y con la caja vacía, esta prueba pasa.

```python
with qtbot.waitSignal(buscador.busquedaCambiada, timeout=1000):
    buscador.texto = ""
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**72.** La clase `Registro` no comprueba nada, pero la tabla tiene `CHECK (… BETWEEN 1 AND 5)` en cada nota. Esta prueba pasa.

```python
def test_la_base_de_datos_no_acepta_notas_fuera_de_1_a_5():
    with pytest.raises(sqlite3.IntegrityError):
        almacen.guardar(Registro(6, 3, 5))
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**73.** `media` divide entre `3` en lugar de entre `len(registros)`, y todas las pruebas pasan. Por tanto, `media` está bien.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**74.** Las pruebas usan la base de datos de verdad, que al principio está vacía. Una prueba guarda dos registros y comprueba que se leen exactamente esos dos: pasa la primera vez y falla la segunda.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**75.** Una media ponderada se compara con `pytest.approx(3.7)` y no con `== 3.7` porque los decimales se guardan de forma aproximada.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**76.** Una ventana restaura con `QSettings` la última búsqueda, «Error», que coincide con 3 de sus 8 registros. `busquedaCambiada` está conectada primero con el filtro y después con `mostrar_resultados`, que cuenta las filas del proxy. Si `restaurar_estado()` se llama antes de cargar los registros, la barra de estado dice «0 registros» y la tabla también se queda vacía.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**77.** Sacar la comprobación del título a una función sin widgets, `error_titulo(titulo)`, permite probar la regla sin abrir el diálogo.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**78.** Para reconocer tres signos de la lengua de signos que no están entre los gestos de un modelo ya entrenado, hay que entrenar un modelo propio.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**79.** El detector acepta un gesto con una confianza mayor que 0,6. Une cada situación con el concepto que la describe.

| | Situación | | Concepto |
|---|---|---|---|
| 1 | El modelo da «Thumb_Up» con 0,58 | a | Modelo propio, con Teachable Machine |
| 2 | El 0,6 a partir del cual se acepta un gesto | b | Falso positivo |
| 3 | Mientras la mano pasa del puño a la victoria, el modelo ve un instante «Thumb_Up» | c | Confirmación durante varias imágenes seguidas |
| 4 | Hay que reconocer tres signos que el modelo no conoce | d | Umbral |
| | | e | Confianza |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**80.** Para dictar las notas de los pacientes de un hospital, el reconocimiento de voz en el propio equipo protege más la privacidad que en la nube.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**81.** Con este código, si el gesto más probable es `Thumb_Up` con 0,55, `gesto` vale `"Thumb_Up"`.

```python
gesto = None
if mejor.category_name != "None" and mejor.score > 0.6:
    gesto = mejor.category_name
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**82.** Con el código de la pregunta 81, si el resultado es `"None"` (la clase del modelo para una mano sin ningún gesto conocido) con 0,9, la aplicación lo toma como un gesto, porque supera el umbral.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

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

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**84.** Con el código de la pregunta 83, la secuencia 6 pulgares arriba, 1 victoria y 6 pulgares arriba emite `gestoDetectado` dos veces.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**85.** Si `CONFIRMAR` pasa de 5 a 10 y la cámara se lee al mismo ritmo, hay que mantener un gesto más o menos el doble de tiempo para que cuente.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**86.** Subir el umbral de confianza de 0,6 a 0,9 hace que, con poca luz, se reconozcan más gestos reales.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**87.** Une cada elemento del código de las preguntas 83 y 92 con su papel.

| | Elemento | | Papel |
|---|---|---|---|
| 1 | `CONFIRMAR` | a | Evita que un gesto mantenido dispare la acción muchas veces |
| 2 | `_ultimo` | b | Lee una imagen de la cámara cada poco tiempo, sin bloquear la ventana |
| 3 | `gestoDetectado` | c | Desmarca la opción del menú si la cámara no se puede abrir |
| 4 | `setChecked(False)` | d | Señal con la que el detector avisa a la aplicación |
| | | e | Nº de imágenes seguidas que tiene que durar un gesto |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**88.** Leer la cámara con un bucle `while` que no para, en lugar de con un `QTimer`, deja la ventana sin responder.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**89.** El detector de gestos tiene que heredar de `QWidget` para tener señales propias.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**90.** El mismo detector de gestos sirve en dos aplicaciones distintas porque solo detecta y avisa con una señal: el significado de cada gesto lo pone cada aplicación.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**91.** En esta clase, si `super().__init__()` se moviera al final del constructor, la línea que crea el detector daría un error.

```python
class VentanaConGestos(VentanaPrincipal):
    def __init__(self):
        super().__init__()
        self.detector = gestos.DetectorGestos(self)
        self.accion_gestos = QAction("Gestos de la mano", self)
        self.ui.menuArchivo.insertAction(self.ui.actionSalir, self.accion_gestos)
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

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

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

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

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**94.** Con `CATEGORIAS = ("docente", "materiales", "clases", "instalaciones")` y el foco en «materiales», cinco gestos de victoria seguidos dejan el foco en «clases».

```python
categoria = CATEGORIAS[(CATEGORIAS.index(categoria) + 1) % len(CATEGORIAS)]
```

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**95.** El selector es el de la pregunta 59, y su método público `limpiar()` hace `self.nota = 0`. Para dejar el selector sin nota, `selector._nota = 0` también redibuja las estrellas y avisa a la ventana, igual que `selector.limpiar()`.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**96.** Une cada pregunta que se hace una aplicación con lo que necesita para responderla.

| | Pregunta | | Lo que necesita |
|---|---|---|---|
| 1 | ¿Tiene la persona los brazos levantados? | a | Un marcador o una superficie reconocida en la imagen |
| 2 | ¿Es un pulgar arriba? | b | El ángulo entre la cadera, la rodilla y el tobillo |
| 3 | ¿Dónde se dibuja la etiqueta del objeto? | c | El texto que ha reconocido el modelo de voz |
| 4 | ¿Está la rodilla doblada? | d | La posición de las muñecas respecto a los hombros, con el modelo de postura |
| | | e | La forma de la mano, con sus 21 puntos |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**97.** Una aplicación de escritorio que se maneje solo con gestos, sin teclado, es más accesible.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**98.** En un almacén ruidoso conviene usar órdenes de voz cortas, pocas y distintas entre sí, y pedir confirmación antes de eliminar.

**V** ☐ &nbsp;&nbsp;&nbsp; **F** ☐

**99.** Une cada criterio de diseño de interfaces naturales con un ejemplo.

| | Criterio | | Ejemplo |
|---|---|---|---|
| 1 | Alternativa | a | Tras cada gesto, la barra de estado dice qué ha entendido la aplicación |
| 2 | Retroalimentación | b | Mantener el brazo levantado durante horas cansa |
| 3 | Privacidad | c | «¿Eliminar el registro "Exportar a CSV"? Di sí o no» |
| 4 | Confirmación | d | Todo lo que se hace con gestos se puede hacer también con el teclado |
| | | e | La cámara solo se enciende al marcar una opción del menú |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐

**100.** Une cada prueba con su tipo.

| | Prueba | | Tipo |
|---|---|---|---|
| 1 | Tras cambiar el orden de los parámetros del `Buscador`, se vuelven a pasar todas las pruebas | a | Unitaria |
| 2 | Se comprueba que `media([4, 2])` da 3, sin ventana ni base de datos | b | De integración |
| 3 | Se escribe un registro en la ventana y se comprueba que queda en la base de datos | c | De usabilidad |
| 4 | Una persona que no conoce la aplicación intenta añadir y eliminar un registro sin ayuda | d | De humo |
| | | e | De regresión |

1 → ☐ &nbsp;&nbsp;&nbsp; 2 → ☐ &nbsp;&nbsp;&nbsp; 3 → ☐ &nbsp;&nbsp;&nbsp; 4 → ☐
