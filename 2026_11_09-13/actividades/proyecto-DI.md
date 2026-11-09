# DI · Proyecto guiado «Mejora tu BugTracker» · 2.ª parte

## Punto de partida

Es la continuación de la 1.ª parte (semana del 2 al 6 de noviembre, pasos 0 a 4): el BugTracker con acciones, menú, barra de herramientas, diálogo con validación y la tabla con Model/View. En esta 2.ª parte le añades un **componente reutilizable** con sus **pruebas automáticas** (UD3), lo pruebas con otra persona (UD1), piensas en las **interfaces naturales** (UD4) y, para terminar la UD3, la aplicación **recuerda su estado** y el componente se **documenta** y se **empaqueta**.

**Usa la IA como guía, no para que lo haga por ti.** Pídele los **pasos necesarios** para implementar cada cosa y que te explique lo que no entiendas; **el código lo pones tú en tu proyecto**, aunque sea copiando y pegando, sabiendo **dónde** lo pones y **para qué**: es la única forma de familiarizarte con tu entorno. El objetivo es que lo que hagas **funcione y cumpla los requisitos** de cada paso («Comprueba que…») y que sepas **dónde está cada cosa y qué habría que tocar para cambiar o añadir algo**: es lo que te van a pedir después.

**El objetivo es entender cada paso:** es lo que necesitas para responder los cuestionarios de autoevaluación y preparar la prueba escrita.

**Evaluación continua.** Algunas semanas hay una **prueba escrita, en papel,** en las dos últimas sesiones del último día de clase, después de que se publiquen las soluciones de lo que entra. La primera es el **jueves 19 de noviembre**, sobre **las dos partes del proyecto** (pasos 0 a 11): Qt Designer y `pyside6-uic`, PySide6 (señales y slots, acciones, menús y diálogos con validación), Model/View, accesibilidad, el componente reutilizable `Buscador` y sus pruebas con pytest-qt, y el propio proyecto.

El proyecto se hace del 10 al 12 de noviembre. Cada paso trae una mini-explicación, una pista y qué hacer si algo falla.

## Con qué trabajas

