# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bugtracker.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(760, 600)
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblTitulo)

        self.txtTitulo = QLineEdit(self.centralwidget)
        self.txtTitulo.setObjectName(u"txtTitulo")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtTitulo)

        self.lblTipo = QLabel(self.centralwidget)
        self.lblTipo.setObjectName(u"lblTipo")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblTipo)

        self.cmbTipo = QComboBox(self.centralwidget)
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.addItem("")
        self.cmbTipo.setObjectName(u"cmbTipo")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbTipo)

        self.lblPrioridad = QLabel(self.centralwidget)
        self.lblPrioridad.setObjectName(u"lblPrioridad")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblPrioridad)

        self.cmbPrioridad = QComboBox(self.centralwidget)
        self.cmbPrioridad.addItem("")
        self.cmbPrioridad.addItem("")
        self.cmbPrioridad.addItem("")
        self.cmbPrioridad.addItem("")
        self.cmbPrioridad.setObjectName(u"cmbPrioridad")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbPrioridad)

        self.lblEstado = QLabel(self.centralwidget)
        self.lblEstado.setObjectName(u"lblEstado")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblEstado)

        self.cmbEstado = QComboBox(self.centralwidget)
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.addItem("")
        self.cmbEstado.setObjectName(u"cmbEstado")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbEstado)

        self.lblDescripcion = QLabel(self.centralwidget)
        self.lblDescripcion.setObjectName(u"lblDescripcion")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.lblDescripcion)

        self.txtDescripcion = QTextEdit(self.centralwidget)
        self.txtDescripcion.setObjectName(u"txtDescripcion")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.txtDescripcion)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnAnadir = QPushButton(self.centralwidget)
        self.btnAnadir.setObjectName(u"btnAnadir")

        self.horizontalLayout.addWidget(self.btnAnadir)

        self.btnModificar = QPushButton(self.centralwidget)
        self.btnModificar.setObjectName(u"btnModificar")
        self.btnModificar.setEnabled(False)

        self.horizontalLayout.addWidget(self.btnModificar)

        self.btnEliminar = QPushButton(self.centralwidget)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setEnabled(False)

        self.horizontalLayout.addWidget(self.btnEliminar)

        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.horizontalLayout.addWidget(self.btnLimpiar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tblIncidencias = QTableWidget(self.centralwidget)
        if (self.tblIncidencias.columnCount() < 5):
            self.tblIncidencias.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblIncidencias.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblIncidencias.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblIncidencias.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblIncidencias.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblIncidencias.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblIncidencias.setObjectName(u"tblIncidencias")
        self.tblIncidencias.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblIncidencias.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblIncidencias.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout.addWidget(self.tblIncidencias)

        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VentanaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 760, 22))
        VentanaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txtTitulo, self.cmbTipo)
        QWidget.setTabOrder(self.cmbTipo, self.cmbPrioridad)
        QWidget.setTabOrder(self.cmbPrioridad, self.cmbEstado)
        QWidget.setTabOrder(self.cmbEstado, self.txtDescripcion)
        QWidget.setTabOrder(self.txtDescripcion, self.btnAnadir)
        QWidget.setTabOrder(self.btnAnadir, self.btnModificar)
        QWidget.setTabOrder(self.btnModificar, self.btnEliminar)
        QWidget.setTabOrder(self.btnEliminar, self.btnLimpiar)
        QWidget.setTabOrder(self.btnLimpiar, self.tblIncidencias)

        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"BugTracker", None))
        self.lblTitulo.setText(QCoreApplication.translate("VentanaPrincipal", u"T\u00edtulo:", None))
        self.txtTitulo.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"T\u00edtulo de la incidencia", None))
        self.lblTipo.setText(QCoreApplication.translate("VentanaPrincipal", u"Tipo:", None))
        self.cmbTipo.setItemText(0, QCoreApplication.translate("VentanaPrincipal", u"Error", None))
        self.cmbTipo.setItemText(1, QCoreApplication.translate("VentanaPrincipal", u"Mejora", None))
        self.cmbTipo.setItemText(2, QCoreApplication.translate("VentanaPrincipal", u"Nueva funcionalidad", None))

        self.lblPrioridad.setText(QCoreApplication.translate("VentanaPrincipal", u"Prioridad:", None))
        self.cmbPrioridad.setItemText(0, QCoreApplication.translate("VentanaPrincipal", u"Baja", None))
        self.cmbPrioridad.setItemText(1, QCoreApplication.translate("VentanaPrincipal", u"Media", None))
        self.cmbPrioridad.setItemText(2, QCoreApplication.translate("VentanaPrincipal", u"Alta", None))
        self.cmbPrioridad.setItemText(3, QCoreApplication.translate("VentanaPrincipal", u"Cr\u00edtica", None))

        self.lblEstado.setText(QCoreApplication.translate("VentanaPrincipal", u"Estado:", None))
        self.cmbEstado.setItemText(0, QCoreApplication.translate("VentanaPrincipal", u"Pendiente", None))
        self.cmbEstado.setItemText(1, QCoreApplication.translate("VentanaPrincipal", u"En proceso", None))
        self.cmbEstado.setItemText(2, QCoreApplication.translate("VentanaPrincipal", u"Resuelta", None))

        self.lblDescripcion.setText(QCoreApplication.translate("VentanaPrincipal", u"Descripci\u00f3n:", None))
        self.txtDescripcion.setPlaceholderText(QCoreApplication.translate("VentanaPrincipal", u"Describe la incidencia...", None))
        self.btnAnadir.setText(QCoreApplication.translate("VentanaPrincipal", u"A\u00f1adir", None))
        self.btnModificar.setText(QCoreApplication.translate("VentanaPrincipal", u"Modificar", None))
        self.btnEliminar.setText(QCoreApplication.translate("VentanaPrincipal", u"Eliminar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("VentanaPrincipal", u"Limpiar", None))
        ___qtablewidgetitem = self.tblIncidencias.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("VentanaPrincipal", u"ID", None))
        ___qtablewidgetitem1 = self.tblIncidencias.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("VentanaPrincipal", u"T\u00edtulo", None))
        ___qtablewidgetitem2 = self.tblIncidencias.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("VentanaPrincipal", u"Tipo", None))
        ___qtablewidgetitem3 = self.tblIncidencias.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("VentanaPrincipal", u"Prioridad", None))
        ___qtablewidgetitem4 = self.tblIncidencias.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("VentanaPrincipal", u"Estado", None))
    # retranslateUi

