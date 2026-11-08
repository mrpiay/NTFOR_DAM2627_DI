# UD1 · Diseño de interfaces, usabilidad y accesibilidad

Lo básico que hay que saber de la UD1. Cada apartado tiene la idea clave, lo que tienes que saber y, cuando hay conceptos que se confunden, una tabla para compararlos. Los ejemplos son del BugTracker del proyecto. Las preguntas para comprobar que lo entiendes están en los cuestionarios de autoevaluación.

---

## 1. Usabilidad, accesibilidad y experiencia de usuario

**En una frase:** una interfaz es buena si se entiende sin explicaciones, la puede usar cualquier persona y resulta agradable.

**Lo que tienes que saber**

- **Usabilidad:** lo fácil que es usar la aplicación para conseguir algo: que se aprenda rápido, se cometan pocos errores y se trabaje sin esfuerzo.
- **Accesibilidad:** que la pueda usar cualquier persona, también con una discapacidad: sin ver bien, sin ratón, con un lector de pantalla…
- **Experiencia de usuario (UX):** todo lo que siente la persona al usarla: si le resulta útil, cómoda y agradable. Incluye las dos anteriores.
- Una interfaz se diseña para quien la va a usar, no para quien la programa.

**Compara**

| | Usabilidad | Accesibilidad |
|---|---|---|
| Pregunta | ¿Es fácil de usar? | ¿La puede usar todo el mundo? |
| Ejemplo en el BugTracker | Un mensaje dice qué se ha guardado | Todo se puede hacer con el teclado |

---

## 2. Las heurísticas de Nielsen

**En una frase:** diez reglas generales para encontrar problemas de usabilidad revisando la interfaz.

**Lo que tienes que saber**

| Heurística | Idea | Ejemplo en el BugTracker |
|---|---|---|
| 1. Visibilidad del estado del sistema | La aplicación dice qué está pasando | «Incidencia añadida» en la barra de estado |
| 2. Relación con el mundo real | Usa las palabras del usuario | «Incidencia», «Prioridad», no términos técnicos |
| 3. Control y libertad | Se puede deshacer o cancelar | Cancelar en el diálogo y al confirmar un borrado |
| 4. Coherencia y estándares | Lo mismo se llama y funciona igual en todas partes | `Ctrl+N` es «Nuevo», como en cualquier programa |
| 5. Prevención de errores | Mejor evitar el error que avisarlo | «Eliminar» desactivado si no hay nada seleccionado |
| 6. Reconocer mejor que recordar | Las opciones a la vista | Tipo y prioridad en listas desplegables |
| 7. Flexibilidad y eficiencia | Atajos para quien tiene práctica | Atajos de teclado y doble clic para editar |
| 8. Diseño estético y minimalista | Solo lo necesario | Sin campos ni botones que no se usan |
| 9. Ayudar a reconocer y corregir errores | Mensajes claros que dicen qué hacer | «Falta el título» y el foco en ese campo |
| 10. Ayuda y documentación | Ayuda fácil de encontrar | Textos de ayuda (*tooltips*) en los botones |

- Una **evaluación heurística** consiste en revisar la interfaz con estas reglas y apuntar cada problema, la heurística que incumple y cómo arreglarlo.

---

## 3. Accesibilidad

**En una frase:** la accesibilidad se consigue con normas concretas: buen contraste, todo usable con el teclado y cada control con un nombre.

**Lo que tienes que saber**

- La referencia son las pautas **WCAG** (del W3C), con cuatro principios: la información tiene que ser **perceptible**, la interfaz **operable**, el contenido **comprensible** y el código **robusto** (que funcione con las ayudas técnicas). Tienen tres niveles: **A**, **AA** (el que se suele exigir) y **AAA**.
- **Contraste:** el texto normal necesita una relación de al menos **4,5:1** con el fondo (nivel AA). Se comprueba con herramientas como el comprobador de contraste de WebAIM.
- **Teclado:** todo se tiene que poder hacer sin ratón. Hacen falta un **orden de tabulación** lógico, **atajos** con `&` en las etiquetas (`&Título` es `Alt+T`), el **buddy** de cada etiqueta (el campo al que lleva su atajo) y que `Tab` no se quede atrapado en un campo de texto o una tabla.
- **Nombres accesibles:** cada control tiene que tener un nombre que lea el lector de pantalla (`accessibleName`), sobre todo los que solo tienen icono.
- **No depender solo del color:** un error no se indica solo en rojo; también con un texto.

**Compara**

