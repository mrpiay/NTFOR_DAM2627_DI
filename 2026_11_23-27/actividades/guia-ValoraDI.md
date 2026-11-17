# App de escritorio - ValoraDI

## Introducción

En esta guía aprenderás a diseñar y desarrollar **ValoraDI**, una aplicación de escritorio para recoger valoraciones anónimas del módulo de DI (Desarrollo de Interfaces) y calcular con ellas una nota global.

Cada persona valora de 1 a 5 estrellas tres aspectos del módulo: el **docente**, los **materiales** y las **clases**. La aplicación guarda las valoraciones en una base de datos en el ordenador y muestra la media de cada aspecto y una **nota global ponderada**: cada aspecto cuenta según un peso, en porcentaje, que se puede cambiar.

El objetivo de esta guía no es únicamente conseguir que la aplicación funcione, sino también comprender cómo se construye una aplicación de escritorio y cómo se comunican sus diferentes partes. Para ello, se usa **Visual Studio Code** (VS Code), el editor donde se escribe y se ejecuta el código. Además, se usan **Python** y **PySide6** (Qt para Python) para crear la interfaz, **Qt Designer** para dibujar la ventana, **SQLite** para guardar los datos y **pytest** para comprobar automáticamente que cada parte hace lo que debe.

El desarrollo se divide en dos partes:

- **Parte 1. Diseño y funcionamiento:** qué hace la aplicación, cómo se guardan los datos y qué arquitectura sigue, antes de empezar a programar.
- **Parte 2. Implementación paso a paso:** se prepara el entorno, se crea el proyecto, se escribe y se prueba el código de cada archivo, se dibuja la ventana en Qt Designer y se comprueba que todo se puede usar también con el teclado.

No es necesario tener experiencia previa con VS Code ni con Qt. La guía explica desde la instalación de Python hasta la aplicación terminada, incluyendo comprobaciones y ejemplos para facilitar el seguimiento.

Al finalizar, tendrás una aplicación funcional y una visión general de cómo se integran la interfaz, la lógica de la aplicación y el almacenamiento de datos en un proyecto de escritorio.

## Índice

