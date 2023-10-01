from PyQt5 import QtWidgets, uic

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Dialog(object):
    def __init__(self):
        super().__init__()



    def set(self):
        print(self.lineEdit.text())
    def setupUi(self, Dialog):
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)

        self.lineEdit.setGeometry(QtCore.QRect(102, 60, 191, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.set)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(98, 110, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.comboBox.setItemText(0, _translate("Dialog", "hi"))
        self.comboBox.setItemText(1, _translate("Dialog", "hi 2"))
        self.comboBox.setItemText(2, _translate("Dialog", "hi 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
