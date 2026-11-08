# Autoevaluación · semana del 2 al 6 de noviembre

Preguntas sobre la 1.ª parte del proyecto «Mejora tu BugTracker». Puede que sufran modificaciones a lo largo de la semana. Responde poniendo el número de cada pregunta.

En las preguntas con código, crea en la carpeta del proyecto un archivo con el nombre que se indica, pega el código y ejecútalo con el entorno virtual (`.venv\Scripts\python nombre.py`). Copia en tu respuesta lo que sale por pantalla y asegúrate de que lo entiendes: en las pruebas escritas tendrás que explicarlo sin ayuda de la IA.

Si en una pregunta aparece algo que no has visto, búscalo en «Dónde consultar», en el [README de `estudio/`](README.md).

---

**1.** ¿Qué es el entorno virtual `.venv` y qué hace `pip install -r requirements.txt`? ¿Por qué cada proyecto tiene su propio entorno?

**2.** ¿Cómo se abre Qt Designer desde la terminal sin que la terminal se quede bloqueada? ¿Qué hace cada parte de la orden?

**3.** Al arrancar, ¿la aplicación lee `bugtracker.ui` o `ui_bugtracker.py`? ¿Qué hay que hacer después de cambiar algo en Qt Designer para verlo en la aplicación?

**4.** ¿Por qué no hay que editar `ui_bugtracker.py` a mano?

**5.** ¿Qué hace cada archivo del proyecto: `main.py`, `bd.py`, `dialogo.py`, `bugtracker.ui`, `ui_bugtracker.py` y `datos_ejemplo.py`?

**6.** En el proyecto, `main.py` nunca contiene SQL y `bd.py` nunca usa widgets. ¿Por qué conviene separarlos así? ¿Qué archivo habría que cambiar si mañana los datos estuvieran en otra base de datos?

**7.** ¿Por qué las consultas de `bd.py` usan `?` en lugar de pegar los datos dentro del texto de la consulta?

**8.** Elige dos heurísticas de Nielsen. Para cada una, di un problema del BugTracker que la incumpla y cómo lo mejoraste.

**9.** ¿Qué hace la `&` de `&Título (obligatorio):`? ¿Qué es el *buddy* de una etiqueta y qué pasa si falta?

**10.** ¿Para qué sirve marcar `tabChangesFocus` en `txtDescripcion`? ¿Y desmarcar `tabKeyNavigation` en `tblIncidencias`?

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

**13.** ¿Por qué la misma `QAction` se pone en el menú y en la barra de herramientas?

**14.** ¿Qué es un diálogo modal? En «Nueva incidencia», ¿qué devuelve `exec()` y en qué momento se llama a `accept()`?

**15.** Cuenta, paso a paso, qué pasa desde que pulsas `Ctrl+N` hasta que la incidencia nueva aparece en la tabla. Di qué método de qué archivo se ejecuta en cada paso.

**16.** Crea `estrella.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
def guardar(titulo, tipo, prioridad):
    print(titulo, "|", tipo, "|", prioridad)

datos = ("No guarda", "Error", "Alta")
guardar(*datos)
guardar(datos)
```

**17.** ¿Qué diferencia hay entre usar un `QTableWidget` y usar Model/View? ¿Qué hace cada pieza: el modelo, el proxy y la vista?

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

**19.** En la tabla, la columna ID no se ve, pero sigue en el modelo. ¿Para qué se usa?

**20.** ¿En qué se diferencia `DialogoIncidencia(self, incidencia)` de `DialogoIncidencia(self)`? ¿Desde dónde se abre cada uno?

## UD1 y UD2

Estas preguntas se responden con los apuntes de cada unidad, en `estudio/`.

**21.** ¿Qué diferencia hay entre usabilidad, accesibilidad y experiencia de usuario?

**22.** ¿Cuáles son los cuatro principios de las pautas WCAG? ¿Qué nivel se suele exigir y qué contraste mínimo necesita en él el texto normal?

**23.** ¿Qué son ISO 9241 y EN 301 549? ¿Por qué conviene seguir los estándares al diseñar una interfaz?

**24.** ¿Qué control de Qt usarías para cada dato: un texto de una línea, una opción entre pocas fijas, sí o no, un número dentro de un rango y una fecha?

**25.** Escribe un buen mensaje para cuando falta el título y di qué tiene que tener un buen mensaje. ¿Qué atajos estándar tienen «Nuevo», «Guardar» y «Salir»?

**26.** ¿En qué se diferencian PySide6, PyQt6 y Tkinter?
