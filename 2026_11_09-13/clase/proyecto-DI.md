# DI · Proyecto guiado «Mejora tu BugTracker» · 2.ª parte

## Punto de partida

Es la continuación de la 1.ª parte (semana del 2 al 6 de noviembre, pasos 0 a 4): el BugTracker con acciones, menú, barra de herramientas, diálogo con validación y la tabla con Model/View. En esta 2.ª parte le añades un **componente reutilizable** con sus **pruebas automáticas** (UD3), lo pruebas con otra persona (UD1) y piensas en las **interfaces naturales** (UD4).

**Usa la IA como guía, no para que lo haga por ti.** Pídele los **pasos necesarios** para implementar cada cosa y que te explique lo que no entiendas; **el código lo pones tú en tu proyecto**, aunque sea copiando y pegando, sabiendo **dónde** lo pones y **para qué**: es la única forma de familiarizarte con tu entorno. El objetivo es que lo que hagas **funcione y cumpla los requisitos** de cada paso («Comprueba que…») y que sepas **dónde está cada cosa y qué habría que tocar para cambiar o añadir algo**: es lo que te van a pedir después.

**El objetivo es entender cada paso:** es lo que necesitas para responder los cuestionarios de autoevaluación y preparar la prueba escrita.

**Evaluación continua.** Algunas semanas hay una **prueba escrita, en papel,** en las dos últimas sesiones del último día de clase, después de que se publiquen las soluciones de lo que entra; se avisa con antelación. La primera es el **jueves 19 de noviembre**, sobre **las dos partes del proyecto** (pasos 0 a 8): Qt Designer y `pyside6-uic`, PySide6 (señales y slots, acciones, menús y diálogos con validación), Model/View, accesibilidad, el componente reutilizable `Buscador` y sus pruebas con pytest-qt, y el propio proyecto.

Del 10 al 12 de noviembre. Cada paso trae una mini-explicación, una pista y qué hacer si algo falla.

## Con qué trabajas

- **Si terminaste la 1.ª parte y funciona**: sigue en tu carpeta `bugtracker_repaso`. Ya tiene `buscador.py` y `test_buscador.py`, que copiaste de la plantilla de la 1.ª parte.
- **Si no la terminaste o no te funciona**: descarga el repositorio del módulo (*Code → Download ZIP*) y copia `2026_11_09-13/clase/plantilla` con el nombre `bugtracker_repaso`, en una **ruta corta y fuera de OneDrive**, por ejemplo `C:\dam\di\bugtracker_repaso`. Es la 1.ª parte terminada. Ábrela en VS Code y, en la terminal (PowerShell):

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python datos_ejemplo.py
python main.py
```

`datos_ejemplo.py` añade cinco incidencias de prueba; ejecútalo una sola vez. En VS Code elige el intérprete del entorno: `Ctrl+Mayús+P` → «Python: Select Interpreter» → el de `.venv`.

**Comprueba que** en la terminal aparece `(.venv)` al principio de la línea y que `python main.py` abre el BugTracker.

**Si te falla…**

- *«La ejecución de scripts está deshabilitada»*: ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activar el entorno.
- *`WinError 206` («el nombre del archivo o la extensión es demasiado largo»)*: la carpeta está en una ruta demasiado larga o en OneDrive. Bórrala, cópiala a `C:\dam\di\` y repite desde `python -m venv .venv`.

Qué tocas en cada paso:

| Archivo | Qué es | Paso en que lo tocas |
|---|---|---|
| `buscador.py` | componente reutilizable `Buscador` | 5 |
| `main.py` | ventana principal y lógica | 5 |
| `test_buscador.py` | pruebas con pytest-qt, ya escritas | 6 |

En la plantilla, los comentarios `# TODO Paso 5` marcan dónde se añade código. Antes del paso 5, `python -m pytest -v` da **4 failed**: es lo esperado, porque el componente aún no está hecho.

