"""Detector de gestos de la mano con la cámara, para usarlo en una ventana de Qt.

Usa el reconocedor de gestos de MediaPipe (MediaPipe Tasks), que ya viene entrenado y
reconoce siete gestos: puño (Closed_Fist), palma abierta (Open_Palm), dedo índice hacia
arriba (Pointing_Up), pulgar abajo (Thumb_Down), pulgar arriba (Thumb_Up), victoria
(Victory) y «te quiero» en lengua de signos (ILoveYou).

Interfaz:
    DetectorGestos(parent=None)
    iniciar() / detener()          enciende y apaga la cámara
    gestoDetectado(str)            señal: el nombre del gesto, una vez por gesto nuevo
    error(str)                     señal: no se pudo abrir la cámara o cargar el modelo

Prueba sin el BugTracker:  python gestos.py
"""
import time
import urllib.request
from pathlib import Path

import cv2
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision
from PySide6.QtCore import QObject, QTimer, Signal

MODELO = Path(__file__).with_name("gesture_recognizer.task")
URL_MODELO = ("https://storage.googleapis.com/mediapipe-models/gesture_recognizer/"
              "gesture_recognizer/float16/latest/gesture_recognizer.task")

NOMBRES = {"Closed_Fist": "puño", "Open_Palm": "palma abierta", "Pointing_Up": "índice arriba",
           "Thumb_Down": "pulgar abajo", "Thumb_Up": "pulgar arriba", "Victory": "victoria",
           "ILoveYou": "te quiero"}


def descargar_modelo():
    """Descarga el modelo de MediaPipe (unos 8 MB) la primera vez."""
    if not MODELO.exists():
        urllib.request.urlretrieve(URL_MODELO, MODELO)


class DetectorGestos(QObject):
    gestoDetectado = Signal(str)
    error = Signal(str)

    CONFIRMAR = 5          # fotogramas seguidos con el mismo gesto para darlo por bueno

    def __init__(self, parent=None, camara=0):
        super().__init__(parent)
        self._camara = camara
        self._captura = None
        self._reconocedor = None
        self._temporizador = QTimer(self)
        self._temporizador.timeout.connect(self._leer_fotograma)
        self._candidato, self._repeticiones, self._ultimo = None, 0, None
        self.fotograma = None          # la última imagen de la cámara (para mostrarla)

    def iniciar(self):
        try:
            descargar_modelo()
            opciones = vision.GestureRecognizerOptions(
                base_options=mp_python.BaseOptions(model_asset_path=str(MODELO)),
                running_mode=vision.RunningMode.VIDEO,
                num_hands=1,
            )
            self._reconocedor = vision.GestureRecognizer.create_from_options(opciones)
        except Exception as e:
            self.error.emit(f"No se ha podido cargar el modelo de gestos: {e}")
            return False
        self._captura = cv2.VideoCapture(self._camara)
        if not self._captura.isOpened():
            self.error.emit("No se ha podido abrir la cámara.")
            self.detener()
            return False
        self._inicio = time.monotonic()
        self._temporizador.start(66)       # unos 15 fotogramas por segundo
        return True

    def detener(self):
        self._temporizador.stop()
        if self._captura is not None:
            self._captura.release()
            self._captura = None
        if self._reconocedor is not None:
            self._reconocedor.close()
            self._reconocedor = None
        self._candidato, self._repeticiones, self._ultimo = None, 0, None

    def _leer_fotograma(self):
        ok, imagen = self._captura.read()
        if not ok:
            return
        imagen = cv2.flip(imagen, 1)                              # como un espejo
        self.fotograma = imagen
        rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)             # MediaPipe trabaja en RGB
        instante = int((time.monotonic() - self._inicio) * 1000)  # milisegundos, siempre creciente
        resultado = self._reconocedor.recognize_for_video(
            mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb), instante)
        gesto = None
        if resultado.gestures:
            mejor = resultado.gestures[0][0]                      # el gesto más probable de la mano
            if mejor.category_name != "None" and mejor.score > 0.6:
                gesto = mejor.category_name
        self._procesar(gesto)

    def _procesar(self, gesto):
        """Emite el gesto solo cuando se repite varios fotogramas y es distinto del anterior."""
        if gesto == self._candidato:
            self._repeticiones += 1
        else:
            self._candidato, self._repeticiones = gesto, 1
        if self._repeticiones == self.CONFIRMAR:
            if gesto is not None and gesto != self._ultimo:
                self.gestoDetectado.emit(gesto)
            self._ultimo = gesto


if __name__ == "__main__":
    # Prueba: una ventana con la imagen de la cámara y el último gesto reconocido.
    import sys
    from PySide6.QtGui import QImage, QPixmap
    from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

    app = QApplication(sys.argv)
    ventana = QWidget()
    ventana.setWindowTitle("Prueba de gestos · Esc para salir")
    imagen, texto = QLabel("Abriendo la cámara…"), QLabel("Gesto: —")
    texto.setStyleSheet("font-size: 20px")
    capa = QVBoxLayout(ventana)
    capa.addWidget(imagen)
    capa.addWidget(texto)

    detector = DetectorGestos(ventana)
    detector.gestoDetectado.connect(lambda g: texto.setText(f"Gesto: {NOMBRES.get(g, g)} ({g})"))
    detector.error.connect(lambda m: texto.setText(m))

    def pintar():
        if detector.fotograma is not None:
            f = cv2.cvtColor(detector.fotograma, cv2.COLOR_BGR2RGB)
            alto, ancho, _ = f.shape
            imagen.setPixmap(QPixmap.fromImage(QImage(f.data, ancho, alto, 3 * ancho, QImage.Format.Format_RGB888)))

    pintor = QTimer()
    pintor.timeout.connect(pintar)
    pintor.start(66)
    ventana.keyPressEvent = lambda e: ventana.close() if e.key() == 0x01000000 else None
    ventana.show()
    detector.iniciar()
    sys.exit(app.exec())
