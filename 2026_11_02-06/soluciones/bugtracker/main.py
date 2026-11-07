"""BugTracker: gestión de incidencias con SQLite.

Incluye: acciones con atajos, menú y barra de herramientas, diálogo con validación
y Model/View con proxy para ordenar.
Regla de separación: main.py nunca contiene SQL y bd.py nunca usa widgets de Qt.
"""
import sys
import sqlite3

from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QHeaderView, QMainWindow, QMessageBox

import bd
from dialogo import DialogoIncidencia
from ui_bugtracker import Ui_VentanaPrincipal


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        self.configurar_tabla()       # Model/View

        self.ui.btnAnadir.clicked.connect(self.anadir_incidencia)
        self.ui.btnModificar.clicked.connect(self.modificar_incidencia)
        self.ui.btnEliminar.clicked.connect(self.eliminar_incidencia)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_formulario)
        self.ui.tblIncidencias.selectionModel().selectionChanged.connect(self.cargar_seleccion)

        # Acciones (menú, barra de herramientas y atajos)
        self.ui.actionNueva.triggered.connect(self.nueva_incidencia)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        self.ui.actionEliminar.triggered.connect(self.eliminar_incidencia)
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.tblIncidencias.doubleClicked.connect(self.editar_incidencia)

        self.cargar_incidencias()
        self.actualizar_botones()

    # ------------------------------------------------------------------
    # Model/View
    # ------------------------------------------------------------------
    def configurar_tabla(self):
        self.modelo = QStandardItemModel(0, 5, self)
        self.modelo.setHorizontalHeaderLabels(["ID", "Título", "Tipo", "Prioridad", "Estado"])

        self.proxy = QSortFilterProxyModel(self)          # filtra y ordena sin tocar los datos
        self.proxy.setSourceModel(self.modelo)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.proxy.setFilterKeyColumn(-1)                 # busca en todas las columnas

        tabla = self.ui.tblIncidencias
        tabla.setModel(self.proxy)
        tabla.setColumnHidden(0, True)                    # después de setModel
        tabla.setSortingEnabled(True)
        tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        tabla.horizontalHeader().setSortIndicator(-1, Qt.SortOrder.AscendingOrder)   # sin orden hasta pulsar una cabecera

    def cargar_incidencias(self):
        try:
            incidencias = bd.obtener_incidencias()
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se han podido cargar las incidencias.")
            return

        self.modelo.removeRows(0, self.modelo.rowCount())
        for incidencia in incidencias:
            celdas = []
            for campo in ("id", "titulo", "tipo", "prioridad", "estado"):
                celda = QStandardItem(str(incidencia[campo]))
                celda.setEditable(False)
                celdas.append(celda)
            self.modelo.appendRow(celdas)
        self.ui.tblIncidencias.clearSelection()
        self.actualizar_botones()

    def id_seleccionado(self):
        """Devuelve el ID de la incidencia seleccionada o None si no hay selección."""
        filas = self.ui.tblIncidencias.selectionModel().selectedRows()
        if not filas:
            return None
        fila = self.proxy.mapToSource(filas[0]).row()     # de la vista (proxy) al modelo
        return int(self.modelo.item(fila, 0).text())      # nunca el número de fila

    def cargar_seleccion(self):
        id_incidencia = self.id_seleccionado()
        if id_incidencia is None:
            self.actualizar_botones()
            return
        try:
            incidencia = bd.obtener_incidencia(id_incidencia)
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido leer la incidencia.")
            return
        if incidencia is None:
            self.ui.tblIncidencias.clearSelection()
            self.actualizar_botones()
            return
        self.ui.txtTitulo.setText(incidencia["titulo"])
        self.ui.cmbTipo.setCurrentText(incidencia["tipo"])
        self.ui.cmbPrioridad.setCurrentText(incidencia["prioridad"])
        self.ui.cmbEstado.setCurrentText(incidencia["estado"])
        self.ui.txtDescripcion.setPlainText(incidencia["descripcion"] or "")
        self.actualizar_botones()

    # ------------------------------------------------------------------
    # Operaciones
    # ------------------------------------------------------------------
    def leer_formulario(self):
        return (self.ui.txtTitulo.text().strip(),
                self.ui.cmbTipo.currentText(),
                self.ui.cmbPrioridad.currentText(),
                self.ui.cmbEstado.currentText(),
                self.ui.txtDescripcion.toPlainText().strip())

    def anadir_incidencia(self):
        datos = self.leer_formulario()
        if not datos[0]:
            QMessageBox.warning(self, "Falta el título", "El título es obligatorio.")
            self.ui.txtTitulo.setFocus()
            return
        try:
            bd.insertar_incidencia(*datos)
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido guardar la incidencia.")
            return
        self.cargar_incidencias()
        self.limpiar_formulario()
        self.statusBar().showMessage("Incidencia añadida", 3000)

    def modificar_incidencia(self):
        id_incidencia = self.id_seleccionado()
        if id_incidencia is None:
            return
        datos = self.leer_formulario()
        if not datos[0]:
            QMessageBox.warning(self, "Falta el título", "El título es obligatorio.")
            self.ui.txtTitulo.setFocus()
            return
        try:
            bd.actualizar_incidencia(id_incidencia, *datos)
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido modificar la incidencia.")
            return
        self.cargar_incidencias()
        self.limpiar_formulario()
        self.statusBar().showMessage("Incidencia modificada", 3000)

    def eliminar_incidencia(self):
        id_incidencia = self.id_seleccionado()
        if id_incidencia is None:
            self.statusBar().showMessage("Selecciona primero una incidencia", 3000)
            return
        respuesta = QMessageBox.question(self, "Eliminar incidencia",
                                         "¿Seguro que quieres eliminar la incidencia seleccionada?")
        if respuesta != QMessageBox.StandardButton.Yes:
            return
        try:
            bd.eliminar_incidencia(id_incidencia)
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido eliminar la incidencia.")
            return
        self.cargar_incidencias()
        self.limpiar_formulario()
        self.statusBar().showMessage("Incidencia eliminada", 3000)

    def limpiar_formulario(self):
        self.ui.txtTitulo.clear()
        self.ui.txtDescripcion.clear()
        self.ui.cmbTipo.setCurrentIndex(0)
        self.ui.cmbPrioridad.setCurrentIndex(0)
        self.ui.cmbEstado.setCurrentIndex(0)
        self.ui.tblIncidencias.clearSelection()
        self.ui.txtTitulo.setFocus()
        self.actualizar_botones()

    def actualizar_botones(self):
        hay_seleccion = self.id_seleccionado() is not None
        self.ui.btnModificar.setEnabled(hay_seleccion)
        self.ui.btnEliminar.setEnabled(hay_seleccion)
        self.ui.actionEliminar.setEnabled(hay_seleccion)

    # ------------------------------------------------------------------
    # Acciones y diálogo
    # ------------------------------------------------------------------
    def guardar(self):
        if self.id_seleccionado() is None:
            self.anadir_incidencia()
        else:
            self.modificar_incidencia()

    def nueva_incidencia(self):
        dialogo = DialogoIncidencia(self)
        if not dialogo.exec():                            # falso si se canceló
            return
        try:
            bd.insertar_incidencia(*dialogo.datos())
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido guardar la incidencia.")
            return
        self.cargar_incidencias()
        self.statusBar().showMessage(f"Incidencia «{dialogo.datos()[0]}» añadida", 3000)

    def editar_incidencia(self):
        """Doble clic en una fila: edita la incidencia en el diálogo."""
        id_incidencia = self.id_seleccionado()
        if id_incidencia is None:
            return
        try:
            incidencia = bd.obtener_incidencia(id_incidencia)
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido leer la incidencia.")
            return
        if incidencia is None:
            return
        dialogo = DialogoIncidencia(self, incidencia)
        if not dialogo.exec():
            return
        try:
            bd.actualizar_incidencia(id_incidencia, *dialogo.datos())
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se ha podido modificar la incidencia.")
            return
        self.cargar_incidencias()
        self.limpiar_formulario()
        self.statusBar().showMessage("Incidencia modificada", 3000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        bd.crear_bd()
    except sqlite3.Error:
        QMessageBox.critical(None, "Error", "No se ha podido preparar la base de datos.")
        sys.exit(1)

    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
