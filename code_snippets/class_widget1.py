# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 16:21:51 2023

@author: Yevhen_Vieskov
"""

"""
Initialises Window, Sets out the geometry management, and adds Widgets
"""
#https://codereview.stackexchange.com/questions/259604/pyqt5-developing-complex-window-gui-and-making-everything-its-own-class
import sys

from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (
  QApplication, QGridLayout, QMainWindow, QTableWidgetItem, QWidget
)

from PyQt5.QtWidgets import (
  QComboBox, QFormLayout, QHBoxLayout, QVBoxLayout,
  QLabel, QPushButton, QTabWidget, QTableWidget, QWidget, QLineEdit
)


class Window(QMainWindow):
    """Create an instance of Window. Sets up main Window"""
    # my_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1000, 800)
        self.centralWgt = QWidget()  # create central widget
        self.setCentralWidget(self.centralWgt)  # set central widget
        self.tabIn = InputTab()  # create input tab widget
        self.tabOut = OutputTab()  # create input tab widget
        self.windowLayout()  # set window layout

        # TODO: Move this and "test" to a class to keep Window minimal
        self.tabIn.tablet1.btnApply.clicked.connect(self.test)

    def test(self):
        """
        When tabIn tablet1 btnApply pressed, Do something in tabOut tablet1
        """
        self.tabOut.tablet1.textGreeting.setText("Hello")
        print("Here!")

    def windowLayout(self):
        """Handles the main windows layout"""
        self.layout = QGridLayout()
        self.centralWgt.setLayout(self.layout)
        self.layout.addWidget(self.tabIn, 0, 1)  # Add widgets to layout
        self.layout.addWidget(self.tabOut, 1, 1, 2, 1)  # Add widgets to layout
        # Handle window and widget resizing
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 1)


# TAB MANAGEMENT


class Tabs(QTabWidget):
    """Tabs master class"""
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()  # Initialise Tab Widget
        self.layout = QVBoxLayout()  # Define Tab Widget Layout
        self.setLayout(self.layout)  # Set Tab Widget Layout
        self.setStyleSheet('QTabBar { font-size: 12pt;}')  # Set tab title size


class InputTab(Tabs):
    """Creates and sets up the InputTab Class. Inherits from Tab Class"""
    def __init__(self):
        super().__init__()
        self.tablet1 = ItemTablet(QWidget())  # Initialise tablet
        self.tabs.addTab(self.tablet1, "Item Queries")  # Add tablet
        self.layout.addWidget(self.tabs)  # Add tablets to layout


class OutputTab(Tabs):
    """Creates and sets up the OutputTab Class. Inherits from Tab Class"""
    def __init__(self):
        super().__init__()
        self.tablet1 = TableTablet(QWidget())  # Initialise tablet
        self.tabs.addTab(self.tablet1, "Output - Item Table")  # Add tablet
        self.layout.addWidget(self.tabs)  # Add tablets to layout


# TABLET MANAGEMENT #


class Tablets(QTableWidget):
    """The Tablets master class. Contains shared methods, variables"""
    def __init__(self, widget):
        super().__init__()
        self.widget = widget  # set tablet widget as given widget type
        self.layout = QVBoxLayout()  # create tablet outer layout
        self.setLayout(self.layout)  # set tablet outer layout
        self.setStyleSheet('font-size: 10pt;')  # Set tablet font size

    def populateForm(self, formFields):
        """Populates a form layout with dict key value pairs"""
        for k, v in formFields.items():
            self.frmLayout.addRow(k, v)  # Add items to tablet form layout

    def stdButtons(self):
        """Adds Apply and Clear buttons to bottom of tablet."""
        self.btnApply = QPushButton(text="Apply")
        self.btnClear = QPushButton(text="Clear")
        self.btnLayout.addWidget(self.btnApply)
        self.btnLayout.addWidget(self.btnClear)

    def stdFormLayout(self):
        """Creates a Form with horizontal buttons at bottom"""
        self.frmLayout = QFormLayout()  # create tablet sublayout
        self.btnLayout = QHBoxLayout()  # create tablet sublayout
        self.layout.addLayout(self.frmLayout)  # set tablet sublayout
        self.layout.addLayout(self.btnLayout)  # set tablet sublayout


class ItemTablet(Tablets):
    """Handles Item Tablet"""
    def __init__(self, widget):
        super().__init__(widget)
        self.stdFormLayout()  # choose stdFormLayout as a sublayout
        self.stdButtons()  # add stdButtons to sublayout
        # create form items
        self.lblItems = QLabel("Item name")
        self.cmbItems = QComboBox()
        self.cmbItems.addItems(["1", "2", "3"])

        # add form items to dict to setup widget associations
        self.formFields = {
            self.lblItems: self.cmbItems,
        }
        self.populateForm(self.formFields)  # add items to form layout


class TableTablet(Tablets, QTableWidget):
    """Handles the output table tablet"""
    def __init__(self, widget):
        super().__init__(widget)
        self.style = "::section{Background-color:lightgray;border-radius:9px;}"
        self.header = self.horizontalHeader()
        self.header.setStyleSheet(self.style)
        self.textGreeting = QLineEdit()
        self.layout.addWidget(self.textGreeting)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec_())