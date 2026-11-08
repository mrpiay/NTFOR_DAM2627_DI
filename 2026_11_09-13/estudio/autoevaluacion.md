# Autoevaluación · semana del 9 al 13 de noviembre

Preguntas sobre la 2.ª parte del proyecto «Mejora tu BugTracker». Puede que sufran modificaciones a lo largo de la semana. Responde poniendo el número de cada pregunta.

En las preguntas con código, crea en la carpeta del proyecto un archivo con el nombre que se indica, pega el código y ejecútalo con el entorno virtual (`.venv\Scripts\python nombre.py`). Copia en tu respuesta lo que sale por pantalla y asegúrate de que lo entiendes: en las pruebas escritas tendrás que explicarlo sin ayuda de la IA.

Si en una pregunta aparece algo que no has visto, búscalo en «Dónde consultar», en el [README de `estudio/`](README.md).

---

**1.** ¿Cómo encuentra pytest las pruebas que tiene que ejecutar? ¿Qué es un `assert`? Antes del paso 5, `python -m pytest -v` daba **4 failed**: ¿por qué?

**2.** En las pruebas de `test_buscador.py`, ¿qué hace `qtbot`? ¿Para qué sirven `qtbot.addWidget`, `qtbot.keyClicks`, `qtbot.mouseClick` y `qtbot.waitSignal`?

**3.** ¿Qué es un componente reutilizable? ¿Cuál es la API pública del `Buscador`: sus propiedades, sus métodos y sus señales?

**4.** ¿Qué diferencia hay entre crear un componente por herencia y por composición? ¿Cómo está hecho el `Buscador`?

**5.** En `buscador.py`, ¿por qué `_caja`, `_boton` y `_al_cambiar_texto` empiezan por `_`? ¿Por qué `main.py` no usa `self.buscador._caja`?

**6.** ¿Dónde se declara la señal `busquedaCambiada` y con qué? ¿Cómo se lanza? ¿Qué pasa si se declara dentro de `__init__`?

**7.** ¿Qué hace `texto = Property(str, _get_texto, _set_texto, notify=busquedaCambiada)`? ¿Qué se ejecuta al escribir `buscador.texto = "Error"` y al leer `buscador.texto`?

**8.** Crea `senal.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
import sys
from PySide6.QtWidgets import QApplication
from buscador import Buscador

app = QApplication(sys.argv)
buscador = Buscador()
buscador.busquedaCambiada.connect(lambda texto: print("Señal:", repr(texto)))
buscador.texto = "Error"
buscador.texto = "Error"
print("Texto:", buscador.texto)
buscador.limpiar()
print("Después de limpiar:", repr(buscador.texto))
```

**9.** Cuenta, paso a paso, qué pasa desde que escribes una letra en el buscador hasta que la tabla se filtra y la barra de estado dice cuántas incidencias quedan. Di qué método de qué archivo se ejecuta en cada paso.

**10.** ¿Qué hace cada línea de `configurar_buscador()`? ¿Por qué `self.configurar_buscador()` se llama después de `self.configurar_tabla()` y no antes?

**11.** Crea `filtro.py` con este código y ejecútalo. Copia lo que sale por pantalla.

```python
from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel

modelo = QStandardItemModel(0, 2)
for id_, titulo in ((1, "Error al guardar"), (2, "Botón sin texto"), (3, "error de contraste")):
    modelo.appendRow([QStandardItem(str(id_)), QStandardItem(titulo)])

proxy = QSortFilterProxyModel()
proxy.setSourceModel(modelo)
proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
proxy.setFilterKeyColumn(-1)                  # busca en todas las columnas

proxy.setFilterFixedString("error")
print("«error»:", proxy.rowCount())
proxy.setFilterFixedString("3")
print("«3» en todas las columnas:", proxy.rowCount())
proxy.setFilterKeyColumn(1)                   # solo en la columna del título
print("«3» solo en el título:", proxy.rowCount())
proxy.setFilterFixedString("")
print("Sin filtro:", proxy.rowCount(), "de", modelo.rowCount())
```

**12.** Con el filtro puesto, la tabla muestra menos filas y en otro orden que el modelo. ¿Por qué, aun así, «Eliminar» borra la incidencia que has seleccionado y no otra?

**13.** Crea `test_pregunta.py` con este código y ejecútalo con `.venv\Scripts\python -m pytest test_pregunta.py -v`. Copia las dos líneas que empiezan por `test_pregunta.py::` y la última línea. ¿Por qué falla una de las pruebas? Cuando termines, borra `test_pregunta.py`: si no, `python -m pytest` también la ejecutará.

```python
from buscador import Buscador


def test_limpiar_deja_vacio(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    buscador.texto = "Alta"
    buscador.limpiar()
    assert buscador.texto == ""


def test_mayusculas(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    buscador.texto = "ALTA"
    assert buscador.texto == "alta"
```

**14.** ¿Qué prueba añadiste como quinta prueba y qué comprueba? ¿Qué es un valor límite y por qué conviene probarlos?

**15.** Quieres usar el mismo `Buscador` en otra aplicación, por ejemplo un editor de notas. ¿Qué tendrías que hacer en esa aplicación? ¿Habría que cambiar algo de `buscador.py`?

**16.** En la ampliación A, ¿qué guarda `QSettings` y dónde lo guarda en Windows? ¿En qué método se guarda y en cuál se recupera? ¿Por qué `restaurar_estado()` se llama al final de `__init__`?

**17.** ¿Qué muestra `python -c "import buscador; help(buscador.Buscador)"` y de dónde sale ese texto? ¿Qué debe contar la documentación de un componente?

**18.** En la ampliación C, ¿para qué sirve `pyproject.toml`? ¿Qué crea `python -m build` y cómo se instala lo que crea en otro proyecto?

**19.** En la prueba de usabilidad del paso 7, ¿por qué quien prueba no recibe ayuda y piensa en voz alta? ¿Qué se apunta de cada tarea?

**20.** ¿Qué es una interfaz natural? Pon un ejemplo para el BugTracker, di a quién ayudaría, un límite que tendría y qué alternativa ofrecerías.

## UD3

Estas preguntas se responden con los apuntes de cada unidad, en `estudio/`.

**21.** ¿Qué herramientas se usan para diseñar un componente visual y cuáles para probarlo?

**22.** ¿Qué tiene que incluir una estrategia de pruebas de un componente? Propón tres casos de prueba para el `Buscador` distintos de los de `test_buscador.py`.
