# Cuestionario C1 · semana del 2 al 6 de noviembre · soluciones

## Cuestiones sobre el proyecto

**1.** `.venv` es una carpeta con su propio Python y las librerías de este proyecto. `pip install -r requirements.txt` instala en ella las librerías que lista ese archivo (PySide6-Essentials, en la versión 6.12, pytest y pytest-qt). Cada proyecto tiene el suyo para no mezclar versiones: un proyecto puede necesitar una versión de una librería y otro, otra.

**2.** `Start-Process .venv\Scripts\pyside6-designer.exe -ArgumentList bugtracker.ui -WindowStyle Hidden`. `Start-Process` lo abre aparte, y la terminal queda libre; `.venv\Scripts\pyside6-designer.exe` es el Designer del entorno virtual; `-ArgumentList bugtracker.ui` le dice qué archivo abrir; y `-WindowStyle Hidden` oculta la ventana de terminal vacía que, si no, se abre junto a Designer.

**3.** Lee `ui_bugtracker.py`: `main.py` importa su clase `Ui_VentanaPrincipal` y llama a `setupUi`. `bugtracker.ui` solo lo lee Qt Designer. Después de cambiar algo en Designer hay que guardar, regenerar con `pyside6-uic bugtracker.ui -o ui_bugtracker.py` y volver a lanzar la aplicación.

**4.** Porque se genera a partir de `bugtracker.ui`: la próxima vez que se regenere, `pyside6-uic` lo sobrescribe y se pierde lo que se hubiera escrito a mano. Los cambios de la interfaz se hacen siempre en Designer.

**5.**

- `main.py`: la ventana principal (`VentanaPrincipal`). Carga la interfaz, conecta señales y slots, y tiene la lógica: añadir, modificar, eliminar, las acciones y la tabla.
- `bd.py`: todo el acceso a SQLite (crear la tabla, leer, insertar, actualizar y borrar).
- `dialogo.py`: el diálogo «Nueva incidencia» / «Editar incidencia», con su validación.
- `bugtracker.ui`: el diseño de la ventana, hecho en Qt Designer.
- `ui_bugtracker.py`: el código Python generado a partir de `bugtracker.ui`.
- `datos_ejemplo.py`: añade incidencias de prueba; se ejecuta una vez.

**6.** Cada archivo tiene una sola responsabilidad: `bd.py`, los datos; `main.py`, la interfaz y su lógica. Así se puede cambiar una parte sin tocar la otra, y es más fácil encontrar y probar cada cosa. Si los datos estuvieran en otra base de datos, solo habría que cambiar `bd.py`: `main.py` seguiría llamando a las mismas funciones (`obtener_incidencias`, `insertar_incidencia`…).

**7.** Con `?`, `sqlite3` pasa los datos aparte, como valores. Si se pegaran en el texto, un título con una comilla rompería la consulta, y alguien podría escribir algo que se ejecutara como SQL (inyección SQL).

**8.** Por ejemplo:

- *Visibilidad del estado del sistema:* al añadir una incidencia no se decía nada. Mejora: un mensaje en la barra de estado, «Incidencia añadida».
- *Prevención de errores:* «Eliminar» estaba activo sin nada seleccionado. Mejora: desactivarlo sin selección y pedir confirmación antes de borrar.

(Valen otras, siempre que cada problema corresponda de verdad a su heurística.)

**9.** La `&` hace que la letra siguiente sea un atajo: `Alt+T` (aparece subrayada). El *buddy* es el campo asociado a la etiqueta: el atajo de la etiqueta lleva el foco a ese campo. Sin *buddy*, `Alt+T` no hace nada, porque una etiqueta no puede recibir el foco.

**10.** `tabChangesFocus` hace que `Tab` salga de la descripción y pase al siguiente campo, en lugar de escribir un tabulador dentro del texto. Desmarcar `tabKeyNavigation` hace que `Tab` salga de la tabla en lugar de ir de celda en celda; dentro de la tabla uno se mueve con las flechas. Las dos permiten usar la aplicación entera con el teclado.

**11.**

```
&Nueva incidencia... -> Ctrl+N
Se ha disparado la acción
```

La `QAction` guarda el texto (con su `&`) y el atajo. `trigger()` hace lo mismo que elegirla en el menú, pulsar su botón o su atajo: emite la señal `triggered`, y se ejecuta lo que está conectado a ella.

**12.**

```
Antes del clic
Guardando
Guardando
Traceback (most recent call last):
  …
TypeError: Expected signal or callable, got "NoneType"
```

`connect(guardar)` conecta la señal con el método, sin ejecutarlo: `guardar` solo se ejecuta con el clic (`boton.click()`), por eso sale «Guardando» después de «Antes del clic». En la última línea, `guardar()` lleva paréntesis: se **ejecuta en ese momento** (el segundo «Guardando») y a `connect` le llega lo que devuelve, `None`, que no se puede conectar. En el proyecto pasa lo mismo con `connect(self.guardar())`: hay que pasar el método sin llamarlo.

**13.** Porque es una sola orden: se programa una vez (una conexión de `triggered`) y aparece en los dos sitios con el mismo texto, atajo y estado. Si se desactiva (como Eliminar sin selección), se desactiva en los dos.