Lo que escribas en los pasos 7 y 8 va en `notas.md`, el archivo de texto de la carpeta de tu proyecto que empezaste en la 1.ª parte (si no lo tienes, créalo).

## Qué se repasa

| Unidad | Qué repasamos | Pasos |
|---|---|---|
| UD3 · Componentes reutilizables | componente por composición, propiedad y señal propias, pruebas con pytest-qt, `QSettings`, documentar y empaquetar | 5, 6 y ampliaciones |
| UD1 · Diseño, UX y accesibilidad | prueba de usabilidad | 7 |
| UD4 · Interfaces naturales | tipos, límites y relación con la accesibilidad | 8 |

## Plan de la semana

Cada sesión dura 50 minutos.

| Día | Sesión | Qué hacemos |
|---|---|---|
| Martes 10 | 10:10 | **Paso 5** (componente `Buscador`). |
| Martes 10 | 11:00 | **Paso 6** (pruebas con pytest-qt, 35 min). Guardar el estado, documentar y empaquetar (15 min). |
| Martes 10 | 12:10 | **Paso 7** (prueba de usabilidad en parejas, 25 min) y **Paso 8** (reflexión UD4, 15 min). Qué entra en la prueba escrita del jueves 19 (10 min). |
| Miércoles 11 | 11:00 y 12:10 | UD4, según el plan del curso. |
| Jueves 12 | 08:30 y 09:20 | Terminar la 2.ª parte del proyecto y hacer las ampliaciones. |

**Los pasos se hacen en orden**, cada uno en la sesión que le toca según el plan de la semana: cada paso usa lo del anterior. Si terminas antes, haz las ampliaciones.

Los pasos 5 y 6 tienen **Objetivo**, **Mini-explicación** (lo justo), **Pista**, **Comprueba que…** y **Si te falla…**; los pasos 7 y 8, **Objetivo**, **Pista** y **Comprueba que…**.

---

## Paso 5 · Componente reutilizable `Buscador` (martes, 50 min)

**Objetivo.** Completar `buscador.py`: un widget propio con una **propiedad** (`texto`), un **método** (`limpiar()`) y una **señal propia** (`busquedaCambiada(str)`), e integrarlo para filtrar la tabla.

**Mini-explicación.**

- Un **componente reutilizable** encapsula aspecto y comportamiento y se usa sin saber cómo está hecho por dentro. Su **API pública** son sus propiedades, métodos y señales.
- Se puede crear por **herencia** (heredar de un widget y cambiar su comportamiento) o por **composición** (un `QWidget` que contiene otros y los coordina). El `Buscador` se hace por composición.
- La **señal propia** se declara **en la clase** con `Signal(str)` y se lanza con `emit(...)`. La **propiedad** (`Property`) se lee y se escribe como un atributo (`buscador.texto = "Error"`); con `notify` se indica qué señal avisa de sus cambios.
- Lo que empieza por `_` es interno: quien use el componente no lo toca.

La señal, la propiedad y el docstring ya están declarados en la plantilla. Te falta el cuerpo.

**Pista.** En `buscador.py`, sustituye los dos comentarios `# TODO Paso 5` de `__init__` (debajo de `super().__init__(parent)`) por esto, con la misma sangría:

```python
        self._etiqueta = QLabel(etiqueta)
        self._caja = QLineEdit()
        self._caja.setPlaceholderText("Escribe para filtrar")
        self._caja.setAccessibleName("Texto de búsqueda")
        self._etiqueta.setBuddy(self._caja)       # Alt+B lleva el foco a la caja
        self._boton = QPushButton("Limpiar")
        self._boton.setAccessibleName("Limpiar búsqueda")
        self._boton.setToolTip("Borra el texto de búsqueda")

        capa = QHBoxLayout(self)
        capa.setContentsMargins(0, 0, 0, 0)
        capa.addWidget(self._etiqueta)
        capa.addWidget(self._caja)
        capa.addWidget(self._boton)

        self._caja.textChanged.connect(self._al_cambiar_texto)
        self._boton.clicked.connect(self.limpiar)
```

