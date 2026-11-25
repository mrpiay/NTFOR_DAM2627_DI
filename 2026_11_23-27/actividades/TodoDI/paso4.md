# TodoDI · paso 4: eliminar tareas

Se parte del paso 3: las tareas se guardan en `tareas.db` y se cargan al abrir. Ahora, debajo de la lista, hay un botón **«Eliminar tarea»** que borra la tarea elegida, de la lista y de la base de datos. El botón solo está **activado** cuando hay una tarea elegida; si no, está desactivado y no se puede pulsar.

## Antes de empezar: cómo se sabe qué tarea borrar

### El problema: hace falta el `id`

En la base de datos, cada tarea tiene su `id` (paso 3). Para borrar la tarea elegida, hay que decirle a la base de datos **qué `id`** borrar. Por el texto no sirve, porque puede haber dos tareas que se llamen igual:

| id | texto |
|---|---|
| 1 | Estudiar SI |
| 2 | Repasar DI |
| 3 | Estudiar SI |

Si se elige la tercera fila y se borra «la tarea que se llama Estudiar SI», se borrarían la 1 y la 3. Hay que borrar **la que tiene el `id` 3**.

Pero la lista de la ventana solo muestra el texto. ¿Dónde se guarda el `id` de cada fila, para saberlo al pulsar «Eliminar tarea»?

### La solución: cada fila de la lista guarda varios datos

Cada fila de un `QListWidget` es un objeto `QListWidgetItem`, y no guarda solo el texto que se ve: puede guardar **varios datos**, cada uno con una **etiqueta** que dice para qué sirve. Qt llama a esas etiquetas **roles** (`Qt.ItemDataRole`). Los que importan aquí:

| Rol | Para qué sirve | En la tercera fila |
|---|---|---|
| `DisplayRole` | El texto que **se ve** en la lista | `'Estudiar SI'` |
| `UserRole` | Un hueco libre para lo que necesite la aplicación; **no se ve** | `3`, el `id` de la tarea |

Es como una ficha con varias casillas: en una va lo que se enseña y en otra, apuntado para uso propio, el `id`. Con dos métodos se escribe y se lee cada casilla:

```python
# Escribir: en la casilla UserRole de la fila, el id 3
elemento.setData(Qt.ItemDataRole.UserRole, 3)
# Leer: lo que hay en la casilla UserRole de la fila (devuelve 3)
id_tarea = elemento.data(Qt.ItemDataRole.UserRole)
```

El texto ya va en `DisplayRole` al crear la fila con `QListWidgetItem('Estudiar SI')`: es lo que hacía `addItem(texto)` por dentro en los pasos anteriores.

### Lo que hay que cambiar

- `obtener_tareas` devuelve también el `id` de cada tarea, y hay una función nueva para borrar por `id`.
- Al cargar la lista, cada fila guarda el `id` de su tarea en `UserRole`.
- Después de añadir o eliminar, la lista **se vuelve a cargar** desde la base de datos. Así cada fila tiene siempre su `id`, también la de una tarea recién añadida, cuyo `id` lo pone la base de datos al guardarla.

## 1 · Los cambios respecto al paso 3

`main.py` se queda igual. Hay un cambio en `bd.py` y el resto en `ventana.py`.

### Cambio 1 · `bd.py`: el `id` de cada tarea y borrar

`obtener_tareas` pide a la base de datos el `id` y el texto, y devuelve las filas tal cual: una lista de tuplas `(id, texto)`, por ejemplo `[(1, 'Estudiar SI'), (2, 'Repasar DI')]`. Y una función nueva, `eliminar_tarea`, borra la tarea con ese `id`:

```python
# Paso 3
def obtener_tareas():
    filas = ejecutar_sql("SELECT texto FROM tareas ORDER BY id")
    return [fila[0] for fila in filas]
```

```python
# Paso 4
def obtener_tareas():
    # Devuelve una tupla (id, texto) por tarea, en el orden en que se añadieron
    return ejecutar_sql("SELECT id, texto FROM tareas ORDER BY id")
def eliminar_tarea(id_tarea):
    # Borra solo la tarea con ese id
    ejecutar_sql("DELETE FROM tareas WHERE id = ?", (id_tarea,))
```

