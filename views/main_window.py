# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(666, 568)
        self.TutoFrame = QFrame(Form)
        self.TutoFrame.setObjectName(u"TutoFrame")
        self.TutoFrame.setGeometry(QRect(10, 10, 631, 111))
        self.TutoFrame.setFrameShape(QFrame.StyledPanel)
        self.TutoFrame.setFrameShadow(QFrame.Raised)
        self.OpenBookBotton = QPushButton(self.TutoFrame)
        self.OpenBookBotton.setObjectName(u"OpenBookBotton")
        self.OpenBookBotton.setGeometry(QRect(10, 10, 81, 71))
        self.OpenBookBotton.setCursor(QCursor(Qt.UpArrowCursor))
        icon = QIcon()
        icon.addFile(u"../assets/icon/estudiar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenBookBotton.setIcon(icon)
        self.OpenBookBotton.setIconSize(QSize(50, 50))
        self.OpenBookBotton.setFlat(True)
        self.label = QLabel(self.TutoFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 80, 81, 16))
        self.OpenNew_botton = QPushButton(self.TutoFrame)
        self.OpenNew_botton.setObjectName(u"OpenNew_botton")
        self.OpenNew_botton.setGeometry(QRect(100, 10, 81, 71))
        self.OpenNew_botton.setCursor(QCursor(Qt.UpArrowCursor))
        icon1 = QIcon()
        icon1.addFile(u"../assets/icon/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenNew_botton.setIcon(icon1)
        self.OpenNew_botton.setIconSize(QSize(50, 50))
        self.OpenNew_botton.setFlat(True)
        self.label_2 = QLabel(self.TutoFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 80, 81, 16))
        self.Open_edit_button = QPushButton(self.TutoFrame)
        self.Open_edit_button.setObjectName(u"Open_edit_button")
        self.Open_edit_button.setGeometry(QRect(190, 10, 81, 71))
        self.Open_edit_button.setCursor(QCursor(Qt.UpArrowCursor))
        icon2 = QIcon()
        icon2.addFile(u"../assets/icon/cuaderno.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Open_edit_button.setIcon(icon2)
        self.Open_edit_button.setIconSize(QSize(50, 50))
        self.Open_edit_button.setFlat(True)
        self.label_3 = QLabel(self.TutoFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 80, 81, 16))
        self.label_4 = QLabel(self.TutoFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 80, 81, 16))
        self.Divi_book_Button = QPushButton(self.TutoFrame)
        self.Divi_book_Button.setObjectName(u"Divi_book_Button")
        self.Divi_book_Button.setGeometry(QRect(270, 10, 81, 71))
        self.Divi_book_Button.setCursor(QCursor(Qt.UpArrowCursor))
        icon3 = QIcon()
        icon3.addFile(u"../assets/icon/libro (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.Divi_book_Button.setIcon(icon3)
        self.Divi_book_Button.setIconSize(QSize(50, 50))
        self.Divi_book_Button.setFlat(True)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 130, 631, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 61, 21))
        self.SearchBcomboBox = QComboBox(self.frame)
        self.SearchBcomboBox.setObjectName(u"SearchBcomboBox")
        self.SearchBcomboBox.setGeometry(QRect(70, 30, 191, 22))
        self.parameterlineEdit = QLineEdit(self.frame)
        self.parameterlineEdit.setObjectName(u"parameterlineEdit")
        self.parameterlineEdit.setGeometry(QRect(270, 30, 113, 20))
        self.SearchButton = QPushButton(self.frame)
        self.SearchButton.setObjectName(u"SearchButton")
        self.SearchButton.setGeometry(QRect(390, 30, 101, 23))
        icon4 = QIcon()
        icon4.addFile(u"../assets/icon/buscar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SearchButton.setIcon(icon4)
        self.RefreshButton = QPushButton(self.frame)
        self.RefreshButton.setObjectName(u"RefreshButton")
        self.RefreshButton.setGeometry(QRect(490, 30, 101, 23))
        icon5 = QIcon()
        icon5.addFile(u"../assets/icon/sincronizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.RefreshButton.setIcon(icon5)
        self.ListButtonTable = QTableWidget(Form)
        self.ListButtonTable.setObjectName(u"ListButtonTable")
        self.ListButtonTable.setGeometry(QRect(10, 210, 631, 301))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 530, 141, 16))
        self.BooksQtyLabel = QLabel(Form)
        self.BooksQtyLabel.setObjectName(u"BooksQtyLabel")
        self.BooksQtyLabel.setGeometry(QRect(200, 530, 47, 13))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Book List", None))
        self.OpenBookBotton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Abrir Libro</span></p></body></html>", None))
        self.OpenNew_botton.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nuevo Libro</span></p></body></html>", None))
        self.Open_edit_button.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Edici\u00f3n Libro</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar Libro</span></p></body></html>", None))
        self.Divi_book_Button.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Bucar por:", None))
        self.SearchButton.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.RefreshButton.setText(QCoreApplication.translate("Form", u"Actualizar", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Cantidad de libros:</span></p></body></html>", None))
        self.BooksQtyLabel.setText(QCoreApplication.translate("Form", u"1", None))
    # retranslateUi