- **Si terminaste la 1.ª parte y funciona**: sigue en tu carpeta `bugtracker`. Ya tiene `buscador.py` y `test_buscador.py`, que copiaste de la plantilla de la 1.ª parte. Ábrela en VS Code (*File > Open Folder…*), abre la terminal (*Terminal > New Terminal*, `Ctrl+ñ`) y activa el entorno con `.venv\Scripts\Activate.ps1`, si no aparece ya `(.venv)` al principio de la línea.
- **Si no la terminaste o no te funciona**: cambia el nombre de tu carpeta a `bugtracker-anterior`. Descarga la plantilla, [`plantilla.zip`](https://github.com/mrpiay/NTFOR_DAM2627_DI/raw/main/2026_11_09-13/actividades/plantilla.zip), Haz doble clic en el zip y arrastra la carpeta de dentro, `bugtracker`, que es la 1.ª parte terminada, a una **ruta corta y fuera de OneDrive**, por ejemplo `C:\dam2627\di`. Ábrela en VS Code: *File > Open Folder…*, elige la carpeta `bugtracker` y pulsa *Seleccionar carpeta* (si pregunta si confías en los autores, *Yes, I trust the authors*). Abre la terminal: *Terminal > New Terminal* (`Ctrl+ñ`); tiene que ser **PowerShell** (lo pone a la derecha del panel de la terminal). En ella, una orden detrás de otra:

  ```
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  python datos_ejemplo.py
  python main.py
  ```

  `datos_ejemplo.py` añade cinco incidencias de prueba; ejecútalo una sola vez. En VS Code elige el intérprete del entorno: `Ctrl+Mayús+P` → «Python: Select Interpreter» → el de `.venv`.

  **Comprueba que** en la terminal aparece `(.venv)` al principio de la línea y que `python main.py` abre el BugTracker.

  **Si te falla…**

  - *«La ejecución de scripts está deshabilitada»*: ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activar el entorno.
  - *`WinError 206` («el nombre del archivo o la extensión es demasiado largo»)*: la carpeta está en una ruta demasiado larga o en OneDrive. Bórrala, cópiala a `C:\dam2627\di\` y repite desde `python -m venv .venv`.

Qué tocas en cada paso:

| Archivo | Qué es | Paso en que lo tocas |
|---|---|---|
| `buscador.py` | componente reutilizable `Buscador` | 5 |
| `main.py` | ventana principal y lógica | 5 |
| `test_buscador.py` | pruebas con pytest-qt, ya escritas | 6 |

En la plantilla, los comentarios `# TODO Paso 5` marcan dónde se añade código. Antes del paso 5, `python -m pytest -v` da **4 failed**: es lo esperado, porque el componente aún no está hecho.

Lo que escribas en los pasos 7 y 8 va en `notas.md`, el archivo de texto de la carpeta de tu proyecto que empezaste en la 1.ª parte (si no lo tienes, créalo).

## Las herramientas

Las de la 1.ª parte: **VS Code** con su terminal (PowerShell), **Python** con el entorno virtual (`.venv`) y **PySide6**. Esta semana se usan sobre todo estas:

| Herramienta | Qué es | Cómo se usa | Pasos |
|---|---|---|---|
| **pytest** y **pytest-qt** | Ejecutan pruebas automáticas ([UD3, apartado 3](../apuntes/UD3-componentes-reutilizables.md#3-pruebas-unitarias)) | `python -m pytest -v`, en la terminal, con el entorno activado | 5 y 6 |
| **`help()`** | La ayuda de Python: muestra la documentación (los *docstrings*) de una clase o función | `python -c "import buscador; help(buscador.Buscador)"`; espacio para avanzar y `q` para salir | 10 |
| **`build`** | Empaqueta un componente para instalarlo con `pip` en otros proyectos | `pip install build` una vez y después `python -m build` | 11 |

## Qué se trabaja

| Unidad | Qué se trabaja | Pasos |
|---|---|---|
| UD3 · Componentes reutilizables | componente por composición, propiedad y señal propias, pruebas con pytest-qt, `QSettings`, documentar y empaquetar | 5, 6, 9, 10 y 11 |
| UD1 · Diseño, UX y accesibilidad | prueba de usabilidad | 7 |
| UD4 · Interfaces naturales | tipos, límites y relación con la accesibilidad | 8 |

## Plan de la semana

Cada sesión dura 50 minutos.

| Día | Sesión | Qué se hace |
|---|---|---|
| Martes 10 | 10:10 | **Paso 5** (componente `Buscador`). |
| Martes 10 | 11:00 | **Paso 6** (pruebas con pytest-qt). |
| Martes 10 | 12:10 | **Paso 7** (prueba de usabilidad en parejas, 25 min) y **Paso 8** (reflexión UD4, 15 min). Leer qué entra en la prueba escrita del jueves 19, en «Punto de partida» (10 min). |
| Miércoles 11 | 11:00 | **Paso 9** (recordar el estado con `QSettings`). |
| Miércoles 11 | 12:10 | **Paso 10** (documentar el componente). |
| Jueves 12 | 08:30 | **Paso 11** (empaquetar el componente). |
| Jueves 12 | 09:20 | Comprobar todo con la lista final («Cómo comprobarlo»). |

**Los pasos se hacen en orden**, cada uno en la sesión que le toca según el plan de la semana: cada paso usa lo del anterior.

Los pasos 5 y 6 tienen **Objetivo**, **Mini-explicación** (lo justo), **Pista**, **Comprueba que…** y **Si te falla…**; los pasos 7 y 8, **Objetivo**, **Pista** y **Comprueba que…**.

---

## Paso 5 · Componente reutilizable `Buscador` (martes, 50 min)

**Objetivo.** Completar `buscador.py`: un widget propio con una **propiedad** (`texto`), un **método** (`limpiar()`) y una **señal propia** (`busquedaCambiada(str)`), e integrarlo para filtrar la tabla.

**Mini-explicación.** El `Buscador` es un componente por **composición** (un `QWidget` que contiene un `QLineEdit` y un botón) con una propiedad, un método y una señal propia. La señal se declara en la clase, no en `__init__`. Qué es un componente reutilizable, su API pública, la propiedad y la señal: [UD3, apartados 1 y 2](../apuntes/UD3-componentes-reutilizables.md#1-qué-es-un-componente-reutilizable).

La señal, la propiedad y el docstring ya están declarados en la plantilla. Te falta el cuerpo.

**Pista.** En `buscador.py`, sustituye los dos comentarios `# TODO Paso 5` de `__init__` (debajo de `super().__init__(parent)`) por esto, con la misma sangría:

```python
        self._etiqueta = QLabel(etiqueta)
        self._caja = QLineEdit()
        self._caja.setPlaceholderText("Escribe para filtrar")
        self._caja.setAccessibleName("Texto de búsqueda")
        self._etiqueta.setBuddy(self._caja)       # Alt+B lleva el foco a la caja
        self._boton = QPushButton("Limpiar")
        self._boton.setAccessibleName("Limpiar búsqueda")
        self._boton.setToolTip("Borra el texto de búsqueda")

        capa = QHBoxLayout(self)
        capa.setContentsMargins(0, 0, 0, 0)
        capa.addWidget(self._etiqueta)
        capa.addWidget(self._caja)
        capa.addWidget(self._boton)

        self._caja.textChanged.connect(self._al_cambiar_texto)
        self._boton.clicked.connect(self.limpiar)
```

Los demás métodos son de una o dos líneas. Sustituye en cada uno el comentario `# TODO Paso 5` y el `pass` o el `raise NotImplementedError` por:

- `_al_cambiar_texto`: `self.busquedaCambiada.emit(texto)`;
- `limpiar`: `self._caja.clear()` y, debajo, `self._caja.setFocus()`;
- `_get_texto`: `return self._caja.text()`;
- `_set_texto`: `self._caja.setText(valor)`.

Para integrarlo en `main.py`: sustituye la línea `# TODO Paso 5: from buscador import Buscador` por `from buscador import Buscador` (sin `#` ni `TODO Paso 5:`; si tu `main.py` no tiene los `TODO`, añade esa línea con los demás imports); sustituye `# TODO Paso 5: self.configurar_buscador()` por `self.configurar_buscador()` (si no está, añádela justo debajo de `self.configurar_tabla()`); y añade este método dentro de la clase, en lugar del comentario `# TODO Paso 5` del final:

```python
    def configurar_buscador(self):
        self.buscador = Buscador()
        layout = self.ui.verticalLayout                       # el layout que contiene la tabla
        layout.insertWidget(layout.indexOf(self.ui.tblIncidencias), self.buscador)
        self.buscador.busquedaCambiada.connect(self.proxy.setFilterFixedString)
```

Añade también a `configurar_buscador()`, después de la conexión con `setFilterFixedString`, `self.buscador.busquedaCambiada.connect(self.mostrar_resultados)`, y este método para que la barra de estado diga cuántas incidencias quedan:

```python
    def mostrar_resultados(self, texto):
        if texto:
            self.statusBar().showMessage(f"{self.proxy.rowCount()} incidencias con «{texto}»")
        else:
            self.statusBar().clearMessage()
```

La ventana principal solo usa la señal del `Buscador`, no lo que tiene dentro: por eso serviría, sin cambios, en otra aplicación ([UD3, apartado 5](../apuntes/UD3-componentes-reutilizables.md#5-usar-el-componente-en-una-aplicación)).

**Comprueba que…**

- al escribir «error» la tabla se filtra al momento, sin distinguir mayúsculas;
- «Limpiar» vuelve a mostrar todas y deja el foco en la caja; `Alt+B` lleva al buscador;
- con el filtro puesto, seleccionar y eliminar afectan a la incidencia correcta.

**Para pensar.** Busca «3»: puede salir alguna fila sin un 3 a la vista. ¿Por qué? Pista: `setFilterKeyColumn(-1)` busca en todas las columnas, también en la del ID, que está oculta. ¿Qué cambiarías para buscar solo en el título?

**Si te falla…**

- *`AttributeError: ... 'verticalLayout'`*: tu layout tiene otro nombre. Míralo en el Object Inspector de Designer o en `ui_bugtracker.py`.
- *El buscador sale en otro sitio*: `indexOf` devuelve -1 porque la tabla está dentro de otro layout. Usa ese layout.
- *`busquedaCambiada` no tiene `connect`*: la señal está declarada dentro de `__init__` y tiene que ir en el cuerpo de la clase.
- *`NotImplementedError`*: quedan `raise NotImplementedError` en `buscador.py`; sustitúyelos como dice la pista.
- *`NameError: name 'Buscador' is not defined`*: falta `from buscador import Buscador` en `main.py`.
- *`'VentanaPrincipal' object has no attribute 'configurar_buscador'`*: el método está fuera de la clase (revisa la sangría) o después de `if __name__ == "__main__":`.

---

## Paso 6 · Probar el componente con pytest-qt (martes, 35 min)

**Objetivo.** Ejecutar y entender las pruebas automáticas de `test_buscador.py` y añadir una.

**Mini-explicación.** Las pruebas usan `qtbot` para simular el teclado y el ratón (`keyClicks`, `mouseClick`) y esperar señales (`waitSignal`). Cómo funcionan pytest y pytest-qt, en [UD3, apartado 3](../apuntes/UD3-componentes-reutilizables.md#3-pruebas-unitarias).

**Pista.** Con el entorno activado y desde la carpeta del proyecto:

```
python -m pytest -v
```

Lee las cuatro pruebas: valor por defecto, escribir cambia la propiedad, cambiar la propiedad emite la señal y el botón «Limpiar» borra el texto.

**Comprueba que…**

- salen las cuatro en verde con `PASSED` y al final `4 passed`; si alguna falla, el mensaje dice qué parte del `Buscador` falta;
- si cambias a propósito un valor esperado (por ejemplo, `"Error"` por `"Erorr"`), esa prueba falla y pytest explica por qué. Después déjalo bien;
- has escrito una **quinta prueba** propia para un valor límite y sale `5 passed`. Cópiala de una de las que ya hay, cámbiale el nombre y lo que comprueba. Por ejemplo, que los espacios no se recortan: `buscador.texto = "  Media  "` y `assert buscador.texto == "  Media  "`.

**Si te falla…**

- *`fixture 'qtbot' not found`*: falta pytest-qt en el entorno activo: `pip install -r requirements.txt`.
- *`ModuleNotFoundError: No module named 'buscador'`*: ejecuta `python -m pytest` desde la carpeta del proyecto.

---

## Paso 7 · Prueba de usabilidad en parejas (martes, 25 min)

**Objetivo.** Comprobar con otra persona si tu BugTracker es fácil de usar y accesible, y proponer mejoras.

**Pista.** Otra persona prueba **tu** aplicación, en tu ordenador; tú observas y apuntas esta tabla en **tu** `notas.md`. Después cambiáis los papeles. Quien prueba puede ser cualquiera que no haya usado tu aplicación: un compañero o compañera, o alguien de casa. Quien prueba **no recibe ayuda** y piensa en voz alta:

| Tarea | ¿La consiguió? (sí / con ayuda / no) | Problemas observados | Heurística o pauta afectada | Mejora propuesta |
|---|---|---|---|---|
| 1. Crea la incidencia «La ventana no se redimensiona», tipo Error, prioridad Alta, **sin usar el ratón** |  |  |  |  |
| 2. Muestra solo las incidencias que contengan «error» |  |  |  |  |
| 3. Elimina una incidencia y cancela en el último momento; luego elimínala de verdad |  |  |  |  |
| 4. Intenta guardar una incidencia sin título. ¿Entiendes el mensaje? |  |  |  |  |

Para la columna «Heurística o pauta afectada», las más habituales son, de usabilidad: *visibilidad del estado del sistema*, *prevención de errores*, *control y libertad*, *coherencia y estándares*, *reconocer mejor que recordar* y *ayudar a reconocer y corregir errores*; y de accesibilidad: *contraste*, *uso con teclado*, *etiquetas y atajos* y *no depender solo del color*.

Al final, elige **las dos mejoras más importantes** y explica por qué. Compáralas con tu evaluación del paso 1 de la 1.ª parte: ¿la otra persona encontró problemas que tú no viste?

**Comprueba que…** la tabla está completa y cada problema está relacionado con una heurística o una pauta.

---

## Paso 8 · Reflexión: interfaces naturales (martes, 15 min)

**Objetivo.** Empezar a pensar en otras formas de interacción (UD4).

**Pista.** Lee [UD4, apartado 1](../apuntes/UD4-interfaces-naturales.md#1-interfaces-naturales-tipos-ventajas-y-límites) y responde en `notas.md`, en tres o cuatro líneas:

1. ¿Qué interfaz natural añadirías al BugTracker y para qué (por ejemplo, dictar la descripción)?
2. ¿A quién le ayudaría?
3. ¿Qué límite o problema podría tener y qué alternativa ofrecerías?

**Comprueba que…** `notas.md` responde a las tres preguntas.

---

## Paso 9 · Recordar el estado con `QSettings` (miércoles)

**Objetivo.** Que la aplicación recuerde el tamaño de la ventana y la última búsqueda al volver a abrirla.

**Mini-explicación.** `QSettings` guarda pares clave–valor que siguen ahí al cerrar la aplicación. Se guarda al cerrar la ventana, en `closeEvent` (Qt lo llama solo al cerrarla), y se recupera al arrancar, al final de `__init__`, cuando ya existen la ventana y el buscador ([UD3, apartado 4](../apuntes/UD3-componentes-reutilizables.md#4-documentar-y-empaquetar)).

**Pista.** Añade `QSettings` al import que ya existe (`from PySide6.QtCore import QSettings, QSortFilterProxyModel, Qt`), llama a `self.restaurar_estado()` al final de `__init__`, después de `self.actualizar_botones()` (necesita `self.buscador` ya creado), y añade estos dos métodos a la clase:

```python
    def restaurar_estado(self):
        ajustes = QSettings("DAM2", "BugTracker")
        geometria = ajustes.value("ventana/geometria")
        if geometria is not None:
            self.restoreGeometry(geometria)
        self.buscador.texto = ajustes.value("buscador/texto", "")

    def closeEvent(self, evento):
        ajustes = QSettings("DAM2", "BugTracker")
        ajustes.setValue("ventana/geometria", self.saveGeometry())
        ajustes.setValue("buscador/texto", self.buscador.texto)
        super().closeEvent(evento)
```

Ojo: al arrancar se recupera la última búsqueda, así que la tabla puede abrirse ya filtrada. Si parece que faltan incidencias, mira el buscador.

**Comprueba que…** cambias el tamaño de la ventana, escribes `error` en el buscador, cierras la aplicación y, al volver a abrirla, la ventana tiene el mismo tamaño y el buscador conserva `error`, con la tabla filtrada.

**Si te falla…**

- *`AttributeError: 'VentanaPrincipal' object has no attribute 'buscador'`*: llamas a `restaurar_estado()` antes de `self.configurar_buscador()`. Tiene que ir al final de `__init__`.
- *`NameError: name 'QSettings' is not defined`*: falta añadirlo al import de `PySide6.QtCore`.
- *No recuerda nada*: el método se tiene que llamar exactamente `closeEvent`, con esa mayúscula, para que Qt lo llame al cerrar.

---

## Paso 10 · Documentar el componente (miércoles)

**Objetivo.** Que el `Buscador` tenga documentación: la que muestra `help()` y un `README-buscador.md`.

**Pista.** El docstring de `Buscador` ya es documentación: compruébalo con `python -c "import buscador; help(buscador.Buscador)"` (pulsa espacio para avanzar y `q` para salir). Escribe además un `README-buscador.md` corto: qué hace, tres líneas de ejemplo de uso, su propiedad, su método y su señal.

**Comprueba que…** `help(buscador.Buscador)` muestra la descripción del componente, y `README-buscador.md` cuenta qué hace, un ejemplo de uso, su propiedad, su método y su señal.

**Si te falla…**

- *`ModuleNotFoundError: No module named 'buscador'`*: ejecuta la orden desde la carpeta del proyecto, con el entorno virtual activado.

---

## Paso 11 · Empaquetar el componente (jueves)

**Objetivo.** Un archivo `.whl` con el `Buscador`, que se puede instalar con `pip` en otro proyecto.

**Pista.** Para instalarlo con `pip` en otros proyectos, el componente se describe en un `pyproject.toml` ([UD3, apartado 4](../apuntes/UD3-componentes-reutilizables.md#4-documentar-y-empaquetar)):

```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "buscador-dam"
version = "0.1.0"
description = "Componente Buscador para PySide6"
dependencies = ["PySide6-Essentials"]

[tool.setuptools]
py-modules = ["buscador"]
```

Guarda `pyproject.toml` en la carpeta del proyecto, junto a `buscador.py`. Instala `build` una vez con `pip install build`; `python -m build` crea en `dist/` el archivo `buscador_dam-0.1.0-py3-none-any.whl`, que se instala en otro proyecto con `pip install` y la ruta de ese archivo.

`python -m build` necesita conexión a Internet (descarga `setuptools`) y crea en la carpeta del proyecto `build/`, `dist/` y una carpeta que termina en `.egg-info`: son archivos generados.

**Comprueba que…** en `dist/` está el archivo `buscador_dam-0.1.0-py3-none-any.whl`.

**Si te falla…**

- *`No module named build`*: falta `pip install build`, con el entorno virtual activado.
- *Error al descargar `setuptools`*: no hay conexión a Internet; conéctate y repite.

---

## Entrega

Qué se entrega esta semana y cuándo: [`entrega.md`](entrega.md).

## Cómo comprobarlo (lista final)

- [ ] El `Buscador` filtra la tabla y tiene propiedad `texto`, método `limpiar()` y señal `busquedaCambiada`.
- [ ] `python -m pytest -v` da `5 passed` con tu prueba.
- [ ] Prueba de usabilidad hecha, con dos mejoras propuestas.
- [ ] Reflexión de la UD4 escrita.
- [ ] Al volver a abrir la aplicación, recuerda el tamaño de la ventana y la última búsqueda.
- [ ] `help(buscador.Buscador)` muestra su documentación y `README-buscador.md` está escrito.
- [ ] En `dist/` está `buscador_dam-0.1.0-py3-none-any.whl`.
