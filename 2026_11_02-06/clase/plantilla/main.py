"""BugTracker: gestión de incidencias con SQLite (Práctica 6 terminada).

Plantilla de partida del proyecto de repaso. Funciona tal cual.
Los comentarios «TODO Paso N» marcan dónde cambiarás o añadirás código en cada paso.
Regla de separación: main.py nunca contiene SQL y bd.py nunca usa widgets de Qt.
"""
import sys
import sqlite3

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem

import bd
from ui_bugtracker import Ui_VentanaPrincipal
# TODO Paso 3: from dialogo import DialogoIncidencia
# TODO Paso 4: from PySide6.QtCore import QSortFilterProxyModel, Qt
#              from PySide6.QtGui import QStandardItem, QStandardItemModel
# TODO Paso 5: from buscador import Buscador


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)

        # TODO Paso 4: self.configurar_tabla()   (modelo + proxy + QTableView)
        # TODO Paso 5: self.configurar_buscador()

        self.ui.btnAnadir.clicked.connect(self.anadir_incidencia)
        self.ui.btnModificar.clicked.connect(self.modificar_incidencia)
        self.ui.btnEliminar.clicked.connect(self.eliminar_incidencia)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_formulario)
        # TODO Paso 4: con QTableView esta señal no existe. Se usa la del modelo de selección:
        #   self.ui.tblIncidencias.selectionModel().selectionChanged.connect(self.cargar_seleccion)
        self.ui.tblIncidencias.itemSelectionChanged.connect(self.cargar_seleccion)

        # TODO Paso 3: conecta las QAction que crees en Designer (señal «triggered»):
        #   actionNueva -> self.nueva_incidencia     actionGuardar -> self.guardar
        #   actionEliminar -> self.eliminar_incidencia   actionSalir -> self.close

        self.cargar_incidencias()
        self.actualizar_botones()

    # ------------------------------------------------------------------
    # Tabla
    # ------------------------------------------------------------------
    def cargar_incidencias(self):
        # TODO Paso 4: esta versión rellena el QTableWidget celda a celda.
        #   Cámbiala para que rellene self.modelo (QStandardItemModel) con appendRow.
        try:
            incidencias = bd.obtener_incidencias()
        except sqlite3.Error:
            QMessageBox.critical(self, "Error", "No se han podido cargar las incidencias.")
            return

        tabla = self.ui.tblIncidencias
        tabla.setRowCount(0)
        for incidencia in incidencias:
            fila = tabla.rowCount()
            tabla.insertRow(fila)
            tabla.setItem(fila, 0, QTableWidgetItem(str(incidencia["id"])))
            tabla.setItem(fila, 1, QTableWidgetItem(incidencia["titulo"]))
            tabla.setItem(fila, 2, QTableWidgetItem(incidencia["tipo"]))
            tabla.setItem(fila, 3, QTableWidgetItem(incidencia["prioridad"]))
            tabla.setItem(fila, 4, QTableWidgetItem(incidencia["estado"]))
        tabla.setColumnHidden(0, True)
        tabla.clearSelection()
        self.actualizar_botones()

    def id_seleccionado(self):
        """Devuelve el ID de la incidencia seleccionada o None si no hay selección."""
        # TODO Paso 4: con QTableView y proxy:
        #   filas = self.ui.tblIncidencias.selectionModel().selectedRows()
        #   fila = self.proxy.mapToSource(filas[0]).row()
        #   y lee el ID de la columna 0 de self.modelo.
        seleccion = self.ui.tblIncidencias.selectedItems()
        if not seleccion:
            return None
        fila = seleccion[0].row()
        return int(self.ui.tblIncidencias.item(fila, 0).text())   # nunca el número de fila

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
        # TODO Paso 3: activa o desactiva también self.ui.actionEliminar.

    # TODO Paso 3: añade aquí los slots de las acciones nuevas:
    #   guardar(): si hay una incidencia seleccionada, modificar_incidencia(); si no, anadir_incidencia().
    #   nueva_incidencia(): abre DialogoIncidencia(self); si exec() es verdadero,
    #   guarda dialogo.datos() con bd.insertar_incidencia(...), recarga y avisa en la barra de estado.

    # TODO Paso 5: configurar_buscador(): crea self.buscador, colócalo encima de la tabla
    #   y conecta busquedaCambiada con self.proxy.setFilterFixedString.


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
