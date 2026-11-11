# Repaso · UD1 y UD2

Repaso de lo que se trabajó con Julia en las tareas de Teams («Wireframe», «Accesibilidad», «TRABAJO UD1» y «Bloc Notas») y vuelve a entrar en la P1: prototipos, auditoría de accesibilidad, rediseño y la ventana principal de una aplicación. Lo que se explica en los apuntes de la semana del 2 al 6 solo se menciona aquí, con su enlace.

---

## 1. Del boceto al prototipo

**En una frase:** una interfaz se diseña por fases, con prototipos cada vez más parecidos al producto final; cuanto antes se prueba, más barato es cambiarla.

**Lo que tienes que saber**

- **Boceto** (*sketch*): a mano o muy simple, para ordenar las ideas. Muy baja fidelidad.
- **Wireframe**: la **estructura** de cada pantalla: qué hay y dónde, con cajas y textos, **sin colores, fuentes ni imágenes**. Baja fidelidad.
- **Mockup**: el wireframe con el **aspecto final** (colores, tipografía, iconos, imágenes), pero **sin funcionar**. Media fidelidad.
- **Prototipo**: ya se puede **usar en parte**, por ejemplo navegar entre pantallas. Alta fidelidad.
- El **mapa de navegación** dibuja las pantallas y cómo se pasa de una a otra.
- Herramientas habituales: draw.io, Figma, Pencil o papel y lápiz.

**Compara**

| | Boceto | Wireframe | Mockup | Prototipo |
|---|---|---|---|---|
| Aspecto final (colores, fuentes) | No | No | Sí | Sí |
| Se puede usar | No | No | No | En parte |
| Para qué | Ordenar ideas | Decidir la estructura | Decidir el aspecto | Probar con usuarios |

---

## 2. Auditoría de accesibilidad con WAVE

**En una frase:** WAVE es una extensión del navegador que marca sobre la propia página los problemas de accesibilidad que se pueden detectar de forma automática; el resto hay que revisarlo a mano.

**Lo que tienes que saber**

- Se instala en Chrome, Firefox o Edge y se lanza sobre la página abierta. Pone **iconos encima de cada elemento** y un resumen con:
  - **errores** (rojo): fallos seguros, como una imagen sin texto alternativo, un campo de formulario sin etiqueta o un enlace vacío;
  - **errores de contraste**: texto que no se distingue bien del fondo;
  - **alertas** (amarillo): posibles problemas que hay que comprobar, como un salto en los niveles de los títulos.
- Una herramienta automática **no lo detecta todo**. Hace falta una **revisión manual**:
  - recorrer la página **solo con el teclado** (Tab, Mayús+Tab, Intro): ¿se llega a todo y se ve dónde está el foco?;
  - ampliar al **200 %**: ¿se sigue leyendo y usando?;
  - comprobar que los textos alternativos y las etiquetas **dicen algo útil**.
- Cada problema se describe con **qué ocurre**, **cómo se ha detectado**, **a quién afecta** y **cómo se corrige**.

**Compara**

| | WAVE (automático) | Revisión manual |
|---|---|---|
| Detecta | Falta de texto alternativo, etiquetas, contraste, estructura | Uso con teclado, foco visible, ampliación, si los textos tienen sentido |
| No detecta | Si el texto alternativo es útil, si el orden de tabulación es lógico | Lo que solo se ve en el código |

