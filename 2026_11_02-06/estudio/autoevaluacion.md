# Autoevaluación · semana del 2 al 6 de noviembre

Preguntas sobre la 1.ª parte del proyecto «Mejora tu BugTracker». Puede que sufran modificaciones a lo largo de la semana. Responde poniendo el número de cada pregunta.

En las preguntas con código, crea en la carpeta del proyecto un archivo con el nombre que se indica, pega el código y ejecútalo con el entorno virtual (`.venv\Scripts\python nombre.py`). Copia en tu respuesta lo que sale por pantalla y asegúrate de que lo entiendes: en las pruebas escritas tendrás que explicarlo sin ayuda de la IA.

Si en una pregunta aparece algo que no has visto, búscalo en «Dónde consultar», en el [README de `estudio/`](README.md).

---

**1.** Al arrancar, ¿la aplicación lee `bugtracker.ui` o `ui_bugtracker.py`? ¿Qué hay que hacer después de cambiar algo en Qt Designer para verlo en la aplicación?

**2.** ¿Por qué no hay que editar `ui_bugtracker.py` a mano?

**3.** En el proyecto, `main.py` nunca contiene SQL y `bd.py` nunca usa widgets. ¿Por qué conviene separarlos así? ¿Qué archivo habría que cambiar si mañana los datos estuvieran en otra base de datos?

**4.** ¿Por qué las consultas de `bd.py` usan `?` en lugar de pegar los datos dentro del texto de la consulta?

**5.** Elige dos heurísticas de Nielsen. Para cada una, di un problema del BugTracker que la incumpla y cómo lo mejoraste.

**6.** ¿Qué hace la `&` de `&Título (obligatorio):`? ¿Qué es el *buddy* de una etiqueta y qué pasa si falta?

**7.** ¿Para qué sirve marcar `tabChangesFocus` en `txtDescripcion`? ¿Y desmarcar `tabKeyNavigation` en `tblIncidencias`?

**8.** Crea `accion.py` con este código y ejecútalo. Copia lo que sale por pantalla.

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

**9.** ¿Por qué la misma `QAction` se pone en el menú y en la barra de herramientas? ¿Qué pasa si escribes `connect(self.guardar())`, con paréntesis?

**10.** ¿Qué es un diálogo modal? En «Nueva incidencia», ¿qué devuelve `exec()` y en qué momento se llama a `accept()`?

**11.** Crea `estrella.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
def guardar(titulo, tipo, prioridad):
    print(titulo, "|", tipo, "|", prioridad)

datos = ("No guarda", "Error", "Alta")
guardar(*datos)
guardar(datos)
```

**12.** ¿Qué diferencia hay entre usar un `QTableWidget` y usar Model/View? ¿Qué hace cada pieza: el modelo, el proxy y la vista?

**13.** Crea `proxy.py` con este código y ejecútalo. Copia lo que sale por pantalla.

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

**14.** En la tabla, la columna ID no se ve, pero sigue en el modelo. ¿Para qué se usa?

**15.** ¿En qué se diferencia `DialogoIncidencia(self, incidencia)` de `DialogoIncidencia(self)`? ¿Desde dónde se abre cada uno?
