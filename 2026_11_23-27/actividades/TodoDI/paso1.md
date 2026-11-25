# TodoDI · paso 1: un botón

TodoDI es una lista de tareas que se construye reutilizando MiniDI, añadiéndole una cosa en cada paso. En este primer paso, la ventana tiene un botón **«Añadir tarea»**. Todavía no hay lista ni base de datos: al pulsar el botón, la aplicación escribe «Añadir tarea» en la terminal. Así se comprueba que el botón está conectado con el código que se ejecutará al pulsarlo.

## 1 · Crear TodoDI a partir de MiniDI

Se copian solo los archivos del proyecto, sin el entorno virtual ni los ejecutables: un entorno virtual no funciona si se copia a otra carpeta, así que se crea uno nuevo.

En CMD:

```bat
robocopy C:\dam2627\di\MiniDI C:\dam2627\di\TodoDI main.py ventana.py requirements.txt
cd /d C:\dam2627\di\TodoDI
code .
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

`robocopy` copia de la primera carpeta a la segunda solo los archivos que se nombran, y crea la segunda si no existe.

## 2 · Los cambios respecto a MiniDI

Casi todo el cambio va en **`ventana.py`**, porque es lo que define cómo es la ventana. En **`main.py`** solo cambia el nombre de la clase. Son seis cambios, y en cada uno se ve lo que había en MiniDI y cómo queda.

### Cambio 1 · Importar el botón y la distribución

`QPushButton` es el botón, y `QVBoxLayout`, una distribución que coloca los controles uno debajo de otro. Se añaden a la línea de importación, que mantiene el orden alfabético:

```python
# MiniDI
from PySide6.QtWidgets import QWidget
```

```python
# Paso 1
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget
```

### Cambio 2 · El nombre de la clase y el título

La aplicación ya no es MiniDI, sino TodoDI: la clase pasa a llamarse `VentanaTodo` y la ventana, «TodoDI»:

```python
# MiniDI
class VentanaMini(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniDI")
```

```python
# Paso 1
class VentanaTodo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TodoDI")
```

### Cambio 3 · Crear el botón

Al final del `__init__`, se crea el botón con su texto. Se guarda con `self`, en `self.boton`, para que sea parte de la ventana y se pueda usar desde otros métodos:

```python
# MiniDI
        self.resize(400, 300)
```

```python
# Paso 1
        self.resize(400, 300)
        self.boton = QPushButton("Añadir tarea")
```

### Cambio 4 · Colocarlo en la distribución

Se crea la distribución sobre la ventana, `QVBoxLayout(self)`, y se le añade el botón. Sin distribución, el botón quedaría en una esquina y no se adaptaría al tamaño de la ventana:

```python
# Paso 1 (nuevo, detrás del botón)
        capa = QVBoxLayout(self)
        capa.addWidget(self.boton)
```

### Cambio 5 · Conectar el botón con un método

La **señal** `clicked`, que el botón emite al pulsarlo, se conecta con el método `anadir_tarea`, el **slot** que se ejecutará entonces. El método se pasa **sin paréntesis**: no se ejecuta ahora, sino cada vez que se pulse:

```python
# Paso 1 (nuevo, al final del __init__)
        self.boton.clicked.connect(self.anadir_tarea)
```

### Cambio 6 · El método del botón

Un método nuevo de la clase, después del `__init__`. Por ahora solo escribe un texto en la terminal, para comprobar que el botón funciona:

```python
# Paso 1 (nuevo, después del __init__)
    def anadir_tarea(self):
        print("Añadir tarea")
```

### `main.py`: el nombre de la clase

`main.py` importa y crea la ventana, así que cambia el nombre de la clase en esas dos líneas:

```python
# MiniDI
from ventana import VentanaMini
ventana = VentanaMini()
```

```python
# Paso 1
from ventana import VentanaTodo
ventana = VentanaTodo()
```

### Los dos archivos completos

Con todos los cambios, `ventana.py` queda así:

```python
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget
class VentanaTodo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TodoDI")
        self.resize(400, 300)
        self.boton = QPushButton("Añadir tarea")
        capa = QVBoxLayout(self)
        capa.addWidget(self.boton)
        self.boton.clicked.connect(self.anadir_tarea)
    def anadir_tarea(self):
        print("Añadir tarea")
```

Y `main.py`:

```python
from PySide6.QtWidgets import QApplication
from ventana import VentanaTodo
app = QApplication()
ventana = VentanaTodo()
ventana.show()
app.exec()
```

## 3 · Comprobar

```bat
python main.py
```

- La ventana se titula «TodoDI» y tiene el botón «Añadir tarea», que ocupa el ancho de la ventana.
- Cada vez que se pulsa el botón, aparece «Añadir tarea» en la terminal.
- Al cerrar la ventana, la terminal queda libre.

## Preguntas y respuestas

**1. ¿Por qué el cambio va en `ventana.py` y casi nada en `main.py`?**

Porque `ventana.py` define cómo es la ventana y qué hace, y el botón es parte de la ventana. `main.py` solo arranca la aplicación: únicamente cambia porque la clase tiene otro nombre.

**2. ¿Por qué el botón se guarda en `self.boton` y la distribución en `capa`, sin `self`?**

Con `self`, el botón queda guardado en la ventana y se puede usar desde otros métodos, por ejemplo para desactivarlo más adelante. La distribución solo se usa dentro del `__init__`, así que basta una variable local.

**3. ¿Qué hace `self.boton.clicked.connect(self.anadir_tarea)`?**

Conecta la **señal** `clicked`, que el botón emite al pulsarlo, con el **slot** `anadir_tarea`, el método que se ejecuta entonces. Es la forma de Qt de decir «cuando pase esto, haz aquello».

**4. ¿Qué pasaría si se escribiera `connect(self.anadir_tarea())`, con paréntesis?**

El método se ejecutaría una sola vez, al crear la ventana, y después se intentaría conectar lo que devuelve, `None`, que no es un método: `connect` da un error (`TypeError: Expected signal or callable, got "NoneType"`) y la ventana ni siquiera llega a abrirse.

**5. ¿Para qué sirve `QVBoxLayout`?**

Coloca los controles uno debajo de otro y los ajusta al tamaño de la ventana. Sin una distribución, el botón quedaría en la esquina y no se adaptaría al cambiar el tamaño. En el paso siguiente, la lista irá debajo del botón, en la misma distribución.
