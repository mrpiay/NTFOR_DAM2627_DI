# DI · Proyecto guiado «Mejora tu BugTracker» · 1.ª parte

## Punto de partida

**Hasta esta fecha, según la programación del módulo, se tendrían que haber estudiado:**

- **UD1 · Diseño de interfaces, experiencia de usuario y accesibilidad**, **UD2 · Desarrollo de interfaces gráficas con PySide6 y Qt Designer** y **UD3 · Creación de componentes visuales reutilizables**, completas.
- **UD4 · Interfaces naturales y multimodales**, empezada.

**La idea.** Esta semana es un **punto de control** para **ponernos al día con la programación, en la medida de lo posible**: un proyecto que repasa lo que se debería haber dado hasta ahora, partiendo de la plantilla, un BugTracker de la Práctica 6 terminado: se mejora con la UD1, se completa con lo que falta de la UD2 y se le añade un componente de la UD3. Lo que ya sabéis, lo afianzáis; lo que no se llegó a dar, **se explica en los apuntes de la semana, enlazados en el paso donde aparece**. El proyecto tiene **dos partes**: esta semana, los pasos 0 a 4 (UD1 y UD2); la semana del 9 al 13 de noviembre, los pasos 5 a 11 (UD3 y UD4).

**Usa la IA como guía, no para que lo haga por ti.** Pídele los **pasos necesarios** para implementar cada cosa y que te explique lo que no entiendas; **el código lo pones tú en tu proyecto**, aunque sea copiando y pegando, sabiendo **dónde** lo pones y **para qué**: es la única forma de familiarizarte con tu entorno. El objetivo es que lo que hagas **funcione y cumpla los requisitos** de cada paso («Comprueba que…») y que sepas **dónde está cada cosa y qué habría que tocar para cambiar o añadir algo**: es lo que te van a pedir después.

**El objetivo es entender cada paso:** es lo que necesitas para responder los cuestionarios y preparar los exámenes.

**Evaluación.** Esta actividad guiada (**A1**) se evalúa con su lista de cotejo: cada «Comprueba que…» se cumple o no. El cuestionario de la semana (**C1**) se entrega hasta el lunes 16 de noviembre, junto con el de la otra semana. El **miércoles 2 de diciembre** hay un examen parcial, **P1**, en papel, con todo lo de la 1ª evaluación que no evaluó Julia, también las dos partes de esta actividad (pasos 0 a 11): Qt Designer y `pyside6-uic`, PySide6 (señales y slots, acciones, menús y diálogos con validación), Model/View, accesibilidad, el componente reutilizable `Buscador` y sus pruebas con pytest-qt; y los apuntes de la UD1 a la UD3. Qué entra y cuánto vale cada parte: [1ª evaluación](../../programacion/1a-evaluacion.md).

El proyecto se hace del 3 al 5 de noviembre. Cada paso trae una pista, enlaces a los apuntes y qué hacer si algo falla.

## Con qué trabajas

- **El proyecto**: copia la carpeta `plantilla` con el nombre `bugtracker`. Es un BugTracker de la Práctica 6 terminado, con los mismos nombres: `bugtracker.ui`, `ui_bugtracker.py`, `main.py`, `bd.py`, `txtTitulo`, `cmbTipo`, `cmbPrioridad`, `cmbEstado`, `txtDescripcion`, `btnAnadir`, `btnModificar`, `btnEliminar`, `btnLimpiar` y `tblIncidencias`.
- **Si tienes tu propio BugTracker de la Práctica 6**: cambia el nombre de su carpeta a `bugtracker-anterior` y guárdalo para consultarlo. El proyecto se hace en `bugtracker`, desde la plantilla.

Qué es cada archivo y en qué paso lo tocas (`bugtracker.db`, la base de datos, se crea sola al ejecutar):

| Archivo | Qué es | Paso en que lo tocas |
|---|---|---|
| `bugtracker.ui` | diseño de la ventana principal; se abre con Qt Designer | 2, 3 y 4 |
| `ui_bugtracker.py` | generado con `pyside6-uic bugtracker.ui -o ui_bugtracker.py`; no se edita a mano | se regenera |
| `bd.py` | acceso a SQLite (todo el SQL está aquí) | ninguno |
| `main.py` | ventana principal y lógica | 3, 4 y 5 |
| `dialogo.py` | diálogo «Nueva incidencia» | 3 |
| `buscador.py` | componente reutilizable `Buscador` | 5 |
| `test_buscador.py` | pruebas con pytest-qt, ya escritas | 6 |
| `datos_ejemplo.py` | incidencias de prueba | ninguno |

