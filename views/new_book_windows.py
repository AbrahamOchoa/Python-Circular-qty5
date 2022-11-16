# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_book_windows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class newbookwindows(object):
    def setupUi(self, newbookwindows):
        if not newbookwindows.objectName():
            newbookwindows.setObjectName(u"newbookwindows")
        newbookwindows.resize(400, 569)
        self.label = QLabel(newbookwindows)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 361, 31))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(newbookwindows)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 47, 13))
        self.Title_lineEdit = QLineEdit(newbookwindows)
        self.Title_lineEdit.setObjectName(u"Title_lineEdit")
        self.Title_lineEdit.setGeometry(QRect(20, 100, 361, 21))
        self.label_3 = QLabel(newbookwindows)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 130, 71, 16))
        self.CategorylineEdit = QLineEdit(newbookwindows)
        self.CategorylineEdit.setObjectName(u"CategorylineEdit")
        self.CategorylineEdit.setGeometry(QRect(20, 150, 231, 21))
        self.label_4 = QLabel(newbookwindows)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 180, 171, 21))
        self.pageQtySpinBox = QSpinBox(newbookwindows)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(20, 210, 101, 22))
        self.label_5 = QLabel(newbookwindows)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 250, 111, 21))
        self.filePathlineEdit = QLineEdit(newbookwindows)
        self.filePathlineEdit.setObjectName(u"filePathlineEdit")
        self.filePathlineEdit.setGeometry(QRect(20, 280, 231, 21))
        self.SelectfileButton = QPushButton(newbookwindows)
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
        self.label_6 = QLabel(newbookwindows)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 320, 151, 16))
        self.descripcionTextedit = QTextEdit(newbookwindows)
        self.descripcionTextedit.setObjectName(u"descripcionTextedit")
        self.descripcionTextedit.setGeometry(QRect(20, 350, 351, 151))
        self.addButton = QPushButton(newbookwindows)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(70, 510, 101, 41))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
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
        icon1.addFile(u"../assets/icon/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setFlat(True)
        self.CancelButton = QPushButton(newbookwindows)
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

        self.retranslateUi(newbookwindows)

        QMetaObject.connectSlotsByName(newbookwindows)
    # setupUi

    def retranslateUi(self, newbookwindows):
        newbookwindows.setWindowTitle(QCoreApplication.translate("newbookwindows", u"Nuevo Libro", None))
        self.label.setText(QCoreApplication.translate("newbookwindows", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Nuevo Libro</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("newbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Titulo</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("newbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Categoria</span></p><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("newbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Cantidad de paguinas </span><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("newbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Seleccionar libro</span></p></body></html>", None))
        self.SelectfileButton.setText("")
        self.label_6.setText(QCoreApplication.translate("newbookwindows", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Descripcion del libro</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("newbookwindows", u"Agregar", None))
        self.CancelButton.setText(QCoreApplication.translate("newbookwindows", u"Cancelar", None))
    # retranslateUi

