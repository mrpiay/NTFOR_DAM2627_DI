"""Componente reutilizable Buscador."""
from PySide6.QtCore import Property, Signal
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget


class Buscador(QWidget):
    """Campo de búsqueda reutilizable: etiqueta + caja de texto + botón «Limpiar».

    Propiedad:
        texto (str): texto que se está buscando. Valor por defecto: "".
    Señal:
        busquedaCambiada(str): se emite cada vez que cambia el texto.
    Método:
        limpiar(): borra el texto y devuelve el foco a la caja.

    Ejemplo:
        buscador = Buscador()
        buscador.busquedaCambiada.connect(lambda t: print("Buscando", t))
    """

    # 1) La señal propia se declara en la CLASE, no dentro de __init__.
    busquedaCambiada = Signal(str)

    def __init__(self, etiqueta="&Buscar:", parent=None):
        super().__init__(parent)

        # 2) Composición: el componente está hecho de otros widgets.
        self._etiqueta = QLabel(etiqueta)
        self._caja = QLineEdit()
        self._caja.setPlaceholderText("Escribe para filtrar")
        self._caja.setAccessibleName("Texto de búsqueda")
        self._etiqueta.setBuddy(self._caja)  # Alt+B lleva el foco a la caja

        self._boton = QPushButton("Limpiar")
        self._boton.setAccessibleName("Limpiar búsqueda")
        self._boton.setToolTip("Borra el texto de búsqueda")

        capa = QHBoxLayout(self)
        capa.setContentsMargins(0, 0, 0, 0)
        capa.addWidget(self._etiqueta)
        capa.addWidget(self._caja)
        capa.addWidget(self._boton)

        # 3) Conexiones internas.
        self._caja.textChanged.connect(self._al_cambiar_texto)
        self._boton.clicked.connect(self.limpiar)

    def _al_cambiar_texto(self, texto):
        self.busquedaCambiada.emit(texto)

    def limpiar(self):
        self._caja.clear()
        self._caja.setFocus()

    # 4) Propiedad «texto»: se lee y se escribe como un atributo.
    def _get_texto(self):
        return self._caja.text()

    def _set_texto(self, valor):
        self._caja.setText(valor)

    texto = Property(str, _get_texto, _set_texto, notify=busquedaCambiada)