### Cambio 2 · `ventana.py`: importar lo nuevo

`QListWidgetItem` es una fila de la lista: hace falta crearla a mano para poder guardar el `id` en ella. `Qt`, de `PySide6.QtCore`, tiene las constantes de Qt; entre ellas, los roles:

```python
# Paso 3
from PySide6.QtWidgets import QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget
```

```python
# Paso 4
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget
```

### Cambio 3 · Dos botones: cada uno con su nombre

Con dos botones, `self.boton` ya no dice cuál es. Pasa a llamarse `self.boton_anadir`, y el nuevo, `self.boton_eliminar`, se crea después de la lista y se coloca debajo de ella:

```python
# Paso 3
        self.boton = QPushButton("Añadir tarea")
        self.lista = QListWidget()
        capa = QVBoxLayout(self)
        capa.addWidget(self.campo)
        capa.addWidget(self.boton)
        capa.addWidget(self.lista)
        self.boton.clicked.connect(self.anadir_tarea)
```

```python
# Paso 4
        self.boton_anadir = QPushButton("Añadir tarea")
        self.lista = QListWidget()
        # El botón nuevo, para borrar la tarea elegida
        self.boton_eliminar = QPushButton("Eliminar tarea")
        capa = QVBoxLayout(self)
        capa.addWidget(self.campo)
        capa.addWidget(self.boton_anadir)
        capa.addWidget(self.lista)
        # Debajo de la lista
        capa.addWidget(self.boton_eliminar)
        self.boton_anadir.clicked.connect(self.anadir_tarea)
```

### Cambio 4 · Las dos conexiones nuevas

El botón «Eliminar tarea» se conecta con el método que borra. Y la lista emite la señal `itemSelectionChanged` cada vez que cambia la selección (se elige una tarea, se elige otra o no queda ninguna): se conecta con el método que activa o desactiva el botón:

```python
# Paso 4 (nuevo, después de la conexión de boton_anadir)
        # Al pulsar «Eliminar tarea», se borra la tarea elegida
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)
        # Cada vez que cambia la selección, se activa o desactiva el botón
        self.lista.itemSelectionChanged.connect(self.actualizar_boton_eliminar)
```

### Cambio 5 · Cargar la lista en un método propio

En el paso 3, las tareas se cargaban con un `for` al final del `__init__`. Ahora hay que cargarlas también después de añadir y de eliminar, así que el `for` pasa a un método propio, `cargar_tareas`, y el `__init__` lo llama. Además, cada fila guarda ahora el `id` de su tarea:

```python
# Paso 3 (al final del __init__)
        for texto in bd.obtener_tareas():
            self.lista.addItem(texto)
```

```python
# Paso 4 (al final del __init__)
        self.cargar_tareas()
```

```python
# Paso 4 (método nuevo)
    def cargar_tareas(self):
        # Vacía la lista, para no repetir las tareas que ya estaban
        self.lista.clear()
        # Cada tarea llega como una tupla (id, texto), que se reparte en dos variables
        for id_tarea, texto in bd.obtener_tareas():
            # Una fila nueva con el texto que se ve (DisplayRole)
            elemento = QListWidgetItem(texto)
            # En la casilla oculta de la fila (UserRole), el id de la tarea
            elemento.setData(Qt.ItemDataRole.UserRole, id_tarea)
            self.lista.addItem(elemento)
        # Después de cargar no hay ninguna tarea elegida: el botón se desactiva
        self.actualizar_boton_eliminar()
```

### Cambio 6 · Activar o desactivar el botón

Un método nuevo: si hay alguna tarea elegida, activa el botón; si no, lo desactiva:

```python
# Paso 4 (método nuevo)
    def actualizar_boton_eliminar(self):
        # selectedItems() devuelve las filas elegidas: una lista vacía si no hay ninguna
        hay_seleccion = len(self.lista.selectedItems()) > 0
        # True activa el botón; False lo desactiva
        self.boton_eliminar.setEnabled(hay_seleccion)
```

