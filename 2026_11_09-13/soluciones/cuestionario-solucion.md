# Cuestionario C2 · semana del 9 al 13 de noviembre · soluciones

## Cuestiones sobre el proyecto

**1.** pytest busca los archivos que se llaman `test_*.py` y, dentro, ejecuta las funciones que empiezan por `test_`. Un `assert` es una comprobación: si lo que sigue es verdadero, la prueba sigue; si es falso, la prueba falla y pytest muestra qué valor esperaba y cuál ha obtenido. Antes del paso 5, el `Buscador` estaba sin hacer: no tenía caja ni botón, sus métodos tenían `pass` o `raise NotImplementedError`, y por eso fallaban las cuatro pruebas. Las pruebas ya estaban escritas para el componente terminado.

**2.** `qtbot` lo da pytest-qt: prepara la aplicación Qt y permite manejar los widgets como lo haría una persona.

- `addWidget` le entrega el widget, para que lo cierre al terminar la prueba.
- `keyClicks` simula que se teclea un texto en un widget.
- `mouseClick` simula un clic.
- `waitSignal` espera a que se emita una señal; si no llega en el tiempo indicado, la prueba falla. Con `espera.args` se ven los valores con que se emitió.

**3.** Un componente reutilizable es un widget que junta aspecto y comportamiento y se puede usar en cualquier aplicación sin saber cómo está hecho por dentro: solo hace falta conocer su API pública. La del `Buscador`:

- propiedad `texto` (`str`), que se puede leer y cambiar;
- método `limpiar()`;
- señal `busquedaCambiada(str)`, que se emite cada vez que cambia el texto.

**4.** Por herencia, se hereda de un widget que ya existe (por ejemplo, `QLineEdit`) y se cambia o se amplía su comportamiento. Por composición, se crea un `QWidget` que contiene otros widgets y los coordina. El `Buscador` es por composición: un `QWidget` con un `QLabel`, un `QLineEdit` y un `QPushButton` en un `QHBoxLayout`.

**5.** El `_` indica que es interno: forma parte de cómo está hecho el componente, no de su API pública. `main.py` solo usa la API (`texto`, `limpiar()` y `busquedaCambiada`). Así, el `Buscador` se puede cambiar por dentro (por ejemplo, otro widget en lugar del `QLineEdit`) sin que la ventana principal se entere ni haya que tocarla.

**6.** En el cuerpo de la clase, fuera de cualquier método: `busquedaCambiada = Signal(str)`; el `str` es el tipo del valor que lleva. Se lanza con `self.busquedaCambiada.emit(texto)`. Si se declara dentro de `__init__`, PySide6 no la convierte en una señal del objeto y no tiene `connect`: da error al intentar conectarla.

**7.** Crea una propiedad de Qt llamada `texto`, de tipo `str`, que se usa como un atributo. `buscador.texto = "Error"` ejecuta `_set_texto("Error")`, que pone ese texto en la caja; leer `buscador.texto` ejecuta `_get_texto()`, que devuelve el texto de la caja. `notify=busquedaCambiada` indica qué señal avisa de que la propiedad ha cambiado.

**8.**

```
Señal: 'Error'
Texto: Error
Señal: ''
Después de limpiar: ''
```

Al poner `"Error"`, cambia el texto de la caja: `textChanged` llama a `_al_cambiar_texto`, que emite `busquedaCambiada` y se ejecuta la lambda. La segunda vez el texto es el mismo, no cambia nada y no se emite la señal: por eso solo hay un «Señal: 'Error'». `limpiar()` borra la caja: el texto cambia a `''` y se emite otra vez.

**9.**

1. Al escribir, el `QLineEdit` interno (`_caja`) emite `textChanged` con el texto nuevo.
2. Esa señal está conectada (en `__init__` de `buscador.py`) a `_al_cambiar_texto`, que emite `busquedaCambiada(texto)`.
3. En `main.py`, `configurar_buscador()` conectó `busquedaCambiada` a dos sitios. El primero es `self.proxy.setFilterFixedString`: el proxy filtra las filas que contienen el texto.
4. La vista (`tblIncidencias`) muestra lo que le da el proxy: la tabla se actualiza sola.
5. El segundo es `mostrar_resultados(texto)`, que escribe en la barra de estado `self.proxy.rowCount()`, el número de filas que quedan.

**10.**

- `self.buscador = Buscador()` crea el componente.
- `layout = self.ui.verticalLayout` toma el layout que contiene la tabla.
- `layout.insertWidget(layout.indexOf(self.ui.tblIncidencias), self.buscador)` lo coloca en la posición de la tabla, es decir, justo encima.
- Las dos `connect` unen la señal `busquedaCambiada` con el filtro del proxy y con `mostrar_resultados`.

Se llama después de `configurar_tabla()` porque necesita `self.proxy`, que se crea allí. Antes no existiría y daría `AttributeError`.

**11.**

```
«error»: 2
«3» en todas las columnas: 1
«3» solo en el título: 0
Sin filtro: 3 de 3
```

