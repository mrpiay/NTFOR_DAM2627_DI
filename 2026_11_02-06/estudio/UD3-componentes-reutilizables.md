# UD3 · Componentes visuales reutilizables

Lo básico que hay que saber de la UD3. Cada apartado tiene la idea clave, lo que tienes que saber y, cuando hay conceptos que se confunden, una tabla para compararlos. Los ejemplos son del componente `Buscador` del proyecto. Las preguntas para comprobar que lo entiendes están en los cuestionarios de autoevaluación.

---

## 1. Qué es un componente reutilizable

**En una frase:** un componente es un control propio que junta aspecto y comportamiento y se puede usar en cualquier aplicación sin saber cómo está hecho por dentro.

**Lo que tienes que saber**

- Se usa a través de su **API pública**: sus **propiedades**, sus **métodos** y sus **señales**. La del `Buscador`: la propiedad `texto`, el método `limpiar()` y la señal `busquedaCambiada(str)`.
- Lo interno empieza por **`_`** (`_caja`, `_boton`): quien usa el componente no lo toca. Así se puede cambiar por dentro sin afectar a las aplicaciones que lo usan.
- Se puede crear de dos formas:
  - **por herencia:** se hereda de un control que ya existe y se cambia o amplía su comportamiento;
  - **por composición:** un `QWidget` que contiene otros controles y los coordina. El `Buscador` es así: una etiqueta, una caja de texto y un botón.
- Las herramientas para diseñarlo y probarlo: Qt Designer para la parte visual, el propio código Python, y **pytest** con **pytest-qt** para probarlo.

**Compara**

| | Herencia | Composición |
|---|---|---|
| Qué es | Una versión ampliada de un control existente | Un control nuevo hecho de otros |
| Ejemplo | Un `QLineEdit` que solo admite números | El `Buscador`: etiqueta, caja y botón |

---

## 2. Propiedades, métodos y señales propias

**En una frase:** las propiedades guardan su estado, los métodos son lo que sabe hacer y las señales avisan de lo que pasa.

**Lo que tienes que saber**

- Una **propiedad** se declara con `Property`, con su tipo, un método para leerla y otro para cambiarla: `texto = Property(str, _get_texto, _set_texto, notify=busquedaCambiada)`. Se usa como un atributo: `buscador.texto = "Error"`. `notify` indica qué señal avisa de sus cambios.
- Cada propiedad tiene un **valor por defecto** (el texto del `Buscador`, vacío).
- Un **método** es una función de la clase que forma parte de la API: `limpiar()` borra el texto y devuelve el foco a la caja.
- Una **señal propia** se declara **en la clase**, no dentro de `__init__`: `busquedaCambiada = Signal(str)`. Se lanza con `self.busquedaCambiada.emit(texto)`.
- La aplicación solo se conecta a la señal: `self.buscador.busquedaCambiada.connect(self.proxy.setFilterFixedString)`. No sabe que dentro hay un `QLineEdit`.

---

## 3. Pruebas unitarias

**En una frase:** una prueba unitaria comprueba automáticamente que una parte pequeña (un componente) hace lo que debe.

**Lo que tienes que saber**

- **pytest** busca los archivos `test_*.py` y ejecuta sus funciones `test_*`. Cada **`assert`** es una comprobación: si es falsa, la prueba falla y pytest muestra qué esperaba y qué ha obtenido.
- **pytest-qt** añade **`qtbot`**, que maneja los controles como una persona: `keyClicks` (escribir), `mouseClick` (hacer clic) y `waitSignal` (esperar a que se emita una señal).
- Una **estrategia de pruebas** dice qué se prueba: el valor por defecto, cada propiedad, cada señal, cada método y los **valores límite** (texto vacío, solo espacios, muy largo, con tildes…).
- Cada prueba comprueba una sola cosa y su nombre dice cuál: `test_limpiar_borra_el_texto`.
- Se ejecutan con `python -m pytest -v`. Si alguien cambia el componente y rompe algo, las pruebas lo avisan.

---

## 4. Documentar y empaquetar

**En una frase:** un componente se documenta para que otros sepan usarlo y se empaqueta para instalarlo en otros proyectos.

**Lo que tienes que saber**

- **Documentar:** el **docstring** de la clase explica qué hace, su API pública (propiedades, métodos y señales, con tipos y valores por defecto) y un ejemplo de uso. `help(buscador.Buscador)` lo muestra. Se completa con un `README`.
- **Empaquetar:** un archivo **`pyproject.toml`** describe el paquete (nombre, versión, dependencias, módulos). `python -m build` crea un archivo **`.whl`** (*wheel*) en `dist/`, que se instala en otro proyecto con `pip install`.
- **Guardar el estado** entre ejecuciones: **`QSettings`** guarda, por ejemplo, el tamaño de la ventana y la última búsqueda; se guarda al cerrar (`closeEvent`) y se recupera al abrir.

---

## 5. Usar el componente en una aplicación

**En una frase:** se crea, se coloca en un layout y se conecta su señal; el resto de la aplicación no cambia.

**Lo que tienes que saber**

- En el BugTracker: `self.buscador = Buscador()`, se inserta encima de la tabla en el layout y su señal se conecta al filtro del proxy y a la barra de estado.
- El mismo componente serviría, sin cambiar nada, en otra aplicación (un editor de notas, una lista de contactos): eso es lo que significa **reutilizable**.
- Se coloca y se ajusta igual que cualquier control: con layouts, con un nombre accesible y en el orden de tabulación.
