# DI · BugTracker: un problema de usabilidad y cómo arreglarlo

Es un ejercicio sobre la 1.ª parte del proyecto. La 2.ª parte empieza desde su propia plantilla, así que este rediseño no afecta a lo que viene después.

## El problema

Al lanzar el BugTracker se ve un formulario con Título, Tipo, Prioridad, Estado y Descripción. Al pulsar `Ctrl+N` se abre un diálogo con **los mismos campos**. Además, cada uno valida distinto: el límite de 100 caracteres del título solo se comprueba en el diálogo.

| | Formulario de la ventana principal | Diálogo «Nueva incidencia» |
|---|---|---|
| Cómo se usa | Siempre a la vista; botón **Añadir** | `Ctrl+N` o **Archivo → Nueva incidencia**; botón **Aceptar** |
| Dónde está | `bugtracker.ui` (Designer) | `dialogo.py` |
| Qué se ejecuta al guardar | `anadir_incidencia()` en `main.py` | `validar()` en `dialogo.py` |
| Qué comprueba | Que el título no esté vacío | Que no esté vacío **y** que no pase de 100 caracteres |

Cada botón ejecuta solo el método al que está conectado. Aunque los dos tengan un campo `txtTitulo`, son widgets distintos: `validar()` nunca mira el campo de la ventana principal.

## Por qué pasa

La aplicación se ha construido por capas. El formulario viene de la Práctica 6, la plantilla de partida. El diálogo se añadió en el Paso 3 para trabajar diálogos modales y validación. El resultado son dos formas de hacer lo mismo, con reglas distintas.

## Por qué es un problema de usabilidad

Es justo lo que se revisa en la evaluación heurística del Paso 1:

- **Consistencia:** la misma tarea debería hacerse siempre de la misma forma, en el mismo sitio.
- **Prevención de errores:** una regla que se cumple en un sitio y en otro no deja pasar datos incorrectos.

## La mejora: lista + diálogo

Es el diseño habitual en aplicaciones de gestión:

- La ventana principal muestra **solo la lista** de incidencias, con su menú y su barra de herramientas.
- Todo lo que se escribe pasa por **un único diálogo**: **Nueva** lo abre vacío y **Editar** lo abre relleno.
- Hay una sola validación para todo.

`DialogoIncidencia` ya está preparado para editar: si recibe `incidencia=...`, se abre con el título «Editar incidencia» y los campos rellenos.

## Ejercicio: rediseñar el BugTracker a lista + diálogo

1. **Designer.** Quita de la ventana principal el formulario (etiquetas y campos) y los botones Añadir, Modificar, Eliminar y Limpiar. Deja la tabla, el menú y la barra de herramientas. Guarda y regenera `ui_bugtracker.py`.
2. **`main.py`: limpiar.** Borra `anadir_incidencia()`, `modificar_incidencia()`, `limpiar_formulario()` y `guardar()`, sus conexiones, y las líneas de `cargar_seleccion()` y `actualizar_botones()` que usaban esos campos y botones. Quita también la acción **Guardar** del menú y de la barra: ya no hay formulario que guardar.
3. **`main.py`: editar.** Crea el método `editar_incidencia()`:
   - coge el ID con `id_seleccionado()` (si no hay selección, no hace nada);
   - lee la incidencia con `bd.obtener_incidencia(id)`;
   - abre `DialogoIncidencia(self, incidencia)` con `exec()`;
   - si se acepta, guarda con `bd.actualizar_incidencia(id, *dialogo.datos())`;
   - recarga la tabla y avisa en la barra de estado.
4. **Acceso a Editar.**
   - Conecta el doble clic en la tabla a `editar_incidencia()`.
   - En Designer, añade una acción **&Editar** con atajo `Ctrl+E`, en el menú Archivo y en la barra de herramientas.
   - Conéctala a `editar_incidencia()` y actívala solo cuando haya una fila seleccionada, como Eliminar.
5. **Prueba sin ratón.**
   - `Ctrl+N` con el título vacío y con uno de 101 caracteres: avisa y el diálogo no se cierra.
   - Selecciona una fila y pulsa `Ctrl+E`: el diálogo se abre relleno y guarda los cambios.
   - Eliminar pide confirmación.
6. **Explica el cambio.** En dos o tres líneas, al principio de `main.py` (en el comentario de arriba): qué principio de usabilidad resuelve y qué has quitado.
