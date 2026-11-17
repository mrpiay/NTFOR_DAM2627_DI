# Cuestionario C1 · semana del 2 al 6 de noviembre · soluciones

## Cuestiones sobre el proyecto

**1.** ¿Qué es el entorno virtual `.venv` y qué hace `pip install -r requirements.txt`? ¿Por qué cada proyecto tiene su propio entorno?

**Respuesta.** `.venv` es una carpeta con su propio Python y las librerías de este proyecto. `pip install -r requirements.txt` instala en ella las librerías que lista ese archivo (PySide6-Essentials, en la versión 6.12, pytest y pytest-qt). Cada proyecto tiene el suyo para no mezclar versiones: un proyecto puede necesitar una versión de una librería y otro, otra.

**2.** ¿Cómo se abre Qt Designer desde la terminal sin que la terminal se quede bloqueada? ¿Qué hace cada parte de la orden?

**Respuesta.** `Start-Process .venv\Scripts\pyside6-designer.exe -ArgumentList bugtracker.ui -WindowStyle Hidden`. `Start-Process` lo abre aparte, y la terminal queda libre; `.venv\Scripts\pyside6-designer.exe` es el Designer del entorno virtual; `-ArgumentList bugtracker.ui` le dice qué archivo abrir; y `-WindowStyle Hidden` oculta la ventana de terminal vacía que, si no, se abre junto a Designer.

**3.** Al arrancar, ¿la aplicación lee `bugtracker.ui` o `ui_bugtracker.py`? ¿Qué hay que hacer después de cambiar algo en Qt Designer para verlo en la aplicación?

**Respuesta.** Lee `ui_bugtracker.py`: `main.py` importa su clase `Ui_VentanaPrincipal` y llama a `setupUi`. `bugtracker.ui` solo lo lee Qt Designer. Después de cambiar algo en Designer hay que guardar, regenerar con `pyside6-uic bugtracker.ui -o ui_bugtracker.py` y volver a lanzar la aplicación.

**4.** ¿Por qué no hay que editar `ui_bugtracker.py` a mano?

**Respuesta.** Porque se genera a partir de `bugtracker.ui`: la próxima vez que se regenere, `pyside6-uic` lo sobrescribe y se pierde lo que se hubiera escrito a mano. Los cambios de la interfaz se hacen siempre en Designer.

**5.** ¿Qué hace cada archivo del proyecto: `main.py`, `bd.py`, `dialogo.py`, `bugtracker.ui`, `ui_bugtracker.py` y `datos_ejemplo.py`?

**Respuesta.**

- `main.py`: la ventana principal (`VentanaPrincipal`). Carga la interfaz, conecta señales y slots, y tiene la lógica: añadir, modificar, eliminar, las acciones y la tabla.
- `bd.py`: todo el acceso a SQLite (crear la tabla, leer, insertar, actualizar y borrar).
- `dialogo.py`: el diálogo «Nueva incidencia» / «Editar incidencia», con su validación.
- `bugtracker.ui`: el diseño de la ventana, hecho en Qt Designer.
- `ui_bugtracker.py`: el código Python generado a partir de `bugtracker.ui`.
- `datos_ejemplo.py`: añade incidencias de prueba; se ejecuta una vez.

**6.** En el proyecto, `main.py` nunca contiene SQL y `bd.py` nunca usa widgets. ¿Por qué conviene separarlos así? ¿Qué archivo habría que cambiar si mañana los datos estuvieran en otra base de datos?

**Respuesta.** Cada archivo tiene una sola responsabilidad: `bd.py`, los datos; `main.py`, la interfaz y su lógica. Así se puede cambiar una parte sin tocar la otra, y es más fácil encontrar y probar cada cosa. Si los datos estuvieran en otra base de datos, solo habría que cambiar `bd.py`: `main.py` seguiría llamando a las mismas funciones (`obtener_incidencias`, `insertar_incidencia`…).

**7.** ¿Por qué las consultas de `bd.py` usan `?` en lugar de pegar los datos dentro del texto de la consulta?

