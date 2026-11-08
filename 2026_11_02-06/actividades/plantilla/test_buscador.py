"""Pruebas del componente Buscador con pytest-qt.

Ya están escritas: fallan hasta que completes buscador.py (paso 5).
Cuando salga «4 passed», el componente está terminado.
Ejecuta desde la carpeta del proyecto:  python -m pytest -v
"""
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit, QPushButton

from buscador import Buscador


def test_valor_por_defecto(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    assert buscador.texto == ""


def test_escribir_cambia_la_propiedad(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    caja = buscador.findChild(QLineEdit)
    assert caja is not None, "El Buscador no tiene caja de texto (QLineEdit) todavía"
    qtbot.keyClicks(caja, "Error")             # simula que alguien teclea
    assert buscador.texto == "Error"


def test_cambiar_texto_emite_la_senal(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    with qtbot.waitSignal(buscador.busquedaCambiada, timeout=1000) as espera:
        buscador.texto = "Pendiente"
    assert espera.args == ["Pendiente"]


def test_limpiar_borra_el_texto(qtbot):
    buscador = Buscador()
    qtbot.addWidget(buscador)
    buscador.show()
    buscador.texto = "Crítica"
    boton = buscador.findChild(QPushButton)
    assert boton is not None, "El Buscador no tiene botón «Limpiar» (QPushButton) todavía"
    with qtbot.waitSignal(buscador.busquedaCambiada, timeout=1000) as espera:
        qtbot.mouseClick(boton, Qt.MouseButton.LeftButton)
    assert buscador.texto == ""
    assert espera.args == [""]
