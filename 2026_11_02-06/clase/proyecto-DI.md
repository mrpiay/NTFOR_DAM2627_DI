# DI · Proyecto guiado «Mejora tu BugTracker» · 1.ª parte

## Punto de partida

**Hasta esta fecha, según la programación del módulo, deberíais haber estudiado:**

- **UD1 · Diseño de interfaces, experiencia de usuario y accesibilidad**, **UD2 · Desarrollo de interfaces gráficas con PySide6 y Qt Designer** y **UD3 · Creación de componentes visuales reutilizables**, completas.
- **UD4 · Interfaces naturales y multimodales**, empezada.

**La idea.** Esta semana es un **punto de control** para **ponernos al día con la programación, en la medida de lo posible**: un proyecto que repasa lo que se debería haber dado hasta ahora, continuando vuestro BugTracker de la Práctica 6 (o recuperándolo con la plantilla, si no lo tenéis): se mejora con la UD1, se completa con lo que falta de la UD2 y se le añade un componente de la UD3. Lo que ya sabéis, lo afianzáis; lo que no se llegó a dar, **se explica en el paso donde aparece**. El proyecto tiene **dos partes**: esta semana, los pasos 0 a 4 (UD1 y UD2); la semana del 9 al 13 de noviembre, los pasos 5 a 8 (UD3 y UD4).

**Usa la IA como guía, no para que lo haga por ti.** Pídele los **pasos necesarios** para implementar cada cosa y que te explique lo que no entiendas; **el código lo pones tú en tu proyecto**, aunque sea copiando y pegando, sabiendo **dónde** lo pones y **para qué**: es la única forma de familiarizarte con tu entorno. El objetivo es que lo que hagas **funcione y cumpla los requisitos** de cada paso («Comprueba que…») y que sepas **dónde está cada cosa y qué habría que tocar para cambiar o añadir algo**: es lo que te van a pedir después.

**El objetivo es entender cada paso:** es lo que necesitas para responder los cuestionarios de autoevaluación y preparar la prueba escrita.

**Evaluación continua.** Algunas semanas hay una **prueba escrita, en papel,** en las dos últimas sesiones del último día de clase, después de que se publiquen las soluciones de lo que entra; se avisa con antelación. La primera es el **jueves 19 de noviembre**, sobre **las dos partes del proyecto** (pasos 0 a 8): Qt Designer y `pyside6-uic`, PySide6 (señales y slots, acciones, menús y diálogos con validación), Model/View, accesibilidad, el componente reutilizable `Buscador` y sus pruebas con pytest-qt, y el propio proyecto.

**Y la UD2.** Su nota sale de su entrega y su examen de octubre. Si te falta alguna de las dos, la sustituyen las preguntas de la prueba escrita del jueves 19 de noviembre sobre los pasos 2 a 4 de este proyecto, corregidas con los criterios de la UD2.

Del 3 al 6 de noviembre. Cada paso trae una mini-explicación, una pista y qué hacer si algo falla.

## Con qué trabajas

- **El proyecto**: copia la carpeta `plantilla` con el nombre `bugtracker`. Es un BugTracker de la Práctica 6 terminado, con los mismos nombres: `bugtracker.ui`, `ui_bugtracker.py`, `main.py`, `bd.py`, `txtTitulo`, `cmbTipo`, `cmbPrioridad`, `cmbEstado`, `txtDescripcion`, `btnAnadir`, `btnModificar`, `btnEliminar`, `btnLimpiar` y `tblIncidencias`.
- **Si tienes tu propio BugTracker de la Práctica 6**: cambia el nombre de su carpeta a `bugtracker-anterior` y guárdalo para consultarlo. El proyecto se hace en `bugtracker`, desde la plantilla.

Qué es cada archivo y en qué paso lo tocas (`bugtracker.db`, la base de datos, se crea sola al ejecutar):

