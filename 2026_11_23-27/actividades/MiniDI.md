# MiniDI · una ventana vacía

Con estas líneas, en este orden, se crea MiniDI: una aplicación de escritorio con PySide6 que abre una ventana vacía titulada «MiniDI», de 400 × 300 píxeles, y su ejecutable de dos formas, en una carpeta y en un solo archivo, que funciona en otro equipo sin tener Python instalado. Hay que usarlas todas, sabiendo dónde se escribe cada una (en la terminal o en qué archivo), para qué sirve y por qué va ahí.

**Qt** es un framework, escrito en C++, para crear aplicaciones con interfaz gráfica: ventanas, botones, campos de texto, tablas, menús y diálogos, además de módulos para bases de datos, red o multimedia. Es multiplataforma: el mismo código funciona en Windows, Linux y macOS.

**PySide6** es la forma oficial de usar Qt desde Python: da acceso a sus clases (`QApplication`, `QWidget`, `QPushButton`…) con la misma forma de trabajar. El 6 es la versión de Qt. **PySide6-Essentials** instala solo los módulos básicos (`QtCore`, `QtGui`, `QtWidgets`…), que son los que necesita MiniDI.

```
mkdir C:\dam2627\di\MiniDI
cd /d C:\dam2627\di\MiniDI
code .
PySide6-Essentials==6.12.*
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
from PySide6.QtWidgets import QWidget
class VentanaMini(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiniDI")
        self.resize(400, 300)
from PySide6.QtWidgets import QApplication
from ventana import VentanaMini
app = QApplication()
ventana = VentanaMini()
ventana.show()
app.exec()
python main.py
pip install pyinstaller
pyinstaller --windowed --name MiniDI-carpeta main.py
dist\MiniDI-carpeta\MiniDI-carpeta.exe
pyinstaller --onefile --windowed --name MiniDI-unico main.py
dist\MiniDI-unico.exe
```
