# DI · Tutorial de Python con el BugTracker

**Para qué.** En este módulo se lee mucho Python: el BugTracker tiene seis archivos `.py`. Este tutorial explica qué es el BugTracker, cómo instalarlo con sus dependencias y usarlo, cómo está hecho por dentro (qué archivo hace qué y quién usa a quién) y, por último, recorre un programa de Python ya hecho, `explorador.py`, que lee esos archivos y la base de datos para sacar información. No hay que escribir código: se **ejecuta**, se **lee** y se **explica**.

Python que aparece: importar módulos, `os`, `sys`, listas, diccionarios, funciones, clases, herencia, excepciones y archivos.

---

## Parte 1 · Qué es el BugTracker

Antes de instalar nada, qué es la aplicación, cómo es y qué guarda.

### 1.1 · Para qué sirve

Un ***bug*** es un fallo de un programa. Un ***bug tracker*** (gestor de incidencias) es la aplicación donde un equipo de desarrollo apunta los fallos, las mejoras y las ideas de su programa, para no olvidarlos, decidir cuáles van primero y saber en qué estado está cada uno. Los equipos reales usan herramientas como GitHub Issues o Jira.

El BugTracker de este módulo es una versión pequeña, de escritorio: una ventana para **añadir, ver, modificar y eliminar incidencias**, que se guardan en una base de datos en el propio equipo. Está hecho en Python con **PySide6** (la librería Qt para Python) y **SQLite** (una base de datos que es un solo archivo).

### 1.2 · La ventana

Así es la ventana, con el nombre de cada parte:

```
┌─ BugTracker ────────────────────────────────────────────┐
│ Archivo                                    ← menú        │
│ [Nueva incidencia] [Guardar] [Eliminar]    ← barra de    │
│                                              herramientas│
│ Título (obligatorio): [____________________]             │
│ Tipo:                 [Error            ▼]               │
│ Prioridad:            [Baja             ▼] ← formulario  │
│ Estado:               [Pendiente        ▼]               │
│ Descripción:          [____________________]             │
│                                                          │
│        [Añadir] [Modificar] [Eliminar] [Limpiar]         │
│                                                          │
│  Título               Tipo     Prioridad   Estado        │
│  El botón Guardar…    Error    Alta        Pendiente     │
│  …                                         ← tabla       │
│                                                          │
│ Incidencia añadida                 ← barra de estado     │
└──────────────────────────────────────────────────────────┘
```

Desde la ventana se trabaja de dos formas: con el **formulario** de arriba y sus botones, o con un **diálogo**, una ventana aparte con el mismo formulario que se abre con *Archivo > Nueva incidencia…* (`Ctrl+N`) o con doble clic en una fila. En la parte 3 se prueba todo.

### 1.3 · Los datos: qué es una incidencia

Cada incidencia es una fila de la tabla `incidencias` de la base de datos `bugtracker.db`, con estos campos:

| Campo | Qué guarda | Valores |
|---|---|---|
| `id` | Número que pone la base de datos a cada incidencia nueva (1, 2, 3…). No se repite. La tabla de la ventana lo tiene, pero oculto | Automático |
| `titulo` | Qué pasa, en una línea | Obligatorio; en el diálogo, 100 caracteres como máximo |
| `tipo` | Qué clase de incidencia es | Error, Mejora o Nueva funcionalidad |
| `prioridad` | Cuánto corre | Baja, Media, Alta o Crítica |
| `estado` | Cómo va | Pendiente, En proceso o Resuelta |
| `descripcion` | Los detalles | Opcional |

La tabla se define con SQL en la función `crear_bd()` de `bd.py` (`CREATE TABLE IF NOT EXISTS incidencias …`). Los valores posibles de tipo, prioridad y estado son las opciones de las listas desplegables: en `bugtracker.ui` para la ventana y en `dialogo.py` (listas `TIPOS`, `PRIORIDADES` y `ESTADOS`) para el diálogo.

---

## Parte 2 · Instalar el BugTracker y sus dependencias

Para el tutorial se usa una **copia nueva** del BugTracker en su propia carpeta: así todo el mundo tiene los mismos archivos y el proyecto propio no se toca.

### Paso 2.1 · Python y VS Code

Hacen falta dos programas:

- **Python**, el lenguaje en el que está escrito el BugTracker.
- **VS Code**, el editor con el que se leen los archivos y se abre la terminal.

Abre una terminal **PowerShell** (en Windows, menú Inicio → «Terminal») y escribe:

