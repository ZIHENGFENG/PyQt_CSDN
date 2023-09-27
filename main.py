from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from menu import Ui_MainWindow as menu_ui
from popup import Ui_MainWindow as pop_ui


class Pop(QMainWindow, pop_ui):

    def __init__(self):
        super(Pop, self).__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.push)

    def push(self):
        print("push")


class Menu(QMainWindow, menu_ui):

    def __init__(self):
        super(Menu, self).__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.push)

    def push(self):
        print("push")
        self.ui_pop = Pop()
        self.ui_pop.show()
        self.close()


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    MainWindow = Menu()
    MainWindow.show()
    sys.exit(app.exec_())
