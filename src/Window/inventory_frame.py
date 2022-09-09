from PyQt5 import QtCore, QtGui, QtWidgets

class inventory_management_ui(object):

    def setupUi(self, inventory_management):
        inventory_management.setObjectName("inventory_management")
        inventory_management.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(inventory_management)
        self.centralwidget.setObjectName("centralwidget")
        self.inventory_list = QtWidgets.QListWidget(self.centralwidget)
        self.inventory_list.setGeometry(QtCore.QRect(10, 10, 781, 501))
        self.inventory_list.setObjectName("inventory_list")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(10, 520, 381, 61))
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_button.setGeometry(QtCore.QRect(410, 520, 381, 61))
        self.remove_button.setObjectName("remove_button")
        inventory_management.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(inventory_management)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        inventory_management.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(inventory_management)
        self.statusbar.setObjectName("statusbar")
        inventory_management.setStatusBar(self.statusbar)

        self.retranslateUi(inventory_management)
        QtCore.QMetaObject.connectSlotsByName(inventory_management)

    def retranslateUi(self, inventory_management):
        _translate = QtCore.QCoreApplication.translate
        inventory_management.setWindowTitle(_translate("inventory_management", "MainWindow"))
        self.add_button.setText(_translate("inventory_management", "Ajouter"))
        self.remove_button.setText(_translate("inventory_management", "Supprimer"))
        self.edit_button.setText(_translate("inventory_management", "Editer"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventory_management = QtWidgets.QMainWindow()
    ui = inventory_management_ui()
    ui.setupUi(inventory_management)
    inventory_management.show()
    sys.exit(app.exec_())