```
python --version
code --version
```

- Si la primera sale `Python 3.` seguido del resto de la versión, Python está instalado. Si sale que no se reconoce o se abre la Microsoft Store, instálalo desde [python.org/downloads](https://www.python.org/downloads/): en la primera pantalla del instalador marca **Add python.exe to PATH** y pulsa *Install Now*.
- Si la segunda sale un número de versión, VS Code está instalado. Si no, instálalo desde [code.visualstudio.com](https://code.visualstudio.com/).
- En VS Code, instala la extensión **Python** (de Microsoft): icono de extensiones de la izquierda (`Ctrl+Mayús+X`), busca «Python» y pulsa *Install*. Sirve para que VS Code entienda el código y deje elegir el entorno virtual.

Después de instalar algo, cierra la terminal y abre otra para que lo reconozca.

**Comprueba que…** las dos órdenes muestran una versión.

### Paso 2.2 · Descargar los archivos desde la terminal

Todo se hace con órdenes, en la misma terminal PowerShell del paso 2.1. Escríbelas (o cópialas) una detrás de otra y pulsa **Intro** después de cada una.

1. Crea la carpeta del tutorial y entra en ella:

   ```
   mkdir C:\dam2627\di\python-bugtracker
   cd C:\dam2627\di\python-bugtracker
   ```

   `mkdir` (*make directory*) crea la carpeta, con las que falten por el camino. `cd` (*change directory*) hace que la terminal trabaje dentro de ella: la línea de la terminal pasa a empezar por `PS C:\dam2627\di\python-bugtracker>`. `PS` indica que es **PowerShell**; lo que sigue es la **carpeta actual**, donde se ejecuta lo que se escribe; y `>` marca dónde se escribe. Tiene que ser una **ruta corta y fuera de OneDrive**: las librerías que se instalan después tienen rutas muy largas y OneDrive las sincroniza mal.

2. Descarga la plantilla del BugTracker, que es la 1.ª parte del proyecto terminada:

   ```
   Invoke-WebRequest https://github.com/mrpiay/NTFOR_DAM2627_DI/raw/main/2026_11_09-13/actividades/plantilla.zip -OutFile plantilla.zip
   ```

   `Invoke-WebRequest` descarga lo que hay en una dirección web. `-OutFile` dice con qué nombre se guarda en la carpeta actual.

3. Descomprime el zip y bórralo:

   ```
   Expand-Archive plantilla.zip -DestinationPath .
   Remove-Item plantilla.zip
   ```

   `Expand-Archive` descomprime. El `.` de `-DestinationPath .` es la **carpeta actual**. Dentro del zip hay una carpeta, `bugtracker`, con los archivos de la aplicación. `Remove-Item` borra el zip, que ya no hace falta.

4. Entra en `bugtracker` y descarga en ella el programa del tutorial, `explorador.py`:

   ```
   cd bugtracker
   Invoke-WebRequest https://github.com/mrpiay/NTFOR_DAM2627_DI/raw/main/2026_11_09-13/actividades/python-bugtracker/explorador.py -OutFile explorador.py
   ```

5. Mira lo que hay:

   ```
   dir
   ```

   `dir` lista los archivos de la carpeta actual.

6. Abre la carpeta en VS Code:

   ```
   code .
   ```

   `code` abre VS Code y el `.` le dice que abra la carpeta actual. Si pregunta si confías en los autores, pulsa *Yes, I trust the authors*.

**Comprueba que…** `dir` muestra, y en el explorador de VS Code (la columna de la izquierda) aparecen, estos diez archivos: `bd.py`, `bugtracker.ui`, `buscador.py`, `datos_ejemplo.py`, `dialogo.py`, `explorador.py`, `main.py`, `requirements.txt`, `test_buscador.py` y `ui_bugtracker.py`.

**Si te falla…**

- *`mkdir` dice que ya existe un elemento con ese nombre*: la carpeta ya estaba creada. Sigue con `cd`.
- *`Expand-Archive` dice que el archivo ya existe*: ya se había descomprimido antes. Borra la carpeta con `Remove-Item -Recurse bugtracker` y repite el apartado 3.
- *`code` no se reconoce*: VS Code no está en el `PATH`. Ábrelo desde el menú Inicio, *File > Open Folder…* y elige `C:\dam2627\di\python-bugtracker\bugtracker`.

### Paso 2.3 · Crear el entorno virtual

A partir de aquí se trabaja en la terminal de VS Code: *Terminal > New Terminal* (`Ctrl+ñ`). Se abre ya en la carpeta `bugtracker`. Tiene que ser **PowerShell** (lo pone a la derecha del panel de la terminal). La terminal de antes se puede cerrar.

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

- Un **entorno virtual** es una carpeta, `.venv`, con una copia de Python y las librerías de **este** proyecto, separadas de las de otros proyectos. Así cada proyecto tiene las versiones que necesita.
- `python -m venv .venv` lo crea. `-m venv` ejecuta el módulo `venv` de Python como si fuera un programa.
- `.venv\Scripts\Activate.ps1` lo **activa**: a partir de ahí, `python` y `pip` son los del entorno. Hay que activarlo en cada terminal nueva.

**Si al activarlo sale «running scripts is disabled on this system»** («la ejecución de scripts está deshabilitada en este sistema»): Windows no deja ejecutar scripts de PowerShell, y `Activate.ps1` es uno. Pasa en casi todos los equipos la primera vez. Ejecuta esto **una sola vez**, responde `S` (o `Y`) si pide confirmación, y vuelve a activar el entorno:

```
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.venv\Scripts\Activate.ps1
```

`RemoteSigned` permite ejecutar los scripts creados en el propio equipo, como el del entorno virtual; los descargados de internet, solo si están firmados. `-Scope CurrentUser` hace el cambio solo para tu usuario, sin necesidad de ser administrador.

**Comprueba que…** la línea de la terminal empieza por `(.venv)`.

### Paso 2.4 · Instalar las dependencias

Las **dependencias** son las librerías que el programa necesita y que no vienen con Python. Están en `requirements.txt`:

```
PySide6-Essentials==6.12.*
pytest
pytest-qt
```

| Librería | Para qué |
|---|---|
| `PySide6-Essentials` | Qt para Python: ventanas, botones, tablas… y las herramientas `pyside6-designer` (Qt Designer) y `pyside6-uic`. `==6.12.*` pide la versión 6.12, sea cual sea el último número |
| `pytest` | Ejecuta pruebas automáticas |
| `pytest-qt` | Añade a pytest lo necesario para probar ventanas de Qt (`qtbot`) |

Instálalas con **pip**, el instalador de librerías de Python:

```
pip install -r requirements.txt
```

`-r` le dice a pip que lea la lista de un archivo. Descarga cada librería (y las que ellas necesitan) y las guarda dentro de `.venv`. Tarda un poco.

Para ver lo que hay instalado:

```
pip list
```

Por último, en VS Code elige el intérprete del entorno, para que reconozca las librerías al leer el código: `Ctrl+Mayús+P` → «Python: Select Interpreter» → el de `.venv`.

**Comprueba que…** `pip list` muestra `PySide6-Essentials`, `pytest` y `pytest-qt`.

### Qué hay ahora en la carpeta

Además de los archivos descargados, ha aparecido `.venv\`, creada por `python -m venv .venv`: el entorno virtual, con las librerías instaladas por pip. No es código del proyecto: no se entrega ni se copia, se vuelve a crear con los pasos 2.3 y 2.4.

**Si te falla…**

- *`python` no se reconoce como comando*: Python no está instalado o no está en el `PATH`. Instálalo desde python.org marcando *Add python.exe to PATH* y abre una terminal nueva.
- *«La ejecución de scripts está deshabilitada» al activar el entorno*: la solución está en el paso 2.3.
- *`WinError 206` («el nombre del archivo o la extensión es demasiado largo»)*: la carpeta está en una ruta demasiado larga o en OneDrive. Bórrala, cópiala a `C:\dam2627\di\python-bugtracker\` y repite desde `python -m venv .venv`.
- *`ModuleNotFoundError: No module named 'PySide6'`*: el entorno no está activado (falta `(.venv)`) o no se instalaron las dependencias. Actívalo y repite `pip install -r requirements.txt`.
- *pip falla o no hay red*: repite `pip install -r requirements.txt` cuando haya red.

### Lo mismo en Linux

Las órdenes de esta parte son de **PowerShell**, la terminal de Windows. En Linux la idea es la misma y cambia la forma de escribir algunas:

| Qué | PowerShell (Windows) | Bash (Linux) |
|---|---|---|
| Versión de Python | `python --version` | `python3 --version` |
| Crear una carpeta | `mkdir C:\dam2627\di\python-bugtracker` | `mkdir -p ~/dam2627/di/python-bugtracker` |
| Entrar en una carpeta | `cd C:\dam2627\di\python-bugtracker` | `cd ~/dam2627/di/python-bugtracker` |
| Descargar | `Invoke-WebRequest URL -OutFile plantilla.zip` | `wget URL` |
| Descomprimir | `Expand-Archive plantilla.zip -DestinationPath .` | `unzip plantilla.zip` |
| Borrar un archivo | `Remove-Item plantilla.zip` | `rm plantilla.zip` |
| Ver qué hay en la carpeta | `dir` | `ls` |
| Abrir la carpeta en VS Code | `code .` | `code .` |
| Crear el entorno virtual | `python -m venv .venv` | `python3 -m venv .venv` |
| Activar el entorno virtual | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Instalar las dependencias | `pip install -r requirements.txt` | `pip install -r requirements.txt` |

- Las rutas de Windows empiezan por la unidad (`C:\`) y separan las carpetas con `\`. Las de Linux empiezan en `/` y las separan con `/`. `~` es la carpeta personal del usuario (`/home/usuario`).
- En Linux la línea de la terminal termina en `$` (en lugar de `>`), por ejemplo `usuario@equipo:~/dam2627$`.
- En Ubuntu, `unzip` y el módulo `venv` pueden no venir instalados: `sudo apt install unzip python3-venv`.
- En un Linux sin escritorio (un servidor, por ejemplo), la ventana del BugTracker (`python main.py`) no se puede abrir. El explorador de la parte 5 sí funciona, porque es un programa de terminal y no usa Qt.

## Parte 3 · Crear la base de datos y usar el BugTracker

### 3.1 · Crear la base de datos

La aplicación guarda las incidencias en `bugtracker.db`, que todavía no existe. `datos_ejemplo.py` la crea y le añade cinco incidencias de prueba, para no empezar con la tabla vacía:

```
python datos_ejemplo.py
```

Sale `Añadidas 5 incidencias de ejemplo.` Ejecútalo **una sola vez**: cada vez que se ejecuta añade otras cinco.

Han aparecido dos cosas en la carpeta:

| Qué | Quién lo crea | Qué es |
|---|---|---|
| `bugtracker.db` | `datos_ejemplo.py`, que llama a `bd.crear_bd()` | La base de datos, con la tabla `incidencias` y las cinco incidencias |
| `__pycache__\` | Python, al importar `bd.py` desde `datos_ejemplo.py` | Versiones ya traducidas de los `.py` importados, para que arranquen antes. Se puede borrar: Python la vuelve a crear |

**Comprueba que…** existe `bugtracker.db` en la carpeta.

### 3.2 · Usarlo antes de leerlo

En la terminal de VS Code, con `(.venv)` delante:

```
python main.py
```

Se abre la ventana de la parte 1, con las cinco incidencias en la tabla. Prueba esto, en orden:

1. **Ordenar.** Pulsa la cabecera **Prioridad** de la tabla: las filas se ordenan por esa columna.
2. **Seleccionar.** Haz clic en una fila: el formulario se rellena con sus datos y se activan **Modificar** y **Eliminar**.
3. **Modificar.** Cambia su estado a **Resuelta** y pulsa **Modificar**. La tabla cambia y abajo, en la barra de estado, sale «Incidencia modificada». Además, el formulario se **vacía** (título y descripción incluidos) y la fila deja de estar seleccionada: es a propósito, para dejarlo listo para otra incidencia. Los datos no se han borrado: siguen en la tabla y, al hacer clic otra vez en la fila, vuelven al formulario. Pasa lo mismo aunque no se cambie nada antes de pulsar **Modificar**.
4. **Añadir.** Pulsa **Limpiar**, escribe un título, elige tipo y prioridad y pulsa **Añadir**. Prueba también a pulsar **Añadir** sin título: sale un aviso, porque el título es obligatorio.
5. **El diálogo.** Pulsa `Ctrl+N` (o *Archivo > Nueva incidencia…*): se abre una ventana aparte, un **diálogo**, con el mismo formulario. Haz doble clic en una fila de la tabla: se abre el mismo diálogo para editarla.
6. **Eliminar.** Selecciona una fila y pulsa `Supr`: pide confirmación antes de borrar.
7. **Cerrar y volver a abrir.** Cierra con `Ctrl+Q` y ejecuta otra vez `python main.py`: los cambios siguen ahí, porque están guardados en la base de datos, el archivo `bugtracker.db`.

**Comprueba que…** sabes señalar en la ventana el menú, la barra de herramientas, el formulario, la tabla y la barra de estado, y sabes hacer las cuatro operaciones: añadir, ver, modificar y eliminar.

---

## Parte 4 · Cómo está hecho por dentro

### 4.1 · Los archivos

| Archivo | Qué contiene | Para qué sirve |
|---|---|---|
| `main.py` | La clase `VentanaPrincipal` y el bloque `if __name__ == "__main__":` | Es el **programa principal**: se ejecuta con `python main.py`. Crea la ventana, conecta botones y acciones con sus funciones y une todo lo demás |
| `bugtracker.ui` | XML con el diseño de la ventana | Lo crea y lo edita **Qt Designer**. Python no lo ejecuta |
| `ui_bugtracker.py` | La clase `Ui_VentanaPrincipal` con el método `setupUi` | Es `bugtracker.ui` traducido a Python con `pyside6-uic`. **No se edita a mano**: se vuelve a generar cada vez que cambia el `.ui` |
| `dialogo.py` | La clase `DialogoIncidencia` | El diálogo «Nueva incidencia» / «Editar incidencia», con su validación (el título es obligatorio) |
| `buscador.py` | La clase `Buscador`, **sin terminar** (comentarios `TODO Paso 5`) | Un componente propio: etiqueta, caja de texto y botón «Limpiar» para filtrar la tabla. Se completa en la 2.ª parte del proyecto; en la plantilla todavía no se usa |
| `bd.py` | Funciones: `conectar`, `crear_bd`, `obtener_incidencias`, `obtener_incidencia`, `insertar_incidencia`, `actualizar_incidencia`, `eliminar_incidencia` | **Todo el SQL** de la aplicación. No usa nada de Qt |
| `bugtracker.db` | La tabla `incidencias` | La **base de datos** SQLite. No existe hasta que se ejecuta la aplicación o `datos_ejemplo.py` |
| `datos_ejemplo.py` | Una lista de cinco incidencias | Las añade a la base de datos para tener datos con los que probar |
| `test_buscador.py` | Funciones `test_…` | Pruebas automáticas del Buscador, con `pytest`. Con el Buscador sin terminar, fallan las cuatro |
| `requirements.txt` | Nombres de librerías | Lo que se instala con `pip install -r requirements.txt` (paso 2.4) |

Los archivos se reparten en dos **capas**:

- **Presentación**, lo que se ve y con lo que se interactúa: `bugtracker.ui` y `ui_bugtracker.py` (el diseño), `main.py` (la lógica de la ventana), `dialogo.py` y `buscador.py`.
- **Datos**, dónde y cómo se guardan las incidencias: `bd.py` y `bugtracker.db`.

### 4.2 · Quién usa a quién

```
                 bugtracker.ui
                      │  pyside6-uic (se genera)
                      ▼
 main.py ──────► ui_bugtracker.py        (el diseño de la ventana)
    │
    ├──────────► dialogo.py              (el diálogo)
    └──────────► bd.py ─────► bugtracker.db
                   ▲
 datos_ejemplo.py ─┘

 test_buscador.py ──► buscador.py        (main.py lo usará en la 2.ª parte)
```

Una flecha `A ──► B` quiere decir que **A importa a B** (`import B` o `from B import …`) y usa lo que B tiene. `bd.py ──► bugtracker.db` quiere decir que `bd.py` abre ese archivo y le hace consultas SQL.

### 4.3 · La regla de separación

- `main.py` **nunca contiene SQL**: cuando necesita datos, llama a una función de `bd.py`.
- `bd.py` **nunca usa widgets de Qt**: si algo falla, lanza un error (`sqlite3.Error`) y es `main.py` quien muestra el mensaje.

Así, la interfaz se puede cambiar sin tocar la base de datos, y al revés. Y otro programa puede usar `bd.py` sin abrir ninguna ventana: es lo que hace el explorador de la parte 5.

### 4.4 · Qué pasa por dentro

**Al ejecutar `python main.py`:**

1. Python lee los `import` de `main.py` y carga `bd`, `dialogo` y `ui_bugtracker` (y PySide6).
2. Se llega al bloque `if __name__ == "__main__":` y se crea la aplicación Qt con `QApplication(sys.argv)`.
3. `bd.crear_bd()` crea la tabla `incidencias` si no existe.
4. Se crea `VentanaPrincipal()`. Su `__init__` llama a `setupUi` (que pone en la ventana todo lo diseñado en Qt Designer), prepara la tabla, **conecta** cada botón y cada acción con su función y carga las incidencias.
5. `ventana.show()` muestra la ventana y `app.exec()` se queda esperando lo que haga el usuario.

**Al pulsar «Añadir»** (modificar y eliminar siguen el mismo recorrido):

```
 clic en Añadir
      │  señal clicked, conectada en __init__ con anadir_incidencia
      ▼
 main.py · anadir_incidencia()
      │  leer_formulario(): los cinco datos del formulario
      │  si no hay título: aviso y termina
      ▼
 bd.py · insertar_incidencia(...)  ──►  INSERT INTO incidencias …  ──►  bugtracker.db
      │
      ▼
 main.py · cargar_incidencias()
      │  bd.obtener_incidencias()  ──►  SELECT … FROM incidencias  ──►  todas las filas
      │  vacía la tabla y añade una fila por incidencia
      ▼
 la tabla se redibuja, se limpia el formulario y la barra de estado dice «Incidencia añadida»
```

Busca en `main.py` las funciones `__init__`, `anadir_incidencia`, `leer_formulario` y `cargar_incidencias`, y en `bd.py` las funciones `insertar_incidencia` y `obtener_incidencias`, y sigue el recorrido en el código.

**Comprueba que…** sabes decir qué archivo o archivos habría que tocar para:

- cambiar el texto del botón «Añadir»;
- que haya un estado nuevo, «Cerrada»;
- guardar también la fecha de cada incidencia.

### 4.5 · Dónde encaja el explorador

`explorador.py` está en la misma carpeta que la aplicación, pero **no forma parte de ella**: `main.py` no lo importa y el explorador no abre ninguna ventana. Es un programa de terminal que se conecta con la plantilla de dos formas:

```
 explorador.py ── lee como texto (os, open) ──►  main.py, bd.py, dialogo.py, …, bugtracker.ui, requirements.txt
       │
       └── import bd ──► bd.py ──► bugtracker.db ◄── bd.py ◄── main.py (la ventana)
```

1. **Lee los archivos de la plantilla como texto**, igual que se leen en VS Code: los lista, cuenta sus líneas y busca las líneas que empiezan por `class`, `def` o `import`. No los ejecuta ni los cambia.
2. **Importa `bd.py`** y usa sus funciones para leer **la misma base de datos** que la ventana. Puede hacerlo sin PySide6 gracias a la regla de separación: `bd.py` no depende de nada de Qt.

Por eso:

- lo que se añade en la ventana, el explorador lo cuenta: los dos leen el mismo `bugtracker.db`;
- el explorador tiene que estar **en la misma carpeta** que `bd.py`: si se mueve a otra, `import bd` falla con `ModuleNotFoundError: No module named 'bd'`.

---

## Parte 5 · El explorador: un programa que lee el proyecto

`explorador.py` es un programa de terminal, sin ventanas. Lee los archivos de la carpeta del BugTracker y su base de datos, y responde a cinco órdenes.

Se ejecuta en la terminal de VS Code, en la carpeta `bugtracker` y con `(.venv)` delante. Abre `explorador.py` en VS Code para leerlo mientras lo ejecutas: está dividido en cuatro bloques numerados en los comentarios.

### Paso 5.1 · Ejecutar sin nada: `sys.argv` y `sys.exit`

```bash
python explorador.py
```

Sale la ayuda y, al final, `sys.argv = ['explorador.py']`.

**Lee** la función `main()` (bloque 4).

- `sys.argv` es la **lista de lo que se escribe en la orden**, separado por espacios. El primer elemento es el nombre del programa. Con `python explorador.py incidencias Pendiente` sería `['explorador.py', 'incidencias', 'Pendiente']`.
- `__doc__` es el texto entre `"""` del principio del archivo: su documentación.
- `sys.exit(1)` termina el programa. El número le dice al sistema cómo terminó: `0` es que todo fue bien y otro número, que no.
- En `main.py` aparecen los dos: `QApplication(sys.argv)` pasa los argumentos a Qt, y `sys.exit(app.exec())` termina el programa cuando se cierra la ventana.

**Comprueba que…** sabes qué valdría `sys.argv` con `python explorador.py estructura` y con `python explorador.py incidencias "En proceso"` (las comillas hacen que `En proceso` sea un solo elemento).

### Paso 5.2 · Los archivos de la carpeta: `import` y `os`

```bash
python explorador.py archivos
```

Sale cada archivo con su tamaño, para qué sirve y, si es `.py`, sus líneas.

**Lee** el bloque 1 y la función `leer_archivos()`.

- `import os` carga un **módulo**: un archivo de Python con funciones ya hechas. `os` sirve para trabajar con archivos y carpetas. Después se usa con un punto: `os.listdir(...)`.
- `import bd` carga **nuestro** `bd.py`. Python lo encuentra porque busca primero en la carpeta del programa que se ejecuta.
- Funciones de `os` que aparecen:

  | Función | Qué hace |
  |---|---|
  | `os.listdir(carpeta)` | Lista con los nombres de lo que hay en la carpeta |
  | `os.path.join(carpeta, nombre)` | Une carpeta y nombre con la barra correcta del sistema (`\` en Windows, `/` en Linux) |
  | `os.path.isdir(ruta)` | `True` si es una carpeta |
  | `os.path.getsize(ruta)` | Tamaño en bytes |
  | `os.path.exists(ruta)` | `True` si existe |
  | `os.path.abspath(__file__)` y `os.path.dirname(…)` | Ruta completa de este archivo y la carpeta donde está |

- `DESCRIPCIONES` es un **diccionario**: guarda parejas clave → valor (`"bd.py"` → `"Acceso a la base de datos…"`). `DESCRIPCIONES.get(nombre, "(sin descripción)")` devuelve el valor o, si la clave no está, el segundo argumento.
- `bd.py` hace lo mismo que `CARPETA` de otra forma, con el módulo `pathlib`: `Path(__file__).with_name("bugtracker.db")`. Las dos formas sirven para que la ruta no dependa de desde dónde se ejecute.

**Comprueba que…** sabes explicar por qué `bugtracker.db` sale sin número de líneas y por qué no salen las carpetas (como `__pycache__`).

### Paso 5.3 · Clases y funciones de cada archivo: clases y herencia

```bash
python explorador.py estructura
```

Sale cada `.py` con sus clases (y los métodos de cada una) y sus funciones.

**Lee** el bloque 2: las clases `Archivo` y `ArchivoPython`.

- Una **clase** es un molde. Cada **objeto** creado con ella (`Archivo("bd.py")`) tiene sus propios datos (**atributos**: `self.nombre`, `self.tamano`) y puede hacer cosas (**métodos**: `descripcion()`).
- `__init__` se ejecuta al crear el objeto. `self` es el propio objeto: `self.nombre = nombre` guarda el dato **en ese objeto**.
- `__str__` decide lo que sale al hacer `print(objeto)` o `str(objeto)`.
- `class ArchivoPython(Archivo)` es **herencia**: un `ArchivoPython` es un `Archivo` con algo más (lee sus líneas y sabe buscar clases, funciones e imports). `super().__init__(nombre)` ejecuta primero el `__init__` de `Archivo`.
- `isinstance(archivo, ArchivoPython)` pregunta si un objeto es de esa clase.

Lo mismo en el BugTracker, en `main.py`:

```python
class VentanaPrincipal(QMainWindow):      # una VentanaPrincipal es una QMainWindow de Qt con algo más
    def __init__(self):
        super().__init__()                # primero, lo que hace QMainWindow
        self.ui = Ui_VentanaPrincipal()   # atributo: el diseño de la ventana
```

**Comprueba que…** en la salida de `estructura` sabes señalar qué clases heredan de una clase de Qt y qué archivos solo tienen funciones (sin clases), y sabes explicar por qué `bd.py` es uno de ellos.

### Paso 5.4 · Quién importa a quién: listas

```bash
python explorador.py dependencias
```

Sale, para cada archivo, qué archivos del proyecto usa y qué librerías.

**Lee** `importa()` y `orden_dependencias()`.

- Una **lista** guarda valores en orden: `[]` vacía, `.append(x)` añade al final, `len(lista)` cuenta.
- `[a.nombre[:-3] for a in archivos]` es una **lista por comprensión**: una lista nueva hecha recorriendo otra. `nombre[:-3]` quita los tres últimos caracteres (`"bd.py"` → `"bd"`).
- `", ".join(lista)` une los elementos con comas; `lista or "-"` pone `-` si la lista está vacía.

**Comprueba que…** la salida coincide con el diagrama del apartado 4.2, y sabes explicar por qué `bd.py` no usa PySide6 y `main.py` no usa `sqlite3` para hacer consultas (solo para reconocer sus errores).

### Paso 5.5 · La base de datos: usar `bd.py` desde otro programa

```bash
python explorador.py incidencias
python explorador.py incidencias Pendiente
python explorador.py incidencias "En proceso"
```

Salen cuántas incidencias hay por estado, prioridad y tipo y, si se indica un estado, sus incidencias. Si no existiera `bugtracker.db`, avisaría de que hay que crearla con `python datos_ejemplo.py`.

**Lee** `contar()` y `orden_incidencias()`.

- `bd.obtener_incidencias()` es **la misma función que usa la ventana** en `cargar_incidencias()`. El explorador no tiene SQL: usa `bd.py`, como pide la regla de separación.
- Cada incidencia se lee por nombre, `incidencia["estado"]`, gracias a `row_factory = sqlite3.Row` en `bd.conectar()`.
- `try: … except sqlite3.Error as error:` intenta algo y, si falla con ese tipo de error, hace otra cosa en lugar de terminar el programa. Es el mismo esquema que `cargar_incidencias()` en `main.py`, que muestra un `QMessageBox` en lugar de un texto.
- `cuenta[valor] = cuenta.get(valor, 0) + 1` suma uno al contador de ese valor, empezando en 0 si es la primera vez.
- El filtro por estado se hace **en Python**, recorriendo todas las incidencias. También se puede hacer **en SQL**, con `WHERE estado = ?`, para que la base de datos devuelva solo esas.

**Comprueba que…** los números coinciden con lo que se ve en la tabla del BugTracker (`python main.py`) y, si añades una incidencia desde la ventana, el explorador la cuenta.

### Paso 5.6 · Guardar un informe: escribir archivos

```bash
python explorador.py informe
```

Crea la carpeta `informes` y dentro `informe.txt`, con la salida de las cuatro órdenes anteriores.

**Lee** `orden_informe()` y el diccionario `ORDENES`.

- `os.makedirs(carpeta, exist_ok=True)` crea la carpeta; `exist_ok=True` evita el error si ya existe.
- `with open(ruta, "w", encoding="utf-8") as f:` abre el archivo para **escribir** (`"w"`) y lo cierra solo al acabar el bloque. `ArchivoPython` usa lo mismo para **leer** (sin `"w"`). `encoding="utf-8"` hace que las tildes se guarden bien.
- `ORDENES` guarda **funciones** como valores: `ORDENES["archivos"]` es la función `orden_archivos`, y `orden()` la ejecuta. Es parecido a lo que hace `connect` en Qt: `btnAnadir.clicked.connect(self.anadir_incidencia)` guarda la función para ejecutarla al pulsar.

**Comprueba que…** existe `informes/informe.txt` y tiene las cuatro partes.

### Paso 5.7 · `if __name__ == "__main__":`

**Lee** las dos últimas líneas de `explorador.py`, de `datos_ejemplo.py` y de `main.py`.

- Al ejecutar un archivo (`python explorador.py`), Python le pone el nombre `"__main__"` y el bloque se ejecuta.
- Al **importarlo** desde otro (`import bd`), su nombre es el del módulo (`"bd"`) y el bloque **no** se ejecuta.
- Por eso `bd.py` no lo necesita (solo se importa) y `main.py` sí (es el que se ejecuta).

**Comprueba que…** sabes explicar qué pasaría si `datos_ejemplo.py` no tuviera ese `if` y otro archivo hiciera `import datos_ejemplo`.

---

## Cómo comprobarlo (lista final)

| Comprobación | Hecho |
|---|---|
| Instalé el BugTracker en su carpeta, con su entorno virtual y sus dependencias, y arranca |  |
| Sé qué es un entorno virtual, qué hace `pip install -r requirements.txt` y qué librerías instala |  |
| Sé para qué sirve cada archivo del BugTracker y cuál no se edita a mano |  |
| Sé usar el BugTracker y qué campos tiene una incidencia |  |
| Sé dibujar quién importa a quién y explicar la regla de separación |  |
| Sé seguir en el código lo que pasa al pulsar «Añadir», de la ventana a la base de datos y vuelta |  |
| Sé cómo se conecta el explorador con la plantilla y por qué tiene que estar en su carpeta |  |
| Sé qué es `sys.argv` y qué hace `sys.exit` |  |
| Sé qué hace un `import` y por qué Python encuentra `bd.py` |  |
| Sé usar las funciones de `os` de la tabla del paso 5.2 |  |
| Sé explicar una clase con `__init__`, `self`, atributos y métodos, y la herencia con `super().__init__()` |  |
| Sé leer listas, diccionarios y listas por comprensión |  |
| Sé qué hace `try`/`except` y lo reconozco en `main.py` |  |
| Sé para qué sirve `if __name__ == "__main__":` |  |
