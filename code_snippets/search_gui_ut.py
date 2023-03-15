# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:44:03 2023

@author: Yevhen_Vieskov
"""

#https://doc.qt.io/qtforpython/overviews/qttestlib-tutorial1-example.html
#https://stackoverflow.com/questions/34045246/unittesting-pyqt-app
#https://stackoverflow.com/questions/1616228/pyqt-gui-testing
#https://johnnado.com/pyqt-qtest-example/          !!!!!!!
#https://doc.qt.io/qtforpython/overviews/qtest-overview.html
#https://github.com/jmcgeheeiv/pyqttestexample
#https://github.com/biolab/PyQtTester
#https://sharplydescribed.wordpress.com/2020/09/17/gui-qt5-testing-with-python-qsignalspy-qtest/  !!!!!

import sys
import unittest
from PyQt5.QtGui import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtTest import QTest, QSignalSpy
from PyQt5.QtCore import Qt
import search



def test_defaults(self):
   '''Test the GUI in its default state'''
   self.assertEqual(self.form.ui.tequilaScrollBar.value(), 8)
   self.assertEqual(self.form.ui.tripleSecSpinBox.value(), 4)
   self.assertEqual(self.form.ui.limeJuiceLineEdit.text(), "12.0")
   self.assertEqual(self.form.ui.iceHorizontalSlider.value(), 12)
   self.assertEqual(self.form.ui.speedButtonGroup.checkedButton().text(), "&Karate Chop")

   # Class is in the default state even without pressing OK
   self.assertEqual(self.form.jiggers, 36.0)
   self.assertEqual(self.form.speedName, "&Karate Chop")
 
   # Push OK with the left mouse button
   okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
   QTest.mouseClick(okWidget, Qt.LeftButton)
   self.assertEqual(self.form.jiggers, 36.0)
   self.assertEqual(self.form.speedName, "&Karate Chop")
   
   
def setFormToZero(self):
    '''Set all ingredients to zero in preparation for setting just one
     to a nonzero value.
     '''
     self.form.ui.tequilaScrollBar.setValue(0)
     self.form.ui.tripleSecSpinBox.setValue(0)
     self.form.ui.limeJuiceLineEdit.setText("0.0")
     self.form.ui.iceHorizontalSlider.setValue(0)
     
     
def test_tequilaScrollBar(self):
    '''Test the tequila scroll bar'''
    self.setFormToZero()
 
    # Test the maximum. This one goes to 11.
    self.form.ui.tequilaScrollBar.setValue(12)
    self.assertEqual(self.form.ui.tequilaScrollBar.value(), 11)

    # Test the minimum of zero.
    self.form.ui.tequilaScrollBar.setValue(-1)
    self.assertEqual(self.form.ui.tequilaScrollBar.value(), 0)

    self.form.ui.tequilaScrollBar.setValue(5)
 
    # Push OK with the left mouse button
    okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
    QTest.mouseClick(okWidget, Qt.LeftButton)
    self.assertEqual(self.form.jiggers, 5)
    
def test_tripleSecSpinBox(self):
    '''Test the triple sec spin box.
    Testing the minimum and maximum is left as an exercise for the reader.
    '''
    self.setFormToZero()
    self.form.ui.tripleSecSpinBox.setValue(2)

    # Push OK with the left mouse button
    okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
    QTest.mouseClick(okWidget, Qt.LeftButton)
    self.assertEqual(self.form.jiggers, 2)
    
def test_limeJuiceLineEdit(self):
    '''Test the lime juice line edit.
    Testing the minimum and maximum is left as an exercise for the reader.
    '''
    self.setFormToZero()
    # Clear and then type "3.5" into the lineEdit widget
    self.form.ui.limeJuiceLineEdit.clear()
    QTest.keyClicks(self.form.ui.limeJuiceLineEdit, "3.5")

    # Push OK with the left mouse button
    okWidget = self.form.ui.buttonBox.button(self.form.ui.buttonBox.Ok)
    QTest.mouseClick(okWidget, Qt.LeftButton)
    self.assertEqual(self.form.jiggers, 3.5)
    
def test_blenderSpeedButtons(self):
    '''Test the blender speed buttons'''
    self.form.ui.speedButton1.click()
    self.assertEqual(self.form.speedName, "&Mix")
    self.form.ui.speedButton2.click()
    self.assertEqual(self.form.speedName, "&Whip")
    self.form.ui.speedButton3.click()
    self.assertEqual(self.form.speedName, "&Puree")
    self.form.ui.speedButton4.click()
    self.assertEqual(self.form.speedName, "&Chop")
    self.form.ui.speedButton5.click()
    self.assertEqual(self.form.speedName, "&Karate Chop")
    self.form.ui.speedButton6.click()
    self.assertEqual(self.form.speedName, "&Beat")
    self.form.ui.speedButton7.click()
    self.assertEqual(self.form.speedName, "&Smash")
    self.form.ui.speedButton8.click()
    self.assertEqual(self.form.speedName, "&Liquefy")
    self.form.ui.speedButton9.click()
    self.assertEqual(self.form.speedName, "&Vaporize")    
    