| Archivo | Qué es | Paso en que lo tocas |
|---|---|---|
| `bugtracker.ui` | ventana principal (`pyside6-designer bugtracker.ui`) | 2, 3 y 4 |
| `ui_bugtracker.py` | generado con `pyside6-uic bugtracker.ui -o ui_bugtracker.py`; no se edita a mano | se regenera |
| `bd.py` | acceso a SQLite (todo el SQL está aquí) | ninguno |
| `main.py` | ventana principal y lógica | 3, 4 y 5 |
| `dialogo.py` | diálogo «Nueva incidencia» | 3 |
| `buscador.py` | componente reutilizable `Buscador` | 5 |
| `test_buscador.py` | pruebas con pytest-qt, ya escritas | 6 |
| `datos_ejemplo.py` | incidencias de prueba | ninguno |

En la plantilla, los comentarios `# TODO Paso N` marcan dónde se cambia o se añade código en cada paso. La aplicación arranca desde el principio.

Lo que escribas (la evaluación y el boceto del paso 1) va en `notas.md`, un archivo de texto en la carpeta de tu proyecto.

## Qué se repasa

| Unidad | Qué repasamos | Pasos |
|---|---|---|
| UD1 · Diseño, UX y accesibilidad | heurísticas de Nielsen, accesibilidad (contraste, teclado, etiquetas, mensajes), wireframe | 1 y 2 |
| UD2 · PySide6 y Qt Designer | Qt Designer y `pyside6-uic`, señales y slots, acciones, menús, barra de herramientas, diálogos y validación, SQLite, Model/View | 2, 3 y 4 |

La UD3 y la UD4 (pasos 5 a 8) van en la 2.ª parte.

## Plan de la semana

Cada sesión dura 50 minutos.

| Día | Sesión | Qué hacemos |
|---|---|---|
| Martes 3 | 10:10 | Dónde deberíamos estar (el punto de partida), dónde estamos de verdad (puesta en común), qué necesitamos para seguir (contenidos y software) y qué vamos a hacer esta semana (30 min). Presentación del proyecto y **Paso 0** (preparar, 20 min); quien tenga que instalar algo, lo hace mientras. |
| Martes 3 | 11:00 | **Paso 0**: cómo está hecho el BugTracker (15 min). **Paso 1** (evaluación heurística y de accesibilidad, 35 min). |
| Martes 3 | 12:10 | **Paso 2** (mejoras de accesibilidad en Designer, 30 min) y empezar el **Paso 3** (20 min). |
| Miércoles 4 | 11:00 | **Paso 3** (acciones, menú, barra de herramientas y diálogo con validación; lo nuevo es la validación) y empezar el **Paso 4**. |
| Miércoles 4 | 12:10 | **Paso 4** (de `QTableWidget` a Model/View). |
| Jueves 5 | 08:30 | Terminar los pasos 3 y 4. |
| Jueves 5 | 09:20 | Terminar el **Paso 4**. Cierre: lo que hemos conseguido y qué viene, la 2.ª parte. |

**El ritmo:** el proyecto se hace en clase, paso a paso, siguiendo el plan de sesiones. No te saltes pasos: antes de pasar al siguiente, la aplicación debe arrancar.

**Los pasos se hacen en orden**, cada uno en la sesión que le toca según el plan de la semana: cada paso usa lo del anterior.

Cada paso tiene **Objetivo**, **Mini-explicación** (lo justo), **Pista**, **Comprueba que…** y **Si te falla…**.

---

## Paso 0 · Preparar (martes, 35 min)

**Objetivo.** Tener tu carpeta de trabajo con su entorno virtual y la aplicación arrancando.

