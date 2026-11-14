# DI · Proyecto guiado «Mejora tu BugTracker» · 3.ª parte

## Punto de partida

Es la continuación de la 2.ª parte (semana del 9 al 13, pasos 5 a 11): el BugTracker con su componente `Buscador`, sus pruebas, el estado guardado con `QSettings` y el componente empaquetado. En esta 3.ª parte:

- se repasa la **base de datos** con una consulta nueva: cuántas incidencias hay en cada estado (UD2);
- el `Buscador` pasa a colocarse **desde Qt Designer**, como cualquier otro control (UD3);
- se añade una **interfaz natural**: manejar la tabla con **gestos de la mano** ante la cámara del portátil (UD4);
- se **prueba** y se **revisa con criterio** lo hecho (UD4).

La teoría de esta semana está en `apuntes/`: la de la UD4 (voz, gestos, cuerpo, realidad aumentada, criterios de diseño, manual de usuario y tipos de pruebas), en [`UD4-interfaces-naturales.md`](../apuntes/UD4-interfaces-naturales.md), y la de los pasos 12 y 13 (contar con SQL y el componente en Qt Designer), en [`UD2-UD3-ampliacion.md`](../apuntes/UD2-UD3-ampliacion.md). La práctica es un solo caso, el de los gestos; lo demás se estudia en los apuntes: qué se puede hacer, para qué y con qué criterios.

**Usa la IA como guía, no para que lo haga por ti.** Pídele los **pasos necesarios** para implementar cada cosa y que te explique lo que no entiendas; **el código lo pones tú en tu proyecto**, aunque sea copiando y pegando, sabiendo **dónde** lo pones y **para qué**. El objetivo es que lo que hagas **funcione y cumpla los requisitos** de cada paso («Comprueba que…») y que sepas **dónde está cada cosa y qué habría que tocar para cambiar o añadir algo**.

**El objetivo es entender cada paso:** es lo que necesitas para responder el cuestionario y preparar los exámenes.

**Evaluación.** Esta actividad guiada (**A3**) se evalúa con su lista de cotejo: cada «Comprueba que…» se cumple o no. El cuestionario de la semana (**C3**) se entrega hasta el lunes 23 de noviembre. La semana del 23 al 27 y el martes 1 de diciembre son de **repaso**. El **miércoles 2 de diciembre** hay un examen parcial, **P1**, en papel, con todo lo de la 1ª evaluación que no evaluó Julia: las tres partes de esta actividad y los apuntes de la UD1 a la UD4. De la UD4, las preguntas son de conceptos y criterio, no de código. Qué entra y cuánto vale cada parte: [1ª evaluación](../../programacion/1a-evaluacion.md).

## Con qué trabajas

- **Si terminaste la 2.ª parte y funciona:** sigue en tu carpeta `bugtracker` (`C:\dam2627\di\bugtracker`). Ábrela en VS Code, abre la terminal (`Ctrl+ñ`, **PowerShell**) y activa el entorno con `.venv\Scripts\Activate.ps1`, si no aparece ya `(.venv)` al principio de la línea.
- **Si no la terminaste o no te funciona:** cambia el nombre de tu carpeta a `bugtracker-anterior` y parte de la plantilla, que es la 2.ª parte terminada. En la terminal, **PowerShell**:

  ```
  cd C:\dam2627\di
  Invoke-WebRequest https://github.com/mrpiay/NTFOR_DAM2627_DI/raw/main/2026_11_16-20/actividades/plantilla.zip -OutFile plantilla.zip
  Expand-Archive plantilla.zip -DestinationPath .
  Remove-Item plantilla.zip
  cd bugtracker
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  python datos_ejemplo.py
  code .
  ```

  Así queda en `C:\dam2627\di\bugtracker`, con su entorno, sus paquetes y cinco incidencias de prueba. Si ya existe una carpeta `bugtracker`, `Expand-Archive` avisa: cámbiale antes el nombre. Lo que escribiste en `notas.md` en la 1.ª y la 2.ª parte está en tu carpeta anterior: cópialo a la nueva.

Cada vez que cambies el diseño en Qt Designer, hay que volver a generar el código de la ventana (como en la 1.ª parte):

```
pyside6-uic bugtracker.ui -o ui_bugtracker.py
```

