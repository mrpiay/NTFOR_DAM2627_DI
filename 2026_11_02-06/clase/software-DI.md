# Software · 2º DAM · DI · semana del 3 al 6 de noviembre

Qué hay que tener instalado para hacer el proyecto de esta semana, cómo instalarlo en Windows y cómo comprobar que funciona. Si algo no se puede instalar, cada apartado dice qué hacer mientras tanto: **nadie se queda parado por el software**.

**Índice**

- [Antes de empezar](#antes-de-empezar)
- [Base común: WSL2 con Ubuntu, Java y Python](#base-común-wsl2-con-ubuntu-java-y-python)
- [2º DAM · DI](#2º-dam--di)
- [Problemas frecuentes](#problemas-frecuentes)

## Antes de empezar

- **Descarga siempre de la web oficial** de cada programa (las direcciones están en cada apartado). No uses páginas de descargas de terceros.
- **Permisos de administrador.** Casi todas las instalaciones los piden. Si tu ordenador no te los da, trabaja en pareja o en un equipo del aula y avisa al docente.
- **Espacio en disco.** Mira cuánto tienes libre (Explorador de archivos → *Este equipo*). Lo que ocupa cada cosa va indicado; son valores aproximados.
- **Virtualización activada.** WSL2 necesita que esté activada en la BIOS/UEFI. Para comprobarlo: *Administrador de tareas* (`Ctrl + Mayús + Esc`) → *Rendimiento* → *CPU* → **Virtualización: Habilitado**. Si pone *Deshabilitado*, avisa al docente antes de tocar nada en la BIOS.
- **Instalar desde la terminal (opcional).** Windows 10 y 11 traen `winget`. Donde se indica, puedes instalar con una sola orden en PowerShell en lugar de descargar el instalador.

## Base común: WSL2 con Ubuntu, Java y Python

**2º DAM (DI y PMDM).** WSL2 es un Ubuntu completo dentro de Windows. Lo usaremos como entorno de trabajo común para todo lo que se hace en la terminal: comandos de Linux, programas de consola en Java y scripts en Python, editados con Visual Studio Code. Lo que tiene ventanas (PySide6 y Qt Designer) sigue en Windows.

| Qué | Para qué | Ocupa |
|---|---|---|
| **WSL2 con Ubuntu 24.04** | La terminal de Linux de todos los módulos | unos 2 GB |
| **Java (OpenJDK 21) dentro de Ubuntu** | Compilar y ejecutar Java en la terminal | unos 300 MB |
| **Python 3 dentro de Ubuntu** (ya viene) y `python3-venv` | Ejecutar scripts y crear entornos virtuales | unos 50 MB |
| **Visual Studio Code** (en Windows) con la extensión **WSL** de Microsoft | Editar los archivos de Ubuntu desde Windows | unos 400 MB |

### Instalar WSL2 y Ubuntu

1. Abre **PowerShell como administrador** (clic derecho en el botón Inicio → *Terminal (Administrador)*) y escribe:

    ```
    wsl --install -d Ubuntu-24.04
    ```

2. Reinicia el ordenador si te lo pide. Al volver (o al abrir *Ubuntu 24.04* desde el menú Inicio), se abre Ubuntu y te pide un **nombre de usuario** y una **contraseña** (es la de Ubuntu, no la de Windows; al escribirla no se ve nada: es normal). Apúntala: la necesitarás para `sudo`.
3. **Comprueba que**, en PowerShell, `wsl -l -v` muestra `Ubuntu-24.04` con **VERSION 2**.

### Instalar Java y lo necesario de Python dentro de Ubuntu

En la terminal de Ubuntu (menú Inicio → *Ubuntu*):

```
sudo apt update
sudo apt install -y openjdk-21-jdk python3-venv python3-pip unzip
```

**Comprueba que** `java -version` muestra 21 y `python3 --version` muestra 3.12 o superior. `unzip` sirve para descomprimir archivos zip: en Ubuntu no viene instalado.

### Visual Studio Code con WSL

1. Instala **Visual Studio Code** en Windows (**code.visualstudio.com**) si no lo tienes.
2. En VS Code, *Extensiones* (`Ctrl + Mayús + X`): instala **WSL** (de Microsoft).
3. En la terminal de Ubuntu, crea una carpeta de trabajo y ábrela en VS Code:

    ```
    mkdir -p ~/dam && cd ~/dam
    code .
    ```

4. **Comprueba que** VS Code se abre y abajo a la izquierda pone **WSL: Ubuntu-24.04**. La primera vez tarda un poco: VS Code instala su parte dentro de Ubuntu. La terminal de VS Code (`Ctrl + Ñ`) es ya la de Ubuntu.

### Dónde guardar el trabajo

- Guarda tus proyectos **dentro de Ubuntu** (por ejemplo, en `~/dam`), no en `/mnt/c/...`: es mucho más rápido.
- Para ver esos archivos desde Windows (para entregarlos, por ejemplo), en el Explorador de archivos escribe `\\wsl$` y entra en `Ubuntu-24.04` → `home` → tu usuario.
- Para copiar una plantilla de Windows a Ubuntu: `cp /mnt/c/Users/<tu-usuario>/Downloads/<archivo>.zip ~/dam/` y después `unzip`.

### Si no puedes instalar

- **«WSL 2 requiere una actualización del kernel» o error de virtualización:** comprueba la virtualización (ver *Antes de empezar*) y ejecuta `wsl --update` en PowerShell como administrador.
- **WSL no arranca y dice que falta una característica de Windows** (por ejemplo, «Plataforma de máquina virtual»): `wsl --install` las activa solo, pero a veces hay que hacerlo a mano. Busca en el menú Inicio **«Activar o desactivar las características de Windows»**, marca **Plataforma de máquina virtual** y **Subsistema de Windows para Linux**, pulsa *Aceptar* y **reinicia**. No hace falta marcar Hyper-V.
- **Sin permisos de administrador:** trabaja en pareja o en un equipo del aula y avisa al docente.
- **No hay tiempo para instalarlo esta semana:** el proyecto de cada módulo se puede hacer también desde Windows, como indica su apartado. WSL se usará cada vez más en las próximas semanas.

## 2º DAM · DI

Proyecto «Mejora tu BugTracker»: continúa la Práctica 6, la aplicación de escritorio con PySide6, Qt Designer y SQLite.

**Esta semana, en Windows:** la aplicación tiene ventanas (PySide6 y Qt Designer) y funciona mejor con el Python de Windows. WSL ([base común](#base-común-wsl2-con-ubuntu-java-y-python)) sirve para scripts y pruebas de consola.

| Programa | Para qué | Ocupa |
|---|---|---|
| **Python 3.11 o superior** (64 bits; probado con 3.11 y 3.12) | Ejecutar la aplicación | unos 100 MB |
| **Visual Studio Code** con la extensión **Python** de Microsoft | Escribir y ejecutar el código | unos 400 MB |
| **PySide6-Essentials** (PySide6 sin los módulos que no usamos; trae Qt Designer y `pyside6-uic`), **pytest** y **pytest-qt** | Interfaz gráfica, diseño visual y pruebas | unos 250 MB, dentro del entorno virtual del proyecto |
| **diagrams.net** (web) | Boceto del Paso 1 (también vale en papel) | no se instala: app.diagrams.net |
| **WebAIM Contrast Checker** (web) | Comprobar el contraste en el Paso 1 | no se instala: webaim.org/resources/contrastchecker |
| **SQLite** | Base de datos | ya viene con Python |

### Python y Visual Studio Code

1. Python: **python.org/downloads** → Windows, instalador de 64 bits de la versión 3.11 o superior (si instalas la más reciente y PySide6 no se instala, usa la 3.12). En la primera pantalla marca **Add python.exe to PATH**.
2. Visual Studio Code: **code.visualstudio.com**. Después, en la barra lateral de *Extensiones* (`Ctrl + Mayús + X`), instala **Python** (de Microsoft).
3. **Comprueba que**, en una terminal nueva, `python --version` (o `py --version`) muestra 3.11 o superior.

### PySide6, pytest y pytest-qt (en un entorno virtual)

Cada proyecto tiene su propio **entorno virtual** (`.venv`): una carpeta con sus librerías, para no mezclar versiones entre proyectos. Es el Paso 0 del proyecto:

1. Prepara la carpeta de trabajo en una **ruta corta y fuera de OneDrive**, por ejemplo `C:\dam\di\` (el entorno virtual tiene archivos con rutas muy largas y, dentro de OneDrive o del Escritorio, la instalación puede fallar), y ábrela en VS Code (*Archivo → Abrir carpeta*):
    - si tu BugTracker de la Práctica 6 funciona, haz una copia de `practica_06` (por ejemplo, `bugtracker_repaso`) y copia en ella los archivos de la plantilla que indica el proyecto;
    - si no, copia la carpeta `plantilla` de `clase` con el nombre `bugtracker_repaso`.
2. En la terminal de VS Code (PowerShell), dentro de esa carpeta:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`requirements.txt` viene en la plantilla e instala PySide6-Essentials 6.12, pytest y pytest-qt.

3. En VS Code, elige el intérprete del entorno: `Ctrl + Mayús + P` → *Python: Select Interpreter* → el que está dentro de `.venv`.
4. **Comprueba que:**
    - la línea de la terminal empieza por `(.venv)`;
    - `python -c "import PySide6; print(PySide6.__version__)"` muestra una versión;
    - `pyside6-designer` abre Qt Designer;
    - `python -m pytest -v` muestra en sus primeras líneas `plugins: qt-…` (es pytest-qt). Las pruebas fallan hasta el Paso 5 del proyecto: es lo esperado.

### Si no puedes instalar

- **«La ejecución de scripts está deshabilitada en este sistema»** al activar el entorno: ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activarlo. O usa la terminal *Command Prompt* y `.venv\Scripts\activate.bat`.
- **Qt Designer no abre:** aplica las mejoras desde `main.py`, después de `setupUi`, como explica el Paso 2 (por ejemplo, `self.ui.txtDescripcion.setTabChangesFocus(True)`).
- **`WinError 206` (nombre de archivo demasiado largo) al instalar:** la carpeta está en una ruta larga o en OneDrive. Bórrala, cópiala a `C:\dam\di\` y repite desde `python -m venv .venv`.
- **pytest-qt no se instala:** usa la prueba manual del Paso 6, que no necesita pytest.
- **Sin red:** haz el Paso 1 (evaluación heurística y de accesibilidad) en pareja con quien tenga el entorno instalado.

## Problemas frecuentes

| Problema | Qué hacer |
|---|---|
| Una orden (`java`, `python`, `winget`…) «no se reconoce» | Cierra y vuelve a abrir la terminal después de instalar. Si sigue, el programa no está en el PATH: reinstálalo marcando la opción de añadir al PATH. |
| El instalador pide permisos de administrador y no los tienes | Avisa al docente y trabaja en pareja o en un equipo del aula. |
| La descarga es muy lenta | Mientras descarga, haz la parte del proyecto que no lo necesita. |
| Te falta espacio en disco | Borra descargas que ya no necesites. |