**Respuesta.** Con `?`, `sqlite3` pasa los datos aparte, como valores. Si se pegaran en el texto, un título con una comilla rompería la consulta, y alguien podría escribir algo que se ejecutara como SQL (inyección SQL).

**8.** Elige dos heurísticas de Nielsen. Para cada una, di un problema del BugTracker que la incumpla y cómo lo mejoraste.

**Respuesta.** Por ejemplo:

- *Visibilidad del estado del sistema:* al añadir una incidencia no se decía nada. Mejora: un mensaje en la barra de estado, «Incidencia añadida».
- *Prevención de errores:* «Eliminar» estaba activo sin nada seleccionado. Mejora: desactivarlo sin selección y pedir confirmación antes de borrar.

(Valen otras, siempre que cada problema corresponda de verdad a su heurística.)

**9.** ¿Qué hace la `&` de `&Título (obligatorio):`? ¿Qué es el *buddy* de una etiqueta y qué pasa si falta?

**Respuesta.** La `&` hace que la letra siguiente sea un atajo: `Alt+T` (aparece subrayada). El *buddy* es el campo asociado a la etiqueta: el atajo de la etiqueta lleva el foco a ese campo. Sin *buddy*, `Alt+T` no hace nada, porque una etiqueta no puede recibir el foco.

**10.** ¿Para qué sirve marcar `tabChangesFocus` en `txtDescripcion`? ¿Y desmarcar `tabKeyNavigation` en `tblIncidencias`?

**Respuesta.** `tabChangesFocus` hace que `Tab` salga de la descripción y pase al siguiente campo, en lugar de escribir un tabulador dentro del texto. Desmarcar `tabKeyNavigation` hace que `Tab` salga de la tabla en lugar de ir de celda en celda; dentro de la tabla uno se mueve con las flechas. Las dos permiten usar la aplicación entera con el teclado.

**11.** Crea `accion.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
import sys
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
accion = QAction("&Nueva incidencia...")
accion.setShortcut(QKeySequence("Ctrl+N"))
accion.triggered.connect(lambda: print("Se ha disparado la acción"))
print(accion.text(), "->", accion.shortcut().toString())
accion.trigger()
```

**Respuesta.**

```
&Nueva incidencia... -> Ctrl+N
Se ha disparado la acción
```

La `QAction` guarda el texto (con su `&`) y el atajo. `trigger()` hace lo mismo que elegirla en el menú, pulsar su botón o su atajo: emite la señal `triggered`, y se ejecuta lo que está conectado a ella.

**12.** Crea `boton.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

def guardar():
    print("Guardando")

boton = QPushButton("&Guardar")
boton.clicked.connect(guardar)
print("Antes del clic")
boton.click()
boton.clicked.connect(guardar())
```

**Respuesta.**

```
Antes del clic
Guardando
Guardando
Traceback (most recent call last):
  …
TypeError: Expected signal or callable, got "NoneType"
```

`connect(guardar)` conecta la señal con el método, sin ejecutarlo: `guardar` solo se ejecuta con el clic (`boton.click()`), por eso sale «Guardando» después de «Antes del clic». En la última línea, `guardar()` lleva paréntesis: se **ejecuta en ese momento** (el segundo «Guardando») y a `connect` le llega lo que devuelve, `None`, que no se puede conectar. En el proyecto pasa lo mismo con `connect(self.guardar())`: hay que pasar el método sin llamarlo.

**13.** ¿Por qué la misma `QAction` se pone en el menú y en la barra de herramientas?

**Respuesta.** Porque es una sola orden: se programa una vez (una conexión de `triggered`) y aparece en los dos sitios con el mismo texto, atajo y estado. Si se desactiva (como Eliminar sin selección), se desactiva en los dos.

**14.** ¿Qué es un diálogo modal? En «Nueva incidencia», ¿qué devuelve `exec()` y en qué momento se llama a `accept()`?

