from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
    QAction,
)

initWidth = 800
initHeigh = 600

'''def _createMenuBar(self):
    menuBar = self.menuBar()
    # File menu
    fileMenu = QMenu("&File", self)
    menuBar.addMenu(fileMenu)
    fileMenu.addAction(self.newAction)
    fileMenu.addAction(self.openAction)
    fileMenu.addAction(self.saveAction)
    fileMenu.addAction(self.exitAction)
    # Edit menu
    editMenu = menuBar.addMenu("&Edit")
    editMenu.addAction(self.copyAction)
    editMenu.addAction(self.pasteAction)
    editMenu.addAction(self.cutAction)
    # Find and Replace submenu in the Edit menu
    findMenu = editMenu.addMenu("Find and Replace")
    findMenu.addAction("Find...")
    findMenu.addAction("Replace...")

    # Help menu
    helpMenu = menuBar.addMenu("&Help")
    helpMenu.addAction(self.helpContentAction)
    helpMenu.addAction(self.aboutAction)
    menuBar.setNativeMenuBar(False)

    def _createActions(self):
        # Creating action using the first constructor
        self.newAction = QAction(self)
        self.newAction.setText("&New")
        # Adding help tips
        newTip = "Create a new file"
        self.newAction.setStatusTip(newTip)
        self.newAction.setToolTip(newTip)
        # Edit actions
        # Creating actions using the second constructor
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
'''
class packAction(QAction):
    pass

class  unpackSpecificFileAction(QAction):
    pass

class  testArchivesAction(QAction):
    pass

class  compareByContentAction(QAction):
    pass

class  associateWithAction(QAction):
    pass

class  internalAssociationAction(QAction):
    pass

class  propertiesAction(QAction):
    pass

class  calculateOccupiedSpaceAction(QAction):
    pass

class  multiRenameToolAction(QAction):
    pass

class  editCommentAction(QAction):
    pass

class  printAction(QAction):
    pass

class  splitFileAction(QAction):
    pass

class  combineFileAction(QAction):
    pass

class  encodeFileAction(QAction):
    pass

class  decodeFileAction(QAction):
    pass

class  createCheckSumAction(QAction):
    pass

class  verifyCheckSumAction(QAction):
    pass


class exitAction(QAction):

    def __init__(self, parent):
        super(exitAction, self).__init__(QIcon('exit.png'), '&Exit', parent)
        self.setShortcut('Ctrl+Q')
        self.setStatusTip('Exit application')
        self.triggered.connect(parent.quit)




# menu5.py

class MenuBar(QWidget):

    def __init__(self, parent):
        super(MenuBar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QMenuBar()
        self.menu_file = self.menu_bar.addMenu("&Files")
        self.menu_file_open = self.menu_file.addAction(packAction)
        self.menu_file_open = self.menu_file.addAction(unpackSpecificFileAction)
        self.menu_file_open = self.menu_file.addAction(testArchivesAction)
        self.menu_file_open = self.menu_file.addAction(compareByContentAction)
        self.menu_file_open = self.menu_file.addAction(associateWithAction)
        self.menu_file_open = self.menu_file.addAction(internalAssociationAction)
        self.menu_file_open = self.menu_file.addAction(propertiesAction)
        self.menu_file_open = self.menu_file.addAction(calculateOccupiedSpaceAction)
        self.menu_file_open = self.menu_file.addAction(multiRenameToolAction)
        self.menu_file_open = self.menu_file.addAction(editCommentAction)
        self.menu_file_open = self.menu_file.addAction(printAction)
        self.menu_file_open = self.menu_file.addAction(splitFileAction)
        self.menu_file_open = self.menu_file.addAction(combineFileAction)
        self.menu_file_open = self.menu_file.addAction(encodeFileAction)
        self.menu_file_open = self.menu_file.addAction(decodeFileAction)
        self.menu_file_open = self.menu_file.addAction(createCheckSumAction)
        self.menu_file_open = self.menu_file.addAction(verifyCheckSumAction)
        self.menu_file_open = self.menu_file.addAction(exitAction)

        self.menu_mark = self.menu_bar.addMenu("&Mark")
        self.menu_commands = self.menu_bar.addMenu("&Commands")
        self.menu_net = self.menu_bar.addMenu("&Net")
        self.menu_show = self.menu_bar.addMenu("&Show")
        self.menu_configuration = self.menu_bar.addMenu("&Configuration")
        self.menu_start = self.menu_bar.addMenu("&Start")

        self.layout.addWidget(self.menu_bar)
        self.setLayout(self.layout)


'''class StatusBar(QWidget):
    def __init__(self, parent):
        super(StatusBar, self).__init__()
        self.initUI()
        self.showMessage("showMessage: Hello world!")

    def initUI(self):
        self.label = QLabel("Status bar...")
        self.label.setFixedHeight(24)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.label.setStyleSheet("""
            background-color: #23272a;
            font-size: 12px;
            padding-left: 5px;
            color: white;
        """)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def showMessage(self, text):
        self.label.setText(text)
'''


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("pyCommander")
        self.resize(800, 600)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.title_bar = MenuBar(self)
        # self.status_bar = StatusBar(self)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.title_bar)
        self.centralWidget.setLayout(self.layout)

        """self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.title_bar)
        self.layout.addStretch(1)
        self.layout.addWidget(self.status_bar)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)"""

    """def initUI(self):
        hbox = QHBoxLayout(self)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter demo')
        self.show()
        """