En la plantilla, los comentarios `# TODO Paso N` marcan dónde se cambia o se añade código en cada paso. La aplicación arranca desde el principio.

Lo que escribas (la evaluación y el boceto del paso 1) va en `notas.md`, un archivo de texto en la carpeta de tu proyecto. Para crearlo, en el panel de archivos de VS Code pulsa el icono *New File* (junto al nombre de la carpeta) y escribe `notas.md`.

## Las herramientas

Todo se hace en **Visual Studio Code** (VS Code), con su terminal. Cómo instalar Python y VS Code: [`software-DI.md`](software-DI.md); lo demás se instala en el paso 0.

| Herramienta | Qué es | Cómo se usa | Pasos |
|---|---|---|---|
| **VS Code** | El editor, con terminal integrada | *File > Open Folder…* abre la carpeta. La terminal, abajo: *Terminal > New Terminal* (`Ctrl+ñ` con teclado español), de tipo **PowerShell** | Todos |
| **Python** y el **entorno virtual** (`.venv`) | Python ejecuta la aplicación; el entorno virtual es una carpeta (`.venv`) con las librerías de este proyecto, separadas de las de otros proyectos | Se crea y se activa en el paso 0. Activado, la terminal muestra `(.venv)` al principio de la línea | Todos |
| **PySide6** | La librería de interfaces gráficas ([UD2, apartado 1](../apuntes/UD2-pyside6-y-qt-designer.md#1-herramientas-y-librerías)) | Se importa en el código: `from PySide6.QtWidgets import …` | Todos |
| **Qt Designer** | El programa para diseñar la ventana; guarda el diseño en `bugtracker.ui` | `Start-Process .venv\Scripts\pyside6-designer.exe -ArgumentList bugtracker.ui -WindowStyle Hidden` | 2, 3 y 4 |
| **`pyside6-uic`** | Convierte `bugtracker.ui` en `ui_bugtracker.py` ([UD2, apartado 2](../apuntes/UD2-pyside6-y-qt-designer.md#2-del-diseño-al-código)) | `pyside6-uic bugtracker.ui -o ui_bugtracker.py`, cada vez que guardas en Designer | 2, 3 y 4 |
| **SQLite** | La base de datos, en un archivo: `bugtracker.db` ([UD2, apartado 7](../apuntes/UD2-pyside6-y-qt-designer.md#7-datos-con-sqlite)) | Se usa desde `bd.py`, que ya está hecho | Ninguno |
| **pytest** y **pytest-qt** | Ejecutan pruebas automáticas | `python -m pytest -v` | 0 (y la 2.ª parte) |
| **diagrams.net** y **WebAIM Contrast Checker** | Dos webs: una para dibujar el boceto y otra para comprobar el contraste de dos colores | En el navegador: app.diagrams.net y webaim.org/resources/contrastchecker | 1 |

## Qué se trabaja

| Unidad | Qué se trabaja | Pasos |
|---|---|---|
| UD1 · Diseño, UX y accesibilidad | heurísticas de Nielsen, accesibilidad (contraste, teclado, etiquetas, mensajes), wireframe | 1 y 2 |
| UD2 · PySide6 y Qt Designer | Qt Designer y `pyside6-uic`, señales y slots, acciones, menús, barra de herramientas, diálogos y validación, SQLite, Model/View | 2, 3 y 4 |

La UD3 y la UD4 (pasos 5 a 11) van en la 2.ª parte.

## Plan de la semana

Cada sesión dura 50 minutos.

| Día | Sesión | Qué se hace |
|---|---|---|
| Martes 3 | 10:10 | Leer «Punto de partida», «Con qué trabajas» y «Las herramientas» (30 min). **Paso 0** (preparar, 20 min); quien tenga que instalar algo, lo hace mientras. |
| Martes 3 | 11:00 | **Paso 0**: cómo está hecho el BugTracker (15 min). **Paso 1** (evaluación heurística y de accesibilidad, 35 min). |
| Martes 3 | 12:10 | **Paso 2** (mejoras de accesibilidad en Designer, 30 min) y empezar el **Paso 3** (20 min). |
| Miércoles 4 | 11:00 | **Paso 3** (acciones, menú, barra de herramientas y diálogo con validación; lo nuevo es la validación) y empezar el **Paso 4**. |
| Miércoles 4 | 12:10 | **Paso 4** (de `QTableWidget` a Model/View). |
| Jueves 5 | 08:30 | Terminar los pasos 3 y 4. |
| Jueves 5 | 09:20 | Terminar el **Paso 4** y repasar la lista final («Cómo comprobarlo»). |

**Los pasos se hacen en orden**, cada uno en la sesión que le toca según el plan de la semana: cada paso usa lo del anterior. Antes de pasar al siguiente, la aplicación debe arrancar.

Cada paso tiene **Objetivo**, **Pista**, **Comprueba que…** y **Si te falla…**; los pasos 1 a 4, además, una **Mini-explicación** (lo justo).

---

## Paso 0 · Preparar (martes, 35 min)

**Objetivo.** Tener tu carpeta de trabajo con su entorno virtual y la aplicación arrancando.

**Pista.**

1. **Instala** antes lo que indica [`software-DI.md`](software-DI.md): Python 3.12 y VS Code con la extensión Python.
2. **El proyecto**: descarga la plantilla, [`plantilla.zip`](https://github.com/mrpiay/NTFOR_DAM2627_DI/raw/main/2026_11_02-06/actividades/plantilla.zip), Haz doble clic en el zip: dentro está la carpeta `bugtracker`. Arrástrala a una **ruta corta y fuera de OneDrive**, por ejemplo `C:\dam2627\di`: queda en `C:\dam2627\di\bugtracker`. El entorno virtual tiene archivos con rutas muy largas: dentro de OneDrive o del Escritorio la instalación puede fallar.
3. **Ábrela en VS Code**: *File > Open Folder…*, elige la carpeta `bugtracker` y pulsa *Seleccionar carpeta*. Si pregunta si confías en los autores, *Yes, I trust the authors*. A la izquierda verás sus archivos.
4. **Abre la terminal**: *Terminal > New Terminal* (`Ctrl+ñ`). Se abre abajo, ya dentro de la carpeta del proyecto. Tiene que ser **PowerShell** (lo pone a la derecha del panel de la terminal); si no, en la flecha junto al **+** elige *PowerShell*.
5. **En la terminal**, una orden detrás de otra: crea el entorno virtual, actívalo, instala las librerías, añade las incidencias de prueba y arranca la aplicación.

   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python datos_ejemplo.py
   python main.py
   ```

   `datos_ejemplo.py` añade cinco incidencias de prueba; ejecútalo una sola vez. Cada vez que abras una terminal nueva, activa el entorno con `.venv\Scripts\Activate.ps1` (cuando ya has elegido el intérprete, como se explica a continuación, VS Code suele hacerlo solo).
6. **Elige el intérprete** en VS Code, para que reconozca las librerías del entorno: `Ctrl+Mayús+P` → «Python: Select Interpreter» → el de `.venv`.

**Comprueba que…**

- en la terminal aparece `(.venv)` al principio de la línea;
- `python main.py` abre el BugTracker con las incidencias de ejemplo y puedes añadir, modificar y eliminar;
- `python -m pytest -v` se ejecuta, en sus primeras líneas sale `plugins: qt-…` (pytest-qt está instalado) y al final da **4 failed**. Es lo esperado: las pruebas son del componente del paso 5, que aún no existe.

**Si te falla…**

- *«La ejecución de scripts está deshabilitada»*: ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activar el entorno.
- *`python` no se reconoce*: reinstala Python marcando **Add python.exe to PATH** (ver [`software-DI.md`](software-DI.md)) y abre una terminal nueva.
- *`WinError 206` («el nombre del archivo o la extensión es demasiado largo») o, después, `fixture 'qtbot' not found`*: la carpeta está en una ruta demasiado larga o en OneDrive. Bórrala, cópiala a `C:\dam2627\di\` y repite los comandos desde `python -m venv .venv`.
- *pip falla o no hay red*: repite `pip install -r requirements.txt` cuando tengas red.

### Cómo está hecho el BugTracker (15 min)

Es la Práctica 6 (SQLite), la base de todo el proyecto. Si no la hiciste, aquí la entiendes; si la hiciste, compárala con la tuya. Abre `bd.py` y `main.py` (con un clic en el panel de archivos de VS Code, a la izquierda) y recórrelos con esta tabla; no hay que escribir nada.

| Dónde | Qué hace |
|---|---|
| `bd.py` · `conectar()` | Abre la base de datos `bugtracker.db` |
| `bd.py` · `crear_bd()` | Crea la tabla `incidencias` si no existe |
| `bd.py` · `obtener_…`, `insertar_…`, `actualizar_…`, `eliminar_…` | Las cuatro operaciones: leer, añadir, modificar y borrar (CRUD) |
| `main.py` · `__init__` | Carga la interfaz y conecta los botones (`clicked.connect(...)`) |
| `main.py` · `cargar_incidencias()` | Pide las filas a `bd.py` y rellena la tabla, celda a celda (en el Paso 4 se cambia por Model/View) |
| `main.py` · `anadir_…`, `modificar_…`, `eliminar_…` | Leen el formulario, llaman a `bd.py` y recargan; si `bd.py` falla, muestran el error con `QMessageBox` |

Lo que hay que saber de SQLite y del código de `bd.py` está en [UD2, apartado 7](../apuntes/UD2-pyside6-y-qt-designer.md#7-datos-con-sqlite), y lo de las señales, en el [apartado 4](../apuntes/UD2-pyside6-y-qt-designer.md#4-señales-y-slots).

**La regla de la plantilla:** `main.py` nunca contiene SQL y `bd.py` nunca usa widgets. ¿Por qué conviene separarlos así? ¿Qué habría que cambiar si mañana los datos estuvieran en otra base de datos?

---

## Paso 1 · Evaluación heurística y de accesibilidad (martes, 35 min)

**Objetivo.** Revisar el BugTracker como lo haría una persona experta en usabilidad y hacer una lista de mejoras.

**Mini-explicación.** Una **evaluación heurística** recorre la interfaz con una lista de principios y apunta dónde no se cumplen. Las heurísticas de Nielsen están en [UD1, apartado 2](../apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#2-las-heurísticas-de-nielsen); las pautas de accesibilidad (contraste, teclado, *buddy*, color), en el [apartado 3](../apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#3-accesibilidad); y cómo se evalúa, en el [apartado 7](../apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#7-evaluar-la-usabilidad-y-la-accesibilidad). El contraste se comprueba con WebAIM Contrast Checker.

**Pista.** Crea `notas.md` en la carpeta de tu proyecto y recorre tu aplicación **sin ratón** durante cinco minutos. Después escribe en `notas.md` una tabla con **al menos cinco problemas**:

| Problema | Dónde | Heurística o pauta | Mejora propuesta |
|---|---|---|---|
| Con `Tab` no se sale de la descripción: se escribe un tabulador | `txtDescripcion` | uso con teclado | activar `tabChangesFocus` |
| `Alt+T` no lleva al título | etiqueta «Título:» | etiquetas y atajos | `&Título:` con buddy `txtTitulo` |
| … | … | … | … |

Cosas que conviene mirar: el orden de tabulación, si las etiquetas tienen atajo y *buddy*, si hay atajos repetidos (por ejemplo, dos etiquetas o botones con la misma letra después de `&`), si se sabe qué campo es obligatorio, si los mensajes se entienden y si las acciones tienen atajo.

Por último, haz un **boceto rápido** (wireframe, en papel o en diagrams.net) de cómo quedará la ventana al final del proyecto: menú «Archivo», barra de herramientas, buscador encima de la tabla.

**Comprueba que…** tienes al menos cinco problemas, cada uno con su heurística o pauta y una mejora, y el boceto.

**Si te falla…** *No te acuerdas de las heurísticas*: están en [UD1, apartado 2](../apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#2-las-heurísticas-de-nielsen); con cinco problemas bien justificados basta.

---

## Paso 2 · Mejoras de accesibilidad en Designer (martes, 30 min)

**Objetivo.** Aplicar en `bugtracker.ui` mejoras de accesibilidad de tu lista del paso 1.

**Mini-explicación.** `ui_bugtracker.py` se genera a partir de `bugtracker.ui`: los cambios se hacen siempre en Designer y luego se regenera ([UD2, apartado 2](../apuntes/UD2-pyside6-y-qt-designer.md#2-del-diseño-al-código)). Qué son el *buddy*, `tabChangesFocus` y `accessibleName`: [UD2, apartado 3](../apuntes/UD2-pyside6-y-qt-designer.md#3-controles-propiedades-y-layouts) y [UD1, apartado 3](../apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#3-accesibilidad).

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
- *Designer no abre*: comprueba que la terminal está en la carpeta del proyecto y que existe `.venv\Scripts\pyside6-designer.exe`; si no existe, activa el entorno y repite `pip install -r requirements.txt`.

---

## Paso 3 · Acciones, menú, barra de herramientas y diálogo (martes y miércoles)

**Objetivo.** Añadir las acciones Nueva, Guardar, Eliminar y Salir con atajos, en un menú y en una barra de herramientas, y un diálogo «Nueva incidencia» que valida los datos.

**Mini-explicación.** Cada acción se crea una vez y se pone en el menú y en la barra; su señal es `triggered` ([UD2, apartado 5](../apuntes/UD2-pyside6-y-qt-designer.md#5-acciones-menús-y-barras-de-herramientas)). En el diálogo, Aceptar llama a `validar()`, que solo hace `accept()` si los datos son correctos ([UD2, apartado 6](../apuntes/UD2-pyside6-y-qt-designer.md#6-diálogos-y-validación)).

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
3. Añade una barra de herramientas (clic derecho en la ventana → *Add Tool Bar*), con `objectName = toolBarPrincipal` y `toolButtonStyle = ToolButtonTextOnly` (en Designer sale como `Qt::ToolButtonTextOnly`), y arrastra a ella Nueva, Guardar y Eliminar. Regenera `ui_bugtracker.py`.
4. En `main.py`, completa los `TODO Paso 3`. Sustituye la línea `# TODO Paso 3: from dialogo import DialogoIncidencia` por `from dialogo import DialogoIncidencia` (sin `#` ni `TODO Paso 3:`). Las cuatro conexiones van en `__init__`, donde está `# TODO Paso 3: conecta las QAction…`. Los métodos `guardar` y `nueva_incidencia` van donde está `# TODO Paso 3: añade aquí los slots`, debajo de `actualizar_botones()`:

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

5. En `dialogo.py`, completa `validar()`: si el título está vacío, `QMessageBox.warning(self, "Falta el título", "Escribe un título.")`, `self.txtTitulo.setFocus()` y `return`; si tiene más de 100 caracteres, otro aviso que diga cuántos tiene (`len(titulo)`).
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
        self.limpiar_formulario()
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
- *Designer no abre*: comprueba que la terminal está en la carpeta del proyecto y que existe `.venv\Scripts\pyside6-designer.exe`; si no existe, activa el entorno y repite `pip install -r requirements.txt`.

---

## Paso 4 · De `QTableWidget` a Model/View (miércoles y jueves)

**Objetivo.** Mostrar las incidencias en un `QTableView` a través de un modelo y un proxy que permitirá filtrar y ordenar.

**Mini-explicación.** Así quedan los datos, de la base de datos a la tabla:

```
SQLite -> bd.py -> MODELO (QStandardItemModel) -> PROXY (QSortFilterProxyModel) -> VISTA (QTableView)
```

Lo que se selecciona en la vista es una fila **del proxy**: se traduce a la del modelo con `mapToSource`. El modelo se rellena con `bd.obtener_incidencias()`, para que `bd.py` siga teniendo todo el SQL. Model/View, el proxy y `mapToSource`, en [UD2, apartado 8](../apuntes/UD2-pyside6-y-qt-designer.md#8-modelview).

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

3. En `__init__`, sustituye la línea `self.ui.tblIncidencias.itemSelectionChanged.connect(self.cargar_seleccion)` y su comentario `# TODO Paso 4` por:

```python
        self.ui.tblIncidencias.selectionModel().selectionChanged.connect(self.cargar_seleccion)
```

4. Sustituye el método `cargar_incidencias()` entero por este. Ya no rellena la tabla celda a celda: rellena el modelo, y la tabla lo muestra sola (las líneas `setColumnHidden` ya están en `configurar_tabla()`):

```python
    def cargar_incidencias(self):
        try:
            incidencias = bd.obtener_incidencias()
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se han podido cargar las incidencias.")
            return

        self.modelo.removeRows(0, self.modelo.rowCount())
        for incidencia in incidencias:
            celdas = []
            for campo in ("id", "titulo", "tipo", "prioridad", "estado"):
                celda = QStandardItem(str(incidencia[campo]))
                celda.setEditable(False)
                celdas.append(celda)
            self.modelo.appendRow(celdas)
        self.ui.tblIncidencias.clearSelection()
        self.actualizar_botones()
```

5. En `id_seleccionado()`, sustituye las líneas desde `seleccion = …` hasta el último `return` por estas:

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
- *La prioridad se ordena como texto* (Alta, Baja, Crítica, Media): es normal, el orden es alfabético.

---

## Entrega

Qué se entrega esta semana y cuándo: [`entrega.md`](entrega.md).

## Cómo comprobarlo (lista final)

- [ ] La evaluación tiene al menos cinco problemas con su heurística o pauta, y hay boceto.
- [ ] Al menos dos mejoras de accesibilidad aplicadas en Designer (buddies y atajos, tabulación, ayudas).
- [ ] Menú Archivo y barra de herramientas con las mismas `QAction`; atajos `Ctrl+N`, `Ctrl+S`, `Supr` y `Ctrl+Q`.
- [ ] El diálogo «Nueva incidencia» se usa entero con teclado, valida el título y da mensajes claros.
- [ ] La tabla es un `QTableView` con modelo y proxy; se ordena por columnas; el ID no se ve.
- [ ] Seleccionar, modificar y eliminar afectan a la incidencia correcta, también después de ordenar.
