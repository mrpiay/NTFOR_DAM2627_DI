# TodoDI · paso 3: guardar las tareas en una base de datos

Se parte del paso 2: el campo, el botón y la lista, con las tareas solo en memoria. Ahora, cada tarea que se añade se **guarda en una base de datos SQLite**, en el archivo `tareas.db`, y al abrir la aplicación se **cargan** las que ya había. Así, las tareas siguen ahí después de cerrar la ventana.

Hacen falta las dos cosas: si solo se guardaran, la lista seguiría saliendo vacía al abrir, aunque las tareas estuvieran en la base de datos.

## 1 · Los cambios respecto al paso 2

Hay un archivo nuevo, **`bd.py`**, con todo lo que tiene que ver con la base de datos. `ventana.py` y `main.py` no llevan SQL: le piden a `bd.py` lo que necesitan. Son cinco cambios.

### Cambio 1 · Un archivo nuevo: `bd.py`

Crea `bd.py` en la carpeta del proyecto. Usa `sqlite3`, que viene con Python: no hay que instalar nada.

Cualquier operación con la base de datos son los mismos pasos: abrir la conexión (`connect`), ejecutar la consulta (`execute`), confirmar los cambios (`commit`; sin él, no se guardan) y cerrar la conexión (`close`). Para no repetirlos en cada función, van una sola vez en una **función auxiliar**, `ejecutar_sql`, y las demás la usan:

| Función | Qué hace |
|---|---|
| `ejecutar_sql(sql, valores)` | La auxiliar: abre la conexión, ejecuta la consulta con sus valores, confirma, cierra y devuelve las filas que haya dado la consulta (ninguna, si no es un `SELECT`). `valores=()` quiere decir que, si no se pasan valores, no hay ninguno |
| `crear_bd()` | Crea la tabla `tareas`, con un `id` que la base de datos numera sola y el `texto` de la tarea. `IF NOT EXISTS`: si la tabla ya existe, no hace nada |
| `insertar_tarea(texto)` | Guarda una tarea nueva. El texto va en el `?`, no pegado dentro del SQL |
| `obtener_tareas()` | Devuelve una lista con los textos de todas las tareas, en el orden en que se añadieron |

```python
# bd.py (nuevo)
import sqlite3
RUTA = "tareas.db"
def ejecutar_sql(sql, valores=()):
    # Abre la conexión con la base de datos (si el archivo no existe, lo crea)
    conexion = sqlite3.connect(RUTA)
    # Ejecuta la consulta, con los valores en el lugar de los ?
    cursor = conexion.execute(sql, valores)
    # Lee todas las filas del resultado ([] si la consulta no devuelve filas)
    filas = cursor.fetchall()
    # Confirma los cambios: sin esto, no se guardan
    conexion.commit()
    # Cierra la conexión
    conexion.close()
    return filas
def crear_bd():
    ejecutar_sql("CREATE TABLE IF NOT EXISTS tareas (id INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT NOT NULL)")
def insertar_tarea(texto):
    ejecutar_sql("INSERT INTO tareas (texto) VALUES (?)", (texto,))
def obtener_tareas():
    filas = ejecutar_sql("SELECT texto FROM tareas ORDER BY id")
    return [fila[0] for fila in filas]
```

`execute` manda la consulta a la base de datos, con los valores en el lugar de los `?`, y devuelve un **cursor**: un objeto que apunta a los resultados, todavía sin leer. `cursor.fetchall()` lee **todas** las filas del resultado y las devuelve en una lista, en la que cada fila es una tupla con las columnas pedidas:

| Consulta | `filas` |
|---|---|
| `SELECT texto FROM tareas ORDER BY id` | `[('Estudiar SI',), ('Repasar DI',)]`: una tupla por tarea, con un solo elemento, el texto |
| `INSERT` o `CREATE TABLE` | `[]`: estas consultas no devuelven filas |

Por eso `ejecutar_sql` sirve para todas las consultas, y por eso `obtener_tareas` hace `[fila[0] for fila in filas]`: de cada tupla `('Estudiar SI',)` se queda con su primer elemento, el texto.

### Cambio 2 · `main.py`: crear la base de datos al arrancar

Antes de crear la ventana, la tabla tiene que existir, porque la ventana va a leer de ella nada más crearse:

```python
# Paso 2
from PySide6.QtWidgets import QApplication
from ventana import VentanaTodo
app = QApplication()
```

```python
# Paso 3
from PySide6.QtWidgets import QApplication
import bd
from ventana import VentanaTodo
bd.crear_bd()
app = QApplication()
```

### Cambio 3 · `ventana.py`: importar `bd`

La ventana usa las funciones de `bd.py`, así que lo importa, debajo de la línea de PySide6:

```python
# Paso 2
from PySide6.QtWidgets import QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget
```

```python
# Paso 3
from PySide6.QtWidgets import QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget
import bd
```