**14.** Un diálogo modal bloquea la ventana principal hasta que se cierra. `exec()` lo muestra y devuelve verdadero si se aceptó y falso si se canceló. El botón Aceptar está conectado a `validar()`, no a `accept()`: `validar()` comprueba que el título no esté vacío ni pase de 100 caracteres, y solo entonces llama a `accept()`. Si no, avisa y el diálogo sigue abierto.

**15.**

1. `Ctrl+N` dispara la `QAction` `actionNueva`: emite `triggered`.
2. Esa señal está conectada (en `__init__` de `main.py`) a `nueva_incidencia()`.
3. `nueva_incidencia()` crea `DialogoIncidencia(self)` (`dialogo.py`) y llama a `exec()`.
4. Al pulsar Aceptar se ejecuta `validar()`, que comprueba el título y llama a `accept()`: `exec()` devuelve verdadero.
5. `nueva_incidencia()` toma `dialogo.datos()` y llama a `bd.insertar_incidencia(*…)` (`bd.py`), que hace el `INSERT`.
6. `cargar_incidencias()` vuelve a leer las incidencias con `bd.obtener_incidencias()` y rellena el modelo: la incidencia aparece en la tabla.
7. La barra de estado muestra que se ha añadido.

**16.**

```
No guarda | Error | Alta
Traceback (most recent call last):
  …
TypeError: guardar() missing 2 required positional arguments: 'tipo' and 'prioridad'
```

El `*` reparte la tupla en tres argumentos: `guardar(*datos)` es lo mismo que `guardar("No guarda", "Error", "Alta")`. Sin `*`, la tupla entera es un solo argumento (`titulo`) y faltan los otros dos. Por eso en el proyecto se escribe `bd.insertar_incidencia(*dialogo.datos())`.

**17.** Con `QTableWidget` los datos viven dentro del widget: se meten celda a celda. En Model/View se separan: el **modelo** (`QStandardItemModel`) guarda las filas y columnas; la **vista** (`QTableView`) solo las dibuja y gestiona la selección; y el **proxy** (`QSortFilterProxyModel`), entre los dos, ordena y filtra sin tocar los datos del modelo.

**18.**

```
Se ve: Botón Guardar
Fila en la vista: 0
Fila en el modelo: 1
ID: 2
ID si no se traduce: 1
```

El proxy ordena por título, así que lo que se ve en la fila 0 («Botón Guardar») está en la fila 1 del modelo. `mapToSource` traduce la fila de la vista a la del modelo. Sin traducirla se coge el ID de otra incidencia (1, «Exportar CSV»): al eliminar o modificar después de ordenar, se cambiaría la que no es.

**19.** Para saber qué incidencia está seleccionada: `id_seleccionado()` lee el ID de la fila seleccionada (traducida con `mapToSource`) y ese ID es el que se pasa a `bd.py` para modificar o eliminar. No se usa el número de fila, porque cambia al ordenar; el ID no cambia. Se oculta porque al usuario no le dice nada.

**20.** `DialogoIncidencia(self)` se abre vacío, con el título «Nueva incidencia», desde la acción Nueva (`Ctrl+N`). `DialogoIncidencia(self, incidencia)` se abre con los datos de esa incidencia ya rellenos y el título «Editar incidencia», al hacer doble clic en una fila. Al aceptar, el primero inserta una incidencia nueva y el segundo actualiza la que había.

## Cuestiones sobre los apuntes

**21.** *(UD1, apartado 1)* La usabilidad es lo fácil que es usar la aplicación para conseguir algo; la accesibilidad, que la pueda usar cualquier persona, también con una discapacidad; la experiencia de usuario es todo lo que siente la persona al usarla (si le resulta útil, cómoda y agradable), e incluye las dos anteriores.

**22.** *(UD1, apartado 3)* Perceptible, operable, comprensible y robusto. Se suele exigir el nivel **AA**, en el que el texto normal necesita un contraste de al menos **4,5:1** con el fondo.

**23.** *(UD1, apartado 4)* ISO 9241 es la norma internacional de ergonomía de la interacción (define la usabilidad como eficacia, eficiencia y satisfacción); EN 301 549 es la norma europea que exige la accesibilidad (WCAG). Seguir los estándares hace que la interfaz se entienda a la primera, reduce lo que hay que aprender y los errores, y en accesibilidad a veces es obligatorio (en España, en el sector público).

**24.** *(UD1, apartado 5)* `QLineEdit`, `QComboBox` (o `QRadioButton`), `QCheckBox`, `QSpinBox` y `QDateEdit`.

**25.** *(UD1, apartados 5 y 6)* Por ejemplo, «Falta el título. Escríbelo para poder guardar la incidencia». Un buen mensaje es breve, está en el idioma del usuario y dice qué ha pasado y qué hacer, sin códigos técnicos. Los atajos: `Ctrl+N`, `Ctrl+S` y `Ctrl+Q`.

**26.** *(UD2, apartado 1)* PySide6 y PyQt6 son Qt para Python y usan Qt Designer; PySide6 es la oficial, con licencia LGPL, y PyQt6 tiene licencia GPL o comercial. Tkinter viene con Python, es más sencilla y no tiene un editor visual oficial.
