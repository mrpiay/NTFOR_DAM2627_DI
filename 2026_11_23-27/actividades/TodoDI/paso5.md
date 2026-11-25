# TodoDI · paso 5: los colores

Se parte del paso 4: TodoDI añade, guarda y elimina tareas. En este último paso se le da color:

| Control | Aspecto |
|---|---|
| El campo de texto | Fondo blanco |
| El botón «Añadir tarea» | Fondo azul y texto blanco |
| La lista | Fondo gris |
| El botón «Eliminar tarea» | Fondo rojo y texto blanco; rojo claro cuando está desactivado |

## Antes de empezar: las hojas de estilo de Qt

Qt da color y forma a los controles con **hojas de estilo**, en un lenguaje llamado **QSS** (*Qt Style Sheets*), muy parecido al CSS de las páginas web. Una hoja de estilo es un texto con **reglas**, y cada regla dice a qué control se aplica y qué propiedades le cambia:

```css
#boton_anadir {
    background-color: royalblue;
    color: white;
}
```

- `#boton_anadir` es el **selector**: a qué control se aplica la regla. El `#` seguido de un nombre elige el control que tiene ese nombre de objeto (*objectName*), que se le pone con `setObjectName`.
- Entre llaves, las **propiedades**, cada una con su valor y un `;` al final: `background-color` es el color de fondo, y `color`, el del texto.
- Los colores se pueden escribir por su nombre en inglés (`white`, `royalblue`, `lightgray`, `red`, `orange`…) o en hexadecimal (`#ff0000` es rojo).

Como con la base de datos, el aspecto va en **un archivo propio, `estilos.py`**, y la ventana solo lo aplica. Así, para cambiar los colores se toca un solo archivo, sin buscar por el código de la ventana.

## 1 · Los cambios respecto al paso 4

`main.py` y `bd.py` se quedan igual. Hay un archivo nuevo y dos cambios en `ventana.py`.

### Cambio 1 · Un archivo nuevo: `estilos.py`

Crea `estilos.py` en la carpeta del proyecto. Solo tiene una variable, `ESTILO`, con la hoja de estilo en un texto de varias líneas, entre `"""` triples:

```python
# estilos.py (nuevo)
# La hoja de estilo de TodoDI: el aspecto de cada control, en el lenguaje QSS de Qt.
# Cada regla empieza por # y el nombre del control (su objectName), y entre llaves sus propiedades.
ESTILO = """
#campo {
    background-color: white;
}
#boton_anadir {
    background-color: royalblue;
    color: white;
    border: none;
    padding: 6px;
}
#lista {
    background-color: lightgray;
}
#boton_eliminar {
    background-color: red;
    color: white;
    border: none;
    padding: 6px;
}
#boton_eliminar:disabled {
    background-color: lightcoral;
}
"""
```

| Propiedad | Qué hace |
|---|---|
| `background-color` | El color de fondo |
| `color` | El color del texto |
| `border: none` | Quita el borde que pone el sistema: el botón queda plano, solo con su color |
| `padding: 6px` | Deja 6 píxeles de margen entre el texto y el borde del botón, para que no quede tan apretado |

`#boton_eliminar:disabled` es una regla para el botón **solo cuando está desactivado**: `:disabled` es un **estado**. Con un rojo más claro, el botón sigue pareciendo desactivado; si fuera del mismo rojo, parecería que se puede pulsar aunque no haya ninguna tarea elegida.

### Cambio 2 · `ventana.py`: importar `estilos`

```python
# Paso 4
import bd
```

```python
# Paso 5
import bd
import estilos
```

### Cambio 3 · `ventana.py`: nombrar los controles y aplicar la hoja de estilo

En el `__init__`, después de crear los controles, se le pone a cada uno su nombre de objeto, el mismo que usan las reglas de `estilos.py`, y se aplica la hoja de estilo a la ventana:

```python
# Paso 5 (nuevo, después de crear los controles y antes de la distribución)
        # El nombre de cada control, para que la hoja de estilo sepa a cuál se refiere cada regla
        self.campo.setObjectName("campo")
        self.boton_anadir.setObjectName("boton_anadir")
        self.lista.setObjectName("lista")
        self.boton_eliminar.setObjectName("boton_eliminar")
        # Los colores: la hoja de estilo de estilos.py se aplica a la ventana y a todo lo que contiene
        self.setStyleSheet(estilos.ESTILO)
```

- El nombre de variable (`self.campo`) es para Python; el nombre de objeto (`setObjectName("campo")`) es para Qt y su hoja de estilo. Aquí se ponen iguales para no liarse, pero son dos cosas distintas.
- `setStyleSheet` se aplica a la ventana, no a cada control: las reglas de una hoja de estilo valen para el control al que se aplica y para todos los que contiene. Por eso basta una sola línea.

### Los archivos completos

`estilos.py` está completo en el cambio 1, y `main.py` y `bd.py` no cambian. `ventana.py` queda así:

```python
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget
import bd
import estilos
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
        # El nombre de cada control, para que la hoja de estilo sepa a cuál se refiere cada regla
        self.campo.setObjectName("campo")
        self.boton_anadir.setObjectName("boton_anadir")
        self.lista.setObjectName("lista")
        self.boton_eliminar.setObjectName("boton_eliminar")
        # Los colores: la hoja de estilo de estilos.py se aplica a la ventana y a todo lo que contiene
        self.setStyleSheet(estilos.ESTILO)
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

## 2 · Comprobar

```bat
python main.py
```

- El campo de texto tiene el fondo blanco, y la lista, gris.
- El botón «Añadir tarea» es azul con el texto blanco.
- Sin ninguna tarea elegida, el botón «Eliminar tarea» es rojo claro; al elegir una, pasa a rojo. Al eliminarla, vuelve a rojo claro.
- Todo lo demás funciona igual que en el paso 4.

## Preguntas y respuestas

**1. ¿Por qué los colores van en un archivo aparte?**

Por lo mismo que el SQL va en `bd.py`: cada archivo, una responsabilidad. `ventana.py` dice qué controles hay y qué hacen; `estilos.py`, cómo se ven. Para cambiar un color se toca solo `estilos.py`.

**2. ¿Para qué sirve `setObjectName`?**

Le da a cada control un nombre que Qt conoce. Las reglas de la hoja de estilo usan ese nombre, con `#` delante, para saber a qué control se aplican. Sin `setObjectName("campo")`, la regla `#campo` no encontraría ningún control y el campo seguiría blanco.

**3. ¿Por qué basta `self.setStyleSheet(...)` una vez, en la ventana?**

Porque una hoja de estilo vale para el control al que se aplica y para todos los que contiene. Aplicada a la ventana, llega al campo, a los botones y a la lista.

**4. ¿Qué es `:disabled`?**

Un **estado**: la regla `#boton_eliminar:disabled` solo se aplica cuando el botón está desactivado. Así el botón cambia de aspecto solo, sin código, cada vez que `setEnabled` lo activa o lo desactiva. Hay más estados, como `:hover` (el ratón encima) o `:pressed` (mientras se pulsa).

**5. ¿Qué pasa si se quita `border: none` de un botón?**

El botón conserva el borde del estilo del sistema alrededor del color, y queda menos plano. Además, la documentación de Qt avisa de que, con algunos estilos, el borde del sistema tapa el color de fondo de un botón y el color no se ve; con `border: none`, el botón se ve igual en todos.

**6. ¿Se pueden poner los colores sin hoja de estilo?**

Se podría llamar a `setStyleSheet` en cada control, con su propio texto, por ejemplo `self.campo.setStyleSheet("background-color: white;")`. Funciona, pero el aspecto queda repartido por el código de la ventana. Con una sola hoja en `estilos.py`, todo está en un sitio.