Los demás métodos son de una o dos líneas. Sustituye en cada uno el comentario `# TODO Paso 5` y el `pass` o el `raise NotImplementedError` por:

- `_al_cambiar_texto`: `self.busquedaCambiada.emit(texto)`;
- `limpiar`: `self._caja.clear()` y, debajo, `self._caja.setFocus()`;
- `_get_texto`: `return self._caja.text()`;
- `_set_texto`: `self._caja.setText(valor)`.

Para integrarlo en `main.py`: descomenta `from buscador import Buscador` (si tu `main.py` no tiene los `TODO`, añade esa línea con los demás imports); descomenta `self.configurar_buscador()`, justo después de `self.configurar_tabla()`; y añade este método dentro de la clase, en lugar del comentario `# TODO Paso 5` del final:

```python
    def configurar_buscador(self):
        self.buscador = Buscador()
        layout = self.ui.verticalLayout                       # el layout que contiene la tabla
        layout.insertWidget(layout.indexOf(self.ui.tblIncidencias), self.buscador)
        self.buscador.busquedaCambiada.connect(self.proxy.setFilterFixedString)
```

Añade también a `configurar_buscador()`, después de la conexión con `setFilterFixedString`, `self.buscador.busquedaCambiada.connect(self.mostrar_resultados)`, y este método para que la barra de estado diga cuántas incidencias quedan:

```python
    def mostrar_resultados(self, texto):
        if texto:
            self.statusBar().showMessage(f"{self.proxy.rowCount()} incidencias con «{texto}»")
        else:
            self.statusBar().clearMessage()
```

La ventana principal **no sabe** que dentro hay un `QLineEdit`: solo usa la señal. Por eso el mismo `Buscador` serviría, sin cambios, en el Editor de notas o en cualquier otra aplicación.

**Comprueba que…**

- al escribir «error» la tabla se filtra al momento, sin distinguir mayúsculas;
- «Limpiar» vuelve a mostrar todas y deja el foco en la caja; `Alt+B` lleva al buscador;
- con el filtro puesto, seleccionar y eliminar afectan a la incidencia correcta.

**Para pensar.** Busca «3»: puede salir alguna fila sin un 3 a la vista. ¿Por qué? Pista: `setFilterKeyColumn(-1)` busca en todas las columnas, también en la del ID, que está oculta. ¿Qué cambiarías para buscar solo en el título?

**Si te falla…**

- *`AttributeError: ... 'verticalLayout'`*: tu layout tiene otro nombre. Míralo en el Object Inspector de Designer o en `ui_bugtracker.py`.
- *El buscador sale en otro sitio*: `indexOf` devuelve -1 porque la tabla está dentro de otro layout. Usa ese layout.
- *`busquedaCambiada` no tiene `connect`*: la señal está declarada dentro de `__init__` y tiene que ir en el cuerpo de la clase.
- *`NotImplementedError`*: quedan `raise NotImplementedError` en `buscador.py`; sustitúyelos como dice la pista.
- *`NameError: name 'Buscador' is not defined`*: falta `from buscador import Buscador` en `main.py`.
- *`'VentanaPrincipal' object has no attribute 'configurar_buscador'`*: el método está fuera de la clase (revisa la sangría) o después de `if __name__ == "__main__":`.

---

## Paso 6 · Probar el componente con pytest-qt (martes, 35 min)

**Objetivo.** Ejecutar y entender las pruebas automáticas de `test_buscador.py` y añadir una.

**Mini-explicación.** **pytest** busca archivos `test_*.py` y ejecuta las funciones `test_*`; cada `assert` es una comprobación. **pytest-qt** añade `qtbot`, que crea la aplicación Qt, simula teclado y ratón (`keyClicks`, `mouseClick`) y espera señales (`waitSignal`). Cada prueba comprueba una sola cosa y su nombre dice cuál.

**Pista.** Con el entorno activado y desde la carpeta del proyecto:

```
python -m pytest -v
```

