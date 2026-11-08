"""Diálogo modal «Nueva incidencia» / «Editar incidencia»."""
from PySide6.QtWidgets import (QComboBox, QDialog, QDialogButtonBox, QFormLayout,
                               QLineEdit, QMessageBox, QTextEdit)

TIPOS = ["Error", "Mejora", "Nueva funcionalidad"]
PRIORIDADES = ["Baja", "Media", "Alta", "Crítica"]
ESTADOS = ["Pendiente", "En proceso", "Resuelta"]


class DialogoIncidencia(QDialog):
    """Pide los datos de una incidencia. Si recibe «incidencia», sirve para editarla."""

    def __init__(self, parent=None, incidencia=None):
        super().__init__(parent)
        self.setWindowTitle("Editar incidencia" if incidencia else "Nueva incidencia")

        self.txtTitulo = QLineEdit()
        self.txtTitulo.setPlaceholderText("Título de la incidencia")
        self.cmbTipo = QComboBox()
        self.cmbTipo.addItems(TIPOS)
        self.cmbPrioridad = QComboBox()
        self.cmbPrioridad.addItems(PRIORIDADES)
        self.cmbEstado = QComboBox()
        self.cmbEstado.addItems(ESTADOS)
        self.txtDescripcion = QTextEdit()
        self.txtDescripcion.setPlaceholderText("Describe la incidencia...")
        self.txtDescripcion.setTabChangesFocus(True)   # Tab sale del campo en vez de escribir un tabulador

        formulario = QFormLayout(self)
        # addRow(texto, widget) crea la etiqueta y la une al campo (buddy): Alt+letra lleva al campo.
        formulario.addRow("&Título (obligatorio):", self.txtTitulo)
        formulario.addRow("T&ipo:", self.cmbTipo)
        formulario.addRow("&Prioridad:", self.cmbPrioridad)
        formulario.addRow("E&stado:", self.cmbEstado)
        formulario.addRow("&Descripción:", self.txtDescripcion)

        botones = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok
                                   | QDialogButtonBox.StandardButton.Cancel)
        botones.accepted.connect(self.validar)   # Aceptar: primero validamos
        botones.rejected.connect(self.reject)    # Cancelar: cerrar sin guardar
        formulario.addRow(botones)

        if incidencia:
            self.txtTitulo.setText(incidencia["titulo"])
            self.cmbTipo.setCurrentText(incidencia["tipo"])
            self.cmbPrioridad.setCurrentText(incidencia["prioridad"])
            self.cmbEstado.setCurrentText(incidencia["estado"])
            self.txtDescripcion.setPlainText(incidencia["descripcion"] or "")

    def validar(self):
        """Se llama al pulsar Aceptar. Solo cierra el diálogo si los datos son correctos."""
        titulo = self.datos()[0]
        if not titulo:
            QMessageBox.warning(self, "Falta el título",
                                "Escribe un título para la incidencia: es obligatorio.")
            self.txtTitulo.setFocus()
            return
        if len(titulo) > 100:
            QMessageBox.warning(self, "Título demasiado largo",
                                f"El título tiene {len(titulo)} caracteres. Acórtalo a 100 como máximo.")
            self.txtTitulo.setFocus()
            return
        self.accept()

    def datos(self):
        """Devuelve (titulo, tipo, prioridad, estado, descripcion)."""
        return (self.txtTitulo.text().strip(),
                self.cmbTipo.currentText(),
                self.cmbPrioridad.currentText(),
                self.cmbEstado.currentText(),
                self.txtDescripcion.toPlainText().strip())
