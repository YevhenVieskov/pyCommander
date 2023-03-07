# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:33:01 2023

@author: Yevhen_Vieskov
"""
#https://stackoverflow.com/questions/22844649/pyqt-how-to-set-combobox-read-only
class ComboBox(QtGui.QComboBox):
    def __init__(self, parent):
        QtGui.QComboBox.__init__(self, parent)
        self.readonly = False

    def mousePressEvent(self, event):
        if not self.readonly:
            QtGui.QComboBox.mousePressEvent(self, event)

    def keyPressEvent(self, event):
        if not self.readonly:
            QtGui.QComboBox.keyPressEvent(self, event)

    def wheelEvent(self, event):
        if not self.readonly():
            QtGui.QComboBox.wheelEvent(self, event)
            
#########################################################################            
class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)  
        self.combo = QtGui.QComboBox(self)
        self.combo.readonly = False
        self.combo.installEventFilter(self)
        ...

    def eventFilter(self, source, event):
        if (source is self.combo and self.combo.readonly and (
            event.type() == QtCore.QEvent.MouseButtonPress or
            event.type() == QtCore.QEvent.KeyPress or
            event.type() == QtCore.QEvent.Wheel)):
            return True
        return QtGui.QWidget.eventFilter(self, source, event)