- [Parte 1 · Diseño](#parte-1--diseño)
  - [1. Qué hace la app](#1-qué-hace-la-app)
  - [2. Dónde se guardan los datos](#2-dónde-se-guardan-los-datos)
  - [3. Cómo se organiza el código](#3-cómo-se-organiza-el-código)
  - [4. Cómo se mueve la información](#4-cómo-se-mueve-la-información)
  - [5. Decisiones de diseño](#5-decisiones-de-diseño)
  - [6. Configuración de librerías y dependencias](#6-configuración-de-librerías-y-dependencias)
- [Parte 2 · Implementación](#parte-2--implementación)
  - [Paso 0 · Preparar Python y VS Code](#paso-0--preparar-python-y-vs-code)
  - [Paso 1 · Crear el proyecto](#paso-1--crear-el-proyecto)
  - [Paso 2 · El modelo](#paso-2--el-modelo)
  - [Paso 3 · El almacén con SQLite](#paso-3--el-almacén-con-sqlite)
  - [Paso 4 · El componente SelectorNota](#paso-4--el-componente-selectornota)
  - [Paso 5 · La ventana en Qt Designer](#paso-5--la-ventana-en-qt-designer)
  - [Paso 6 · El diálogo de pesos](#paso-6--el-diálogo-de-pesos)
  - [Paso 7 · El código de la ventana](#paso-7--el-código-de-la-ventana)
  - [Paso 8 · Arrancar la app](#paso-8--arrancar-la-app)
  - [Paso 9 · Probar la app](#paso-9--probar-la-app)
- [Si algo falla](#si-algo-falla)
- [Los archivos del proyecto](#los-archivos-del-proyecto)

---

# Parte 1 · Diseño

## 1. Qué hace la app

```
┌──────────────────────────────────────────────────────────┐
│ ValoraDI                                                 │
│ Valoración                                               │  ← menú: guardar, pesos y salir
│ ┌ Nueva valoración ────────────────────────────────────┐ │
│ │ Docente:      * * * * ·   4                          │ │  ← cinco estrellas por categoría
│ │ Materiales:   * * * · ·   3                          │ │
│ │ Clases:       * * * * *   5                          │ │
│ │                              [ Guardar valoración ]  │ │  ← solo con las tres notas
│ └──────────────────────────────────────────────────────┘ │
│ ┌ Resumen ─────────────────────────────────────────────┐ │
│ │ 13 valoraciones                         [ Pesos… ]   │ │  ← abre el diálogo de pesos
│ │ Docente          4.2          peso 40 %              │ │  ← media de cada categoría
│ │ Materiales       3.6          peso 30 %              │ │
│ │ Clases           3.9          peso 30 %              │ │
│ │ Nota global      3.9                                 │ │  ← media ponderada
│ └──────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

| N.º | Requisito |
|---|---|
| R1 | Al abrir, la app muestra el resumen de lo guardado. Si no hay nada, dice «Aún no hay valoraciones». |
| R2 | Cada categoría se valora de **1 a 5 estrellas**, con el ratón o con el teclado. «Guardar valoración» está desactivado hasta que las tres categorías tienen nota. |
| R3 | Al guardar, la valoración se guarda en la base de datos, el formulario se vacía para la siguiente persona y el resumen se actualiza. |
| R4 | El resumen muestra el **número de valoraciones**, la **media** de cada categoría con un decimal y su **peso**, y la **nota global ponderada**. |
| R5 | Los pesos se cambian en un **diálogo** aparte. Tienen que sumar 100 %: si no, «Aceptar» está desactivado y un aviso dice cuánto falta o sobra. Los pesos se guardan. |
| R6 | Al cambiar los pesos, la nota global se recalcula sola, sin volver a introducir ninguna valoración. |
| R7 | Todo se puede hacer **solo con el teclado**: Tab para moverse, Alt + letra para ir a cada categoría, las teclas 1 a 5 o las flechas para elegir la nota, Intro o Ctrl + S para guardar y Ctrl + P para los pesos. Cada control tiene un nombre que lee el lector de pantalla. |
| R8 | Las valoraciones son **anónimas**: solo se guardan las tres notas. |

## 2. Dónde se guardan los datos

Las valoraciones se escriben en la propia app y se guardan en una base de datos **SQLite**: un único archivo, `valora.db`, en la carpeta del proyecto. No hace falta ningún servidor ni conexión a Internet, y lo guardado sigue ahí al cerrar y volver a abrir la app.

```
Cada persona, en la ventana
        │  elige tres notas y pulsa «Guardar valoración»
        ▼
ValoraDI ──guarda──► valora.db (SQLite, en la carpeta del proyecto) ──lee──► resumen
```

**Las dos tablas.**

| Tabla | Qué guarda | Columnas |
|---|---|---|
| `valora` | Una fila por valoración | `id` (un número que pone SQLite, uno distinto para cada fila), `docente`, `materiales` y `clases` (notas de 1 a 5) |
| `pesos` | Una sola fila, con los pesos | `id` (siempre 1), `docente`, `materiales` y `clases` (en %) |

La tabla `valora` **no admite** notas fuera de 1 a 5: aunque un error en el código intentara guardar un 6, la base de datos lo rechazaría. Mientras nadie cambie los pesos, la tabla `pesos` está vacía y se usan los de por defecto: 40 % docente, 30 % materiales y 30 % clases.

**La nota global.** Es una **media ponderada**: la media de cada categoría se multiplica por su peso, se suman los tres resultados y se divide entre 100. Con las medias docente 4.0, materiales 3.0 y clases 5.0, y los pesos de por defecto:

```
(4.0 · 40  +  3.0 · 30  +  5.0 · 30) / 100  =  (160 + 90 + 150) / 100  =  4.0
```

Si los pesos fueran 100 %, 0 % y 0 %, la nota global sería solo la media de docente. Por eso los pesos tienen que sumar 100: si no, la nota global no estaría entre 1 y 5.

## 3. Cómo se organiza el código

### 3.1 · Las palabras que hay que conocer

La app se escribe en **Python**, un lenguaje de programación. El código se guarda en archivos con la extensión **`.py`** (de *Python*), igual que un texto acaba en `.txt` o una foto en `.jpg`. Cada archivo `.py` es un **módulo**: una pieza de la app que otras pueden usar con `import`.

Dentro de esos archivos hay, sobre todo, dos cosas:

- **Clases.** Una clase es un molde que describe un tipo de cosa y qué datos tiene. Por ejemplo, la clase `Valora` dice que una valoración tiene una nota de docente, otra de materiales y otra de clases. Con ese molde se crean tantas valoraciones como hagan falta; cada una es un **objeto**.
- **Funciones.** Una función es una acción con nombre. Se escribe con paréntesis: `guardar_valora(valora)` guarda una valoración; `media(valoras, "docente")` calcula la media de docente. Lo que va entre los paréntesis son los datos que necesita la acción. Una función que pertenece a una clase se llama **método**.

Estas son las piezas que usa la app:

| Palabra | Qué es | En esta app |
|---|---|---|
| **Librería** | Código ya hecho, escrito por otros, que se añade al proyecto para no tener que programarlo desde cero. | PySide6, pytest y pytest-qt |
| **Entorno virtual** | Una carpeta (`.venv`) con una copia de Python y las librerías de **este** proyecto. Así, las librerías de un proyecto no se mezclan con las de otro. | `.venv`, con las librerías de `requirements.txt` |
| **PySide6 (Qt)** | **Qt** es una librería para crear interfaces de escritorio: ventanas, botones, menús… **PySide6** permite usarla desde Python. | Toda la interfaz |
| **Widget** | Cada pieza de una ventana de Qt: una etiqueta (`QLabel`), un botón (`QPushButton`), un grupo con título (`QGroupBox`)… La propia ventana también es un widget. | Las etiquetas, los botones, los grupos |
| **Layout** | Una regla que coloca los widgets: uno debajo de otro, uno al lado de otro, en rejilla o en parejas «etiqueta y campo». Con layouts, la ventana se adapta al cambiar de tamaño. | Los dos grupos y su contenido |
| **Qt Designer** | Un programa para **dibujar** la ventana arrastrando widgets, sin escribir código. Guarda el diseño en un archivo **`.ui`**. | `ventana.ui` |
| **`pyside6-uic`** | Una herramienta que convierte el `.ui` en código Python. Ese código no se edita a mano: se vuelve a generar cada vez que cambia el diseño. | `ventana.ui` → `ui_ventana.py` |
| **Señal y slot** | Una **señal** es un aviso que lanza un widget cuando pasa algo (`clicked`: «me han pulsado»). Un **slot** es la función que se ejecuta al recibirlo. Se unen con `connect`. | `btnGuardar.clicked.connect(self.guardar)` |
| **Componente** | Un widget propio, hecho con otros widgets, que se usa como uno más y se puede reutilizar en otros proyectos. Tiene sus propias **propiedades** (datos) y **señales**. | `SelectorNota`: cinco estrellas, usado tres veces |
| **Diálogo** | Una ventana pequeña que pide algo y espera la respuesta antes de seguir (Aceptar o Cancelar). | El diálogo de pesos |
| **SQLite** | Una base de datos en un solo archivo, sin servidor. Python la trae incluida (`import sqlite3`). Los datos se piden y se guardan con **SQL**, el lenguaje de las bases de datos. | `valora.db` |
| **Prueba automática** | Un trozo de código que usa otro y comprueba que el resultado es el esperado. **pytest** las ejecuta todas y dice cuáles fallan; **pytest-qt** permite probar widgets simulando clics y teclas. | Los archivos `test_*.py` |
| **Accesibilidad** | Que la app la pueda usar todo el mundo: también quien no usa ratón o quien usa un **lector de pantalla**, un programa que lee en voz alta lo que hay en la pantalla. | El teclado (R7) y los nombres accesibles |

### 3.2 · Las capas

Una app pequeña se podría escribir en un solo archivo, pero sería difícil de leer, de probar y de cambiar. Por eso el código se reparte en **capas**, cada una con un solo trabajo:

- **Interfaz:** la ventana y el diálogo. Recogen lo que se pulsa y dibujan lo que reciben. No calculan nada ni saben cómo se guardan los datos.
- **Componente:** el selector de estrellas. Solo sabe elegir una nota y avisar de que ha cambiado; no sabe para qué se usa.
- **Modelo:** qué es una valoración y unos pesos, y **todos los cálculos**: las medias, la nota global, si los pesos son válidos y los textos del resumen. Es Python puro: no usa Qt ni SQL.
- **Almacén:** todo el SQL. Guarda y lee las valoraciones y los pesos en `valora.db`.

En resumen: **el modelo calcula, el almacén guarda y la interfaz dibuja**. Como el modelo y el almacén no usan ventanas, se pueden probar con pytest sin abrir ninguna.

**Cómo se lee el esquema.** Cada caja es una capa, con sus archivos y lo que hace cada uno; a la derecha, el paso de la Parte 2 en el que se escribe. Las flechas dicen quién pide qué a quién. Por ejemplo, «guardar_valora(v)» quiere decir que la ventana le pide al almacén que guarde una valoración.

El esquema se lee de arriba abajo, desde lo que se ve hasta los datos. La app se construye al revés, de abajo arriba: del paso 2 al 8.

```
┌──────────────────────────────────────────────────────────────┐
│ INTERFAZ                                      pasos 5 a 8    │
│   ventana.ui → ui_ventana.py   el dibujo (Qt Designer)       │
│   ventana.py                   recoge lo pulsado y dibuja    │
│   dialogo_pesos.py             pide los pesos                │
│   main.py                      abre la ventana               │
└───────┬───────▲────────────────┬─────────────────┬───────────┘
        │ usa   │ notaCambiada   │ resumir()       │ guarda y lee
        │ ×3    │                │ → Resumen       │
┌───────▼───────┴────┐  ┌────────▼────────┐  ┌─────▼───────────┐
│ COMPONENTE  paso 4 │  │ MODELO   paso 2 │  │ ALMACÉN  paso 3 │
│ selector_nota.py   │  │ modelo.py       │  │ almacen.py      │
│ cinco estrellas    │  │ los cálculos    │  │ SQL y valora.db │
└────────────────────┘  └────────▲────────┘  └────────┬────────┘
                                 │ Valora, Pesos      │
                                 └────────────────────┘
```

| Paso | Capa | Archivo | Qué contiene |
|---|---|---|---|
| 2 | Modelo | `modelo.py` | Las clases `Valora` y `Pesos`, el resumen ya calculado y todos los cálculos |
| 3 | Almacén | `almacen.py` | Las tablas de SQLite y las funciones para guardar y leer |
| 4 | Componente | `selector_nota.py` | `SelectorNota`: cinco estrellas, con su propiedad `nota` y su señal `notaCambiada` |
| 5 | Interfaz | `ventana.ui` → `ui_ventana.py` | El dibujo de la ventana, hecho en Qt Designer, y el código que genera `pyside6-uic` |
| 6 | Interfaz | `dialogo_pesos.py` | El diálogo de pesos |
| 7 | Interfaz | `ventana.py` | La ventana: conecta las señales, guarda, abre el diálogo y dibuja el resumen |
| 8 | Arranque | `main.py` | Crea las tablas, la aplicación y la ventana |
| 2 a 7 | Pruebas | `test_*.py` | Las pruebas automáticas de cada parte |

## 4. Cómo se mueve la información

Esto es lo que pasa por dentro en cada situación, siguiendo el esquema del punto 3. Entre paréntesis va el nombre que tiene en el código.

**Al abrir la app (R1)**

1. `main.py` pide al almacén que cree las tablas, si aún no existen (`crear_bd`), y abre la ventana (`VentanaPrincipal`).
2. La ventana se dibuja a partir del diseño de Qt Designer (`setupUi`) y conecta cada señal con su slot: qué pasa al cambiar una nota, al pulsar «Guardar», al pulsar «Pesos…».
3. Pide al almacén los pesos guardados (`leer_pesos`) y todas las valoraciones (`leer_valoras`).
4. Pasa las dos cosas al modelo, que calcula el resumen entero (`resumir`): el número de valoraciones, las medias, los pesos, la nota global y sus textos.
5. La ventana escribe esos textos en sus etiquetas. Si no hay valoraciones, «Aún no hay valoraciones» y rayas en lugar de números.

**Al elegir una nota (R2)**

1. Con un clic en una estrella, o con una tecla de 1 a 5, el selector cambia su nota, se redibuja y lanza su señal (`notaCambiada`).
2. La ventana la recibe (`actualizar_guardar`) y comprueba si las tres categorías tienen nota. Solo entonces activa «Guardar valoración» y su opción del menú.

**Al guardar (R3, R4)**

1. Con «Guardar valoración», Intro o Ctrl + S, la ventana crea una `Valora` con las tres notas y pide al almacén que la guarde (`guardar_valora`).
2. Vacía los tres selectores (`limpiar`), lleva el foco a la primera categoría y muestra «Valoración guardada» abajo, en la barra de estado.
3. Vuelve a pedir el resumen, como al abrir, y lo dibuja: ahora cuenta una valoración más.

**Al cambiar los pesos (R5, R6)**

1. Con «Pesos…» o Ctrl + P, la ventana abre el diálogo con los pesos actuales y espera.
2. Cada vez que cambia un peso, el diálogo pregunta al modelo si son válidos y qué aviso mostrar (`Pesos.validos` y `Pesos.aviso`). Si no suman 100, desactiva «Aceptar».
3. Con «Aceptar», la ventana pide al almacén que guarde los pesos nuevos (`guardar_pesos`) y vuelve a dibujar el resumen: la nota global cambia; las valoraciones, no. Con «Cancelar», no cambia nada.

**Si algo falla al leer o guardar:** el almacén lanza un error de SQLite (`sqlite3.Error`). La ventana lo recoge (`except`) y muestra un mensaje que explica qué no se ha podido hacer; la app no se cierra sin avisar.

## 5. Decisiones de diseño

| Decisión | Por qué |
|---|---|
| Guardar en **SQLite** | Lo guardado sigue ahí al cerrar la app, en un solo archivo y sin instalar ningún servidor. Python lo trae incluido. |
| El modelo **calcula**, el almacén **guarda** y la interfaz **dibuja** | Cada parte se entiende y se cambia por separado. El modelo y el almacén se prueban con pytest sin abrir ventanas. |
| El resumen llega **ya calculado y escrito** (`Resumen`, `texto_media`, `texto_global`) | La ventana no hace ninguna cuenta: solo copia textos en etiquetas. Si cambia el cálculo, la ventana no se toca. |
| La media y la nota global **se calculan**, no se guardan | Se obtienen de las valoraciones en cada momento: no pueden quedar desactualizadas, y al cambiar los pesos se recalculan solas (R6). |
| Escala de **1 a 5** estrellas | Con estrellas, «0 estrellas» se confundiría con «aún no se ha elegido». El 0 significa «sin nota», y así «Guardar» puede esperar a las tres notas (R2). |
| Las notas se comprueban **también en la base de datos** (`CHECK`) | Si un error en el código intentara guardar un 6, SQLite lo rechazaría. |
| Los pesos se validan en el **modelo**, no en el diálogo | El diálogo solo muestra lo que dice el modelo (`validos`, `aviso`); la misma regla se prueba con pytest. |
| El selector es un **componente** propio | Se escribe una vez y se usa tres veces; tiene sus propias pruebas y se puede llevar a otro proyecto. |
| La ventana se **dibuja en Qt Designer** | El diseño se ve mientras se hace y se cambia sin tocar el código. El selector se coloca en el diseño **promocionando** un widget. |
| **Teclado** y **nombres accesibles** en todo | Quien no usa ratón o usa lector de pantalla puede valorar igual (R7). |
| Valoraciones **anónimas** | Solo tres notas (R8): nada en los datos dice quién valoró. |

## 6. Configuración de librerías y dependencias

Antes de programar, cada requisito del punto 1 se convierte en lo que necesita el proyecto. Quien empieza una app sabe **qué quiere ver y qué quiere que pase**, pero no qué librerías hacen falta. Esto se averigua siempre de la misma forma.

### 6.1 · El método, en cuatro preguntas

Para cada cosa que tiene que hacer la app:

1. **¿Qué necesita, en palabras técnicas?** «Que se vean ventanas con botones» es *una librería de interfaces gráficas*; «que no se pierdan las valoraciones al cerrar» es *una base de datos*; «comprobar que el cálculo está bien» es *pruebas automáticas*.
2. **¿Lo trae ya Python, o hace falta una librería?** Python trae de serie su **biblioteca estándar**: `sqlite3`, `dataclasses`, `pathlib`… Su lista está en la [documentación de Python](https://docs.python.org/es/3/library/index.html). Lo que no está ahí se busca en **PyPI** ([pypi.org](https://pypi.org)), el catálogo de librerías de Python.
3. **¿Qué pide esa librería?** Cada una tiene en su página de PyPI y en su documentación un apartado de instalación (*Installation*), con el nombre exacto que se instala y la última versión.
4. **¿Dónde se apunta?** En Python, todas las librerías del proyecto se apuntan en un solo archivo, `requirements.txt`, una por línea. `pip install -r requirements.txt` las instala todas en el entorno virtual.

### 6.2 · Las preguntas aplicadas a esta app

| Lo que se quiere (requisito) | Qué necesita | Con qué se hace | ¿Lo trae Python? | Dónde se mira qué añadir |
|---|---|---|---|---|
| Ver la ventana, los botones y el diálogo (R1 a R7) | Una librería de interfaces gráficas | PySide6 (Qt para Python) | No | [PySide6 en PyPI](https://pypi.org/project/PySide6-Essentials/) y [Qt for Python](https://doc.qt.io/qtforpython-6/) |
| Dibujar la ventana sin escribir su código | Un diseñador visual | Qt Designer y `pyside6-uic` | No: **llegan con PySide6** | — |
| Guardar las valoraciones y los pesos (R1, R3, R5) | Una base de datos | SQLite (`sqlite3`) | **Sí** | [sqlite3](https://docs.python.org/es/3/library/sqlite3.html) |
| Clases de datos sencillas (`Valora`, `Pesos`) | Clases que solo guardan datos | `dataclasses` | **Sí** | [dataclasses](https://docs.python.org/es/3/library/dataclasses.html) |
| Saber dónde está `valora.db` | Rutas de archivos | `pathlib` | **Sí** | [pathlib](https://docs.python.org/es/3/library/pathlib.html) |
| Comprobar el cálculo y el almacén | Pruebas automáticas | pytest | No | [pytest en PyPI](https://pypi.org/project/pytest/) |
| Comprobar el selector y la ventana con clics y teclas | Pruebas de widgets de Qt | pytest-qt | No | [pytest-qt en PyPI](https://pypi.org/project/pytest-qt/) |

Con esta tabla hecha, ya se sabe qué hay que poner en `requirements.txt` (paso 1), y por qué: tres líneas.

### 6.3 · Qué se escribe en `requirements.txt`

| Línea | Qué instala |
|---|---|
| `PySide6-Essentials==6.12.*` | Los módulos principales de Qt (ventanas, widgets, SQL de Qt…), Qt Designer y `pyside6-uic`. `PySide6-Essentials` es la parte básica de PySide6: ocupa mucho menos que el paquete completo, `PySide6`, que añade módulos que esta app no usa (gráficos 3D, multimedia, web…). |
| `pytest` | El programa que ejecuta las pruebas |
| `pytest-qt` | Un añadido (*plugin*) de pytest para probar widgets: da la herramienta `qtbot`, que simula clics y teclas |

### 6.4 · Qué versión poner

- **Sin versión** (`pytest`), pip instala la última. Es lo normal en librerías que cambian poco por dentro, como las de pruebas.
- **Con versión exacta** (`==6.12.0`), se instala esa y ninguna otra: el proyecto funciona igual en todos los ordenadores, pero no recibe correcciones.
- **Con asterisco** (`==6.12.*`), se instala la última de la serie 6.12: recibe las correcciones (6.12.1, 6.12.2…), pero no los cambios grandes de la 6.13. Es lo que se usa con PySide6, porque esta guía está probada con la 6.12.
- **Comprobar qué se ha instalado:** `pip list` muestra todas las librerías del entorno y su versión.
- **Si falta algo, el error lo dice:**

| Error | Lo que falta |
|---|---|
| `ModuleNotFoundError: No module named 'PySide6'` | La librería no está instalada **en el entorno activo**: activa el entorno (`.venv\Scripts\Activate.ps1`) y repite `pip install -r requirements.txt` |
| `fixture 'qtbot' not found` | pytest-qt no está instalado en el entorno |
| `pyside6-uic` o `pyside6-designer` no se reconocen | El entorno no está activado, o PySide6 no se ha instalado en él |

---

# Parte 2 · Implementación

Cada paso dice **qué se hace**, trae el **código completo** del archivo y termina con **Comprueba que…**: no pases al siguiente hasta que se cumpla.

## Paso 0 · Preparar Python y VS Code

### 0.1 · Instalar Python y VS Code

Esta guía está probada con **Python 3.12**, **PySide6 6.12** y **VS Code**, en Windows 11. En otras versiones, algunos menús pueden tener otro nombre o estar en otro sitio.

Si ya los tienes instalados, pasa al 0.2.

1. **Python:** en [python.org/downloads](https://www.python.org/downloads/), el instalador de Windows de 64 bits de la versión 3.12. En la primera pantalla del instalador, marca **Add python.exe to PATH** antes de pulsar *Install Now*. Sin esa casilla, la terminal no encuentra Python.
2. **VS Code:** en [code.visualstudio.com](https://code.visualstudio.com), el instalador de Windows. Deja todas las opciones como vienen.
3. Abre VS Code. A la izquierda, en *Extensiones* (`Ctrl + Mayús + X`), busca **Python** e instala la de Microsoft.

### 0.2 · Las partes de la ventana de VS Code

| Zona | Dónde | Para qué |
|---|---|---|
| **Explorador** | Panel de la izquierda (`Ctrl + Mayús + E`) | Los archivos de la carpeta abierta. Un clic abre un archivo |
| **Editor** | En el centro | Donde se escribe el código. Cada archivo abierto es una pestaña |
| **Terminal** | Abajo: *Terminal > New Terminal* (`Ctrl + ñ` con teclado español) | Una línea de comandos de **PowerShell** en la carpeta del proyecto. Ahí se instalan las librerías, se ejecuta la app y se pasan las pruebas |
| **Barra de estado** | La línea de abajo del todo | A la derecha, la versión de Python que usa el proyecto |

### 0.3 · Si trabajas en Linux

Los comandos de esta guía son para **PowerShell**, la terminal de Windows que abre VS Code. En Linux (por ejemplo, Ubuntu), la terminal es **bash** y cambian estos:

| Para | En Windows (PowerShell) | En Linux (bash) |
|---|---|---|
| Instalar Python | El instalador de python.org (0.1) | Ya viene instalado. Falta el módulo de entornos virtuales: `sudo apt install python3-venv` |
| La carpeta del proyecto | `C:\dam2627\di\ValoraDI` | `~/dam2627/di/ValoraDI` |
| Comprobar Python | `python --version` | `python3 --version` |
| Crear el entorno virtual (paso 1) | `python -m venv .venv` | `python3 -m venv .venv` |
| Activarlo (paso 1 y cada terminal nueva) | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Abrir Qt Designer (paso 5.1) | `Start-Process .venv\Scripts\pyside6-designer.exe -WindowStyle Hidden` | `pyside6-designer &` (el `&` deja la terminal libre) |

Con el entorno activado, **todo lo demás es igual** en los dos sistemas: `python`, `pip install -r requirements.txt`, `pyside6-uic`, `python -m pytest -v` y `python main.py`.

**Comprueba que…** en la terminal de VS Code, `python --version` muestra `Python 3.12` y algo más (por ejemplo, `Python 3.12.10`). En Linux, `python3 --version`.

## Paso 1 · Crear el proyecto

1. Crea la carpeta **`C:\dam2627\di\ValoraDI`** con el Explorador de Windows. Usa una ruta corta y fuera de OneDrive: en rutas largas, la instalación de PySide6 falla.
2. En VS Code: *File > Open Folder…*, elige `ValoraDI` y pulsa **Seleccionar carpeta**. Si pregunta si confías en los autores, **Yes, I trust the authors**.
3. Crea el archivo **`requirements.txt`** (ver «Cómo se crea un archivo», más abajo) con las librerías del punto 6:

   ```text
   PySide6-Essentials==6.12.*
   pytest
   pytest-qt
   ```

4. Abre la terminal (*Terminal > New Terminal*) y escribe, una línea cada vez:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

   | Comando | Qué hace |
   |---|---|
   | `python -m venv .venv` | Crea el entorno virtual en la carpeta `.venv` |
   | `.venv\Scripts\Activate.ps1` | **Activa** el entorno: desde ahora, `python` y `pip` son los de `.venv`. Al principio de la línea de la terminal aparece `(.venv)` |
   | `pip install -r requirements.txt` | Instala en el entorno las librerías de `requirements.txt`. La primera vez tarda unos minutos |

   Cada vez que abras una terminal nueva, el entorno tiene que estar activado: si no ves `(.venv)`, vuelve a escribir `.venv\Scripts\Activate.ps1`.

5. **Elige el intérprete** en VS Code, para que reconozca las librerías del entorno: `Ctrl + Mayús + P` → escribe «Python: Select Interpreter» → elige el que tiene `.venv` en su ruta.

**Comprueba que…** la línea de la terminal empieza por `(.venv)` y `pip list` muestra `PySide6-Essentials`, `pytest` y `pytest-qt`.

**El árbol de archivos.** Así queda la carpeta al terminar la guía, en el Explorador de VS Code. Lo marcado como **NUEVO** lo creas tú en el paso que se indica. VS Code ordena los archivos por orden alfabético, no por el orden de los pasos.

```
VALORADI
├── .venv                   el entorno virtual (paso 1) · no se toca
├── almacen.py              NUEVO · paso 3
├── dialogo_pesos.py        NUEVO · paso 6
├── main.py                 NUEVO · paso 8
├── modelo.py               NUEVO · paso 2
├── requirements.txt        NUEVO · paso 1
├── selector_nota.py        NUEVO · paso 4
├── test_almacen.py         NUEVO · paso 3
├── test_modelo.py          NUEVO · paso 2
├── test_selector_nota.py   NUEVO · paso 4
├── test_ventana.py         NUEVO · paso 7
├── ui_ventana.py           lo genera pyside6-uic (paso 5) · no se edita
├── valora.db               lo crea la app al abrirla (paso 8)
├── ventana.py              NUEVO · paso 7
└── ventana.ui              NUEVO · paso 5, en Qt Designer
```

**Cómo se crea un archivo** (pasos 1 a 8): en el Explorador de VS Code, pasa el ratón por encima del nombre de la carpeta, `VALORADI`, y pulsa el icono **New File** (una hoja con un `+`). Escribe el nombre **con** su extensión (por ejemplo, `modelo.py`) y pulsa **Intro**. Se abre vacío a la derecha: pega el código de la guía y guarda con **Ctrl + S**.

## Paso 2 · El modelo

Es la capa **Modelo** del esquema del punto 3: qué es una valoración, qué son los pesos y todos los cálculos. No usa Qt ni SQL, solo Python, así que se puede probar sin abrir ninguna ventana.

Crea el archivo **`modelo.py`**:

**Las piezas del código:**

| Pieza | Qué hace |
|---|---|
| `"""…"""` al principio | El **docstring**: un texto que explica qué es el módulo, la clase o la función. No se ejecuta; lo muestran VS Code y `help()` |
| `from dataclasses import dataclass` | Trae `dataclass` de la biblioteca estándar de Python |
| `@dataclass(frozen=True)` | Lo que empieza por **`@`** es un **decorador**: modifica lo que va debajo. `@dataclass` convierte la clase en una **clase de datos**: Python le escribe solo el método que la crea (`Valora(4, 3, 5)`), el que la compara (`==`) y el que la muestra como texto. `frozen=True` impide cambiarla después de crearla |
| `docente: int` | Un **atributo** de la clase con su **tipo**: un número entero |
| `docente: int = 40` | Un atributo con **valor por defecto**: `Pesos()` crea los pesos 40, 30 y 30 |
| `def nota(self, categoria):` | Un **método**: una función de la clase. `self` es el propio objeto: `valora.nota("docente")` |
| `getattr(self, categoria)` | Lee el atributo cuyo nombre está en el texto `categoria`: `getattr(valora, "docente")` es lo mismo que `valora.docente` |
| `@property` | Convierte un método en algo que se lee como un atributo, **sin paréntesis**: `pesos.suma`, `pesos.validos`. Se calcula cada vez que se lee |
| `f"Faltan {100 - self.suma} puntos…"` | Una **cadena f**: lo que va entre llaves se calcula y se escribe dentro del texto |
| `f"{numero:.1f}"` | Escribe un número con un decimal y con punto: `3.8` |
| `float \| None` | El tipo «número decimal o nada». `None` es el valor de Python para «no hay» |
| `sum(v.nota(c) for v in valoras)` | Suma la nota de la categoría `c` de cada valoración de la lista |
| `[FilaResumen(…) for c in CATEGORIAS]` | Una **lista por comprensión**: crea una fila del resumen por cada categoría |

```python
"""El modelo de ValoraDI: los datos y todos los cálculos.

Este módulo no usa Qt ni SQL: solo Python. Por eso se puede probar con pytest
sin abrir ninguna ventana. La ventana le pide el resumen ya calculado y lo dibuja.
"""
from dataclasses import dataclass

# ── Las categorías ───────────────────────────────────────────────────────
# El nombre interno (el de las columnas de la base de datos) y el que se ve
CATEGORIAS = ("docente", "materiales", "clases")
NOMBRES = {"docente": "Docente", "materiales": "Materiales", "clases": "Clases"}

NOTA_MINIMA = 1
NOTA_MAXIMA = 5


# ── Una valoración: una nota de 1 a 5 para cada categoría ────────────────
@dataclass(frozen=True)
class Valora:
    docente: int
    materiales: int
    clases: int

    def nota(self, categoria):
        """La nota de una categoría: valora.nota("docente")."""
        return getattr(self, categoria)


# ── Los pesos: cuánto cuenta cada categoría en la nota global, en % ──────
@dataclass(frozen=True)
class Pesos:
    docente: int = 40
    materiales: int = 30
    clases: int = 30

    def peso(self, categoria):
        return getattr(self, categoria)

    @property
    def suma(self):
        return self.docente + self.materiales + self.clases

    @property
    def validos(self):
        """Los pesos solo son válidos si suman exactamente 100."""
        return self.suma == 100

    @property
    def aviso(self):
        """El mensaje para quien los está cambiando: cuánto falta o sobra."""
        if self.suma < 100:
            return f"Faltan {100 - self.suma} puntos para llegar a 100 %"
        if self.suma > 100:
            return f"Sobran {self.suma - 100} puntos: la suma pasa de 100 %"
        return ""


# ── El resumen, ya calculado: la ventana solo lo dibuja ──────────────────
@dataclass(frozen=True)
class FilaResumen:
    nombre: str          # "Docente"
    media: float | None  # la media de esa categoría; None si no hay valoraciones
    peso: int            # su peso, en %

    @property
    def texto_media(self):
        return formatear(self.media)


@dataclass(frozen=True)
class Resumen:
    total: int                  # cuántas valoraciones hay
    filas: list                 # una FilaResumen por categoría
    nota_global: float | None   # la media ponderada; None si no hay valoraciones

    @property
    def texto_total(self):
        if self.total == 0:
            return "Aún no hay valoraciones"
        if self.total == 1:
            return "1 valoración"
        return f"{self.total} valoraciones"

    @property
    def texto_global(self):
        return formatear(self.nota_global)


# ── Los cálculos ─────────────────────────────────────────────────────────
def formatear(numero):
    """Un número con un decimal y punto decimal (3.8). Sin número, una raya."""
    return "–" if numero is None else f"{numero:.1f}"


def media(valoras, categoria):
    """La media de una categoría. None si no hay valoraciones."""
    if not valoras:
        return None
    return sum(v.nota(categoria) for v in valoras) / len(valoras)


def nota_global(valoras, pesos):
    """La media ponderada: cada media por su peso, y la suma entre 100.

    Con docente 4.0 (40 %), materiales 3.0 (30 %) y clases 5.0 (30 %):
    (4.0 · 40 + 3.0 · 30 + 5.0 · 30) / 100 = 4.0
    """
    if not valoras:
        return None
    return sum(media(valoras, c) * pesos.peso(c) for c in CATEGORIAS) / 100


def resumir(valoras, pesos):
    """Todo lo que muestra el resumen, en un solo objeto."""
    filas = [FilaResumen(NOMBRES[c], media(valoras, c), pesos.peso(c)) for c in CATEGORIAS]
    return Resumen(total=len(valoras), filas=filas, nota_global=nota_global(valoras, pesos))
```

Crea también el archivo **`test_modelo.py`**, con las pruebas del modelo. Cada función que empieza por `test_` es una prueba; `assert` comprueba que algo es cierto y, si no lo es, la prueba falla:

```python
"""Pruebas del modelo: los cálculos, sin ventanas ni base de datos.

Ejecuta desde la carpeta del proyecto:  python -m pytest -v
"""
import pytest

from modelo import Pesos, Valora, formatear, media, nota_global, resumir

# Tres valoraciones de ejemplo
VALORAS = [Valora(4, 3, 5), Valora(5, 2, 4), Valora(3, 4, 3)]


def test_media_de_una_categoria():
    assert media(VALORAS, "docente") == 4.0          # (4 + 5 + 3) / 3
    assert media(VALORAS, "materiales") == 3.0       # (3 + 2 + 4) / 3


def test_sin_valoraciones_no_hay_media_ni_nota_global():
    assert media([], "docente") is None
    assert nota_global([], Pesos()) is None


def test_nota_global_ponderada():
    # docente 4.0 · 40 + materiales 3.0 · 30 + clases 4.0 · 30 = 370 → 3.7
    assert nota_global(VALORAS, Pesos(40, 30, 30)) == pytest.approx(3.7)


def test_cambiar_los_pesos_cambia_la_nota_global():
    # Solo cuenta docente: la nota global es la media de docente
    assert nota_global(VALORAS, Pesos(100, 0, 0)) == pytest.approx(4.0)


def test_pesos_validos_y_aviso():
    assert Pesos(40, 30, 30).validos
    assert Pesos(40, 30, 30).aviso == ""
    assert not Pesos(40, 30, 20).validos
    assert Pesos(40, 30, 20).aviso == "Faltan 10 puntos para llegar a 100 %"
    assert Pesos(50, 30, 30).aviso == "Sobran 10 puntos: la suma pasa de 100 %"


def test_resumen_y_textos():
    resumen = resumir(VALORAS, Pesos())
    assert resumen.texto_total == "3 valoraciones"
    assert [f.texto_media for f in resumen.filas] == ["4.0", "3.0", "4.0"]
    assert resumen.texto_global == "3.7"
    assert resumir([Valora(5, 5, 5)], Pesos()).texto_total == "1 valoración"
    assert resumir([], Pesos()).texto_total == "Aún no hay valoraciones"
    assert formatear(None) == "–"
```

En la terminal, con el entorno activado:

```powershell
python -m pytest -v
```

**Comprueba que…** sale **6 passed** (seis pruebas superadas), en verde. Si alguna sale `FAILED`, pytest dice qué línea y qué valor no coinciden.

**Comprueba que lo entiendes.** Contesta antes de abrir las respuestas:

1. Con las valoraciones `Valora(5, 4, 3)` y `Valora(3, 4, 5)`, y los pesos de por defecto, ¿cuánto valen las tres medias y la nota global?
2. ¿Qué devuelve `Pesos(50, 30, 30).aviso`? ¿Y `Pesos(50, 30, 30).validos`?
3. ¿Por qué `texto_global` está en el modelo y no en la ventana?

<details>
<summary>Respuestas</summary>

1. Medias: docente 4.0, materiales 4.0 y clases 4.0. Nota global: (4.0 · 40 + 4.0 · 30 + 4.0 · 30) / 100 = 4.0.
2. `"Sobran 10 puntos: la suma pasa de 100 %"`, porque suman 110; y `False`.
3. Porque escribir la nota con un decimal, o una raya si no hay, también es una decisión del cálculo. Así la ventana solo copia el texto, y la regla se prueba con pytest.

</details>

## Paso 3 · El almacén con SQLite

Es la capa **Almacén**: todo el SQL de la app está aquí. Crea las dos tablas del punto 2, guarda y lee. No usa Qt: si algo falla, lanza el error y es la ventana quien avisa.

Crea el archivo **`almacen.py`**:

**Las piezas del código:**

| Pieza | Qué hace |
|---|---|
| `Path(__file__).with_name("valora.db")` | La ruta de `valora.db`, en la misma carpeta que `almacen.py`. `__file__` es la ruta del propio archivo. Así la base de datos está siempre en el mismo sitio, se ejecute la app desde donde se ejecute |
| `sqlite3.connect(RUTA_BD)` | Abre la base de datos. Si el archivo no existe, lo crea vacío |
| `row_factory = sqlite3.Row` | Permite leer cada columna por su nombre: `fila["docente"]` |
| `CREATE TABLE IF NOT EXISTS` | Crea la tabla solo si aún no existe: la primera vez que se abre la app |
| `INTEGER PRIMARY KEY AUTOINCREMENT` | La **clave primaria**: un número distinto para cada fila, que pone SQLite solo |
| `CHECK (docente BETWEEN 1 AND 5)` | Una **restricción**: SQLite rechaza cualquier nota fuera de 1 a 5 |
| `CHECK (id = 1)` | En `pesos`, solo puede haber una fila: la de `id` 1 |
| `try:` … `finally: conexion.close()` | Lo que va en `finally` se ejecuta siempre, haya ido bien o mal: la conexión se cierra pase lo que pase |
| `"INSERT INTO valora (…) VALUES (?, ?, ?)"` y la tupla de valores | Cada `?` se sustituye por un valor, en orden. Los valores **nunca se pegan** al texto del SQL: así ningún dato puede cambiar la consulta |
| `conexion.commit()` | **Guarda** los cambios. Sin `commit()`, lo que hacen `INSERT` y `CREATE` se pierde al cerrar |
| `fetchall()` y `fetchone()` | Devuelven todas las filas del resultado, o solo la primera (`None` si no hay ninguna) |
| `INSERT OR REPLACE` | Inserta la fila o, si ya hay una con la misma clave (`id` 1), la sustituye |

```python
"""El almacén de ValoraDI: guarda y lee las valoraciones y los pesos con SQLite.

Aquí está todo el SQL. Este módulo no usa Qt: si algo falla, lanza sqlite3.Error
y es la ventana quien muestra el mensaje.
"""
import sqlite3
from pathlib import Path

from modelo import Pesos, Valora

# La base de datos se guarda junto a este archivo, se ejecute desde donde se ejecute
RUTA_BD = Path(__file__).with_name("valora.db")


def conectar():
    conexion = sqlite3.connect(RUTA_BD)
    conexion.row_factory = sqlite3.Row   # acceso por nombre: fila["docente"]
    return conexion


# ── Crear las tablas (solo la primera vez) ───────────────────────────────
def crear_bd():
    conexion = conectar()
    try:
        # Una fila por valoración. CHECK: la base de datos no acepta notas fuera de 1 a 5
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS valora (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                docente    INTEGER NOT NULL CHECK (docente BETWEEN 1 AND 5),
                materiales INTEGER NOT NULL CHECK (materiales BETWEEN 1 AND 5),
                clases     INTEGER NOT NULL CHECK (clases BETWEEN 1 AND 5)
            )
        """)
        # Una sola fila (id = 1) con los pesos de la nota global
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS pesos (
                id         INTEGER PRIMARY KEY CHECK (id = 1),
                docente    INTEGER NOT NULL,
                materiales INTEGER NOT NULL,
                clases     INTEGER NOT NULL
            )
        """)
        conexion.commit()
    finally:
        conexion.close()


# ── Las valoraciones ─────────────────────────────────────────────────────
def guardar_valora(valora):
    conexion = conectar()
    try:
        # Los ? se sustituyen por los valores, en orden: nunca se pegan al texto del SQL
        conexion.execute(
            "INSERT INTO valora (docente, materiales, clases) VALUES (?, ?, ?)",
            (valora.docente, valora.materiales, valora.clases),
        )
        conexion.commit()
    finally:
        conexion.close()


def leer_valoras():
    conexion = conectar()
    try:
        filas = conexion.execute("SELECT docente, materiales, clases FROM valora ORDER BY id").fetchall()
        return [Valora(f["docente"], f["materiales"], f["clases"]) for f in filas]
    finally:
        conexion.close()


# ── Los pesos ────────────────────────────────────────────────────────────
def leer_pesos():
    """Los pesos guardados o, si aún no se han cambiado nunca, los de por defecto."""
    conexion = conectar()
    try:
        fila = conexion.execute("SELECT docente, materiales, clases FROM pesos WHERE id = 1").fetchone()
        return Pesos() if fila is None else Pesos(fila["docente"], fila["materiales"], fila["clases"])
    finally:
        conexion.close()


def guardar_pesos(pesos):
    conexion = conectar()
    try:
        # INSERT OR REPLACE: si ya hay una fila con id = 1, la sustituye
        conexion.execute(
            "INSERT OR REPLACE INTO pesos (id, docente, materiales, clases) VALUES (1, ?, ?, ?)",
            (pesos.docente, pesos.materiales, pesos.clases),
        )
        conexion.commit()
    finally:
        conexion.close()
```

Crea también **`test_almacen.py`**. Sus pruebas usan una base de datos **temporal**, en otra carpeta, para no tocar `valora.db`:

```python
"""Pruebas del almacén: guardar y leer con SQLite, en una base de datos de prueba.

Ejecuta desde la carpeta del proyecto:  python -m pytest -v
"""
import sqlite3

import pytest

import almacen
from modelo import Pesos, Valora


@pytest.fixture(autouse=True)
def bd_de_prueba(tmp_path, monkeypatch):
    # Cada prueba usa una base de datos nueva en una carpeta temporal: valora.db no se toca
    monkeypatch.setattr(almacen, "RUTA_BD", tmp_path / "prueba.db")
    almacen.crear_bd()


def test_guardar_y_leer_valoraciones():
    almacen.guardar_valora(Valora(4, 3, 5))
    almacen.guardar_valora(Valora(5, 2, 4))
    assert almacen.leer_valoras() == [Valora(4, 3, 5), Valora(5, 2, 4)]


def test_la_base_de_datos_no_acepta_notas_fuera_de_1_a_5():
    with pytest.raises(sqlite3.IntegrityError):
        almacen.guardar_valora(Valora(6, 3, 5))


def test_pesos_por_defecto_y_guardados():
    assert almacen.leer_pesos() == Pesos(40, 30, 30)
    almacen.guardar_pesos(Pesos(50, 25, 25))
    almacen.guardar_pesos(Pesos(60, 20, 20))        # sustituye, no añade otra fila
    assert almacen.leer_pesos() == Pesos(60, 20, 20)
```

| Pieza de las pruebas | Qué hace |
|---|---|
| `@pytest.fixture` | Una **fixture**: preparación que pytest ejecuta antes de cada prueba. `autouse=True`: en todas, sin nombrarla |
| `tmp_path` | Una fixture de pytest: una carpeta temporal nueva para cada prueba |
| `monkeypatch.setattr(almacen, "RUTA_BD", …)` | Cambia `RUTA_BD` solo durante la prueba: el almacén usa la base de datos de prueba |
| `with pytest.raises(sqlite3.IntegrityError):` | La prueba pasa solo si el código de dentro lanza ese error: aquí, al intentar guardar un 6 |

**Comprueba que…** `python -m pytest -v` muestra **9 passed**: las 6 del modelo y las 3 del almacén.

**Comprueba que lo entiendes.** Contesta antes de abrir las respuestas:

1. ¿Qué pasaría si `guardar_valora` no llamara a `conexion.commit()`?
2. Si nadie ha cambiado nunca los pesos, ¿qué devuelve `leer_pesos()`, y de dónde sale?
3. ¿Por qué el almacén no muestra mensajes de error en una ventana?

<details>
<summary>Respuestas</summary>

1. El `INSERT` no se guardaría: al cerrar la conexión, la valoración se perdería.
2. `Pesos(40, 30, 30)`: la tabla `pesos` está vacía, `fetchone()` devuelve `None` y se crean los pesos de por defecto de la clase `Pesos`.
3. Porque el almacén no usa Qt: solo guarda y lee. Si algo falla, lanza el error, y la ventana, que sí sabe mostrar mensajes, lo recoge. Así el almacén se prueba con pytest sin abrir ventanas.

</details>

## Paso 4 · El componente SelectorNota

Es la capa **Componente**: cinco estrellas para elegir una nota de 1 a 5. Es un widget propio, hecho con otros widgets de Qt, que la ventana usará tres veces. No sabe para qué se usa: solo guarda su nota y avisa cuando cambia.

Crea el archivo **`selector_nota.py`**:

**Las piezas del código:**

| Pieza | Qué hace |
|---|---|
| `class SelectorNota(QFrame):` | La clase **hereda** de `QFrame`, un widget con marco opcional: tiene todo lo que tiene `QFrame` y lo que se le añade |
| `notaCambiada = Signal(int)` | Una **señal propia**, que lleva un número entero. Se declara en la **clase**, no dentro de `__init__` |
| `def __init__(self, parent=None):` y `super().__init__(parent)` | El método que crea el objeto. `super().__init__` crea primero la parte de `QFrame` |
| `self._nota` | El guion bajo al principio indica que es **interno**: desde fuera se usa la propiedad `nota` |
| `setFocusPolicy(Qt.StrongFocus)` | El componente recibe el foco del teclado, con Tab o con un clic |
| `QHBoxLayout(self)` | Un layout que coloca los widgets uno al lado de otro, dentro del componente |
| `QToolButton` con `setAutoRaise(True)` | Un botón pequeño sin borde: cada estrella |
| `setFocusPolicy(Qt.NoFocus)` en cada estrella | Las estrellas no reciben el foco: lo tiene el componente entero, y Tab salta de un selector al siguiente, no de estrella en estrella |
| `lambda _=False, valor=valor: self._set_nota(valor)` | Una **lambda**: una función pequeña sin nombre. `valor=valor` hace que cada estrella recuerde su número; sin eso, las cinco usarían el último (5) |
| `nota = Property(int, _get_nota, _set_nota, notify=notaCambiada)` | Una **propiedad de Qt**: se usa como un atributo (`selector.nota = 4`), pero al cambiarla se ejecuta `_set_nota`. Qt Designer y pytest-qt también la ven |
| `self.notaCambiada.emit(valor)` | **Lanza** la señal con la nota nueva: todo lo conectado a ella se ejecuta |
| `if valor == self._nota: return` | Si la nota no cambia, no se avisa |
| `setAccessibleDescription(…)` | Lo que lee el lector de pantalla además del nombre: «4 de 5» |
| `def keyPressEvent(self, evento):` | Qt llama a este método con cada tecla pulsada mientras el componente tiene el foco. Las teclas que no usa se pasan a `super()`, para que Tab siga funcionando |
| `focusInEvent` y `focusOutEvent` | Al recibir y perder el foco, se pone y se quita el marco: así se ve dónde está el teclado |

```python
"""Componente reutilizable SelectorNota: cinco estrellas para elegir una nota de 1 a 5."""
from PySide6.QtCore import Property, Qt, Signal
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QToolButton


class SelectorNota(QFrame):
    """Cinco estrellas para elegir una nota de 1 a 5, con el ratón o con el teclado.

    Propiedad:
        nota (int): la nota elegida, de 1 a 5. 0 si aún no se ha elegido ninguna.
    Señal:
        notaCambiada(int): se emite cada vez que cambia la nota.
    Método:
        limpiar(): vuelve a «sin nota» (0).
    Teclado (con el foco en el componente):
        teclas 1 a 5 → esa nota; flecha derecha → una más; flecha izquierda → una menos.

    Ejemplo:
        selector = SelectorNota()
        selector.notaCambiada.connect(lambda n: print("Nota:", n))
    """

    # La señal propia se declara en la CLASE, no dentro de __init__
    notaCambiada = Signal(int)

    LLENA = "★"
    VACIA = "☆"

    def __init__(self, parent=None):
        super().__init__(parent)
        self._nota = 0

        # ── El foco: el componente entero recibe el teclado ──────────────
        # StrongFocus: se llega con Tab y con un clic
        self.setFocusPolicy(Qt.StrongFocus)

        # ── Composición: cinco botones-estrella y la nota en número ──────
        disposicion = QHBoxLayout(self)
        disposicion.setContentsMargins(4, 2, 4, 2)
        disposicion.setSpacing(0)
        self._estrellas = []
        for valor in range(1, 6):
            estrella = QToolButton()
            estrella.setAutoRaise(True)                # sin borde de botón
            estrella.setFocusPolicy(Qt.NoFocus)        # el foco lo tiene el componente, no cada estrella
            estrella.setToolTip(f"{valor} de 5")
            estrella.setStyleSheet("font-size: 20px;")
            # valor=valor: cada estrella recuerda su propio número
            estrella.clicked.connect(lambda _=False, valor=valor: self._set_nota(valor))
            disposicion.addWidget(estrella)
            self._estrellas.append(estrella)
        self._numero = QLabel()
        self._numero.setMinimumWidth(24)
        disposicion.addSpacing(8)
        disposicion.addWidget(self._numero)
        disposicion.addStretch()

        self._dibujar()

    # ── La propiedad «nota» ──────────────────────────────────────────────
    def _get_nota(self):
        return self._nota

    def _set_nota(self, valor):
        valor = max(0, min(5, valor))      # siempre entre 0 y 5
        if valor == self._nota:
            return                          # sin cambios: no se avisa
        self._nota = valor
        self._dibujar()
        self.notaCambiada.emit(valor)

    nota = Property(int, _get_nota, _set_nota, notify=notaCambiada)

    def limpiar(self):
        self._set_nota(0)

    # ── Dibujar: estrellas llenas hasta la nota y el número ──────────────
    def _dibujar(self):
        for valor, estrella in enumerate(self._estrellas, start=1):
            estrella.setText(self.LLENA if valor <= self._nota else self.VACIA)
        self._numero.setText(str(self._nota) if self._nota else "–")
        # Lo que lee el lector de pantalla, además del nombre accesible
        self.setAccessibleDescription(f"{self._nota} de 5" if self._nota else "Sin nota")

    # ── El teclado ───────────────────────────────────────────────────────
    def keyPressEvent(self, evento):
        tecla = evento.key()
        if Qt.Key_1 <= tecla <= Qt.Key_5:
            self._set_nota(tecla - Qt.Key_0)
        elif tecla == Qt.Key_Right:
            self._set_nota(max(1, self._nota + 1))
        elif tecla == Qt.Key_Left:
            self._set_nota(max(1, self._nota - 1))
        else:
            super().keyPressEvent(evento)   # el resto (Tab…), como siempre

    # Un marco alrededor cuando tiene el foco, para que se vea dónde está el teclado
    def focusInEvent(self, evento):
        self.setFrameShape(QFrame.StyledPanel)
        super().focusInEvent(evento)

    def focusOutEvent(self, evento):
        self.setFrameShape(QFrame.NoFrame)
        super().focusOutEvent(evento)
```

Crea también **`test_selector_nota.py`**. Usa **`qtbot`**, la herramienta de pytest-qt que simula el ratón y el teclado:

```python
"""Pruebas del componente SelectorNota con pytest-qt.

Ejecuta desde la carpeta del proyecto:  python -m pytest -v
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QToolButton

from selector_nota import SelectorNota


def test_empieza_sin_nota(qtbot):
    selector = SelectorNota()
    qtbot.addWidget(selector)
    assert selector.nota == 0


def test_clic_en_la_cuarta_estrella(qtbot):
    selector = SelectorNota()
    qtbot.addWidget(selector)
    estrellas = selector.findChildren(QToolButton)
    assert len(estrellas) == 5
    with qtbot.waitSignal(selector.notaCambiada, timeout=1000) as espera:
        qtbot.mouseClick(estrellas[3], Qt.LeftButton)   # la cuarta (se cuenta desde 0)
    assert espera.args == [4]
    assert selector.nota == 4


def test_teclado(qtbot):
    selector = SelectorNota()
    qtbot.addWidget(selector)
    qtbot.keyClick(selector, Qt.Key_3)
    assert selector.nota == 3
    qtbot.keyClick(selector, Qt.Key_Right)
    assert selector.nota == 4
    qtbot.keyClick(selector, Qt.Key_Left)
    qtbot.keyClick(selector, Qt.Key_Left)
    assert selector.nota == 2


def test_limpiar(qtbot):
    selector = SelectorNota()
    qtbot.addWidget(selector)
    selector.nota = 5
    selector.limpiar()
    assert selector.nota == 0
```

| Pieza de las pruebas | Qué hace |
|---|---|
| `qtbot` como parámetro | pytest-qt le pasa a la prueba un `qtbot` ya preparado |
| `qtbot.addWidget(selector)` | Registra el widget para cerrarlo al terminar la prueba |
| `findChildren(QToolButton)` | Busca dentro del componente todos los widgets de ese tipo: las cinco estrellas |
| `qtbot.mouseClick(…)` y `qtbot.keyClick(…)` | Simulan un clic y una tecla |
| `with qtbot.waitSignal(…) as espera:` | Espera a que la señal se lance dentro del bloque; `espera.args` tiene los valores con los que se lanzó |

**Comprueba que…** `python -m pytest -v` muestra **13 passed**.

**Comprueba que lo entiendes.** Contesta antes de abrir las respuestas:

1. Con la nota en 2, ¿qué nota queda tras pulsar dos veces la flecha derecha? ¿Y si después se pulsa `5` y otra vez la flecha derecha?
2. ¿Por qué cada estrella tiene `NoFocus`?
3. Si se ejecuta `selector.nota = 4` dos veces seguidas, ¿cuántas veces se lanza `notaCambiada`?

<details>
<summary>Respuestas</summary>

1. 4. Después, `5` la pone en 5, y la flecha derecha la deja en 5: `_set_nota` no pasa de 5.
2. Para que el foco lo tenga el componente entero: Tab salta de una categoría a la siguiente, y las teclas 1 a 5 y las flechas llegan a `keyPressEvent`.
3. Una: la segunda vez la nota ya es 4, y `_set_nota` sale sin avisar.

</details>

## Paso 5 · La ventana en Qt Designer

La ventana se **dibuja** en Qt Designer: se arrastran los widgets, se colocan con layouts y se les da nombre y propiedades. Designer lo guarda en `ventana.ui`, y `pyside6-uic` lo convierte en código Python.

```
ventana.ui  ──(pyside6-uic)──►  ui_ventana.py  ──(import y setupUi)──►  ventana.py (paso 7)
```

### 5.1 · Abrir Qt Designer

En la terminal de VS Code, con el entorno activado:

```powershell
Start-Process .venv\Scripts\pyside6-designer.exe -WindowStyle Hidden
```

`Start-Process` abre Designer aparte, y la terminal queda libre. En la ventana **New Form**, elige **Main Window** y pulsa **Create**: sale una ventana vacía con su barra de menú (*Type Here*) y su barra de estado.

| Zona de Designer | Dónde | Para qué |
|---|---|---|
| **Widget Box** | Izquierda | Los widgets, por grupos: *Layouts*, *Spacers*, *Buttons*, *Containers*, *Display Widgets*… Se arrastran a la ventana |
| **Object Inspector** | Arriba a la derecha | El árbol de widgets de la ventana. Un clic selecciona uno |
| **Property Editor** | Debajo del anterior | Las propiedades del widget seleccionado: `objectName`, `text`, `toolTip`… |
| **Action Editor** | Abajo a la derecha, en una pestaña | Las acciones del menú, con su atajo |

**Cómo se cambia una propiedad:** selecciona el widget (en la ventana o en el *Object Inspector*), busca la propiedad en el *Property Editor* (el filtro de arriba ayuda: escribe `object`, `text`, `tool`…) y haz doble clic en su valor.

### 5.2 · La ventana

Con la ventana seleccionada (en el *Object Inspector*, la primera línea, `MainWindow`), cambia:

| Propiedad | Valor |
|---|---|
| `objectName` | `VentanaPrincipal` |
| `windowTitle` | `ValoraDI` |

### 5.3 · El grupo «Nueva valoración»

1. Arrastra un **Group Box** (de *Containers*) a la parte de arriba de la ventana.
2. Dentro del grupo, arrastra tres **Label** (de *Display Widgets*), uno debajo de otro, a la izquierda. A la derecha de cada uno, un **Widget** (de *Containers*): un rectángulo vacío donde irán las estrellas.
3. Selecciona los seis (clic en el primero y **Ctrl + clic** en los demás) → clic derecho → *Lay out* → **Lay Out in a Form Layout**. Quedan en dos columnas, etiqueta y campo.
4. Debajo, dentro del grupo, arrastra un **Horizontal Spacer** (de *Spacers*) y, a su derecha, un **Push Button** (de *Buttons*). Selecciona los dos → clic derecho → *Lay out* → **Lay Out Horizontally**. El espaciador empuja el botón a la derecha.
5. Haz clic en una zona vacía del grupo → clic derecho → *Lay out* → **Lay Out Vertically**.

### 5.4 · El grupo «Resumen»

1. Arrastra otro **Group Box** debajo del primero.
2. Dentro, coloca widgets en **cinco filas y tres columnas**, aproximadamente alineados:

   | Fila | Columna 1 | Columna 2 | Columna 3 |
   |---|---|---|---|
   | 1 | Label | (nada) | Push Button |
   | 2 | Label | Label | Label |
   | 3 | Label | Label | Label |
   | 4 | Label | Label | Label |
   | 5 | Label | Label | (nada) |

3. Haz clic en una zona vacía del grupo → clic derecho → *Lay out* → **Lay Out in a Grid**. Si algún widget cae en otra fila o columna, deshazlo (**Ctrl + Z**), recolócalo y repite.
4. Por último, haz clic en una zona vacía de la ventana, fuera de los grupos → clic derecho → *Lay out* → **Lay Out Vertically**. Los dos grupos ocupan ya toda la ventana.

### 5.5 · Nombres y propiedades

Cambia, widget a widget, estas propiedades. El `objectName` es importante: es el nombre con el que el código del paso 7 usa cada widget (`self.ui.btnGuardar`). La `&` del texto marca la letra del atajo: `&Docente:` se ve con la D subrayada, y **Alt + D** lleva a ese campo.

**Grupo «Nueva valoración»**

| Widget | `objectName` | Otras propiedades |
|---|---|---|
| Group Box de arriba | `grpNueva` | `title`: `Nueva valoración` |
| Label 1 | `lblDocente` | `text`: `&Docente:` |
| Widget 1 | `selDocente` | `accessibleName`: `Nota de docente`; `focusPolicy`: `StrongFocus` |
| Label 2 | `lblMateriales` | `text`: `&Materiales:` |
| Widget 2 | `selMateriales` | `accessibleName`: `Nota de materiales`; `focusPolicy`: `StrongFocus` |
| Label 3 | `lblClases` | `text`: `&Clases:` |
| Widget 3 | `selClases` | `accessibleName`: `Nota de clases`; `focusPolicy`: `StrongFocus` |
| Push Button | `btnGuardar` | `text`: `&Guardar valoración`; `enabled`: **sin marcar**; `autoDefault`: **marcado**; `toolTip`: `Guarda la valoración (Ctrl+S). Se activa cuando las tres categorías tienen nota` |

**Grupo «Resumen»**

| Widget | `objectName` | Otras propiedades |
|---|---|---|
| Group Box de abajo | `grpResumen` | `title`: `Resumen` |
| Fila 1, columna 1 | `lblTotal` | `text`: `Aún no hay valoraciones` |
| Fila 1, columna 3 (botón) | `btnPesos` | `text`: `&Pesos…`; `autoDefault`: **marcado**; `toolTip`: `Cambia cuánto cuenta cada categoría en la nota global (Ctrl+P)` |
| Fila 2 | `lblNombreDocente`, `lblMediaDocente`, `lblPesoDocente` | `text`: `Docente`, `–` y `peso 40 %` |
| Fila 3 | `lblNombreMateriales`, `lblMediaMateriales`, `lblPesoMateriales` | `text`: `Materiales`, `–` y `peso 30 %` |
| Fila 4 | `lblNombreClases`, `lblMediaClases`, `lblPesoClases` | `text`: `Clases`, `–` y `peso 30 %` |
| Fila 5, columna 1 | `lblNombreGlobal` | `text`: `Nota global`; `styleSheet`: `font-weight: bold;` |
| Fila 5, columna 2 | `lblGlobal` | `text`: `–`; `accessibleName`: `Nota global`; `styleSheet`: `font-size: 24px; font-weight: bold;` |

| Propiedad | Qué hace |
|---|---|
| `accessibleName` | El nombre que lee el lector de pantalla. Las estrellas no tienen texto, así que sin él no se sabría qué se está valorando |
| `focusPolicy`: `StrongFocus` | El widget recibe el foco con Tab y con un clic. Designer solo deja unir una etiqueta a un widget que puede recibir el foco (5.7) |
| `enabled` sin marcar | El botón empieza desactivado: «Guardar» se activa cuando las tres categorías tienen nota (paso 7) |
| `autoDefault` | Con el foco en el botón, **Intro** lo pulsa. En los diálogos Qt lo hace solo; en una ventana principal, no |
| `toolTip` | La ayuda que sale al dejar el ratón encima |
| `styleSheet` | El aspecto, con la sintaxis de CSS: negrita (`font-weight: bold`) y tamaño de letra (`font-size`) |

### 5.6 · Promocionar los tres Widget a SelectorNota

Designer no conoce `SelectorNota`, el componente del paso 4: solo conoce los widgets de Qt. Por eso se ha puesto un **Widget** vacío en su lugar, y ahora se **promociona**: se le dice a Designer que, en el código, ese widget será un `SelectorNota`.

1. Clic derecho en `selDocente` → **Promote to…**
2. En la ventana *Promoted Widgets*, escribe:
   - *Promoted class name*: `SelectorNota`
   - *Header file*: `selector_nota.h`
3. Pulsa **Add** y después **Promote**.
4. Clic derecho en `selMateriales` → *Promote to* → **SelectorNota** (ya sale en la lista). Lo mismo con `selClases`.

El *header file* es cosa de C++, el lenguaje en el que está escrito Qt. En Python solo sirve para el nombre del módulo: `pyside6-uic` escribirá `from selector_nota import SelectorNota`. En Designer, los tres siguen viéndose como rectángulos vacíos: las estrellas solo aparecen al ejecutar la app.

### 5.7 · Etiquetas, orden del tabulador y menú

**Unir cada etiqueta con su campo** (para que Alt + D, Alt + M y Alt + C funcionen):

1. Menú *Edit* → **Edit Buddies**.
2. Arrastra desde `lblDocente` hasta `selDocente`: aparece una línea que los une. Lo mismo con materiales y clases.
3. Menú *Edit* → **Edit Widgets**, para volver al modo normal.

**El orden del tabulador** (el camino que sigue Tab):

1. Menú *Edit* → **Edit Tab Order**. Sobre cada widget que recibe el foco aparece un número.
2. Haz clic, en este orden, en `selDocente`, `selMateriales`, `selClases`, `btnGuardar` y `btnPesos`.
3. Menú *Edit* → **Edit Widgets**.

**El menú:**

1. Doble clic en *Type Here*, en la barra de menú. Escribe `&Valoración` e **Intro**.
2. En el menú que se abre, en *Type Here*, escribe `Guardar valoración` e **Intro**. Después, `Pesos…` e **Intro**. Después, **Add Separator**. Por último, `Salir` e **Intro**.
3. En el **Action Editor** (pestaña de abajo a la derecha) salen las tres acciones. Haz doble clic en cada una y cambia su *Object name* y su *Shortcut* (en *Shortcut*, haz clic y **pulsa** la combinación):

   | Acción | *Object name* | *Shortcut* |
   |---|---|---|
   | Guardar valoración | `actionGuardar` | Ctrl+S |
   | Pesos… | `actionPesos` | Ctrl+P |
   | Salir | `actionSalir` | Ctrl+Q |

4. Selecciona `actionGuardar` en el *Action Editor* y, en el *Property Editor*, desmarca **`enabled`**: como el botón, empieza desactivada.
5. En el *Object Inspector*, selecciona el menú (`menuValoraci_n`) y cambia su `objectName` a `menuValora`.

### 5.8 · Guardar y generar el código

1. *File* → **Save As…** → en la carpeta del proyecto (`C:\dam2627\di\ValoraDI`), con el nombre **`ventana.ui`**.
2. Para ver cómo queda: *Form* → **Preview** (**Ctrl + R**). Los selectores salen vacíos, como se ha dicho. Cierra la vista previa.
3. En la terminal de VS Code:

   ```powershell
   pyside6-uic ventana.ui -o ui_ventana.py
   ```

   Crea `ui_ventana.py`, con la clase `Ui_VentanaPrincipal`. **No se edita a mano**: cada vez que cambies algo en Designer, guarda y vuelve a ejecutar este comando, y el archivo se sustituye entero.

**Comprueba que…**

- el *Object Inspector* muestra este árbol (el orden de los widgets dentro de cada grupo puede variar, y los layouts salen con nombres como `formLayout` o `gridLayout`):

  ```
  VentanaPrincipal                  QMainWindow
  ├── centralwidget                 QWidget
  │   ├── grpNueva                  QGroupBox
  │   │   ├── lblDocente            QLabel
  │   │   ├── selDocente            SelectorNota
  │   │   ├── lblMateriales         QLabel
  │   │   ├── selMateriales         SelectorNota
  │   │   ├── lblClases             QLabel
  │   │   ├── selClases             SelectorNota
  │   │   └── btnGuardar            QPushButton
  │   └── grpResumen                QGroupBox
  │       ├── lblTotal              QLabel
  │       ├── btnPesos              QPushButton
  │       ├── lblNombreDocente …    QLabel (las 11 etiquetas del resumen)
  │       └── lblGlobal             QLabel
  ├── menubar                       QMenuBar
  │   └── menuValora                QMenu
  └── statusbar                     QStatusBar
  ```

- `ui_ventana.py` existe y, cerca del principio, tiene la línea `from selector_nota import SelectorNota`.

**Comprueba que lo entiendes.** Contesta antes de abrir las respuestas:

1. Cambias en Designer el texto de `btnPesos` y guardas, pero al ejecutar la app sigue el texto anterior. ¿Qué falta?
2. ¿Por qué los tres selectores son `Widget` en Designer y no otra cosa?
3. ¿Qué pasaría si `btnGuardar` se llamara `pushButton`, como lo crea Designer?

<details>
<summary>Respuestas</summary>

1. Volver a generar el código: `pyside6-uic ventana.ui -o ui_ventana.py`. La app no lee `ventana.ui`, sino `ui_ventana.py`.
2. Porque Designer solo conoce los widgets de Qt. Se pone un `QWidget` vacío, que es la clase de la que heredan todos, y se promociona a `SelectorNota`: en el código generado, ese widget se crea como un `SelectorNota`.
3. El código del paso 7 usa `self.ui.btnGuardar`, que no existiría: al abrir la app saldría el error `AttributeError: 'Ui_VentanaPrincipal' object has no attribute 'btnGuardar'`.

</details>

## Paso 6 · El diálogo de pesos

El diálogo se hace **con código**, sin Designer: es pequeño y sus tres campos se crean con un bucle, uno por categoría. Pide los pesos, muestra el aviso que da el modelo y solo deja aceptar si suman 100.

Crea el archivo **`dialogo_pesos.py`**:

**Las piezas del código:**

| Pieza | Qué hace |
|---|---|
| `class DialogoPesos(QDialog):` | Un **diálogo**: una ventana que pide algo y devuelve si se aceptó o se canceló |
| `QFormLayout(self)` | Un layout de parejas «etiqueta y campo» |
| `QSpinBox` con `setRange(0, 100)`, `setSingleStep(5)` y `setSuffix(" %")` | Un campo numérico de 0 a 100, que con las flechas sube y baja de 5 en 5, y que muestra « %» detrás |
| `campo.valueChanged.connect(self._comprobar)` | Cada vez que cambia un peso, se vuelve a comprobar |
| `formulario.addRow(f"&{…}:", campo)` | Crea la etiqueta y la une al campo: Alt + D, Alt + M y Alt + C llevan a cada uno |
| `fontMetrics()` y `horizontalAdvance(…)` | Miden cuánto ocupa un texto con la letra de la etiqueta. Con ellas se reserva desde el principio el sitio del aviso más largo, y el diálogo no cambia de tamaño al aparecer el aviso |
| `QDialogButtonBox(Ok \| Cancel)` | Los botones Aceptar y Cancelar, en el orden habitual de cada sistema |
| `accepted.connect(self.accept)` | «Aceptar» cierra el diálogo con resultado *aceptado*; «Cancelar», con *rechazado* |
| `Pesos(*(… for c in CATEGORIAS))` | El `*` reparte los tres valores como los tres datos de `Pesos`: `Pesos(40, 30, 30)` |

```python
"""Diálogo modal «Pesos»: cuánto cuenta cada categoría en la nota global."""
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLabel, QSpinBox

from modelo import CATEGORIAS, NOMBRES, Pesos


class DialogoPesos(QDialog):
    """Pide los tres pesos, en %. «Aceptar» solo se activa si suman 100."""

    def __init__(self, pesos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pesos de la nota global")

        # ── Un campo por categoría, de 0 a 100 % ─────────────────────────
        formulario = QFormLayout(self)
        self._campos = {}
        for categoria in CATEGORIAS:
            campo = QSpinBox()
            campo.setRange(0, 100)
            campo.setSingleStep(5)
            campo.setSuffix(" %")
            campo.setValue(pesos.peso(categoria))
            campo.setAccessibleName(f"Peso de {NOMBRES[categoria].lower()}")
            campo.valueChanged.connect(self._comprobar)
            # addRow(texto, campo) crea la etiqueta y la une al campo (buddy): Alt+letra lleva al campo
            formulario.addRow(f"&{NOMBRES[categoria]}:", campo)
            self._campos[categoria] = campo

        # ── El aviso: cuánto falta o sobra para 100 % ────────────────────
        self._aviso = QLabel()
        self._aviso.setStyleSheet("color: #B00020;")   # rojo oscuro: buen contraste sobre fondo claro
        # Sitio reservado desde el principio para el aviso más largo (los tres pesos al 100 %),
        # para que el diálogo no cambie de tamaño al aparecer o cambiar el mensaje
        medidas = self._aviso.fontMetrics()
        self._aviso.setMinimumSize(medidas.horizontalAdvance(Pesos(100, 100, 100).aviso), medidas.height())
        formulario.addRow(self._aviso)

        # ── Aceptar y Cancelar ───────────────────────────────────────────
        self._botones = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # Qt los escribe en inglés («OK», «Cancel») si no se le dice otra cosa
        self._botones.button(QDialogButtonBox.Ok).setText("Aceptar")
        self._botones.button(QDialogButtonBox.Cancel).setText("Cancelar")
        self._botones.accepted.connect(self.accept)
        self._botones.rejected.connect(self.reject)
        formulario.addRow(self._botones)

        self._comprobar()

    def pesos(self):
        """Los pesos que hay escritos ahora en el diálogo."""
        return Pesos(*(self._campos[c].value() for c in CATEGORIAS))

    def _comprobar(self):
        # El modelo dice si son válidos y qué falta; el diálogo solo lo muestra
        pesos = self.pesos()
        self._aviso.setText(pesos.aviso)
        self._botones.button(QDialogButtonBox.Ok).setEnabled(pesos.validos)
```

**Comprueba que…** `python -m pytest -v` sigue mostrando **13 passed**: el diálogo aún no se usa en ninguna prueba, pero si tuviera un error de sintaxis, las pruebas ya fallarían al importarlo en el paso 7.

**Comprueba que lo entiendes.** Contesta antes de abrir las respuestas:

1. ¿Quién decide si los pesos son válidos: el diálogo o el modelo?
2. Con los pesos en 40, 30 y 20, ¿qué se ve en el diálogo?

<details>
<summary>Respuestas</summary>

1. El modelo (`Pesos.validos` y `Pesos.aviso`). El diálogo solo muestra el aviso y activa o desactiva «Aceptar» según lo que dice el modelo.
2. El aviso «Faltan 10 puntos para llegar a 100 %», en rojo oscuro, y «Aceptar» desactivado.

</details>

## Paso 7 · El código de la ventana

La ventana une todo: crea los widgets del diseño (`setupUi`), conecta cada señal con su slot, guarda con el almacén, abre el diálogo y dibuja el resumen que calcula el modelo. No tiene SQL ni cálculos.

Crea el archivo **`ventana.py`**:

**Las piezas del código:**

| Pieza | Qué hace |
|---|---|
| `class VentanaPrincipal(QMainWindow):` | La ventana principal: la clase hereda de `QMainWindow`, la ventana de Qt con menú y barra de estado |
| `self.ui = Ui_VentanaPrincipal()` y `self.ui.setupUi(self)` | Crea los widgets del diseño (paso 5) dentro de la ventana. Desde ahí, cada widget se usa por su `objectName`: `self.ui.btnGuardar` |
| `self.selectores = {"docente": self.ui.selDocente, …}` | Un **diccionario**: a cada nombre de categoría le corresponde su selector. Así, un bucle `for` recorre las tres categorías sin repetir código |
| `señal.connect(slot)` | Une una señal con la función que se ejecuta al recibirla: `clicked` de un botón, `triggered` de una acción del menú, `notaCambiada` del selector |
| `all(s.nota > 0 for s in …)` | `True` solo si las tres categorías tienen nota |
| `Valora(*(self.selectores[c].nota for c in CATEGORIAS))` | Crea la valoración con las tres notas, en el orden de `CATEGORIAS` |
| `try:` … `except sqlite3.Error as e:` | Si el almacén falla, se recoge el error y se avisa con `QMessageBox.critical`, una ventana de error, en lugar de cerrar la app |
| `statusbar.showMessage("…", 3000)` | Un mensaje en la barra de estado durante 3000 milisegundos (3 segundos) |
| `dialogo.exec()` | Abre el diálogo y **espera** a que se cierre. Devuelve si se aceptó |
| `def keyPressEvent(self, evento):` | Si llega a la ventana un **Intro** que no ha recogido ningún botón (por ejemplo, con el foco en las estrellas), guarda |
| `zip(CATEGORIAS, resumen.filas)` | Recorre las dos listas a la vez: cada categoría con su fila del resumen |

```python
"""La ventana principal de ValoraDI.

Regla de separación: aquí no hay SQL (está en almacen.py) ni cálculos (están en
modelo.py). La ventana recoge lo que se pulsa, pide el resumen y lo dibuja.
"""
import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox

import almacen
from dialogo_pesos import DialogoPesos
from modelo import CATEGORIAS, Valora, resumir
from ui_ventana import Ui_VentanaPrincipal


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        # ── Los controles de cada categoría, por su nombre interno ───────
        self.selectores = {
            "docente": self.ui.selDocente,
            "materiales": self.ui.selMateriales,
            "clases": self.ui.selClases,
        }
        self.etiquetas_media = {
            "docente": self.ui.lblMediaDocente,
            "materiales": self.ui.lblMediaMateriales,
            "clases": self.ui.lblMediaClases,
        }
        self.etiquetas_peso = {
            "docente": self.ui.lblPesoDocente,
            "materiales": self.ui.lblPesoMateriales,
            "clases": self.ui.lblPesoClases,
        }

        # ── Conexiones: qué pasa al pulsar cada cosa ─────────────────────
        for selector in self.selectores.values():
            selector.notaCambiada.connect(self.actualizar_guardar)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.btnPesos.clicked.connect(self.cambiar_pesos)
        self.ui.actionPesos.triggered.connect(self.cambiar_pesos)
        self.ui.actionSalir.triggered.connect(self.close)

        # ── Al abrir: los pesos guardados y el resumen de lo guardado ────
        self.pesos = self.leer(almacen.leer_pesos)
        self.actualizar_resumen()
        self.ui.selDocente.setFocus()

    # ── El formulario ────────────────────────────────────────────────────
    def actualizar_guardar(self):
        """«Guardar» solo se activa cuando las tres categorías tienen nota."""
        completo = all(s.nota > 0 for s in self.selectores.values())
        self.ui.btnGuardar.setEnabled(completo)
        self.ui.actionGuardar.setEnabled(completo)

    def guardar(self):
        if not self.ui.btnGuardar.isEnabled():
            return
        valora = Valora(*(self.selectores[c].nota for c in CATEGORIAS))
        try:
            almacen.guardar_valora(valora)
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"No se ha podido guardar la valoración:\n{e}")
            return
        # Formulario vacío para la siguiente persona, y el foco en la primera categoría
        for selector in self.selectores.values():
            selector.limpiar()
        self.ui.selDocente.setFocus()
        self.ui.statusbar.showMessage("Valoración guardada", 3000)
        self.actualizar_resumen()

    # Intro en las estrellas guarda, como al enviar un formulario. (Con el foco en
    # un botón, Intro lo pulsa él mismo: autoDefault, en ventana.ui)
    def keyPressEvent(self, evento):
        if evento.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.guardar()          # si falta alguna nota, guardar() no hace nada
        else:
            super().keyPressEvent(evento)

    # ── Los pesos ────────────────────────────────────────────────────────
    def cambiar_pesos(self):
        dialogo = DialogoPesos(self.pesos, self)
        if dialogo.exec() != DialogoPesos.Accepted:
            return                                  # Cancelar: no cambia nada
        nuevos = dialogo.pesos()
        try:
            almacen.guardar_pesos(nuevos)
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"No se han podido guardar los pesos:\n{e}")
            return
        self.pesos = nuevos
        self.ui.statusbar.showMessage("Pesos guardados", 3000)
        self.actualizar_resumen()

    # ── El resumen: lo calcula el modelo; aquí solo se dibuja ────────────
    def actualizar_resumen(self):
        valoras = self.leer(almacen.leer_valoras)
        resumen = resumir(valoras, self.pesos)
        self.ui.lblTotal.setText(resumen.texto_total)
        for categoria, fila in zip(CATEGORIAS, resumen.filas):
            self.etiquetas_media[categoria].setText(fila.texto_media)
            self.etiquetas_peso[categoria].setText(f"peso {fila.peso} %")
        self.ui.lblGlobal.setText(resumen.texto_global)

    # ── Leer del almacén avisando si falla ───────────────────────────────
    def leer(self, funcion):
        try:
            return funcion()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"No se ha podido leer la base de datos:\n{e}")
            raise SystemExit(1)
```

Crea también **`test_ventana.py`**, que prueba la ventana entera usando solo el teclado:

```python
"""Pruebas de la ventana con pytest-qt: el formulario completo, con el teclado.

Ejecuta desde la carpeta del proyecto:  python -m pytest -v
"""
import pytest
from PySide6.QtCore import Qt

import almacen
from ventana import VentanaPrincipal


@pytest.fixture
def ventana(qtbot, tmp_path, monkeypatch):
    # Una base de datos nueva en una carpeta temporal: valora.db no se toca
    monkeypatch.setattr(almacen, "RUTA_BD", tmp_path / "prueba.db")
    almacen.crear_bd()
    v = VentanaPrincipal()
    qtbot.addWidget(v)
    return v


def test_intro_sin_las_tres_notas_no_guarda(ventana, qtbot):
    qtbot.keyClick(ventana.ui.selDocente, Qt.Key_4)
    qtbot.keyClick(ventana.ui.selDocente, Qt.Key_Return)
    assert almacen.leer_valoras() == []


def test_intro_con_las_tres_notas_guarda(ventana, qtbot):
    qtbot.keyClick(ventana.ui.selDocente, Qt.Key_4)
    qtbot.keyClick(ventana.ui.selMateriales, Qt.Key_3)
    qtbot.keyClick(ventana.ui.selClases, Qt.Key_5)
    qtbot.keyClick(ventana.ui.selClases, Qt.Key_Return)
    assert len(almacen.leer_valoras()) == 1
    assert ventana.ui.lblTotal.text() == "1 valoración"
    assert ventana.ui.selDocente.nota == 0          # el formulario se vacía


def test_intro_en_el_boton_guardar(ventana, qtbot):
    for selector in (ventana.ui.selDocente, ventana.ui.selMateriales, ventana.ui.selClases):
        selector.nota = 5
    qtbot.keyClick(ventana.ui.btnGuardar, Qt.Key_Return)
    assert len(almacen.leer_valoras()) == 1
```

**Comprueba que…** `python -m pytest -v` muestra **16 passed**: todas las pruebas de la app.

**Comprueba que lo entiendes.** Contesta antes de abrir las respuestas:

1. ¿Qué método se ejecuta al pulsar una estrella, y qué hace?
2. ¿Por qué `actualizar_resumen` no hace ninguna cuenta?
3. ¿Qué pasa si se pulsa Intro con el foco en las estrellas y solo dos categorías tienen nota?

<details>
<summary>Respuestas</summary>

1. El selector lanza `notaCambiada`, que está conectada a `actualizar_guardar`. Este comprueba si las tres categorías tienen nota y activa o desactiva «Guardar valoración» y su acción del menú.
2. Porque las hace el modelo: `resumir` devuelve el resumen con sus textos ya escritos (`texto_total`, `texto_media`, `texto_global`), y la ventana solo los copia en las etiquetas.
3. Nada: `keyPressEvent` llama a `guardar`, y `guardar` sale sin hacer nada porque el botón está desactivado.

</details>

## Paso 8 · Arrancar la app

`main.py` es el punto de entrada: crea las tablas, si no existen, crea la aplicación de Qt y abre la ventana.

Crea el archivo **`main.py`**:

**Las piezas del código:**

| Pieza | Qué hace |
|---|---|
| `QApplication(sys.argv)` | La aplicación de Qt. Tiene que existir, y solo una, antes de crear cualquier ventana |
| `ventana.show()` | Muestra la ventana |
| `app.exec()` | Arranca el **bucle de eventos**: Qt espera clics y teclas y los reparte a los widgets, hasta que se cierra la ventana |
| `sys.exit(…)` | Termina el programa con el resultado de la aplicación |
| `if __name__ == "__main__":` | El código de dentro solo se ejecuta al lanzar el archivo directamente (`python main.py`), no al importarlo desde otro |

```python
"""ValoraDI: valoraciones anónimas de docente, materiales y clases, con nota global ponderada.

Se ejecuta desde la carpeta del proyecto, con el entorno virtual activado:
    python main.py
"""
import sys

from PySide6.QtWidgets import QApplication

import almacen
from ventana import VentanaPrincipal


def main():
    almacen.crear_bd()                 # crea las tablas la primera vez
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```

En la terminal, con el entorno activado:

```powershell
python main.py
```

**Comprueba que…** se abre la ventana «ValoraDI» con las tres filas de estrellas vacías, «Guardar valoración» en gris y, en el resumen, «Aún no hay valoraciones» y rayas en lugar de números. En la carpeta del proyecto ha aparecido `valora.db`.

## Paso 9 · Probar la app

**9.1 · Las pruebas.** Hazlas en orden, con `python main.py`:

| N.º | Prueba | Cómo | Resultado esperado |
|---|---|---|---|
| 1 | Primera apertura | Abrir la app | «Aún no hay valoraciones», rayas en las medias y en la nota global, y «Guardar valoración» en gris |
| 2 | Guardar solo con las tres notas | Elegir docente y materiales | «Guardar valoración» sigue en gris. Al elegir clases, se activa |
| 3 | Guardar | Docente 4, materiales 3 y clases 5, y «Guardar valoración» | «Valoración guardada» abajo; las estrellas vacías; en el resumen, «1 valoración», 4.0, 3.0, 5.0 y nota global **4.0** |
| 4 | Segunda valoración | Docente 2, materiales 3 y clases 3, y guardar | «2 valoraciones», 3.0, 3.0, 4.0 y nota global **3.3** |
| 5 | Pesos que no suman 100 | «Pesos…» y clases a 20 % | El aviso «Faltan 10 puntos para llegar a 100 %» y «Aceptar» en gris. El diálogo no cambia de tamaño |
| 6 | Cambiar los pesos | Docente 60, materiales 20 y clases 20, y «Aceptar» | «Pesos guardados»; los pesos del resumen cambian y la nota global pasa a **3.2**: (3.0 · 60 + 3.0 · 20 + 4.0 · 20) / 100 = 320 / 100 |
| 7 | Cancelar | «Pesos…», cambiar algo y «Cancelar» | Nada cambia |
| 8 | Lo guardado sigue | Cerrar la app y volver a abrirla | El mismo resumen: «2 valoraciones», los pesos 60, 20 y 20 y la nota global 3.2 |

**9.2 · Solo con el teclado (R7).** Sin tocar el ratón:

| Tecla | Resultado esperado |
|---|---|
| **Tab** | El foco pasa por docente, materiales, clases, «Guardar valoración» y «Pesos…». Alrededor de las estrellas con el foco se ve un marco |
| **4**, con el foco en docente | Cuatro estrellas llenas y el número 4 |
| **Flecha derecha** y **flecha izquierda** | Una estrella más o una menos, entre 1 y 5 |
| **Alt + M** | El foco salta a materiales |
| **Intro**, con las tres notas y el foco en las estrellas | Guarda, como con el botón |
| **Ctrl + P** | Abre «Pesos». Dentro, **Tab** pasa de un campo a otro, las flechas suben y bajan de 5 en 5, **Intro** acepta y **Esc** cancela |
| **Ctrl + Q** | Cierra la app |

**9.3 · Ver la base de datos.** Con la app cerrada, en la terminal:

```powershell
python -c "import sqlite3; c = sqlite3.connect('valora.db'); print(c.execute('SELECT * FROM valora').fetchall()); print(c.execute('SELECT * FROM pesos').fetchall())"
```

Salen las filas de las dos tablas: `[(1, 4, 3, 5), (2, 2, 3, 3)]` y `[(1, 60, 20, 20)]`. Para empezar de cero, cierra la app y borra `valora.db`: se vuelve a crear vacía al abrirla.

**Comprueba que…** las ocho pruebas de 9.1 dan el resultado esperado, todo se puede hacer solo con el teclado y `python -m pytest -v` muestra **16 passed**.

---

## Si algo falla

| Qué pasa | Qué hacer |
|---|---|
| `python` no se reconoce | Cierra la terminal y abre una nueva. Si sigue, reinstala Python marcando **Add python.exe to PATH** (paso 0) |
| «La ejecución de scripts está deshabilitada en este sistema» al activar el entorno | Ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activarlo |
| `WinError 206` («el nombre del archivo o la extensión es demasiado largo») al instalar | La carpeta está en una ruta larga o en OneDrive. Usa `C:\dam2627\di\ValoraDI` y repite desde `python -m venv .venv` |
| `ModuleNotFoundError: No module named 'PySide6'` | El entorno no está activado (falta `(.venv)` al principio de la línea), o la librería no se instaló en él. Actívalo y repite `pip install -r requirements.txt` |
| VS Code subraya en amarillo los `import` de PySide6 | VS Code no usa el Python del entorno: `Ctrl + Mayús + P` → «Python: Select Interpreter» → el de `.venv` |
| `fixture 'qtbot' not found` | Falta pytest-qt en el entorno: actívalo y repite `pip install -r requirements.txt` |
| `ModuleNotFoundError: No module named 'ui_ventana'` | Falta generar el código del diseño: `pyside6-uic ventana.ui -o ui_ventana.py` (paso 5.8) |
| `AttributeError: 'Ui_VentanaPrincipal' object has no attribute '…'` | Un `objectName` del diseño no coincide con el del código. Compáralo con la tabla del paso 5.5, guarda en Designer y vuelve a generar `ui_ventana.py` |
| En lugar de estrellas sale un rectángulo vacío | Falta promocionar ese widget a `SelectorNota` (paso 5.6). Guarda y vuelve a generar `ui_ventana.py` |
| Designer no deja unir una etiqueta con su selector | Al widget le falta `focusPolicy`: `StrongFocus` (paso 5.5) |
| Designer no abre | Comprueba que la terminal está en la carpeta del proyecto, con el entorno activado, y que existe `.venv\Scripts\pyside6-designer.exe` |
| Designer no abre y sale «Una directiva de Control de aplicaciones bloqueó este archivo» | Windows tiene activado un control de aplicaciones (por ejemplo, *Smart App Control*) que solo deja abrir programas firmados. `.venv\Scripts\pyside6-designer.exe` es un acceso directo que crea `pip` al instalar PySide6 y no está firmado; el programa real, `.venv\Lib\site-packages\PySide6\designer.exe`, está firmado por The Qt Company. Ábrelo directamente: `& ".venv\Lib\site-packages\PySide6\designer.exe"`. Lo mismo con `pyside6-uic`: `& ".venv\Lib\site-packages\PySide6\uic.exe" -g python ventana.ui -o ui_ventana.py` |
| Tab no sigue el orden docente, materiales, clases, Guardar, Pesos | Repite *Edit Tab Order* en Designer (paso 5.7), guarda y vuelve a generar `ui_ventana.py` |
| Sale «No se ha podido leer la base de datos» o «No se ha podido guardar…» | El mensaje dice el motivo. Si `valora.db` está abierta en otro programa, ciérralo; si está dañada, borra el archivo y abre la app otra vez |
| En Linux, al abrir la app o Designer: `Could not load the Qt platform plugin "xcb"` | Falta una librería del sistema que necesita Qt: `sudo apt install libxcb-cursor0` (en Ubuntu y Debian) y vuelve a abrir |
| En Linux, `python3 -m venv .venv` falla con «ensurepip is not available» | Falta el módulo de entornos virtuales: `sudo apt install python3-venv` y repite el comando |
| Una prueba sale `FAILED` | pytest muestra la línea del `assert` que falla y los dos valores que no coinciden: compara ese archivo con el de la guía |

## Los archivos del proyecto

Al terminar, así está la carpeta del proyecto. Son los mismos archivos que muestra el Explorador de VS Code, más las carpetas que crean Python y pytest al trabajar (`__pycache__` y `.pytest_cache`), que no se tocan.

```
C:\dam2627\di\ValoraDI
├── .venv                   el entorno virtual, con las librerías
├── modelo.py               Valora, Pesos y los cálculos (paso 2)
├── almacen.py              el SQL y valora.db (paso 3)
├── selector_nota.py        el componente de estrellas (paso 4)
├── ventana.ui              el diseño, en Qt Designer (paso 5)
├── ui_ventana.py           el código del diseño, generado (paso 5)
├── dialogo_pesos.py        el diálogo de pesos (paso 6)
├── ventana.py              la ventana: conecta y dibuja (paso 7)
├── main.py                 el punto de entrada (paso 8)
├── test_modelo.py          pruebas del modelo (paso 2)
├── test_almacen.py         pruebas del almacén (paso 3)
├── test_selector_nota.py   pruebas del componente (paso 4)
├── test_ventana.py         pruebas de la ventana (paso 7)
├── requirements.txt        las librerías (paso 1)
└── valora.db               la base de datos (la crea la app)
```
