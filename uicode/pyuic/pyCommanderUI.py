from PyQt5 import QtWidgets
import sys, doublecommander

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = doublecommander.Ui_MainWindow()
ui.setupUi(window)
ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)
window.show()
sys.exit(aoo.exec_())