Lee las cuatro pruebas: valor por defecto, escribir cambia la propiedad, cambiar la propiedad emite la señal y el botón «Limpiar» borra el texto.

**Comprueba que…**

- salen las cuatro en verde con `PASSED` y al final `4 passed`; si alguna falla, el mensaje dice qué parte del `Buscador` falta;
- si cambias a propósito un valor esperado (por ejemplo, `"Error"` por `"Erorr"`), esa prueba falla y pytest explica por qué. Después déjalo bien;
- has escrito una **quinta prueba** propia para un valor límite y sale `5 passed`. Cópiala de una de las que ya hay, cámbiale el nombre y lo que comprueba. Por ejemplo, que los espacios no se recortan: `buscador.texto = "  Media  "` y `assert buscador.texto == "  Media  "`.

**Si te falla…**

- *`fixture 'qtbot' not found`*: falta pytest-qt en el entorno activo: `pip install -r requirements.txt`.
- *`ModuleNotFoundError: No module named 'buscador'`*: ejecuta `python -m pytest` desde la carpeta del proyecto.

### Guardar el estado, documentar y empaquetar (martes, 15 min)

Es lo que queda de la UD3, en las ampliaciones **A** (la aplicación recuerda el tamaño de la ventana y la última búsqueda con `QSettings`), **B** (`help(buscador.Buscador)` y un `README.md`) y **C** (`pyproject.toml` y `python -m build`). Fíjate en tres cosas: dónde se guarda el estado y cuándo se recupera (`closeEvent` y `__init__`), qué debe contar la documentación de un componente y qué hace falta para instalarlo en otro proyecto. Las haces el jueves 12, con lo que explica cada ampliación.

### Ampliaciones (jueves 12)

**A. Persistencia con `QSettings`.** Que la aplicación recuerde el tamaño de la ventana y la última búsqueda. Añade `QSettings` al import que ya existe (`from PySide6.QtCore import QSettings, QSortFilterProxyModel, Qt`), llama a `self.restaurar_estado()` al final de `__init__`, después de `self.actualizar_botones()` (necesita `self.buscador` ya creado), y añade estos dos métodos a la clase. En Windows, `QSettings` lo guarda en el registro, en `HKEY_CURRENT_USER\Software\DAM2\BugTracker`:

```python
    def restaurar_estado(self):
        ajustes = QSettings("DAM2", "BugTracker")
        geometria = ajustes.value("ventana/geometria")
        if geometria is not None:
            self.restoreGeometry(geometria)
        self.buscador.texto = ajustes.value("buscador/texto", "")

    def closeEvent(self, evento):
        ajustes = QSettings("DAM2", "BugTracker")
        ajustes.setValue("ventana/geometria", self.saveGeometry())
        ajustes.setValue("buscador/texto", self.buscador.texto)
        super().closeEvent(evento)
```

Ojo: al arrancar se recupera la última búsqueda, así que la tabla puede abrirse ya filtrada. Si parece que faltan incidencias, mira el buscador.

**B. Documentar el componente.** El docstring de `Buscador` ya es documentación: compruébalo con `python -c "import buscador; help(buscador.Buscador)"` (pulsa espacio para avanzar y `q` para salir). Escribe además un `README-buscador.md` corto: qué hace, tres líneas de ejemplo de uso, su propiedad, su método y su señal.

**C. Empaquetar el componente.** Para instalarlo con `pip` en otros proyectos se describe en un `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "buscador-dam"
version = "0.1.0"
description = "Componente Buscador para PySide6"
dependencies = ["PySide6-Essentials"]

[tool.setuptools]
py-modules = ["buscador"]
```

Guarda `pyproject.toml` en la carpeta del proyecto, junto a `buscador.py`. Instala `build` una vez con `pip install build`; `python -m build` crea en `dist/` el archivo `buscador_dam-0.1.0-py3-none-any.whl`, que se instala en otro proyecto con `pip install` y la ruta de ese archivo. Lo normal es tener el componente en su propia carpeta, separado de la aplicación.