**Respuesta.** Un diálogo modal bloquea la ventana principal hasta que se cierra. `exec()` lo muestra y devuelve verdadero si se aceptó y falso si se canceló. El botón Aceptar está conectado a `validar()`, no a `accept()`: `validar()` comprueba que el título no esté vacío ni pase de 100 caracteres, y solo entonces llama a `accept()`. Si no, avisa y el diálogo sigue abierto.

**15.** Cuenta, paso a paso, qué pasa desde que pulsas `Ctrl+N` hasta que la incidencia nueva aparece en la tabla. Di qué método de qué archivo se ejecuta en cada paso.

**Respuesta.**

1. `Ctrl+N` dispara la `QAction` `actionNueva`: emite `triggered`.
2. Esa señal está conectada (en `__init__` de `main.py`) a `nueva_incidencia()`.
3. `nueva_incidencia()` crea `DialogoIncidencia(self)` (`dialogo.py`) y llama a `exec()`.
4. Al pulsar Aceptar se ejecuta `validar()`, que comprueba el título y llama a `accept()`: `exec()` devuelve verdadero.
5. `nueva_incidencia()` toma `dialogo.datos()` y llama a `bd.insertar_incidencia(*…)` (`bd.py`), que hace el `INSERT`.
6. `cargar_incidencias()` vuelve a leer las incidencias con `bd.obtener_incidencias()` y rellena el modelo: la incidencia aparece en la tabla.
7. La barra de estado muestra que se ha añadido.

**16.** Crea `estrella.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
def guardar(titulo, tipo, prioridad):
    print(titulo, "|", tipo, "|", prioridad)

datos = ("No guarda", "Error", "Alta")
guardar(*datos)
guardar(datos)
```

**Respuesta.**

```
No guarda | Error | Alta
Traceback (most recent call last):
  …
TypeError: guardar() missing 2 required positional arguments: 'tipo' and 'prioridad'
```

El `*` reparte la tupla en tres argumentos: `guardar(*datos)` es lo mismo que `guardar("No guarda", "Error", "Alta")`. Sin `*`, la tupla entera es un solo argumento (`titulo`) y faltan los otros dos. Por eso en el proyecto se escribe `bd.insertar_incidencia(*dialogo.datos())`.

**17.** ¿Qué diferencia hay entre usar un `QTableWidget` y usar Model/View? ¿Qué hace cada pieza: el modelo, el proxy y la vista?

**Respuesta.** Con `QTableWidget` los datos viven dentro del widget: se meten celda a celda. En Model/View se separan: el **modelo** (`QStandardItemModel`) guarda las filas y columnas; la **vista** (`QTableView`) solo las dibuja y gestiona la selección; y el **proxy** (`QSortFilterProxyModel`), entre los dos, ordena y filtra sin tocar los datos del modelo.

**18.** Crea `proxy.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

modelo = QStandardItemModel(0, 2)
for id_, titulo in ((1, "Exportar CSV"), (2, "Botón Guardar"), (3, "Contraste")):
    modelo.appendRow([QStandardItem(str(id_)), QStandardItem(titulo)])

proxy = QSortFilterProxyModel()
proxy.setSourceModel(modelo)
proxy.sort(1, Qt.SortOrder.AscendingOrder)   # ordena por título

fila_vista = 0                                # la primera fila que se ve
indice = proxy.index(fila_vista, 1)
print("Se ve:", indice.data())
print("Fila en la vista:", fila_vista)
print("Fila en el modelo:", proxy.mapToSource(indice).row())
print("ID:", modelo.item(proxy.mapToSource(indice).row(), 0).text())
print("ID si no se traduce:", modelo.item(fila_vista, 0).text())
```

**Respuesta.**

```
Se ve: Botón Guardar
Fila en la vista: 0
Fila en el modelo: 1
ID: 2
ID si no se traduce: 1
```

