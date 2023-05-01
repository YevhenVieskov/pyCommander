# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:48:20 2023

@author: Yevhen_Vieskov
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex

class FileSystemView(QWidget):
	def __init__(self, dir_path):
		super().__init__()
		appWidth = 800
		appHeight = 300
		self.setWindowTitle('File System Viewer')
		self.setGeometry(300, 300, appWidth, appHeight)
		
		self.model = QFileSystemModel()
		self.model.setRootPath(dir_path)
		self.tree =  QTreeView()
		self.tree.setModel(self.model)
		self.tree.setRootIndex(self.model.index(dirPath))
		self.tree.setColumnWidth(0, 250)        
		self.tree.setAlternatingRowColors(True)        
		layout = QVBoxLayout()
		layout.addWidget(self.tree)
		self.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	dirPath = r'C:'
	demo = FileSystemView(dirPath)
	demo.show()
	sys.exit(app.exec_())