Las pautas de accesibilidad (WCAG) y el contraste: [UD1, apartado 3](../../2026_11_02-06/apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#3-accesibilidad).

---

## 3. Del análisis al rediseño

**En una frase:** rediseñar una interfaz es encontrar sus problemas, decidir cuáles arreglar primero y proponer una versión mejor que los resuelva.

**Lo que tienes que saber**

1. **Analizar**: hacer las tareas habituales de la aplicación y anotar los problemas de **usabilidad** (cada uno con la **heurística de Nielsen** que incumple) y de **accesibilidad** (auditoría con WAVE y revisión manual).
2. **Priorizar**: ordenar los problemas por **gravedad** (¿impide terminar la tarea?), **frecuencia** (¿pasa siempre o a veces?) y **a cuántas personas afecta**.
3. **Rediseñar**: un wireframe o un mockup de cada pantalla que resuelva los problemas, empezando por los más urgentes.
4. **Justificar**: para cada cambio, qué problema resuelve y qué heurística o pauta cumple ahora.

Las diez heurísticas de Nielsen: [UD1, apartado 2](../../2026_11_02-06/apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#2-las-heurísticas-de-nielsen). Cómo evaluar la usabilidad y la accesibilidad: [UD1, apartado 7](../../2026_11_02-06/apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#7-evaluar-la-usabilidad-y-la-accesibilidad).

---

## 4. La ventana principal: `QMainWindow`

**En una frase:** `QMainWindow` es la ventana típica de una aplicación de escritorio, con zonas ya preparadas para el menú, la barra de herramientas, el contenido y la barra de estado.

**Lo que tienes que saber**

- Sus zonas, de arriba abajo:
  - **barra de menús** (`menuBar()`);
  - **barras de herramientas** (`QToolBar`);
  - **widget central** (`setCentralWidget(...)`), que es el contenido, por ejemplo un `QTextEdit` en un editor de notas;
  - **barra de estado** (`statusBar()`), para mensajes breves: `self.statusBar().showMessage("Guardado", 3000)` lo muestra 3 segundos.
- Una **acción** (`QAction`) es una orden con su texto, su icono y su **atajo** (`Ctrl+S`). La **misma acción** se pone en el menú y en la barra de herramientas, y su señal `triggered` se conecta una sola vez.
- **Diálogo propio**: una ventana `QDialog` hecha en Designer con un **`QDialogButtonBox`** (Aceptar / Cancelar). Sus señales `accepted` y `rejected` se conectan a `accept()` y `reject()`, y **`exec()`** abre el diálogo y espera: devuelve si se aceptó.
- **Diálogos ya hechos**: `QMessageBox` para avisar o preguntar, y **`QFileDialog`** para elegir un archivo.

```python
ruta, _ = QFileDialog.getOpenFileName(self, "Abrir nota", "", "Texto (*.txt)")
if ruta:                                   # vacía si se cancela
    with open(ruta, encoding="utf-8") as f:
        self.ui.texto.setPlainText(f.read())
    self.statusBar().showMessage("Nota abierta", 3000)
```

Acciones, menús y barras de herramientas: [UD2, apartado 5](../../2026_11_02-06/apuntes/UD2-pyside6-y-qt-designer.md#5-acciones-menús-y-barras-de-herramientas). Diálogos y validación: [UD2, apartado 6](../../2026_11_02-06/apuntes/UD2-pyside6-y-qt-designer.md#6-diálogos-y-validación).

---

## 5. Lo demás, en los apuntes de la semana del 2 al 6

| Tema | Dónde |
|---|---|
| Usabilidad, accesibilidad y experiencia de usuario | [UD1, apartado 1](../../2026_11_02-06/apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#1-usabilidad-accesibilidad-y-experiencia-de-usuario) |
| Estándares | [UD1, apartado 4](../../2026_11_02-06/apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#4-estándares) |
| Distribuir y elegir los controles; colores y fuentes | [UD1, apartado 5](../../2026_11_02-06/apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#5-distribuir-los-controles-elegirlos-y-darles-aspecto) |
| Menús, barras de herramientas y atajos (diseño) | [UD1, apartado 6](../../2026_11_02-06/apuntes/UD1-diseno-usabilidad-y-accesibilidad.md#6-menús-barras-de-herramientas-y-atajos) |
| Qt Designer, archivos `.ui` y `pyside6-uic` | [UD2, apartado 2](../../2026_11_02-06/apuntes/UD2-pyside6-y-qt-designer.md#2-del-diseño-al-código) |
| Controles, propiedades y layouts | [UD2, apartado 3](../../2026_11_02-06/apuntes/UD2-pyside6-y-qt-designer.md#3-controles-propiedades-y-layouts) |
| Señales y slots | [UD2, apartado 4](../../2026_11_02-06/apuntes/UD2-pyside6-y-qt-designer.md#4-señales-y-slots) |
| Datos con SQLite | [UD2, apartado 7](../../2026_11_02-06/apuntes/UD2-pyside6-y-qt-designer.md#7-datos-con-sqlite) |