El proxy ordena por título, así que lo que se ve en la fila 0 («Botón Guardar») está en la fila 1 del modelo. `mapToSource` traduce la fila de la vista a la del modelo. Sin traducirla se coge el ID de otra incidencia (1, «Exportar CSV»): al eliminar o modificar después de ordenar, se cambiaría la que no es.

**19.** En la tabla, la columna ID no se ve, pero sigue en el modelo. ¿Para qué se usa?

**Respuesta.** Para saber qué incidencia está seleccionada: `id_seleccionado()` lee el ID de la fila seleccionada (traducida con `mapToSource`) y ese ID es el que se pasa a `bd.py` para modificar o eliminar. No se usa el número de fila, porque cambia al ordenar; el ID no cambia. Se oculta porque al usuario no le dice nada.

**20.** ¿En qué se diferencia `DialogoIncidencia(self, incidencia)` de `DialogoIncidencia(self)`? ¿Desde dónde se abre cada uno?

**Respuesta.** `DialogoIncidencia(self)` se abre vacío, con el título «Nueva incidencia», desde la acción Nueva (`Ctrl+N`). `DialogoIncidencia(self, incidencia)` se abre con los datos de esa incidencia ya rellenos y el título «Editar incidencia», al hacer doble clic en una fila. Al aceptar, el primero inserta una incidencia nueva y el segundo actualiza la que había.

## Cuestiones sobre los apuntes

**21.** ¿Qué diferencia hay entre usabilidad, accesibilidad y experiencia de usuario?

**Respuesta.** *(UD1, apartado 1)* La usabilidad es lo fácil que es usar la aplicación para conseguir algo; la accesibilidad, que la pueda usar cualquier persona, también con una discapacidad; la experiencia de usuario es todo lo que siente la persona al usarla (si le resulta útil, cómoda y agradable), e incluye las dos anteriores.

**22.** ¿Cuáles son los cuatro principios de las pautas WCAG? ¿Qué nivel se suele exigir y qué contraste mínimo necesita en él el texto normal?

**Respuesta.** *(UD1, apartado 3)* Perceptible, operable, comprensible y robusto. Se suele exigir el nivel **AA**, en el que el texto normal necesita un contraste de al menos **4,5:1** con el fondo.

**23.** ¿Qué son ISO 9241 y EN 301 549? ¿Por qué conviene seguir los estándares al diseñar una interfaz?

**Respuesta.** *(UD1, apartado 4)* ISO 9241 es la norma internacional de ergonomía de la interacción (define la usabilidad como eficacia, eficiencia y satisfacción); EN 301 549 es la norma europea que exige la accesibilidad (WCAG). Seguir los estándares hace que la interfaz se entienda a la primera, reduce lo que hay que aprender y los errores, y en accesibilidad a veces es obligatorio (en España, en el sector público).

**24.** ¿Qué control de Qt usarías para cada dato: un texto de una línea, una opción entre pocas fijas, sí o no, un número dentro de un rango y una fecha?

**Respuesta.** *(UD1, apartado 5)* `QLineEdit`, `QComboBox` (o `QRadioButton`), `QCheckBox`, `QSpinBox` y `QDateEdit`.

**25.** Escribe un buen mensaje para cuando falta el título y di qué tiene que tener un buen mensaje. ¿Qué atajos estándar tienen «Nuevo», «Guardar» y «Salir»?

**Respuesta.** *(UD1, apartados 5 y 6)* Por ejemplo, «Falta el título. Escríbelo para poder guardar la incidencia». Un buen mensaje es breve, está en el idioma del usuario y dice qué ha pasado y qué hacer, sin códigos técnicos. Los atajos: `Ctrl+N`, `Ctrl+S` y `Ctrl+Q`.

**26.** ¿En qué se diferencian PySide6, PyQt6 y Tkinter?

**Respuesta.** *(UD2, apartado 1)* PySide6 y PyQt6 son Qt para Python y usan Qt Designer; PySide6 es la oficial, con licencia LGPL, y PyQt6 tiene licencia GPL o comercial. Tkinter viene con Python, es más sencilla y no tiene un editor visual oficial.