### Cambio 7 · Añadir: volver a cargar en lugar de añadir a mano

Después de guardar la tarea, en lugar de añadirla a la lista con `addItem`, se vuelve a cargar la lista, para que la fila nueva lleve su `id`:

```python
# Paso 3
            bd.insertar_tarea(texto)
            self.lista.addItem(texto)
            self.campo.clear()
```

```python
# Paso 4
            bd.insertar_tarea(texto)
            # Se vuelve a cargar, para que la fila nueva lleve el id que le ha dado la base de datos
            self.cargar_tareas()
            self.campo.clear()
```

### Cambio 8 · Eliminar la tarea elegida

El método del botón «Eliminar tarea»: toma la fila elegida, lee de ella el `id`, la borra de la base de datos y vuelve a cargar la lista:

```python
# Paso 4 (método nuevo)
    def eliminar_tarea(self):
        # La fila elegida (siempre hay una: si no, el botón estaría desactivado)
        elemento = self.lista.selectedItems()[0]
        # El id guardado en su casilla oculta (UserRole)
        id_tarea = elemento.data(Qt.ItemDataRole.UserRole)
        # Se borra de la base de datos
        bd.eliminar_tarea(id_tarea)
        # Y se vuelve a cargar la lista, ya sin ella
        self.cargar_tareas()
```

### Los archivos completos

`bd.py`:

```python
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
    # Crea la tabla, si no existe: un id que se numera solo y el texto de la tarea
    ejecutar_sql("CREATE TABLE IF NOT EXISTS tareas (id INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT NOT NULL)")
def insertar_tarea(texto):
    # Guarda una tarea nueva; el texto va en el ?
    ejecutar_sql("INSERT INTO tareas (texto) VALUES (?)", (texto,))
def obtener_tareas():
    # Devuelve una tupla (id, texto) por tarea, en el orden en que se añadieron
    return ejecutar_sql("SELECT id, texto FROM tareas ORDER BY id")
def eliminar_tarea(id_tarea):
    # Borra solo la tarea con ese id
    ejecutar_sql("DELETE FROM tareas WHERE id = ?", (id_tarea,))
```

`ventana.py`:

```python
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget
import bd
class VentanaTodo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TodoDI")
        self.resize(400, 300)
        # Los controles, de arriba abajo
        self.campo = QLineEdit()
        self.boton_anadir = QPushButton("Añadir tarea")
        self.lista = QListWidget()
        self.boton_eliminar = QPushButton("Eliminar tarea")
        # La distribución: uno debajo de otro, en este orden
        capa = QVBoxLayout(self)
        capa.addWidget(self.campo)
        capa.addWidget(self.boton_anadir)
        capa.addWidget(self.lista)
        capa.addWidget(self.boton_eliminar)
        # Las señales: qué método se ejecuta con cada acción
        self.boton_anadir.clicked.connect(self.anadir_tarea)
        self.boton_eliminar.clicked.connect(self.eliminar_tarea)
        self.lista.itemSelectionChanged.connect(self.actualizar_boton_eliminar)
        # Las tareas guardadas, al abrir
        self.cargar_tareas()
    def cargar_tareas(self):
        # Vacía la lista, para no repetir las tareas que ya estaban
        self.lista.clear()
        # Cada tarea llega como una tupla (id, texto), que se reparte en dos variables
        for id_tarea, texto in bd.obtener_tareas():
            # Una fila nueva con el texto que se ve (DisplayRole)
            elemento = QListWidgetItem(texto)
            # En la casilla oculta de la fila (UserRole), el id de la tarea
            elemento.setData(Qt.ItemDataRole.UserRole, id_tarea)
            self.lista.addItem(elemento)
        # Después de cargar no hay ninguna tarea elegida: el botón se desactiva
        self.actualizar_boton_eliminar()
    def actualizar_boton_eliminar(self):
        # selectedItems() devuelve las filas elegidas: una lista vacía si no hay ninguna
        hay_seleccion = len(self.lista.selectedItems()) > 0
        # True activa el botón; False lo desactiva
        self.boton_eliminar.setEnabled(hay_seleccion)
    def anadir_tarea(self):
        # El texto escrito, sin espacios al principio ni al final
        texto = self.campo.text().strip()
        # Solo si hay algo escrito
        if texto:
            bd.insertar_tarea(texto)
            # Se vuelve a cargar, para que la fila nueva lleve el id que le ha dado la base de datos
            self.cargar_tareas()
            self.campo.clear()
    def eliminar_tarea(self):
        # La fila elegida (siempre hay una: si no, el botón estaría desactivado)
        elemento = self.lista.selectedItems()[0]
        # El id guardado en su casilla oculta (UserRole)
        id_tarea = elemento.data(Qt.ItemDataRole.UserRole)
        # Se borra de la base de datos
        bd.eliminar_tarea(id_tarea)
        # Y se vuelve a cargar la lista, ya sin ella
        self.cargar_tareas()
```

