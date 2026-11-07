# Software · DI · semana del 2 al 6 de noviembre

Lo que hace falta esta semana para el proyecto «Mejora tu BugTracker». Todo se instala en **Windows**.

| Programa | Para qué | Ocupa |
|---|---|---|
| **Python 3.12** (64 bits) | Ejecutar la aplicación | unos 100 MB |
| **Visual Studio Code** con la extensión **Python** de Microsoft | Escribir y ejecutar el código | unos 400 MB |
| **PySide6-Essentials** (trae Qt Designer y `pyside6-uic`), **pytest** y **pytest-qt** | La interfaz gráfica, el diseño visual y las pruebas | unos 250 MB, dentro del entorno virtual del proyecto |
| **SQLite** | La base de datos | Ya viene con Python |
| **diagrams.net** y **WebAIM Contrast Checker** (web) | El boceto y la comprobación del contraste del paso 1 | No se instalan: app.diagrams.net y webaim.org/resources/contrastchecker |

## Python y Visual Studio Code

1. Python: **python.org/downloads** → Windows, instalador de 64 bits de la versión 3.12. En la primera pantalla marca **Add python.exe to PATH**.
2. Visual Studio Code: **code.visualstudio.com**. Después, en *Extensiones* (`Ctrl + Mayús + X`), instala **Python** (de Microsoft).
3. **Comprueba que**, en una terminal nueva de PowerShell, `python --version` muestra 3.12.

PySide6, pytest y pytest-qt se instalan en el **entorno virtual** del proyecto (`.venv`) con su `requirements.txt`, en el paso 0 del proyecto.

## Si algo falla

| Qué pasa | Qué hacer |
|---|---|
| `python` no se reconoce | Cierra la terminal y abre una nueva. Si sigue, reinstala Python marcando **Add python.exe to PATH** |
| «La ejecución de scripts está deshabilitada en este sistema» al activar el entorno | Ejecuta una vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y vuelve a activarlo |
| `WinError 206` (nombre de archivo demasiado largo) al instalar | La carpeta está en una ruta larga o en OneDrive: cópiala a `C:\dam\di\` y repite desde `python -m venv .venv` |