### Cambio 4 · `ventana.py`: cargar las tareas al abrir

Al final del `__init__`, cuando la lista ya existe, se añaden a ella las tareas guardadas:

```python
# Paso 3 (nuevo, al final del __init__)
        for texto in bd.obtener_tareas():
            self.lista.addItem(texto)
```

### Cambio 5 · `ventana.py`: guardar al añadir

En `anadir_tarea`, antes de añadir la tarea a la lista, se guarda en la base de datos:

```python
# Paso 2
        if texto:
            self.lista.addItem(texto)
            self.campo.clear()
```

```python
# Paso 3
        if texto:
            bd.insertar_tarea(texto)
            self.lista.addItem(texto)
            self.campo.clear()
```

### Los tres archivos completos

`bd.py` está completo en el cambio 1. `ventana.py` queda así:

```python
from PySide6.QtWidgets import QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget
import bd
class VentanaTodo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TodoDI")
        self.resize(400, 300)
        self.campo = QLineEdit()
        self.boton = QPushButton("Añadir tarea")
        self.lista = QListWidget()
        capa = QVBoxLayout(self)
        capa.addWidget(self.campo)
        capa.addWidget(self.boton)
        capa.addWidget(self.lista)
        self.boton.clicked.connect(self.anadir_tarea)
        for texto in bd.obtener_tareas():
            self.lista.addItem(texto)
    def anadir_tarea(self):
        texto = self.campo.text().strip()
        if texto:
            bd.insertar_tarea(texto)
            self.lista.addItem(texto)
            self.campo.clear()
```

Y `main.py`:

```python
from PySide6.QtWidgets import QApplication
import bd
from ventana import VentanaTodo
bd.crear_bd()
app = QApplication()
ventana = VentanaTodo()
ventana.show()
app.exec()
```

## 2 · Comprobar

Ejecuta la aplicación **desde la carpeta del proyecto**, porque `tareas.db` se crea en la carpeta desde la que se lanza:

```bat
python main.py
```

- La primera vez, la lista está vacía y aparece el archivo `tareas.db` en la carpeta del proyecto.
- Al añadir tareas, aparecen en la lista como en el paso 2.
- Al cerrar la ventana y volver a abrirla, **las tareas siguen ahí**, en el mismo orden.
- Una tarea vacía, o con solo espacios, sigue sin añadirse, ni a la lista ni a la base de datos.

## Preguntas y respuestas

**1. ¿Por qué el SQL va en un archivo aparte, `bd.py`?**

Para separar responsabilidades: `ventana.py` se ocupa de la interfaz y `bd.py`, de los datos. Si mañana las tareas se guardaran de otra forma, solo cambiaría `bd.py`; la ventana seguiría llamando a las mismas funciones.

**2. ¿Por qué el texto va en un `?` y no pegado dentro del SQL?**

Con `?`, `sqlite3` pasa el texto aparte, como un valor. Si se pegara dentro de la consulta, una tarea con un apóstrofo, como `Revisar l'agenda`, rompería el SQL, porque en SQL los textos van entre comillas simples, y alguien podría escribir algo que se ejecutara como SQL: es la **inyección SQL**.

**3. ¿Por qué `(texto,)` lleva una coma?**

Porque `execute` espera los valores en una tupla, aunque solo haya uno. `(texto)` es solo `texto` entre paréntesis; `(texto,)`, con la coma, es una tupla de un elemento.

**4. ¿Para qué sirve `IF NOT EXISTS`?**

`crear_bd()` se ejecuta cada vez que se abre la aplicación. La primera vez crea la tabla; las siguientes, como ya existe, no hace nada. Sin `IF NOT EXISTS`, la segunda vez daría un error porque la tabla ya está creada.

**5. ¿Qué pasa si se olvida el `commit()`?**

La tarea no se guarda: al cerrar la conexión sin confirmar, SQLite descarta los cambios. Al volver a abrir la aplicación, la tarea no estaría.

**6. ¿Para qué sirve la función auxiliar `ejecutar_sql`?**

Para no repetir lo mismo en cada función: abrir, ejecutar, confirmar y cerrar están escritos una sola vez. Las funciones quedan en una línea, se ve mejor qué consulta hace cada una y, si hubiera que cambiar algo de la conexión (por ejemplo, el archivo de la base de datos), se cambia en un solo sitio.

**7. ¿Por qué se llama a `bd.crear_bd()` en `main.py` y antes de crear la ventana?**

Porque la ventana, al crearse, lee las tareas de la tabla. Si la tabla no existiera todavía, `obtener_tareas()` fallaría. Y va en `main.py` porque es preparar la aplicación antes de arrancarla, no parte de la ventana.

**8. La tabla tiene un `id` que todavía no se usa: ¿para qué sirve?**

Identifica cada tarea aunque haya dos con el mismo texto. Hará falta para **eliminar** una tarea concreta: será un paso posterior.