`main.py` no cambia.

## 2 · Comprobar

```bat
python main.py
```

- Debajo de la lista está el botón «Eliminar tarea», **desactivado** (en gris).
- Al hacer clic en una tarea, el botón se activa; al pulsarlo, la tarea desaparece y el botón vuelve a desactivarse.
- Para quitar la selección sin eliminar, **Ctrl + clic** en la tarea elegida: el botón se desactiva. Un clic normal en la misma tarea o en la zona vacía de la lista no quita la selección: es como funcionan las listas de Qt, igual que el Explorador de Windows.
- Con dos tareas que se llaman igual, se elimina **solo la elegida**.
- Al cerrar la ventana y volver a abrirla, la tarea eliminada sigue sin estar: se ha borrado también de la base de datos.

## Preguntas y respuestas

**1. ¿Por qué se borra por `id` y no por texto?**

Porque puede haber dos tareas con el mismo texto. `DELETE FROM tareas WHERE texto = ?` las borraría las dos; con el `id`, que es único, se borra solo la elegida.

**2. ¿Dónde se guarda el `id` de cada tarea, si en la lista solo se ve el texto?**

En la propia fila de la lista. Cada fila (`QListWidgetItem`) guarda varios datos, cada uno con un rol: en `DisplayRole`, el texto que se ve; en `UserRole`, el `id`, que no se ve. Se escribe con `setData(Qt.ItemDataRole.UserRole, id_tarea)` al cargar la lista y se lee con `data(Qt.ItemDataRole.UserRole)` al eliminar.

**3. ¿Por qué se vuelve a cargar la lista después de añadir?**

Porque el `id` de una tarea nueva lo pone la base de datos al guardarla. Si se añadiera a la lista a mano, como en el paso 3, esa fila no tendría `id` en `UserRole` y no se podría eliminar hasta volver a abrir la aplicación.

**4. ¿Por qué `cargar_tareas` empieza con `clear()`?**

Porque añade a la lista todas las tareas de la base de datos. Sin vaciarla antes, cada carga repetiría las que ya estaban.

**5. ¿Qué es `itemSelectionChanged` y por qué se usa?**

Es la señal que emite la lista cada vez que cambia la selección. Conectándola con `actualizar_boton_eliminar`, el botón se activa o desactiva solo, en el momento justo, sin comprobarlo en ningún otro sitio.

**6. ¿Por qué `eliminar_tarea` no comprueba si hay alguna tarea elegida?**

Porque el botón solo está activado cuando la hay. Desactivar lo que no se puede hacer es más claro para quien usa la aplicación que dejarlo pulsar y mostrarle un error.

**7. ¿Qué hace `for id_tarea, texto in bd.obtener_tareas():`?**

Cada elemento de la lista que devuelve `obtener_tareas` es una tupla de dos valores, `(id, texto)`. Al poner dos variables en el `for`, Python reparte cada tupla: el primer valor en `id_tarea` y el segundo en `texto`.
