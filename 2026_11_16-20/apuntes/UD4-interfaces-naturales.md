# UD4 · Interfaces naturales (2)

Continuación de los [apuntes de la UD4 de la semana del 9 al 13](../../2026_11_09-13/apuntes/UD4-interfaces-naturales.md) (apartado 1: tipos, ventajas y límites). Aquí, cómo reconoce un ordenador la voz, los gestos y el cuerpo, qué herramientas hay, qué criterios seguir al diseñar una interfaz natural y cómo se documenta y se prueba una aplicación. Las preguntas para comprobar que lo entiendes están en el [cuestionario](../cuestionario.md) de la semana.

**Qué hay que saber de estos apuntes:** qué se puede hacer con cada tecnología, para qué sirve y con qué criterios se usa. **No hay que saber programarlo:** las librerías cambian mucho de un año a otro; lo que dura es el criterio. La práctica de esta semana es un solo caso, un gesto de la mano en el BugTracker.

Hay tres tipos de contenido:

- Lo que no lleva marca es lo **imprescindible**: hay que entenderlo y saber explicarlo con tus palabras.
- > **Para saber más.** Lo que va en un recuadro como este ayuda a entender, pero no hay que aprenderlo de memoria.
- *Para la práctica: paso N del proyecto.* Los apartados que empiezan así recogen los detalles que se usan en ese paso.

---

## 2. Cómo reconoce un ordenador la voz, los gestos y el cuerpo

**En una frase:** un **modelo** de aprendizaje automático, entrenado antes con muchos ejemplos, recibe la imagen de la cámara o el sonido del micrófono y devuelve qué ha reconocido y con cuánta **confianza**.

**Lo que tienes que saber**

- Nadie programa a mano «si los píxeles son así, es un pulgar arriba». Se reúnen miles de ejemplos etiquetados (imágenes de manos con su gesto, grabaciones con su texto) y un algoritmo **entrena un modelo** que aprende a reconocerlos. Después, la aplicación solo **usa** el modelo ya entrenado.
- El modelo no está seguro de nada: da cada resultado con una **puntuación de confianza**, de 0 a 1. La aplicación decide a partir de qué confianza lo acepta (por ejemplo, 0,6) y qué hace con los resultados dudosos.
- **Funcionamiento en el equipo o en la nube.** Algunos modelos se ejecutan en el propio ordenador (MediaPipe, Vosk): funcionan sin conexión y la imagen o la voz no salen del equipo. Otros, en servidores de internet (los asistentes de voz comerciales): suelen acertar más, pero necesitan conexión y envían los datos fuera, y eso afecta a la **privacidad**.

**Las herramientas**

| Herramienta | Qué hace | Cómo se usa |
|---|---|---|
| **MediaPipe** (Google) | Modelos ya entrenados para manos, gestos, cuerpo y cara, que funcionan en el equipo | Librería para Python, Android, iOS y la web |
| **Teachable Machine** (Google) | Entrenar un modelo **propio** sin programar: se graban ejemplos de cada clase (por ejemplo, tres gestos inventados) con la cámara o el micrófono, y la web entrena el modelo | Desde el navegador; el modelo se exporta para usarlo en una aplicación |
| **Vosk**, **Whisper** | Reconocimiento de voz que funciona en el equipo, sin conexión | Librerías para Python y otros lenguajes |
| **OpenCV** | Leer la cámara y tratar las imágenes (girarlas, dibujar sobre ellas) | Librería para Python, C++ y otros |

**Compara**

| | Modelo ya entrenado (MediaPipe) | Modelo propio (Teachable Machine) |
|---|---|---|
| Qué reconoce | Lo que decidió quien lo entrenó (siete gestos de la mano, por ejemplo) | Lo que tú quieras, si le das ejemplos |
| Qué hace falta | Instalar la librería y el modelo | Grabar ejemplos de cada clase y entrenar |
| Cuándo conviene | Si lo que reconoce encaja con lo que necesitas | Si necesitas algo propio (gestos de una lengua de signos, sonidos de una máquina) |

---

## 3. La voz

**En una frase:** el **reconocimiento de voz** convierte lo que se dice en texto; la **síntesis de voz** convierte un texto en voz.

**Lo que tienes que saber**

