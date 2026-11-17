"""Diagnóstico de la cámara y de los paquetes de gestos.py.

Uso, en la carpeta del BugTracker:
    .venv\\Scripts\\python diagnostico_camara.py

Comprueba los paquetes instalados y el modelo de gestos, y prueba cada cámara (0 a 3)
con los dos sistemas de captura de Windows que usa OpenCV: MSMF (el de por defecto) y
DSHOW. De cada combinación dice si se abre, cuánto tarda, qué tamaño de imagen da y si
la imagen es negra.
"""
import platform
import sys
import time
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path


def paquete(nombre):
    try:
        return version(nombre)
    except PackageNotFoundError:
        return "NO INSTALADO"


print("== Programas")
print(f"Python      {platform.python_version()} ({sys.executable})")
for p in ("PySide6-Essentials", "mediapipe", "opencv-contrib-python", "opencv-python", "numpy"):
    print(f"{p:<22}{paquete(p)}")

print("\n== Modelo de gestos")
modelo = Path(__file__).with_name("gesture_recognizer.task")
if modelo.exists():
    print(f"gesture_recognizer.task: sí, {modelo.stat().st_size // 1024} KB")
else:
    print("gesture_recognizer.task: no está (se descarga al activar los gestos; hace falta Internet)")

try:
    import cv2
except ImportError as e:
    sys.exit(f"\nNo se puede importar OpenCV (cv2): {e}")

print("\n== Cámaras (puede tardar un poco: cada prueba abre y cierra la cámara)")
SISTEMAS = {"MSMF": cv2.CAP_MSMF, "DSHOW": cv2.CAP_DSHOW}
buenas = []
for indice in range(4):
    for nombre, api in SISTEMAS.items():
        t0 = time.monotonic()
        cap = cv2.VideoCapture(indice, api)
        abierta = cap.isOpened()
        t_abrir = time.monotonic() - t0
        if not abierta:
            print(f"cámara {indice} · {nombre:<5}: no se abre ({t_abrir:.1f} s)")
            cap.release()
            continue
        brillo, tam, leidos = 0.0, None, 0
        for _ in range(15):                     # las primeras imágenes suelen salir oscuras
            ok, img = cap.read()
            if ok and img is not None:
                leidos += 1
                tam = f"{img.shape[1]}x{img.shape[0]}"
                brillo = float(img.mean())
        cap.release()
        if leidos == 0:
            estado = "se abre, pero no da imágenes"
        elif brillo < 10:
            estado = f"imagen NEGRA (brillo {brillo:.0f} de 255)"
        else:
            estado = f"imagen correcta (brillo {brillo:.0f} de 255)"
            buenas.append((indice, nombre))
        print(f"cámara {indice} · {nombre:<5}: se abre en {t_abrir:.1f} s, {tam}, {estado}")

print("\n== Resultado")
if not buenas:
    print("Ninguna cámara da imagen. Revisa: el permiso de cámara para aplicaciones de escritorio,\n"
          "que no la esté usando otra aplicación (Teams, el navegador…), y la tapa o la tecla\n"
          "de la cámara del portátil.")
elif buenas[0] == (0, "MSMF"):
    print("La cámara 0 funciona como la usa gestos.py. Si en el BugTracker sigue negra,\n"
          "cierra las aplicaciones que puedan estar usando la cámara y vuelve a probar.")
else:
    indice, nombre = buenas[0]
    print(f"Funciona la cámara {indice} con {nombre}, pero no la 0 con MSMF, que es la que usa gestos.py.\n"
          f"En gestos.py, cambia la línea de cv2.VideoCapture por:\n"
          f"    self._captura = cv2.VideoCapture({indice}, cv2.CAP_{nombre})")