| Problema | Quién lo sufre | Solución en Qt |
|---|---|---|
| Poco contraste | Personas con baja visión, o con mucha luz en la pantalla | Cambiar los colores hasta 4,5:1 |
| No se puede usar sin ratón | Personas con movilidad reducida o que usan lector de pantalla | Orden de tabulación, `&`, *buddy*, atajos |
| Un botón con solo un icono | Personas que usan lector de pantalla | `accessibleName` y *tooltip* |

---

## 4. Estándares

**En una frase:** seguir los estándares hace que la interfaz se entienda a la primera, porque funciona como las que ya se conocen.

**Lo que tienes que saber**

- **ISO 9241:** norma internacional de ergonomía de la interacción; define la usabilidad como eficacia, eficiencia y satisfacción.
- **WCAG 2.2:** las pautas de accesibilidad del W3C. En Europa se exigen a través de la norma **EN 301 549**, y en España, a las webs y aplicaciones del sector público, con el **Real Decreto 1112/2018**.
- Las **guías de cada sistema** (Windows, macOS, GNOME, Material Design) fijan menús, atajos y aspecto habituales.
- Seguir los estándares reduce lo que hay que aprender, evita errores y, en accesibilidad, a veces es obligatorio.

---

## 5. Distribuir los controles, elegirlos y darles aspecto

**En una frase:** cada control en su sitio, el adecuado para cada dato, legible y con mensajes claros.

**Lo que tienes que saber**

- **Distribución:** agrupar lo relacionado, alinear, seguir el orden de lectura (de arriba abajo y de izquierda a derecha) y dejar los botones principales donde se esperan (Aceptar y Cancelar, abajo a la derecha). En Qt, con **layouts**, para que se adapte al cambiar el tamaño.
- **Elegir el control:**

| Dato | Control (Qt) |
|---|---|
| Texto de una línea | `QLineEdit` |
| Texto largo | `QTextEdit` / `QPlainTextEdit` |
| Uno entre pocas opciones fijas | `QComboBox` o `QRadioButton` |
| Sí o no | `QCheckBox` |
| Un número en un rango | `QSpinBox` |
| Una fecha | `QDateEdit` |
| Una lista de registros | `QTableView` |

- **Aspecto:** pocos colores y con buen contraste, una o dos tipografías legibles y tamaños suficientes. El color destaca lo importante, no decora.
- **Mensajes:** breves, en el idioma del usuario, que digan qué ha pasado y qué hacer («Falta el título», no «Error 23»). Si piden confirmación, que se vea qué se va a hacer («¿Eliminar la incidencia 4?»).

---

## 6. Menús, barras de herramientas y atajos

**En una frase:** cada orden de la aplicación está en el menú, en la barra de herramientas y en un atajo, y en los tres sitios es la misma.

**Lo que tienes que saber**

- Los **menús** siguen el orden estándar: *Archivo* (Nuevo, Guardar, Salir), *Editar*, *Ver*… y *Ayuda* al final.
- La **barra de herramientas** lleva las órdenes más usadas; el resto, solo en el menú.
- Los **atajos** son los habituales: `Ctrl+N` (nuevo), `Ctrl+S` (guardar), `Supr` (eliminar), `Ctrl+Q` (salir).
- Una orden que no se puede hacer en ese momento se **desactiva**, en el menú y en la barra a la vez.
- En Qt, todo esto es una **`QAction`**: una sola acción con su texto, su atajo y su estado, puesta en el menú y en la barra (UD2).

---

## 7. Evaluar la usabilidad y la accesibilidad

**En una frase:** la usabilidad se comprueba revisando la interfaz con reglas y viendo a personas reales usarla.

**Lo que tienes que saber**

- **Evaluación heurística:** una o varias personas revisan la interfaz con las heurísticas de Nielsen y las pautas de accesibilidad, y apuntan cada problema, su gravedad y la mejora.
- **Prueba con usuarios:** una persona hace tareas concretas («crea una incidencia sin usar el ratón») mientras **piensa en voz alta**, sin recibir ayuda. Se apunta si lo consigue, dónde duda y qué falla.
- **Bocetos y prototipos** (*wireframes*, con herramientas como diagrams.net o Figma): se prueban antes de programar, cuando cambiar algo es barato.
- **Herramientas de comprobación:** comprobadores de contraste, y probar la aplicación entera solo con el teclado y con un lector de pantalla.

**Compara**

| | Evaluación heurística | Prueba con usuarios |
|---|---|---|
| Quién | Personas que conocen las reglas | Personas que van a usar la aplicación |
| Qué encuentra | Problemas que incumplen reglas conocidas | Problemas reales, que a veces nadie había previsto |
| Coste | Bajo | Algo mayor |