- Dos usos del reconocimiento: **dictado** (todo lo que se dice se convierte en texto: la descripción de una incidencia) y **órdenes** (unas pocas frases fijas que disparan acciones: «nueva incidencia», «guardar»).
- **Límites:** el ruido, varias personas hablando a la vez, los acentos y las palabras técnicas hacen que se equivoque. Por eso la práctica de esta semana no es de voz: en un aula con todo el grupo hablando a la vez, falla.
- **A quién ayuda:** a personas que no pueden usar el teclado o el ratón, y a cualquiera que tenga las manos ocupadas. La síntesis de voz es la base de los **lectores de pantalla** para personas ciegas.
- **Criterios:** pocas órdenes, cortas y distintas entre sí; confirmar lo que se ha entendido antes de hacer algo que no se puede deshacer («¿Eliminar la incidencia 7?»); y que se pueda hacer todo también con el teclado.

---

## 4. Los gestos de la mano

*Para la práctica: pasos 14 y 15 del proyecto.*

**En una frase:** el modelo localiza la mano en la imagen de la cámara, marca 21 puntos (las articulaciones de los dedos y la muñeca) y, a partir de su posición, dice qué gesto es.

**Lo que tienes que saber**

- El reconocedor de gestos de MediaPipe reconoce siete gestos: **puño**, **palma abierta**, **índice hacia arriba**, **pulgar arriba**, **pulgar abajo**, **victoria** y **«te quiero»** de la lengua de signos.
- **Falsos positivos:** el modelo puede «ver» un gesto que nadie ha hecho, por ejemplo mientras la mano se mueve de un gesto a otro. Por eso un gesto solo se da por bueno si se **repite varios fotogramas seguidos** y con confianza suficiente; y la misma acción no se repite hasta que el gesto cambia.
- **Límites:** la luz (a contraluz o con poca luz falla), la distancia a la cámara, la **fatiga** (mantener el brazo levantado cansa: no sirve para trabajar horas) y la **privacidad** (la cámara encendida).
- **Criterios:**
  - **pocos gestos, distintos entre sí y cómodos**, y asociados a acciones que se entiendan (pulgar arriba y abajo para siguiente y anterior);
  - **retroalimentación:** la aplicación dice qué gesto ha entendido (en la barra de estado, por ejemplo);
  - la cámara se **activa y se desactiva** a voluntad, y se ve cuándo está activa;
  - **siempre una alternativa** con teclado y ratón: el gesto es un atajo, no la única forma de hacer algo.

---

## 5. El cuerpo y la realidad aumentada

**En una frase:** la **detección del cuerpo** localiza la postura de una persona en la imagen; la **realidad aumentada** superpone información generada por el ordenador sobre la imagen real.

**Lo que tienes que saber**

- **El cuerpo.** El modelo de postura de MediaPipe marca 33 puntos del cuerpo (hombros, codos, muñecas, caderas, rodillas…). Con ellos se calcula, por ejemplo, si los brazos están levantados o el ángulo de una rodilla. Usos: aplicaciones de ejercicio y rehabilitación que cuentan repeticiones o corrigen la postura, juegos, y controlar una aplicación con movimientos amplios.
- **La realidad aumentada (RA).** Se dibuja algo sobre la imagen de la cámara en el sitio correcto: una etiqueta sobre cada objeto, unas gafas sobre una cara, las instrucciones de montaje sobre una pieza. Puede apoyarse en **marcadores** (un código impreso que la cámara reconoce y que marca dónde dibujar) o funcionar **sin marcadores**, reconociendo superficies, caras o manos.
- **Criterios:** los mismos que con los gestos (luz, espacio, fatiga, privacidad, alternativa), y además que lo que se superpone **no tape** la información real importante y sea **legible** sobre cualquier fondo.

**Compara**

| | Gestos de la mano | Cuerpo | Realidad aumentada |
|---|---|---|---|
| Qué detecta o hace | La forma de la mano | La postura de todo el cuerpo | Dibuja sobre la imagen real |
| Puntos que localiza (MediaPipe) | 21 | 33 | — (usa los de la mano, la cara o el cuerpo) |
| Ejemplo | Pasar de incidencia con el pulgar | Contar sentadillas | Una etiqueta sobre cada objeto que ve la cámara |

---

## 6. Diseñar una interfaz natural con criterio

**En una frase:** una interfaz natural se añade cuando **ayuda** a alguien en una situación concreta, y siempre como alternativa, nunca como la única forma de usar la aplicación.

**Lo que tienes que saber**

