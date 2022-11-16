# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_book_windows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class editbookwindows(object):
    def setupUi(self, editbookwindows):
        if not editbookwindows.objectName():
            editbookwindows.setObjectName(u"editbookwindows")
        editbookwindows.resize(400, 569)
        self.label = QLabel(editbookwindows)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 361, 31))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(editbookwindows)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 47, 13))
        self.Title_lineEdit = QLineEdit(editbookwindows)
        self.Title_lineEdit.setObjectName(u"Title_lineEdit")
        self.Title_lineEdit.setGeometry(QRect(20, 100, 361, 21))
        self.label_3 = QLabel(editbookwindows)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 130, 71, 16))
        self.CategorylineEdit = QLineEdit(editbookwindows)
        self.CategorylineEdit.setObjectName(u"CategorylineEdit")
        self.CategorylineEdit.setGeometry(QRect(20, 150, 231, 21))
        self.label_4 = QLabel(editbookwindows)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 171, 21))
        self.pageQtySpinBox = QSpinBox(editbookwindows)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(20, 210, 101, 22))
        self.label_5 = QLabel(editbookwindows)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 250, 111, 21))
        self.filePathlineEdit = QLineEdit(editbookwindows)
        self.filePathlineEdit.setObjectName(u"filePathlineEdit")
        self.filePathlineEdit.setGeometry(QRect(20, 280, 231, 21))
        self.SelectfileButton = QPushButton(editbookwindows)
        self.SelectfileButton.setObjectName(u"SelectfileButton")
        self.SelectfileButton.setGeometry(QRect(250, 280, 51, 31))
        self.SelectfileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SelectfileButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"    background-color: #bbdefb;\n"
"}\n"
"QPushButton:-moz-suppressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icon/buscar_2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SelectfileButton.setIcon(icon)
        self.SelectfileButton.setIconSize(QSize(30, 30))
        self.SelectfileButton.setFlat(True)
        self.label_6 = QLabel(editbookwindows)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 320, 151, 16))
        self.descripcionTextedit = QTextEdit(editbookwindows)
        self.descripcionTextedit.setObjectName(u"descripcionTextedit")
        self.descripcionTextedit.setGeometry(QRect(20, 350, 351, 151))
        self.editButton = QPushButton(editbookwindows)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(70, 510, 101, 41))
        self.editButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton.setStyleSheet(u"QPushButton\n"
"{\n"
"    height: 2em;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: #0069c0;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: #0069c0;\n"
"    color: white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icon/cuaderno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editButton.setIcon(icon1)
        self.editButton.setIconSize(QSize(30, 30))
        self.editButton.setFlat(True)
        self.CancelButton = QPushButton(editbookwindows)
        self.CancelButton.setObjectName(u"CancelButton")
        self.CancelButton.setGeometry(QRect(210, 510, 101, 41))
        self.CancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CancelButton.setStyleSheet(u"QPushButton\n"
"{\n"
"    height: 2em;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: grey;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: grey;\n"
"    color: white;\n"
"}")
        self.CancelButton.setIconSize(QSize(30, 30))
        self.CancelButton.setFlat(True)
        self.label_7 = QLabel(editbookwindows)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, 180, 191, 21))
        self.pageReadQtySpinBox_2 = QSpinBox(editbookwindows)
        self.pageReadQtySpinBox_2.setObjectName(u"pageReadQtySpinBox_2")
        self.pageReadQtySpinBox_2.setGeometry(QRect(200, 210, 101, 22))

        self.retranslateUi(editbookwindows)

        QMetaObject.connectSlotsByName(editbookwindows)
    # setupUi

    def retranslateUi(self, editbookwindows):
        editbookwindows.setWindowTitle(QCoreApplication.translate("editbookwindows", u"Editar Libro", None))
        self.label.setText(QCoreApplication.translate("editbookwindows", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Editar Libro</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("editbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Titulo</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("editbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Categoria</span></p><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("editbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de paguinas </span><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("editbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Seleccionar libro</span></p></body></html>", None))
        self.SelectfileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("editbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Descripcion del libro</span></p></body></html>", None))
        self.editButton.setText(QCoreApplication.translate("editbookwindows", u"Editar", None))
        self.CancelButton.setText(QCoreApplication.translate("editbookwindows", u"Cancelar", None))
        self.label_7.setText(QCoreApplication.translate("editbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de paguinas leidas</span></p><p><span style=\" font-size:10pt; font-weight:600;\"/><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
    # retranslateUi