Sin distinguir mayúsculas, «error» está en dos títulos. Buscando en todas las columnas (`-1`), «3» aparece en el ID de la tercera fila aunque no esté en su título: es lo que pasa en el BugTracker, donde la columna ID está oculta. Con `setFilterKeyColumn(1)` solo se busca en el título, y ninguno tiene un 3. Con el texto vacío no se filtra nada. El modelo siempre tiene las tres filas: el proxy no borra, solo decide qué se ve.

**12.** Porque `id_seleccionado()` no usa la fila de la vista: la traduce con `self.proxy.mapToSource(...)` a la fila del modelo y lee de ahí el ID de la incidencia. Ese ID es el que se pasa a `bd.py`. Da igual cuántas filas oculte el filtro o cómo esté ordenada la tabla.

**13.**

```
test_pregunta.py::test_limpiar_deja_vacio PASSED
test_pregunta.py::test_mayusculas FAILED
1 failed, 1 passed in 0.17s
```

(El tiempo cambia de un ordenador a otro.) La segunda prueba falla porque la propiedad `texto` devuelve lo que se escribió, sin cambiar las mayúsculas: `'ALTA'`, y la prueba esperaba `'alta'`. pytest lo explica con `AssertionError: assert 'ALTA' == 'alta'`. La prueba estaba mal planteada: el componente hace lo que debe. (Que el filtro no distinga mayúsculas es cosa del proxy, no del `Buscador`.)

**14.** Por ejemplo, `test_texto_con_espacios_se_conserva`: pone `"  Media  "` y comprueba que `texto` lo devuelve igual, con los espacios, y que la señal lleva ese mismo valor. Un valor límite es un caso en el borde de lo normal: texto vacío, solo espacios, muy largo, con tildes o símbolos… Conviene probarlos porque es donde más fallos aparecen.

(Vale cualquier quinta prueba que compruebe un caso así con su `assert`.)

**15.** Nada en `buscador.py`. En la otra aplicación: tener `buscador.py` (copiado o instalado con `pip`), importarlo (`from buscador import Buscador`), crearlo, ponerlo en un layout y conectar `busquedaCambiada` a la función que filtre las notas. Es justo lo que se gana con un componente reutilizable.

**16.** Guarda el tamaño y la posición de la ventana (`saveGeometry()`) y el último texto del buscador. En Windows lo guarda en el registro, en `HKEY_CURRENT_USER\Software\DAM2\BugTracker`. Se guarda en `closeEvent`, que se ejecuta al cerrar la ventana, y se recupera en `restaurar_estado()`. Este se llama al final de `__init__` porque necesita `self.buscador` ya creado, y la tabla ya cargada para poder filtrarla.

**17.** Muestra la documentación de la clase `Buscador`: su docstring (el texto entre `"""` debajo de `class Buscador`) y sus métodos. La documentación de un componente debe contar qué hace, su API pública (propiedades, métodos y señales, con sus tipos y valores por defecto) y un ejemplo de uso.

**18.** `pyproject.toml` describe el paquete: cómo se construye, su nombre, su versión, de qué depende (`PySide6-Essentials`) y qué módulo incluye (`buscador`). `python -m build` crea en `dist/` un archivo `.whl`, por ejemplo `buscador_dam-0.1.0-py3-none-any.whl`. En otro proyecto se instala con `pip install` y la ruta de ese archivo. Después ya se puede hacer `from buscador import Buscador`.

**19.** Para ver si la aplicación se entiende sola, sin explicaciones, como le pasaría a un usuario real. Si se le ayuda, ya no se sabe si lo habría conseguido. Pensar en voz alta deja ver qué espera encontrar y dónde se pierde. De cada tarea se apunta si la consiguió (sí, con ayuda o no), los problemas observados, la heurística o pauta afectada y la mejora propuesta.

**20.** Una interfaz que usa formas de comunicarse propias de las personas: voz, gestos, movimiento, tacto, mirada… Por ejemplo, dictar la descripción de una incidencia. Ayudaría a quien no puede usar bien el teclado o las manos, o a quien está haciendo otra cosa. Límites: el ruido, la privacidad en una oficina compartida o los errores de reconocimiento con nombres técnicos. Por eso siempre hay que ofrecer una alternativa: el teclado y el ratón de siempre.

(Valen otros ejemplos razonados.)

## Cuestiones sobre los apuntes

**21.** *(UD3, apartado 1)* Para diseñarlo, Qt Designer (la parte visual) y el propio código Python; para probarlo, pytest con pytest-qt.

**22.** *(UD3, apartado 3)* Probar el valor por defecto, cada propiedad, cada señal, cada método y los valores límite; cada prueba comprueba una sola cosa. Por ejemplo: un texto muy largo se conserva entero; un texto con tildes y `ñ` se conserva; `limpiar()` con la caja ya vacía no falla y deja el foco en la caja. (Valen otros casos razonados.)