Qué tocas en cada paso:

| Archivo | Qué es | Paso |
|---|---|---|
| `bd.py` | Todo el SQL | 12 |
| `main.py` | La ventana principal y su lógica | 12, 13 y 15 |
| `bugtracker.ui` y `ui_bugtracker.py` | El diseño de la ventana y su código generado | 13 |
| `buscador.py` | El componente `Buscador` | 13 |
| `gestos.py` | El detector de gestos, **ya hecho**: se descarga en el paso 14 | 14 y 15 |
| `notas.md` | Tus notas del proyecto | 16 |

## Las herramientas

Las de la 1.ª y la 2.ª parte (VS Code, Python con el entorno virtual, PySide6, Qt Designer y pytest), y dos nuevas:

| Herramienta | Qué es | Pasos |
|---|---|---|
| **MediaPipe** | Librería de Google con modelos ya entrenados para reconocer manos, gestos y cuerpo en la imagen de la cámara. Su reconocedor de gestos distingue siete gestos de la mano | 14 y 15 |
| **OpenCV** | Lee la imagen de la cámara. Se instala con MediaPipe | 14 y 15 |

## Qué se trabaja

| Unidad | Qué se trabaja | Pasos |
|---|---|---|
| UD2 · Interfaces gráficas | Una consulta SQL con `GROUP BY`, en `bd.py`, y su resultado en la barra de estado | 12 |
| UD3 · Componentes | Usar un componente propio desde Qt Designer (*Promote to*); una prueba de regresión | 13 |
| UD4 · Interfaces naturales | Gestos de la mano con MediaPipe; criterios de diseño; pruebas de integración y de regresión | 14, 15 y 16 |

## Plan de la semana

Cada sesión dura 50 minutos.

| Día | Sesión | Qué se hace |
|---|---|---|
| Martes 17 | 10:10 | **Paso 12** (cuántas incidencias hay en cada estado). |
| Martes 17 | 11:00 | **Paso 13** (el `Buscador` en Qt Designer). |
| Martes 17 | 12:10 | **Paso 14** (instalar MediaPipe y probar los gestos). |
| Miércoles 18 | 11:00 | **Paso 15** (gestos en el BugTracker): los métodos. |
| Miércoles 18 | 12:10 | **Paso 15**: probarlo con su «Comprueba que…». |
| Jueves 19 | 08:30 | **Paso 16** (probar y revisar con criterio). |
| Jueves 19 | 09:20 | Leer los apartados 2, 3 y 5 de los apuntes de la UD4 y comprobar todo con la lista final («Cómo comprobarlo»). |

**Los pasos se hacen en orden**, cada uno en la sesión que le toca según el plan de la semana: cada paso usa lo del anterior.

---

## Paso 12 · Cuántas incidencias hay en cada estado

**Objetivo.** Que la barra de estado muestre siempre, a la derecha, cuántas incidencias hay en cada estado (por ejemplo, `En proceso: 1 · Pendiente: 3 · Resuelta: 1`), contadas por la base de datos.

