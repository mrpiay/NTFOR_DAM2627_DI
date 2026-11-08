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

    # La señal propia se declara en la CLASE, no dentro de __init__.
    busquedaCambiada = Signal(str)

    def __init__(self, etiqueta="&Buscar:", parent=None):
        super().__init__(parent)

        # TODO Paso 5 (composición): crea los widgets internos.
        #   - self._etiqueta: QLabel con el texto de «etiqueta»
        #   - self._caja: QLineEdit con placeholder y accessibleName
        #   - self._etiqueta.setBuddy(self._caja)   -> Alt+B lleva el foco a la caja
        #   - self._boton: QPushButton("Limpiar") con accessibleName y toolTip
        # y colócalos en un QHBoxLayout(self) con márgenes 0.

        # TODO Paso 5 (conexiones internas):
        #   - textChanged de la caja -> self._al_cambiar_texto
        #   - clicked del botón      -> self.limpiar

    def _al_cambiar_texto(self, texto):
        # TODO Paso 5: emite la señal propia con el texto.
        pass

    def limpiar(self):
        # TODO Paso 5: borra el texto de la caja y devuélvele el foco.
        pass

    # Propiedad «texto»: se lee y se escribe como un atributo (buscador.texto = "Ana").
    def _get_texto(self):
        # TODO Paso 5: devuelve el texto de la caja.
        raise NotImplementedError("TODO Paso 5: completa Buscador._get_texto")

    def _set_texto(self, valor):
        # TODO Paso 5: pon «valor» como texto de la caja.
        raise NotImplementedError("TODO Paso 5: completa Buscador._set_texto")

    texto = Property(str, _get_texto, _set_texto, notify=busquedaCambiada)
