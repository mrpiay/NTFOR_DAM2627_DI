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

## 2 · Añadir el botón

Todo el cambio va en **`ventana.py`**, porque es lo que define cómo es la ventana:

1. Importa también `QPushButton`, el botón, y `QVBoxLayout`, una distribución que coloca los controles uno debajo de otro.
2. Cambia el nombre de la clase a `VentanaTodo` y el título a «TodoDI».
3. En el `__init__`, crea el botón con su texto y guárdalo en `self.boton`, para poder usarlo desde otros métodos.
4. Crea la distribución sobre la ventana (`QVBoxLayout(self)`) y añádele el botón.
5. Conecta la señal `clicked` del botón con un método nuevo, `anadir_tarea`. Se pasa el método **sin paréntesis**: no se ejecuta ahora, sino cada vez que se pulse.
6. Escribe el método `anadir_tarea`, que por ahora solo escribe un texto en la terminal.

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

En **`main.py`** solo cambia el nombre de la clase, porque es la que importa y crea:

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

El método se ejecutaría una sola vez, al crear la ventana, y se conectaría lo que devuelve (`None`), no el método. El botón no haría nada al pulsarlo.

**5. ¿Para qué sirve `QVBoxLayout`?**

Coloca los controles uno debajo de otro y los ajusta al tamaño de la ventana. Sin una distribución, el botón quedaría en la esquina y no se adaptaría al cambiar el tamaño. En el paso siguiente, la lista irá debajo del botón, en la misma distribución.
