# Autoevaluación · semana del 16 al 20 de noviembre · soluciones

Entre paréntesis, dónde está la respuesta para repasarla. El proyecto con la 3.ª parte terminada está en la carpeta `bugtracker`.

## Cuestiones sobre el proyecto

**1.** En el paso 12, ¿qué hace la consulta `SELECT estado, COUNT(*) AS total FROM incidencias GROUP BY estado`? ¿Por qué va en `bd.py` y no en `main.py`? ¿Por qué se llama a `actualizar_resumen()` al final de `cargar_incidencias()`?

**Respuesta.** *(ampliación UD2 y UD3, apartado 1; proyecto, paso 12)* Agrupa las incidencias por estado y cuenta cuántas hay en cada grupo: una fila por estado con su total (`AS total` da nombre a la columna del recuento). Va en `bd.py` por la **regla de separación**: todo el SQL está en `bd.py` y `main.py` solo muestra el resultado; así la interfaz se puede cambiar sin tocar la base de datos, y al revés. Se llama al final de `cargar_incidencias()` porque ese método se ejecuta cada vez que cambian los datos (al arrancar, al añadir, al modificar y al eliminar): así el recuento siempre está al día.

**2.** En el paso 13, ¿qué hace **Promote to…** en Qt Designer? ¿Por qué el `Buscador` se ve como un recuadro vacío en el diseño? ¿Por qué hubo que cambiar el orden de los parámetros de su `__init__`?

**Respuesta.** *(ampliación UD2 y UD3, apartado 2; proyecto, paso 13)* Hace que un `QWidget` del diseño se genere como un componente propio: en el código generado, `Buscador(self.centralwidget)` en lugar de un `QWidget`. Se ve vacío porque Qt Designer solo sabe dibujar los controles de Qt, no los propios; el componente aparece al ejecutar. Hubo que poner `parent` primero porque el código generado le pasa el padre como **primer parámetro**; con `etiqueta` primero, el padre llegaba como texto de la etiqueta y daba error.

**3.** Después de cambiar el orden de los parámetros del `Buscador`, se ejecutó `python -m pytest -v`. ¿Qué tipo de prueba es esa y por qué hace falta?

**Respuesta.** *(UD4, apartado 7; proyecto, pasos 13 y 16)* Es una **prueba de regresión**: repetir las pruebas que ya pasaban después de un cambio, para comprobar que lo que funcionaba sigue funcionando. Hace falta porque cambiar cómo se crea un componente puede romper a quien ya lo usa (las pruebas, otras aplicaciones).

**4.** En el paso 15, ¿por qué los gestos se activan con una acción marcable (`Ctrl+G`) y no están siempre encendidos? ¿Qué pasa con la cámara al cerrar la aplicación?

**Respuesta.** *(UD4, apartados 4 y 6; proyecto, paso 15)* Por **privacidad** (la cámara solo se enciende cuando la persona lo pide, y se ve si está activa) y porque los gestos son un **atajo** opcional: todo se puede hacer con el teclado y el ratón. Al cerrar, `closeEvent` llama a `detector.detener()`, que apaga la cámara.

**5.** ¿Por qué el detector solo da un gesto por bueno cuando se repite varios fotogramas seguidos y no lo repite hasta que cambia? ¿Qué problema evita?

**Respuesta.** *(UD4, apartado 4; proyecto, paso 15)* Para evitar **falsos positivos**: al mover la mano de un gesto a otro, el modelo puede «ver» durante un instante un gesto que nadie ha hecho. Exigir varios fotogramas seguidos filtra esos instantes, y no repetir el gesto hasta que cambia evita que un mismo gesto mantenido dispare la acción muchas veces.

## Cuestiones sobre los apuntes

**6.** ¿Qué es un modelo de aprendizaje automático y qué significa la **confianza** de un resultado? ¿Qué ventaja tiene, para la privacidad, que el modelo funcione en el propio equipo y no en la nube?

**Respuesta.** *(UD4, apartado 2)* Un modelo es el resultado de **entrenar** un algoritmo con muchos ejemplos etiquetados; después, la aplicación solo lo usa para reconocer entradas nuevas. La **confianza** es una puntuación de 0 a 1 de lo seguro que está de cada resultado; la aplicación decide a partir de cuánto lo acepta. Si funciona en el equipo, la imagen o la voz **no salen del ordenador**, y además funciona sin conexión.

**7.** ¿En qué se diferencia usar un modelo ya entrenado, como el reconocedor de gestos de MediaPipe, de entrenar uno propio con Teachable Machine? Pon un ejemplo en el que convenga cada uno.

**Respuesta.** *(UD4, apartado 2)* El modelo ya entrenado reconoce lo que decidió quien lo entrenó (los siete gestos de MediaPipe) y solo hay que usarlo; con Teachable Machine se entrena uno **propio** grabando ejemplos de cada clase, para reconocer lo que se necesite. Ejemplos: pasar de incidencia con el pulgar (MediaPipe ya lo reconoce); reconocer tres gestos inventados para una aplicación concreta o los signos de una lengua de signos que el modelo general no conoce (Teachable Machine).

**8.** Una aplicación de un taller de coches quiere que el mecánico, con las manos sucias, consulte el siguiente paso de una reparación. ¿Usarías voz o gestos? Razónalo con al menos tres criterios de diseño de una interfaz natural.

**Respuesta.** *(UD4, apartados 3, 4 y 6)* Respuesta abierta; se valora el razonamiento con criterios. Por ejemplo: **voz**, porque tiene las manos ocupadas y sucias (para quién y en qué situación) y un gesto obligaría a dejar lo que hace; pero un taller es ruidoso (entorno), así que conviene usar **órdenes cortas y pocas** («siguiente», «repetir») y no dictado, dar **retroalimentación** (repetir en pantalla o en voz lo entendido) y mantener una **alternativa** (un pedal o la pantalla táctil). Con gestos, el problema serían la grasa en la cámara, la luz y tener que mostrar la mano limpia a la cámara.

**9.** ¿Qué es la realidad aumentada? Pon un ejemplo útil para una aplicación de mantenimiento de equipos. ¿Qué detecta el modelo de postura del cuerpo y para qué se puede usar?

**Respuesta.** *(UD4, apartado 5)* La realidad aumentada superpone información generada por el ordenador sobre la imagen real de la cámara, en el sitio correcto. Ejemplo: al enfocar un ordenador abierto, la aplicación marca cada componente con su nombre o señala qué cable desconectar primero. El modelo de postura localiza **33 puntos del cuerpo** (hombros, codos, caderas, rodillas…); sirve para contar repeticiones de un ejercicio, corregir posturas en rehabilitación, juegos o controlar una aplicación con movimientos amplios.

**10.** ¿En qué se diferencian una prueba unitaria, una de integración y una de regresión? Pon un ejemplo de cada una en el BugTracker. ¿Qué debe incluir el manual de usuario del BugTracker y para quién se escribe?

**Respuesta.** *(UD4, apartado 7)* **Unitaria:** una pieza sola (las pruebas del `Buscador` con pytest-qt). **De integración:** que las piezas funcionen juntas (añadir una incidencia desde la ventana, que se guarde en la base de datos y que el recuento por estado cambie). **De regresión:** volver a pasar las pruebas después de un cambio (pytest después de cambiar el orden de los parámetros del `Buscador`). El manual de usuario se escribe para quien **usa** la aplicación, no para quien la programa: qué hace, cómo se instala y se abre, cómo se hace cada tarea paso a paso (añadir, buscar, modificar, eliminar, usar los gestos), los atajos y qué hacer ante los problemas frecuentes (la cámara no se abre, poca luz).

