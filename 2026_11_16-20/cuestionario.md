# C3 · Cuestionario · semana del 16 al 20 de noviembre

Preguntas sobre el proyecto «Mejora tu BugTracker» (3.ª parte) y sobre los apuntes. Puede que sufran modificaciones a lo largo de la semana. Responde poniendo el número de cada pregunta.

Responde con tus palabras y asegúrate de que lo entiendes: en las pruebas escritas tendrás que explicarlo sin ayuda de la IA. De la UD4, las preguntas son de conceptos y criterio, no de código.

Si en una pregunta aparece algo que no has visto, búscalo en «Dónde consultar», en el [README de `apuntes/`](apuntes/README.md).

---

## Cuestiones sobre el proyecto

**1.** En el paso 12, ¿qué hace la consulta `SELECT estado, COUNT(*) AS total FROM incidencias GROUP BY estado`? ¿Por qué va en `bd.py` y no en `main.py`? ¿Por qué se llama a `actualizar_resumen()` al final de `cargar_incidencias()`?

**2.** En el paso 13, ¿qué hace **Promote to…** en Qt Designer? ¿Por qué el `Buscador` se ve como un recuadro vacío en el diseño? ¿Por qué hubo que cambiar el orden de los parámetros de su `__init__`?

**3.** Después de cambiar el orden de los parámetros del `Buscador`, se ejecutó `python -m pytest -v`. ¿Qué tipo de prueba es esa y por qué hace falta?

**4.** En el paso 15, ¿por qué los gestos se activan con una acción marcable (`Ctrl+G`) y no están siempre encendidos? ¿Qué pasa con la cámara al cerrar la aplicación?

**5.** ¿Por qué el detector solo da un gesto por bueno cuando se repite varios fotogramas seguidos y no lo repite hasta que cambia? ¿Qué problema evita?

## Cuestiones sobre los apuntes

Estas preguntas se responden con los apuntes de esta semana, en `apuntes/`.

**6.** ¿Qué es un modelo de aprendizaje automático y qué significa la **confianza** de un resultado? ¿Qué ventaja tiene, para la privacidad, que el modelo funcione en el propio equipo y no en la nube?

**7.** ¿En qué se diferencia usar un modelo ya entrenado, como el reconocedor de gestos de MediaPipe, de entrenar uno propio con Teachable Machine? Pon un ejemplo en el que convenga cada uno.

**8.** Una aplicación de un taller de coches quiere que el mecánico, con las manos sucias, consulte el siguiente paso de una reparación. ¿Usarías voz o gestos? Razónalo con al menos tres criterios de diseño de una interfaz natural.

**9.** ¿Qué es la realidad aumentada? Pon un ejemplo útil para una aplicación de mantenimiento de equipos. ¿Qué detecta el modelo de postura del cuerpo y para qué se puede usar?

**10.** ¿En qué se diferencian una prueba unitaria, una de integración y una de regresión? Pon un ejemplo de cada una en el BugTracker. ¿Qué debe incluir el manual de usuario del BugTracker y para quién se escribe?