**D. Otro componente: selector de prioridad.** Un `QWidget` con cinco botones de opción (Todas, Baja, Media, Alta, Crítica), la propiedad `prioridad` (por defecto «Todas») y la señal `prioridadCambiada(str)`. Para filtrar por la columna Prioridad sin romper el `Buscador`, usa un **segundo proxy** encadenado al primero: `self.proxy2 = QSortFilterProxyModel(self)`, `self.proxy2.setSourceModel(self.proxy)`, `self.proxy2.setFilterKeyColumn(3)` y `self.ui.tblIncidencias.setModel(self.proxy2)` Crea `proxy2` al final de `configurar_tabla()`, antes de que `__init__` conecte `selectionChanged`. En `id_seleccionado`, la traducción se hace dos veces: `fila = self.proxy.mapToSource(self.proxy2.mapToSource(filas[0])).row()`. Para los cinco botones usa `QRadioButton` y un `QButtonGroup`. Con «Todas», filtra con el texto vacío. Pruébalo con pytest-qt como el buscador.

---

## Paso 7 · Prueba de usabilidad en parejas (martes, 25 min)

**Objetivo.** Comprobar con otra persona si tu BugTracker es fácil de usar y accesible, y proponer mejoras.

**Pista.** Intercambiad los ordenadores. Quien prueba **no recibe ayuda** y piensa en voz alta. Quien observa apunta esta tabla en el `notas.md` de quien prueba:

| Tarea | ¿La consiguió? (sí / con ayuda / no) | Problemas observados | Heurística o pauta afectada | Mejora propuesta |
|---|---|---|---|---|
| 1. Crea la incidencia «La ventana no se redimensiona», tipo Error, prioridad Alta, **sin usar el ratón** |  |  |  |  |
| 2. Muestra solo las incidencias que contengan «error» |  |  |  |  |
| 3. Elimina una incidencia y cancela en el último momento; luego elimínala de verdad |  |  |  |  |
| 4. Intenta guardar una incidencia sin título. ¿Entiendes el mensaje? |  |  |  |  |

Al final, elige **las dos mejoras más importantes** y explica por qué. Compáralas con tu evaluación del paso 1 (las heurísticas y pautas están en el paso 1 de la 1.ª parte, `2026_11_02-06/clase/proyecto-DI.md`): ¿la otra persona encontró problemas que tú no viste?

**Comprueba que…** la tabla está completa y cada problema está relacionado con una heurística o una pauta.

---

## Paso 8 · Reflexión: interfaces naturales (martes, 15 min)

**Objetivo.** Empezar a pensar en otras formas de interacción, que veremos en la UD4.

**Mini-explicación.** Una **interfaz natural** usa formas de comunicarse propias de las personas: **voz**, **gestos**, **movimiento del cuerpo**, **tacto**, **mirada** o **realidad aumentada**. Pueden mejorar la accesibilidad (dictar una incidencia si no puedes usar las manos), pero tienen **límites**: ruido, privacidad, precisión del reconocimiento, cansancio, luz o idioma. Por eso conviene ofrecer siempre una **alternativa** (teclado, ratón).

**Pista.** En `notas.md`, en tres o cuatro líneas:

1. ¿Qué interfaz natural añadirías al BugTracker y para qué (por ejemplo, dictar la descripción)?
2. ¿A quién le ayudaría?
3. ¿Qué límite o problema podría tener y qué alternativa ofrecerías?

**Comprueba que…** `notas.md` responde a las tres preguntas.

---

## Entrega

Qué se entrega esta semana y cuándo: [`entrega.md`](entrega.md).

## Cómo comprobar que está todo bien

- [ ] El `Buscador` filtra la tabla y tiene propiedad `texto`, método `limpiar()` y señal `busquedaCambiada`.
- [ ] `python -m pytest -v` da `5 passed` con tu prueba.
- [ ] Prueba de usabilidad hecha, con dos mejoras propuestas.
- [ ] Reflexión de la UD4 escrita.
