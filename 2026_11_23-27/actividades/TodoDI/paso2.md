# TodoDI · paso 2: la lista de tareas

Se parte del paso 1: la ventana con el botón «Añadir tarea». Ahora se añaden un **campo de texto**, para escribir la tarea, y una **lista**, debajo del botón, donde se van mostrando. Al pulsar el botón, lo escrito pasa a la lista y el campo se vacía. Todavía no hay base de datos: las tareas solo existen mientras la ventana está abierta, y al cerrarla se pierden.

## 1 · Los cambios respecto al paso 1

Todo el cambio va en **`ventana.py`**; `main.py` se queda igual. Son cuatro cambios, y en cada uno se ve lo que había en el paso 1 y cómo queda.

### Cambio 1 · Importar los dos controles nuevos

`QLineEdit` es el campo de texto de una línea, y `QListWidget`, la lista. Se añaden a la línea de importación, que mantiene el orden alfabético:

```python
# Paso 1
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget
```

```python
# Paso 2
from PySide6.QtWidgets import QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget
```

### Cambio 2 · Crear el campo y la lista

En el `__init__`, junto al botón, se crean el campo y la lista. Los dos van con `self`, porque el método `anadir_tarea` los va a usar:

```python
# Paso 1
        self.boton = QPushButton("Añadir tarea")
```

```python
# Paso 2
        self.campo = QLineEdit()
        self.boton = QPushButton("Añadir tarea")
        self.lista = QListWidget()
```

### Cambio 3 · Colocarlos en la distribución

Se añaden a la distribución en el orden en que se ven, de arriba abajo: el campo, el botón y la lista:

```python
# Paso 1
        capa = QVBoxLayout(self)
        capa.addWidget(self.boton)
```

```python
# Paso 2
        capa = QVBoxLayout(self)
        capa.addWidget(self.campo)
        capa.addWidget(self.boton)
        capa.addWidget(self.lista)
```

La conexión del botón, `self.boton.clicked.connect(self.anadir_tarea)`, **no cambia**: el botón sigue llamando al mismo método. Lo que cambia es lo que hace ese método.

### Cambio 4 · Lo que hace el botón

En el paso 1, `anadir_tarea` solo escribía en la terminal. Ahora lee el texto del campo, le quita los espacios del principio y del final con `strip()` y, si no queda vacío, lo añade a la lista y vacía el campo:

```python
# Paso 1
    def anadir_tarea(self):
        print("Añadir tarea")
```

```python
# Paso 2
    def anadir_tarea(self):
        texto = self.campo.text().strip()
        if texto:
            self.lista.addItem(texto)
            self.campo.clear()
```

### `ventana.py` completo

Con los cuatro cambios, el archivo queda así:

```python
from PySide6.QtWidgets import QLineEdit, QListWidget, QPushButton, QVBoxLayout, QWidget
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
    def anadir_tarea(self):
        texto = self.campo.text().strip()
        if texto:
            self.lista.addItem(texto)
            self.campo.clear()
```

## 2 · Comprobar

```bat
python main.py
```

- La ventana tiene, de arriba abajo, el campo de texto, el botón y la lista, que ocupa el resto del espacio.
- Al escribir una tarea y pulsar el botón, la tarea aparece al final de la lista y el campo se vacía.
- Con el campo vacío, o con solo espacios, el botón no añade nada.
- Al cerrar la ventana y volver a abrirla, la lista está vacía: las tareas no se guardan.

## Preguntas y respuestas

**1. ¿Por qué el campo y la lista se guardan con `self` y la distribución no?**

Porque `anadir_tarea` necesita leer el campo y añadir a la lista, y es otro método: solo puede llegar a ellos si están guardados en la ventana, con `self`. La distribución solo se usa en el `__init__`.

**2. ¿Por qué el orden de los `addWidget` importa?**

Porque `QVBoxLayout` coloca los controles uno debajo de otro, en el orden en que se añaden. Cambiando el orden, cambia la ventana sin tocar nada más.

**3. ¿Para qué sirve `strip()`?**

Quita los espacios del principio y del final. Así, un texto con solo espacios se queda vacío y no se añade como tarea, y «  Repasar DI  » se guarda como «Repasar DI».

**4. ¿Qué es `if texto:`?**

En Python, un texto vacío cuenta como falso. `if texto:` significa «si hay algo escrito».

**5. ¿Por qué se pierden las tareas al cerrar la ventana?**

Porque solo están en la lista de la ventana, en la memoria del programa. Al cerrar, el programa termina y la memoria se libera. Para conservarlas hay que guardarlas en algún sitio, por ejemplo en una base de datos: será un paso posterior.
