# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_masukkan(object):
    def setupUi(self, masukkan):
        masukkan.setObjectName("masukkan")
        masukkan.resize(494, 394)
        self.label = QtWidgets.QLabel(masukkan)
        self.label.setGeometry(QtCore.QRect(170, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.perhitungan = QtWidgets.QLineEdit(masukkan)
        self.perhitungan.setGeometry(QtCore.QRect(130, 70, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.perhitungan.setFont(font)
        self.perhitungan.setText("")
        self.perhitungan.setObjectName("perhitungan")
        self.ENTER = QtWidgets.QPushButton(masukkan)
        self.ENTER.setGeometry(QtCore.QRect(30, 230, 445, 61))
        self.ENTER.setObjectName("ENTER")
        self.ENTER_2 = QtWidgets.QPushButton(masukkan)
        self.ENTER_2.setGeometry(QtCore.QRect(30, 310, 445, 61))
        self.ENTER_2.setObjectName("ENTER_2")
        self.label_2 = QtWidgets.QLabel(masukkan)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(masukkan)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(masukkan)
        self.label_4.setGeometry(QtCore.QRect(130, 150, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setLineWidth(3)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(masukkan)
        QtCore.QMetaObject.connectSlotsByName(masukkan)

    def retranslateUi(self, masukkan):
        _translate = QtCore.QCoreApplication.translate
        masukkan.setWindowTitle(_translate("masukkan", "Form"))
        self.label.setText(_translate("masukkan", "CALCULAOTR V0.1"))
        self.ENTER.setText(_translate("masukkan", "ENTER"))
        self.ENTER_2.setText(_translate("masukkan", "DEl"))
        self.label_2.setText(_translate("masukkan", "INPUT =>"))
        self.label_3.setText(_translate("masukkan", "OUTPUT =>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    masukkan = QtWidgets.QWidget()
    ui = Ui_masukkan()
    ui.setupUi(masukkan)
    masukkan.show()
    sys.exit(app.exec_())
