# Repaso · UD2 · Interfaces gráficas con PySide6 y Qt Designer

Lo básico que hay que saber de la UD2. Cada apartado tiene la idea clave, lo que tienes que saber y, cuando hay conceptos que se confunden, una tabla para compararlos. Los ejemplos son del BugTracker del proyecto. Las preguntas para comprobar que lo entiendes están en los cuestionarios de autoevaluación.

---

## 1. Herramientas y librerías

**En una frase:** para crear una interfaz gráfica se usa una librería de controles y, a menudo, un editor visual para dibujarla.

**Lo que tienes que saber**

- **Qt** es una librería de interfaces gráficas, escrita en C++, que funciona en Windows, Linux y macOS. **PySide6** es Qt para Python, la oficial, con licencia LGPL. **PyQt6** es otra versión de Qt para Python, con licencia GPL o comercial.
- Otras librerías: **Tkinter** (viene con Python, sencilla), **JavaFX** (Java), **WPF** y **WinUI** (Windows), **GTK** (Linux), y las web (HTML, CSS y JavaScript).
- Un **editor visual** permite colocar los controles con el ratón. El de Qt es **Qt Designer**, que viene con PySide6.
- En el proyecto se trabaja dentro de un **entorno virtual** (`.venv`) con las librerías de `requirements.txt`.

**Compara**

| | PySide6 | PyQt6 | Tkinter |
|---|---|---|---|
| Base | Qt | Qt | Tk |
| Licencia | LGPL | GPL o comercial | Libre, viene con Python |
| Editor visual | Qt Designer | Qt Designer | No tiene uno oficial |

---

## 2. Del diseño al código

**En una frase:** en Qt Designer se dibuja la ventana, `pyside6-uic` la convierte en Python y la aplicación carga ese código.

**Lo que tienes que saber**

```
bugtracker.ui  ──(pyside6-uic)──►  ui_bugtracker.py  ──(import y setupUi)──►  main.py
  (Designer)                          (generado)                              (tu lógica)
```

- `bugtracker.ui` es un archivo XML con el diseño; solo lo lee Qt Designer.
- `pyside6-uic bugtracker.ui -o ui_bugtracker.py` genera la clase `Ui_VentanaPrincipal`. **No se edita a mano:** se sobrescribe cada vez que se regenera.
- `main.py` importa esa clase y llama a `setupUi(self)`, que crea los controles. La lógica (qué hace cada botón) va en `main.py`.
- Después de cambiar algo en Designer: guardar, regenerar con `pyside6-uic` y volver a ejecutar.

---

## 3. Controles, propiedades y layouts

**En una frase:** cada control tiene un nombre y unas propiedades, y los layouts los colocan para que se adapten al tamaño de la ventana.

**Lo que tienes que saber**

- **`objectName`**: el nombre con el que se usa el control desde el código, con un prefijo que dice qué es: `txtTitulo`, `cmbTipo`, `btnAnadir`, `tblIncidencias`.
- Propiedades habituales: `text`, `enabled` (activado o no), `toolTip` (ayuda al pasar el ratón), `accessibleName`, `placeholderText` (texto de ejemplo dentro del campo) y `tabChangesFocus` (que `Tab` salte de campo en lugar de escribir un tabulador).
- **Layouts:** `QVBoxLayout` (en vertical), `QHBoxLayout` (en horizontal), `QGridLayout` (en rejilla) y `QFormLayout` (etiqueta y campo). Sin layouts, la ventana no se adapta al cambiar de tamaño.
- **Atajo de una etiqueta:** `&Título` subraya la T y `Alt+T` lleva el foco a su **buddy**, el campo asociado.

---

## 4. Señales y slots

**En una frase:** cuando pasa algo en un control, emite una **señal**, y se ejecuta el **slot** (la función) conectado a ella.

**Lo que tienes que saber**

- Se conecta así: `self.ui.btnAnadir.clicked.connect(self.anadir_incidencia)`.
- La función se pasa **sin paréntesis**: con paréntesis (`self.anadir_incidencia()`) se ejecutaría en ese momento y se conectaría lo que devuelve.
- Señales habituales: `clicked` (botón), `triggered` (acción), `textChanged` (campo de texto), `currentIndexChanged` (lista desplegable), `doubleClicked` (tabla), `selectionChanged` (selección de la tabla).
- Una **lambda** sirve para conectar algo corto o pasar un dato: `boton.clicked.connect(lambda: print("Hola"))`.
- Una señal puede conectarse a varios slots, y varios controles a un mismo slot.