| Criterio | Pregunta que hay que hacerse |
|---|---|
| **Para quién** | ¿A quién ayuda y en qué situación? (manos ocupadas, movilidad reducida, distancia) |
| **Alternativa** | ¿Se puede hacer lo mismo con teclado y ratón? (WCAG: toda la funcionalidad, también desde el teclado) |
| **Retroalimentación** | ¿Sabe la persona qué ha entendido la aplicación? |
| **Errores** | ¿Qué pasa si el reconocimiento se equivoca? ¿Se puede deshacer? ¿Se pide confirmación antes de lo irreversible? |
| **Entorno** | ¿Funciona con ruido, con poca luz, con más gente alrededor? |
| **Privacidad** | ¿Se avisa de que la cámara o el micrófono están activos? ¿Los datos salen del equipo? |
| **Esfuerzo** | ¿Cansa? ¿Se puede usar durante mucho rato? |

Se comprueba con una **prueba de usabilidad**, como la del paso 7: una persona que no conoce la aplicación hace tareas concretas sin ayuda, y se anota dónde duda o se equivoca.

---

## 7. Documentar y probar una aplicación

*Para la práctica: paso 16 del proyecto.*

**En una frase:** una aplicación se entrega con su **documentación** (para quien la usa y para quien la mantiene) y **probada**, también después de cada cambio.

**Lo que tienes que saber**

- **La información persistente** es lo que se guarda aunque se cierre la aplicación: en el BugTracker, la base de datos (`bugtracker.db`) y los ajustes de `QSettings`. Se **documenta su estructura**: qué tablas y campos hay, de qué tipo, qué valores admiten (la tabla `incidencias`, con sus seis campos, en `bd.py`).
- **El manual de usuario** explica a quien **usa** la aplicación cómo hacer sus tareas, no cómo está programada: qué hace, cómo se instala y se abre, cómo se hace cada tarea paso a paso (con capturas), los atajos y qué hacer ante los problemas frecuentes. La **guía de referencia** es más breve: la lista de órdenes, opciones y atajos para consultar.
- Hoy se suele escribir en **Markdown** y publicarse como **PDF** o como **web estática** (GitHub Pages, Read the Docs): se escribe el contenido y la herramienta le da el formato.
- **Tipos de pruebas funcionales** (comprueban que la aplicación hace lo que debe):

| Prueba | Qué comprueba | En el BugTracker |
|---|---|---|
| **Unitaria** | Una pieza sola, aislada del resto | Las pruebas del `Buscador` con pytest-qt (paso 6) |
| **De integración** | Que las piezas funcionan **juntas** | Que al añadir una incidencia desde la ventana se guarda en la base de datos y el resumen por estado se actualiza |
| **De regresión** | Que lo que funcionaba **sigue funcionando** después de un cambio | Volver a pasar todas las pruebas después de cambiar el orden de los parámetros del `Buscador` (paso 13) |
| **De humo** | Lo mínimo, rápido: ¿arranca y abre la ventana? | Abrir la aplicación y ver la tabla |
| **De aceptación** | Que hace lo que pidió quien la encargó | Recorrer con esa persona sus tareas reales |

- Las **no funcionales** comprueban cómo lo hace: rendimiento, carga, seguridad, compatibilidad, **usabilidad**…
- Las pruebas automáticas (como las de pytest) se pueden repetir en segundos después de cada cambio: por eso son la base de las pruebas de regresión.

> **Para saber más.** En el **desarrollo guiado por pruebas** (TDD), primero se escribe una prueba que falla, después el código mínimo para que pase y después se mejora el código. Con la **integración continua**, las pruebas se ejecutan solas cada vez que se sube un cambio al repositorio.

---

## Dónde consultar

- **MediaPipe**, documentación oficial, en inglés: [reconocedor de gestos](https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer), [puntos de la mano](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) y [postura del cuerpo](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker).
- **Teachable Machine:** [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com/), con sus tutoriales.
- **Accesibilidad:** las pautas WCAG, en español: [resumen de las WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/es), del W3C.
- **Qt Designer y los componentes propios** (*Promote to*), en inglés: [Using Custom Widgets with Qt Designer](https://doc.qt.io/qt-6/designer-using-custom-widgets.html).
- **Pruebas:** [documentación de pytest](https://docs.pytest.org/) y de [pytest-qt](https://pytest-qt.readthedocs.io/), en inglés.
- **Libro:** McGraw-Hill, *Desarrollo de interfaces*, U6 «Pruebas, distribución e implantación de aplicaciones» (tipos de pruebas) y U7 «Documentación de proyectos» (Markdown, manual, publicación).