**Pista.** Instala antes lo que indica [`software-DI.md`](software-DI.md). Descarga el repositorio del módulo (https://github.com/mrpiay/NTFOR_DAM2627_DI → *Code → Download ZIP*); en `2026_11_02-06/clase` está la carpeta `plantilla`. Prepara la carpeta como se explica en «Con qué trabajas», en una **ruta corta y fuera de OneDrive**, por ejemplo `C:\dam\di\bugtracker`. El entorno virtual tiene archivos con rutas muy largas: dentro de OneDrive o del Escritorio la instalación puede fallar. Ábrela en VS Code y, en la terminal (PowerShell):

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python datos_ejemplo.py
python main.py
```

`datos_ejemplo.py` añade cinco incidencias de prueba; ejecútalo una sola vez. En VS Code elige el intérprete del entorno: `Ctrl+Mayús+P` → «Python: Select Interpreter» → el de `.venv`.

**Comprueba que…**

- en la terminal aparece `(.venv)` al principio de la línea;
- `python main.py` abre el BugTracker con las incidencias de ejemplo y puedes añadir, modificar y eliminar;
- `python -m pytest -v` se ejecuta, en sus primeras líneas sale `plugins: qt-…` (pytest-qt está instalado) y al final da **4 failed**. Es lo esperado: las pruebas son del componente del paso 5, que aún no existe.

**Si te falla…**

- *«La ejecución de scripts está deshabilitada»*: ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activar, o usa la terminal «Command Prompt» con `.venv\Scripts\activate.bat`.
- *`python` no se reconoce*: reinstala Python marcando **Add python.exe to PATH** (ver [`software-DI.md`](software-DI.md)) y abre una terminal nueva.
- *`WinError 206` («el nombre del archivo o la extensión es demasiado largo») o, después, `fixture 'qtbot' not found`*: la carpeta está en una ruta demasiado larga o en OneDrive. Bórrala, cópiala a `C:\dam\di\` y repite los comandos desde `python -m venv .venv`.
- *pip falla o no hay red*: haz mientras el paso 1, que no necesita instalar nada, y repite `pip install -r requirements.txt` cuando tengas red.
- *Tu BugTracker no arranca*: usa la plantilla. No pierdas la sesión arreglando la práctica.

### Cómo está hecho el BugTracker (15 min)

Es la Práctica 6 (SQLite), la base de todo el proyecto. Si no la hiciste, aquí la entiendes; si la hiciste, compárala con la tuya. Abre `bd.py` y `main.py` y recórrelos con esta tabla; no hay que escribir nada.

| Dónde | Qué hace | Qué hay que saber |
|---|---|---|
| `bd.py` · `conectar()` | Abre la base de datos `bugtracker.db` | `sqlite3` viene con Python; `row_factory = sqlite3.Row` permite leer `fila["titulo"]` |
| `bd.py` · `crear_bd()` | Crea la tabla `incidencias` si no existe | `CREATE TABLE IF NOT EXISTS`; `commit()` guarda los cambios |
| `bd.py` · `obtener_…`, `insertar_…`, `actualizar_…`, `eliminar_…` | Las cuatro operaciones: leer, añadir, modificar y borrar (CRUD) | `SELECT`, `INSERT`, `UPDATE`, `DELETE` con `?` en vez de pegar los datos en el texto: evita errores e inyección SQL |
| `main.py` · `__init__` | Carga la interfaz y conecta los botones | `clicked.connect(self.anadir_incidencia)`: señal → slot |
| `main.py` · `cargar_incidencias()` | Pide las filas a `bd.py` y rellena la tabla | El modo «a mano» con `QTableWidget`; en el Paso 4 lo cambiamos por Model/View |
| `main.py` · `anadir_…`, `modificar_…`, `eliminar_…` | Leen el formulario, llaman a `bd.py` y recargan | Si `bd.py` falla, `main.py` muestra el error con `QMessageBox` |

**La regla de la plantilla:** `main.py` nunca contiene SQL y `bd.py` nunca usa widgets. ¿Por qué conviene separarlos así? ¿Qué habría que cambiar si mañana los datos estuvieran en otra base de datos?

---

## Paso 1 · Evaluación heurística y de accesibilidad (martes, 35 min)

**Objetivo.** Revisar tu BugTracker (o la plantilla) como lo haría una persona experta en usabilidad y hacer una lista de mejoras.

**Mini-explicación.**

- **UI** es lo que se ve y se toca; **UX** es cómo le va a quien la usa: si consigue lo que quiere, rápido y sin frustrarse.
- Una **evaluación heurística** consiste en recorrer la interfaz con una lista de principios y apuntar dónde no se cumplen. Algunas **heurísticas de Nielsen**:
  - *Visibilidad del estado del sistema*: la aplicación dice lo que pasa («Incidencia añadida» en la barra de estado).
  - *Prevención de errores*: confirmar antes de eliminar; desactivar «Modificar» si no hay nada seleccionado.
  - *Control y libertad*: poder cancelar o salir («Limpiar», «Cancelar»).
  - *Consistencia y estándares*: menú «Archivo», atajos habituales (`Ctrl+N`, `Ctrl+S`, `Ctrl+Q`).
  - *Reconocer mejor que recordar*: acciones visibles en menús y botones.
  - *Ayudar a reconocer y corregir errores*: mensajes que dicen qué ha pasado y cómo arreglarlo.
- **Accesibilidad básica**:
  - contraste suficiente: en WCAG nivel AA, al menos **4,5:1** para texto normal (compruébalo con WebAIM Contrast Checker);
  - todo se puede hacer con el **teclado**, con un orden de tabulación lógico;
  - cada campo tiene una **etiqueta asociada** (*buddy*) y, si la etiqueta lleva `&`, un atajo `Alt+letra` que lleva al campo;
  - la información **no depende solo del color**;
  - mensajes **breves y claros**.

**Pista.** Crea `notas.md` en la carpeta de tu proyecto y recorre tu aplicación **sin ratón** durante cinco minutos. Después escribe en `notas.md` una tabla con **al menos cinco problemas**:

| Problema | Dónde | Heurística o pauta | Mejora propuesta |
|---|---|---|---|
| Con `Tab` no se sale de la descripción: se escribe un tabulador | `txtDescripcion` | uso con teclado | activar `tabChangesFocus` |
| `Alt+T` no lleva al título | etiqueta «Título:» | etiquetas y atajos | `&Título:` con buddy `txtTitulo` |
| … | … | … | … |

Cosas que conviene mirar: el orden de tabulación, si las etiquetas tienen atajo y *buddy*, si hay atajos repetidos (por ejemplo, dos etiquetas o botones con la misma letra después de `&`), si se sabe qué campo es obligatorio, si los mensajes se entienden y si las acciones tienen atajo.

Por último, haz un **boceto rápido** (wireframe, en papel o en diagrams.net) de cómo quedará la ventana al final del proyecto: menú «Archivo», barra de herramientas, buscador encima de la tabla.

**Comprueba que…** tienes al menos cinco problemas, cada uno con su heurística o pauta y una mejora, y el boceto.

**Si te falla…** *No te acuerdas de las heurísticas*: usa la lista de arriba; con cinco problemas bien justificados basta.

---

## Paso 2 · Mejoras de accesibilidad en Designer (martes, 30 min)

**Objetivo.** Aplicar en `bugtracker.ui` mejoras de accesibilidad de tu lista del paso 1.

**Mini-explicación.** `ui_bugtracker.py` se genera a partir de `bugtracker.ui`: los cambios se hacen siempre en Designer y luego se regenera. Si editas `ui_bugtracker.py` a mano, lo pierdes en la siguiente generación.

**Pista.** Abre el diseño con `Start-Process .venv\Scripts\pyside6-designer.exe -ArgumentList bugtracker.ui -WindowStyle Hidden` (así la terminal queda libre; paso a paso y con capturas, en [`designer-regenerar.md`](designer-regenerar/designer-regenerar.md)) y haz estas cuatro mejoras:

1. **Etiquetas con atajo y buddy.** Cambia el texto de las etiquetas a `&Título (obligatorio):`, `T&ipo:`, `&Prioridad:`, `E&stado:`, `&Descripción:`. Después, *Edit → Edit Buddies* y arrastra de cada etiqueta a su campo. Pon también atajo a los botones: `A&ñadir` (la A queda para el menú Archivo del paso 3), `&Modificar`, `&Eliminar` y `&Limpiar`.
2. **Tabulación en la descripción.** Selecciona `txtDescripcion` y marca `tabChangesFocus`.
3. **Orden de tabulación.** *Edit → Edit Tab Order*: título, tipo, prioridad, estado, descripción, botones y tabla. En `tblIncidencias`, desmarca `tabKeyNavigation`, para que `Tab` salga de la tabla (dentro de ella te mueves con las flechas).
4. **Ayudas.** `toolTip` en los botones y `accessibleName` = «Lista de incidencias» en la tabla.

Guarda y regenera:

```
pyside6-uic bugtracker.ui -o ui_bugtracker.py
```

**Comprueba que…** (sin ratón)

- `Alt+T` lleva al título y `Alt+D` a la descripción;
- `Tab` recorre los campos en orden, sale de la descripción y también sale de la tabla;
- `python main.py` sigue funcionando igual que antes.

**Si te falla…**

- *El atajo no hace nada*: falta el *buddy* o has puesto la `&` en el campo y no en la etiqueta.
- *No ves los cambios*: no has regenerado `ui_bugtracker.py` o no has guardado el `.ui`.
- *Designer no abre*: aplica la mejora desde `main.py`, después de `setupUi`. Por ejemplo: `self.ui.txtDescripcion.setTabChangesFocus(True)` o `self.ui.lblTitulo.setBuddy(self.ui.txtTitulo)`.

---

## Paso 3 · Acciones, menú, barra de herramientas y diálogo (martes y miércoles, 55 min)

**Objetivo.** Añadir las acciones Nueva, Guardar, Eliminar y Salir con atajos, en un menú y en una barra de herramientas, y un diálogo «Nueva incidencia» que valida los datos.

**Mini-explicación.**

- Una **`QAction`** es una orden con texto, atajo y `statusTip`. La misma acción se pone en el menú y en la barra de herramientas y se programa una sola vez, como en el Editor de notas (Práctica 5). Su señal es `triggered`.
- Un **diálogo modal** bloquea la ventana principal hasta que se cierra. `exec()` lo muestra y devuelve verdadero si se aceptó. Para validar, Aceptar no cierra directamente: llama a un método que comprueba los datos y solo entonces hace `accept()`.

**Pista.**

1. En Designer, abre el **Action Editor** (*View → Action Editor*) y crea estas acciones con su botón *New*:

   | objectName | text | shortcut | statusTip |
   |---|---|---|---|
   | `actionNueva` | `&Nueva incidencia...` | `Ctrl+N` | Abre el diálogo para crear una incidencia |
   | `actionGuardar` | `&Guardar` | `Ctrl+S` | Añade o modifica la incidencia del formulario |
   | `actionEliminar` | `&Eliminar` | `Supr` | Elimina la incidencia seleccionada |
   | `actionSalir` | `&Salir` | `Ctrl+Q` | Cierra la aplicación |

   En el editor de atajos de Designer pulsa la combinación; la tecla Supr aparece como `Del`.

2. Crea el menú: doble clic en «Type Here» de la barra de menús y escribe `&Archivo`. Mete cada acción arrastrándola desde el Action Editor al menú, en este orden: Nueva, Guardar, Eliminar, un separador (*Add Separator*) y Salir.
3. Añade una barra de herramientas (clic derecho en la ventana → *Add Tool Bar*), con `objectName = toolBarPrincipal` y `toolButtonStyle = ToolButtonTextOnly`, y arrastra a ella Nueva, Guardar y Eliminar. Regenera `ui_bugtracker.py`.
4. En `main.py`, completa los `TODO Paso 3`. Descomenta el import del diálogo. Las cuatro conexiones van en `__init__`, donde está `# TODO Paso 3: conecta las QAction…`. Los métodos `guardar` y `nueva_incidencia` van donde está `# TODO Paso 3: añade aquí los slots`, debajo de `actualizar_botones()`:

```python
        self.ui.actionNueva.triggered.connect(self.nueva_incidencia)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionEliminar.triggered.connect(self.eliminar_incidencia)
        self.ui.actionSalir.triggered.connect(self.close)

    def guardar(self):
        if self.id_seleccionado() is None:
            self.anadir_incidencia()
        else:
            self.modificar_incidencia()

    def nueva_incidencia(self):
        dialogo = DialogoIncidencia(self)
        if not dialogo.exec():          # falso si se canceló
            return
        try:
            bd.insertar_incidencia(*dialogo.datos())   # el * reparte los cinco datos
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido guardar la incidencia.")
            return
        self.cargar_incidencias()
        self.statusBar().showMessage("Incidencia añadida", 3000)
```

   En `actualizar_botones()`, activa o desactiva también `self.ui.actionEliminar`.

5. En `dialogo.py`, completa `validar()`: si el título está vacío, `QMessageBox.warning(...)`, foco en `self.txtTitulo` y `return`; si tiene más de 100 caracteres, otro aviso que diga cuántos tiene.
6. **Editar con el mismo diálogo.** El diálogo también sirve para editar, porque acepta una incidencia: `DialogoIncidencia(self, incidencia)`. En `__init__`, conecta el doble clic de la tabla: `self.ui.tblIncidencias.doubleClicked.connect(self.editar_incidencia)`. Y añade este método junto a los otros dos:

```python
    def editar_incidencia(self):
        id_incidencia = self.id_seleccionado()
        if id_incidencia is None:
            return
        incidencia = bd.obtener_incidencia(id_incidencia)
        dialogo = DialogoIncidencia(self, incidencia)
        if not dialogo.exec():
            return
        try:
            bd.actualizar_incidencia(id_incidencia, *dialogo.datos())
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido modificar la incidencia.")
            return
        self.cargar_incidencias()
        self.statusBar().showMessage("Incidencia modificada", 3000)
```

**Comprueba que…** (sin ratón)

- `Alt+A` abre el menú Archivo y los atajos aparecen junto a cada acción;
- al pasar por una acción del menú, su `statusTip` sale en la barra de estado;
- `Ctrl+N` abre el diálogo; `Tab` recorre sus campos; Aceptar con el título vacío avisa y el diálogo **no** se cierra; `Esc` cancela sin guardar;
- `Ctrl+S` sin selección añade y, con una incidencia seleccionada, la modifica;
- «Eliminar» de la barra está desactivado si no hay selección y, con selección, pide confirmación;
- doble clic en una incidencia abre el diálogo con sus datos y guarda los cambios.

**Si te falla…**

- *`AttributeError: ... has no attribute 'actionNueva'`*: el `objectName` en Designer es otro (por ejemplo, `actionNueva_incidencia`) o no has regenerado.
- *El diálogo se cierra con el título vacío*: has conectado `accepted` a `self.accept` en vez de a `self.validar`, o falta el `return`.
- *La acción se ejecuta al arrancar*: has escrito `connect(self.guardar())` con paréntesis.
- *Designer no te funciona*: crea las acciones en código, después de `setupUi` y con `from PySide6.QtGui import QAction`: `self.ui.actionNueva = QAction("&Nueva incidencia...", self)`, `self.ui.actionNueva.setShortcut("Ctrl+N")`, `self.menuBar().addMenu("&Archivo").addAction(self.ui.actionNueva)` y `self.addToolBar("Principal").addAction(self.ui.actionNueva)`. Con el mismo nombre que en Designer (`self.ui.…`), el resto del paso funciona igual.


---

## Paso 4 · De `QTableWidget` a Model/View (miércoles, 65 min)

**Objetivo.** Mostrar las incidencias en un `QTableView` a través de un modelo y un proxy que permitirá filtrar y ordenar.

**Mini-explicación.** Con `QTableWidget` los datos viven **dentro** del widget: los metes celda a celda con `setItem`. En **Model/View** se separan:

```
SQLite -> bd.py -> MODELO (QStandardItemModel) -> PROXY (QSortFilterProxyModel) -> VISTA (QTableView)
```

- El **modelo** guarda filas y columnas; la **vista** solo las dibuja y gestiona la selección.
- El **proxy** se pone en medio para **filtrar y ordenar sin tocar los datos**. Lo usará el buscador del paso 5.
- Lo que se selecciona en la vista es una fila **del proxy**. Para saber qué fila es en el modelo se traduce con `mapToSource`.

Usamos `QStandardItemModel`, rellenado con `bd.obtener_incidencias()`: así se mantiene la regla de la Práctica 6 (main.py sin SQL, bd.py sin widgets). Existe también `QSqlTableModel` (módulo `QtSql`), que lee la tabla directamente, pero se salta `bd.py` y obliga a cambiar la forma de conectar con la base de datos.

**Pista.**

1. En Designer, clic derecho en `tblIncidencias` → *Morph into* → `QTableView`. Conserva el nombre, el layout y las propiedades de selección. Regenera `ui_bugtracker.py`. A partir de aquí, `main.py` no arrancará hasta que termines este paso.
2. En `main.py`, sustituye las dos líneas `# TODO Paso 4: …` de los imports por estas dos, sin espacios delante:

```python
from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
```

   En la línea de `PySide6.QtWidgets`, borra `QTableWidgetItem` y añade `QHeaderView`. Añade el método `configurar_tabla()` justo antes de `cargar_incidencias()` y llámalo en `__init__` **antes** de las conexiones (`self.configurar_tabla()`, donde está `# TODO Paso 4`):

```python
    def configurar_tabla(self):
        self.modelo = QStandardItemModel(0, 5, self)
        self.modelo.setHorizontalHeaderLabels(["ID", "Título", "Tipo", "Prioridad", "Estado"])
        self.proxy = QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.modelo)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.proxy.setFilterKeyColumn(-1)              # busca en todas las columnas
        tabla = self.ui.tblIncidencias
        tabla.setModel(self.proxy)
        tabla.setColumnHidden(0, True)                   # después de setModel
        tabla.setSortingEnabled(True)
        tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)    # el título ocupa el sitio libre
        tabla.horizontalHeader().setSortIndicator(-1, Qt.SortOrder.AscendingOrder)          # sin orden hasta pulsar una cabecera
```

3. Cambia la señal de selección:

```python
        self.ui.tblIncidencias.selectionModel().selectionChanged.connect(self.cargar_seleccion)
```

4. En `cargar_incidencias()`, en lugar de `setRowCount(0)` e `insertRow` + `setItem`:

```python
        self.modelo.removeRows(0, self.modelo.rowCount())
        for incidencia in incidencias:
            celdas = []
            for campo in ("id", "titulo", "tipo", "prioridad", "estado"):
                celda = QStandardItem(str(incidencia[campo]))
                celda.setEditable(False)
                celdas.append(celda)
            self.modelo.appendRow(celdas)
```

5. En `id_seleccionado()`:

```python
        filas = self.ui.tblIncidencias.selectionModel().selectedRows()
        if not filas:
            return None
        fila = self.proxy.mapToSource(filas[0]).row()   # de la vista (proxy) al modelo
        return int(self.modelo.item(fila, 0).text())
```

**Comprueba que…**

- aparecen las incidencias y la columna ID no se ve;
- al pulsar en una cabecera, la tabla se ordena por esa columna;
- seleccionar, añadir, modificar, eliminar y limpiar funcionan como en la Práctica 6;
- después de ordenar, al eliminar desaparece la incidencia que habías seleccionado y no otra.

**Si te falla…**

- *`'QTableView' object has no attribute 'setRowCount'`* (o `setItem`, `selectedItems`): queda código de `QTableWidget`. En Model/View los datos van al **modelo**.
- *`'NoneType' object has no attribute 'selectionChanged'`*: conectas la señal antes de `setModel`. Llama a `configurar_tabla()` primero.
- *Se borra otra incidencia*: falta `mapToSource`.
- *La prioridad se ordena como texto* (Alta, Baja, Crítica, Media): es normal, el orden es alfabético. Para ordenarla por importancia, guarda en cada celda de prioridad un número con `setData(n, Qt.ItemDataRole.UserRole)` y usa `self.proxy.setSortRole(Qt.ItemDataRole.UserRole)`.

---

## Entrega

Qué se entrega esta semana y cuándo: [`entrega.md`](entrega.md).

## Cómo comprobar que está todo bien

- [ ] La evaluación tiene al menos cinco problemas con su heurística o pauta, y hay boceto.
- [ ] Al menos dos mejoras de accesibilidad aplicadas en Designer (buddies y atajos, tabulación, ayudas).
- [ ] Menú Archivo y barra de herramientas con las mismas `QAction`; atajos `Ctrl+N`, `Ctrl+S`, `Supr` y `Ctrl+Q`.
- [ ] El diálogo «Nueva incidencia» se usa entero con teclado, valida el título y da mensajes claros.
- [ ] La tabla es un `QTableView` con modelo y proxy; se ordena por columnas; el ID no se ve.
- [ ] Seleccionar, modificar y eliminar afectan a la incidencia correcta, también después de ordenar.