**Compara**

| | `connect(self.guardar)` | `connect(self.guardar())` |
|---|---|---|
| Qué se conecta | El método | Lo que devuelve el método (normalmente `None`) |
| Cuándo se ejecuta `guardar` | Al emitirse la señal | En ese momento, una sola vez |
| Resultado | Correcto | Error o no hace nada |

---

## 5. Acciones, menús y barras de herramientas

**En una frase:** una `QAction` es una orden con su texto, atajo y estado, que se pone a la vez en el menú y en la barra de herramientas.

**Lo que tienes que saber**

- Se crea en Qt Designer, en el **Action Editor**, con su texto (`&Nueva incidencia...`), su atajo (`Ctrl+N`) y su ayuda.
- Se arrastra al menú y a la barra de herramientas: es la misma acción en los dos sitios.
- Su señal es **`triggered`**, que se conecta una sola vez: `self.ui.actionNueva.triggered.connect(self.nueva_incidencia)`.
- `setEnabled(False)` la desactiva en el menú y en la barra a la vez (por ejemplo, «Eliminar» si no hay nada seleccionado).
- Los puntos suspensivos («Nueva incidencia…») indican que la orden abre un diálogo.

---

## 6. Diálogos y validación

**En una frase:** un diálogo modal pide datos y bloquea la ventana principal hasta que se acepta o se cancela; antes de aceptar, se validan los datos.

**Lo que tienes que saber**

- Un diálogo es una clase que hereda de **`QDialog`**. `exec()` lo muestra en modo **modal** y devuelve verdadero si se aceptó y falso si se canceló.
- **`accept()`** y **`reject()`** lo cierran. El botón Aceptar se conecta a un método de **validación**, que solo llama a `accept()` si los datos son correctos.
- Si algo está mal, se avisa (por ejemplo, con `QMessageBox.warning`), se pone el foco en el campo y el diálogo **sigue abierto**.
- **`QMessageBox`** da los mensajes estándar: `information`, `warning`, `critical` y `question` (para confirmar).
- El mismo diálogo puede servir para **crear** (vacío) y para **editar** (con los datos ya rellenos).

---

## 7. Datos con SQLite

**En una frase:** la aplicación guarda los datos en una base de datos SQLite, y todo el SQL va en un archivo aparte.

**Lo que tienes que saber**

- **SQLite** es una base de datos en un solo archivo (`bugtracker.db`), sin servidor. Python la trae: `import sqlite3`.
- Las operaciones básicas, **CRUD**: crear (`INSERT`), leer (`SELECT`), actualizar (`UPDATE`) y borrar (`DELETE`).
- Los datos se pasan con **`?`** y no pegados en el texto de la consulta: así no se rompe con una comilla y se evita la **inyección SQL**.
- **Separación:** `bd.py` tiene todo el SQL y no usa ningún control; `main.py` tiene la interfaz y no tiene SQL. Si se cambia de base de datos, solo se toca `bd.py`.

---

## 8. Model/View

**En una frase:** los datos están en un **modelo** y la **vista** solo los muestra; entre los dos, un **proxy** ordena y filtra sin tocar los datos.

**Lo que tienes que saber**

- **`QTableWidget`**: la tabla guarda los datos dentro, celda a celda. Sencillo, pero mezcla datos y vista.
- **Model/View**: un modelo (`QStandardItemModel`) con los datos, una vista (`QTableView`) que los dibuja y, entre los dos, un **`QSortFilterProxyModel`** que ordena y filtra.
- Al ordenar o filtrar, la fila que se ve no es la misma que la del modelo. **`mapToSource`** traduce la fila de la vista a la del modelo, para modificar o borrar la incidencia correcta.
- La columna del **ID** se oculta (`setColumnHidden`), pero sigue en el modelo: identifica la incidencia aunque cambie su posición.

**Compara**

| | `QTableWidget` | Model/View (`QTableView` + modelo + proxy) |
|---|---|---|
| Dónde están los datos | Dentro de la tabla | En el modelo |
| Ordenar y filtrar | Limitado | Con el proxy, sin tocar los datos |
| Uso | Tablas pequeñas y sencillas | Aplicaciones con datos que cambian |