**Mini-explicación.** Contar es trabajo de la base de datos: `GROUP BY estado` agrupa las filas que tienen el mismo estado y `COUNT(*)` cuenta las de cada grupo. Se hace en `bd.py`, como todo el SQL: `main.py` solo pide el resultado y lo muestra (la regla de separación de la 1.ª parte). Más, en los [apuntes de ampliación, apartado 1](../apuntes/UD2-UD3-ampliacion.md#1-contar-por-grupos-con-sql).

**Pista.** En `bd.py`, al final, añade:

```python
def contar_por_estado():
    """Devuelve una lista de filas (estado, total): cuántas incidencias hay en cada estado."""
    conexion = conectar()
    try:
        cursor = conexion.execute(
            "SELECT estado, COUNT(*) AS total FROM incidencias GROUP BY estado ORDER BY estado"
        )
        return cursor.fetchall()
    finally:
        conexion.close()
```

`AS total` da nombre a la columna del recuento: así se lee como `fila["total"]`.

En `main.py`:

1. Añade `QLabel` a la lista de `from PySide6.QtWidgets import …`.
2. En `__init__`, debajo de `self.configurar_buscador()`, añade `self.configurar_resumen()`.
3. En `cargar_incidencias()`, al final (debajo de `self.actualizar_botones()`), añade `self.actualizar_resumen()`. Así el resumen se actualiza cada vez que se recarga la tabla: al arrancar, al añadir, al modificar y al eliminar.
4. Añade estos dos métodos dentro de la clase, por ejemplo debajo de `mostrar_resultados`:

```python
    def configurar_resumen(self):
        self.lblResumen = QLabel()
        self.lblResumen.setAccessibleName("Resumen de incidencias por estado")
        self.statusBar().addPermanentWidget(self.lblResumen)   # a la derecha, siempre visible

    def actualizar_resumen(self):
        try:
            filas = bd.contar_por_estado()
        except sqlite3.Error:
            self.lblResumen.setText("")
            return
        self.lblResumen.setText(" · ".join(f"{fila['estado']}: {fila['total']}" for fila in filas))
```

`addPermanentWidget` coloca la etiqueta en la parte derecha de la barra de estado: los mensajes temporales («Incidencia añadida») siguen saliendo a la izquierda sin taparla.

**Comprueba que…**

- al arrancar, la barra de estado muestra a la derecha el recuento de cada estado (con las cinco incidencias de ejemplo, `En proceso: 1 · Pendiente: 3 · Resuelta: 1`);
- al añadir, modificar el estado o eliminar una incidencia, el recuento cambia al momento;
- `main.py` no tiene ninguna sentencia SQL.

**Si te falla…**

- *`AttributeError: module 'bd' has no attribute 'contar_por_estado'`*: la función no está en `bd.py` o tiene otro nombre.
- *El recuento no cambia al añadir*: falta `self.actualizar_resumen()` al final de `cargar_incidencias()`.
- *`AttributeError: … 'lblResumen'`*: `configurar_resumen()` tiene que llamarse en `__init__` **antes** de `self.cargar_incidencias()`.

---

## Paso 13 · El `Buscador` en Qt Designer

**Objetivo.** Que el `Buscador` deje de añadirse por código y se coloque **en el diseño**, en Qt Designer, como cualquier otro control.

**Mini-explicación.** Qt Designer solo conoce los controles de Qt. Para usar uno propio se coloca un `QWidget` vacío donde debe ir y se **promociona** (*Promote to…*): se le dice que, al generar el código, en lugar de un `QWidget` cree un `Buscador`. Qt Designer no sabe dibujarlo, así que en el diseño se ve como un recuadro vacío; el componente de verdad aparece al ejecutar. El código generado lo crea así: `Buscador(self.centralwidget)`, es decir, con el **padre como primer parámetro**. Por eso un componente pensado para usarse desde Qt Designer recibe `parent` primero. Más, en los [apuntes de ampliación, apartado 2](../apuntes/UD2-UD3-ampliacion.md#2-usar-un-componente-propio-desde-qt-designer).

**Pista.**

1. En `buscador.py`, cambia el orden de los parámetros de `__init__`, para que `parent` vaya primero:

   ```python
       def __init__(self, parent=None, etiqueta="&Buscar:"):
   ```

2. Comprueba que no se ha roto nada: `python -m pytest -v` tiene que dar **4 passed** (o los que tuvieras). Es una **prueba de regresión**: repetir las pruebas después de un cambio para ver que lo que funcionaba sigue funcionando ([apuntes de la UD4, apartado 7](../apuntes/UD4-interfaces-naturales.md#7-documentar-y-probar-una-aplicación)).
3. Abre el diseño: `Start-Process .venv\Scripts\pyside6-designer.exe -ArgumentList bugtracker.ui -WindowStyle Hidden`.
4. En **Widget Box**, en *Containers*, arrastra un **Widget** justo encima de la tabla de incidencias, dentro del mismo layout (una línea azul marca dónde se suelta).
5. En **Property Editor**, cambia su `objectName` a `buscador`.
6. Clic derecho sobre el widget → **Promote to…** (*Promover a…*). Rellena:
   - **Base class name:** `QWidget`;
   - **Promoted class name:** `Buscador`;
   - **Header file:** `buscador.h`. Para Python solo importa el nombre: el código generado hará `from buscador import Buscador`.

   Pulsa **Add** y después **Promote**. En **Object Inspector**, el widget aparece ahora como `buscador : Buscador`.
7. Guarda (`Ctrl+S`), cierra Qt Designer y genera de nuevo el código: `pyside6-uic bugtracker.ui -o ui_bugtracker.py`.
8. En `main.py`, el `Buscador` ya lo crea `setupUi`. Cambia el principio de `configurar_buscador()`: en lugar de crearlo e insertarlo en el layout, usa el del diseño. Debe quedar así:

   ```python
       def configurar_buscador(self):
           self.buscador = self.ui.buscador          # lo crea setupUi: está en el diseño (Promote to)
           self.buscador.busquedaCambiada.connect(self.proxy.setFilterFixedString)
           self.buscador.busquedaCambiada.connect(self.mostrar_resultados)
   ```

   Y borra la línea `from buscador import Buscador` de `main.py`: ahora la importa `ui_bugtracker.py`.

**Comprueba que…**

- en Qt Designer, el `Buscador` está en el diseño, encima de la tabla, y en *Object Inspector* sale como `buscador : Buscador`;
- en `ui_bugtracker.py` aparecen `from buscador import Buscador` y `self.buscador = Buscador(self.centralwidget)`;
- al ejecutar, el `Buscador` sale encima de la tabla y filtra como antes (escribe `error`), y `Alt+B` lleva a su caja;
- `python -m pytest -v` sigue pasando todas las pruebas.

**Si te falla…**

- *`TypeError` al arrancar, en `QLabel(etiqueta)`*: no has cambiado el orden de los parámetros en `buscador.py`: el código generado le pasa el padre como primer parámetro.
- *Sale dos veces el buscador*: `configurar_buscador()` sigue creando otro. Debe usar `self.ui.buscador`.
- *`ModuleNotFoundError: No module named 'buscador'`*: en *Header file* pusiste otro nombre. Debe ser `buscador.h`, y `buscador.py` tiene que estar en la misma carpeta.
- *No sale la opción Promote to…*: haz clic derecho sobre el widget mismo, no sobre el layout.

---

## Paso 14 · Instalar MediaPipe y probar los gestos

**Objetivo.** Tener MediaPipe instalado y ver que el portátil reconoce los gestos de la mano con su cámara.

**Mini-explicación.** El reconocimiento de gestos lo hace un **modelo ya entrenado** de MediaPipe: recibe cada imagen de la cámara y devuelve qué gesto ve y con cuánta confianza ([apuntes de la UD4, apartados 2 y 4](../apuntes/UD4-interfaces-naturales.md#2-cómo-reconoce-un-ordenador-la-voz-los-gestos-y-el-cuerpo)). Hablar con la cámara y con el modelo es lo técnico, y ya está hecho en `gestos.py`: un componente con una señal, `gestoDetectado(str)`, como el `Buscador`. Esta semana se **usa**, no se programa.

**Pista.** En la terminal, con el entorno activado y en la carpeta `bugtracker`:

1. Instala MediaPipe (con él se instala también OpenCV). Tarda unos minutos:

   ```
   pip install mediapipe
   ```

2. Añade una línea `mediapipe` al final de `requirements.txt`, para que quien instale el proyecto la tenga.
3. Descarga `gestos.py` en la carpeta:

   ```
   Invoke-WebRequest https://github.com/mrpiay/NTFOR_DAM2627_DI/raw/main/2026_11_16-20/actividades/gestos.py -OutFile gestos.py
   ```

4. Pruébalo solo, sin el BugTracker:

   ```
   python gestos.py
   ```

   La primera vez descarga el modelo, `gesture_recognizer.task` (unos 8 MB). Se abre una ventana con la imagen de la cámara, como un espejo, y debajo el último gesto reconocido. Prueba con la mano a unos 50 cm de la cámara: pulgar arriba, pulgar abajo, palma abierta, puño y victoria. `Esc` cierra la ventana.
5. Lee en el principio de `gestos.py` su documentación: qué gestos reconoce y qué métodos y señales tiene (`help(gestos.DetectorGestos)` también la muestra).

**Comprueba que…**

- `pip list` muestra `mediapipe`;
- `python gestos.py` muestra la imagen de la cámara y reconoce al menos pulgar arriba, pulgar abajo y palma abierta;
- sabes decir qué señales tiene `DetectorGestos` y para qué sirve cada una.

**Si te falla…**

- *«No se ha podido abrir la cámara»*: otra aplicación la está usando (Teams, el navegador): ciérrala. En Windows, comprueba en **Configuración → Privacidad y seguridad → Cámara** que las aplicaciones de escritorio pueden usarla.
- *«No se ha podido cargar el modelo de gestos»*: no hay conexión para descargarlo la primera vez. Vuelve a probar con conexión.
- *No reconoce casi nada*: hay poca luz o la mano está a contraluz (una ventana detrás), muy cerca o muy lejos. Ponte de cara a la luz.
- *`pip` falla con `WinError 206`*: la carpeta está en una ruta demasiado larga o en OneDrive, como en la 1.ª parte.

---

## Paso 15 · Gestos en el BugTracker

**Objetivo.** Que, con los gestos activados, el **pulgar arriba** seleccione la incidencia siguiente, el **pulgar abajo** la anterior y la **palma abierta** limpie el formulario; y que los gestos se activen y desactiven con una acción del menú, con su atajo.

**Mini-explicación.** La ventana usa el detector como usa el `Buscador`: crea el componente y conecta su señal a un método suyo. Los gestos son un **atajo**, no la única forma: todo se sigue pudiendo hacer con el teclado y el ratón, y la cámara solo se enciende si se pide (privacidad). Por eso se añade una acción **marcable** en el menú y en la barra de herramientas ([apuntes de la UD4, apartados 4 y 6](../apuntes/UD4-interfaces-naturales.md#4-los-gestos-de-la-mano)).

**Pista.** En `main.py`:

1. Añade los imports: `from PySide6.QtGui import QAction` y `from gestos import NOMBRES, DetectorGestos`.
2. En `__init__`, debajo de `self.configurar_resumen()`, añade `self.configurar_gestos()`.
3. Añade estos métodos dentro de la clase, debajo de los del paso 12:

```python
    def configurar_gestos(self):
        self.detector = DetectorGestos(self)
        self.detector.gestoDetectado.connect(self.aplicar_gesto)
        self.detector.error.connect(self.error_gestos)
        self.accionGestos = QAction("&Gestos con la cámara", self)
        self.accionGestos.setCheckable(True)
        self.accionGestos.setShortcut("Ctrl+G")
        self.accionGestos.setStatusTip("Pulgar arriba o abajo: incidencia siguiente o anterior. Palma abierta: limpiar")
        self.accionGestos.toggled.connect(self.activar_gestos)
        self.ui.menuArchivo.insertAction(self.ui.actionSalir, self.accionGestos)
        self.ui.toolBarPrincipal.addAction(self.accionGestos)

    def activar_gestos(self, activar):
        if activar:
            if self.detector.iniciar():
                self.statusBar().showMessage("Gestos activados", 3000)
        else:
            self.detector.detener()
            self.statusBar().showMessage("Gestos desactivados", 3000)

    def error_gestos(self, mensaje):
        self.accionGestos.setChecked(False)
        QMessageBox.warning(self, "Gestos", mensaje)

    def aplicar_gesto(self, gesto):
        if gesto == "Thumb_Up":
            self.mover_seleccion(1)
        elif gesto == "Thumb_Down":
            self.mover_seleccion(-1)
        elif gesto == "Open_Palm":
            self.limpiar_formulario()
        else:
            return
        self.statusBar().showMessage(f"Gesto: {NOMBRES[gesto]}", 2000)

    def mover_seleccion(self, paso):
        """Selecciona la fila siguiente (paso 1) o la anterior (paso -1) de la tabla."""
        filas = self.proxy.rowCount()
        if filas == 0:
            return
        actuales = self.ui.tblIncidencias.selectionModel().selectedRows()
        fila = actuales[0].row() + paso if actuales else 0
        self.ui.tblIncidencias.selectRow(max(0, min(fila, filas - 1)))
```

4. En `closeEvent`, antes de `super().closeEvent(evento)`, añade `self.detector.detener()`: así la cámara se apaga al cerrar.

- `setCheckable(True)` hace que la acción tenga dos estados, activada y desactivada, y la señal `toggled(bool)` dice cuál.
- `mover_seleccion` trabaja con las filas **de la vista** (`self.proxy`): si el `Buscador` está filtrando, el pulgar recorre solo las incidencias que se ven. Al seleccionar una fila, se rellena el formulario solo, como al hacer clic.
- El detector solo emite un gesto cuando se mantiene varios fotogramas, y no lo repite hasta que cambia: así se evitan los **falsos positivos** al mover la mano.

**Comprueba que…**

- en el menú **Archivo** y en la barra de herramientas está **Gestos con la cámara**, y `Ctrl+G` la activa y la desactiva;
- con los gestos activados: el **pulgar arriba** selecciona la incidencia siguiente y rellena el formulario, el **pulgar abajo** la anterior, la **palma abierta** limpia el formulario, y la barra de estado dice qué gesto ha entendido;
- con el `Buscador` filtrando (`error`), el pulgar recorre solo las incidencias que se ven;
- al desactivarlos, la cámara se apaga (la luz de la cámara del portátil se apaga);
- con la cámara ocupada por otra aplicación, sale un aviso y la acción vuelve a desactivarse;
- todo lo que hacen los gestos se puede hacer también con el teclado y el ratón.

**Si te falla…**

- *`ModuleNotFoundError: No module named 'gestos'`*: `gestos.py` no está en la carpeta `bugtracker`.
- *Repite el gesto sin parar*: no; si te pasa, es que la mano cambia de gesto a otro y vuelve. Haz el gesto, quieto, y baja la mano.
- *La cámara sigue encendida al cerrar*: falta `self.detector.detener()` en `closeEvent`.

---

## Paso 16 · Probar y revisar con criterio

**Objetivo.** Probar lo hecho esta semana con tres tipos de prueba y revisar los gestos con los criterios de diseño de una interfaz natural.

**Pista.** En `notas.md`, añade un apartado «3.ª parte» con dos tablas ([apuntes de la UD4, apartados 6 y 7](../apuntes/UD4-interfaces-naturales.md#6-diseñar-una-interfaz-natural-con-criterio)):

1. **Pruebas.** Hazlas y apunta qué haces, qué esperas y qué sale:

   | Tipo | Prueba | Resultado esperado | Resultado |
   |---|---|---|---|
   | De humo | Abrir la aplicación | Se abre con la tabla y el resumen por estado | |
   | De integración | Añadir una incidencia «Pendiente» desde la ventana | Aparece en la tabla, se guarda en la base de datos (sigue al cerrar y abrir) y el recuento de «Pendiente» sube en 1 | |
   | De regresión | `python -m pytest -v` después de todos los cambios | Todas las pruebas pasan | |

2. **Criterios.** Para los gestos del BugTracker, responde en una línea cada pregunta: ¿para quién son útiles y en qué situación?, ¿hay alternativa con teclado y ratón?, ¿sabe la persona qué ha entendido la aplicación?, ¿qué pasa si se equivoca?, ¿en qué entorno fallan?, ¿se avisa de que la cámara está activa?, ¿cansan?

**Comprueba que…**

- `notas.md` tiene la tabla de pruebas con las tres pruebas hechas y su resultado;
- tiene las siete respuestas sobre los criterios, una por línea;
- sabes explicar la diferencia entre una prueba unitaria, una de integración y una de regresión.

---

## Entrega

Qué se entrega y cuándo: [`entrega.md`](entrega.md).

## Cómo comprobarlo (lista final)

| Comprobación | Hecho |
|---|---|
| La barra de estado muestra el recuento de cada estado, sale de una consulta con `GROUP BY` en `bd.py` y se actualiza al añadir, modificar y eliminar |  |
| El `Buscador` está en el diseño de Qt Designer, promocionado, y funciona como antes |  |
| Sé por qué el componente tiene que recibir `parent` como primer parámetro para usarlo desde Qt Designer |  |
| `python gestos.py` reconoce los gestos con la cámara del portátil |  |
| Con **Gestos con la cámara** (`Ctrl+G`), el pulgar arriba y abajo recorren la tabla y la palma abierta limpia el formulario |  |
| La cámara solo está encendida con la acción activada, y hay aviso si no se puede abrir |  |
| Hice las pruebas de humo, de integración y de regresión y apunté el resultado |  |
| Revisé los gestos con los criterios de diseño de una interfaz natural |  |
