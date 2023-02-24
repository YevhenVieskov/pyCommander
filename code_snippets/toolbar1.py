# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:54:24 2023

@author: Yevhen_Vieskov
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class ToolDemo(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ToolDemo, self).__init__(parent)
        self.setWindowTitle("toolbar demo")

        toolbarBox = QtWidgets.QToolBar(self)
        toolbarBox.setFixedWidth(180)

        self.addToolBar(QtCore.Qt.RightToolBarArea, toolbarBox)

        vscode_button = QtWidgets.QCheckBox(self, text="VSCode", checkable=True)
        ptt_button = QtWidgets.QCheckBox(self, text="Ppt", checkable=True)
        word_button = QtWidgets.QRadioButton(self, text="Word", checkable=True)
        excel_button = QtWidgets.QPushButton(self, text="Excel", checkable=True)
        other_button = QtWidgets.QToolButton(self, text="other", checkable=True)

        group = QtWidgets.QButtonGroup(self, exclusive=True)

        for button in (
            vscode_button,
            ptt_button,
            word_button,
            excel_button,
            other_button,
        ):
            toolbarBox.addWidget(button)
            group.addButton(button)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = ToolDemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()