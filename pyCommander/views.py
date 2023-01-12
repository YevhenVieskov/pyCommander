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

class exitAction(QAction):

    def __init__(self,parent):
        super(exitAction, self).__init__(QIcon('exit.png'), '&Exit', parent)
        self.setShortcut('Ctrl+Q')
        self.setStatusTip('Exit application')
        self.triggered.connect(parent.quit)



#menu5.py

class TitleBar(QWidget):
    height = 35
    def __init__(self, parent):
        super(TitleBar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)



        self.menu_bar = QMenuBar()
        self.menu_bar.setStyleSheet("""
            color: #fff;
            background-color: #23272A;
            font-size: 14px;
            padding: 4px; 
        """)
        self.menu_file = self.menu_bar.addMenu('file')
        self.menu_file_open=self.menu_file.addAction('open')
        self.menu_file_save=self.menu_file.addAction('save')
        self.menu_file_saveas=self.menu_file.addAction('save as...')
        self.menu_file_quit=self.menu_file.addAction('exit')
        self.menu_file_quit.triggered.connect(qApp.quit)

        self.menu_work=self.menu_bar.addMenu('work')
        self.menu_analysis=self.menu_bar.addMenu('analysis')
        self.menu_edit=self.menu_bar.addMenu('edit')
        self.menu_window=self.menu_bar.addMenu('window')
        self.menu_help=self.menu_bar.addMenu('help')

        self.layout.addWidget(self.menu_bar)

        self.title = QLabel("Hello World!")
        self.title.setFixedHeight(self.height)
        self.layout.addWidget(self.title)
        self.title.setStyleSheet("""
            background-color: #23272a;  /* 23272a   #f00*/
            font-weight: bold;
            font-size: 16px;
            color: blue;
            padding-left: 170px;
        """)

        self.closeButton = QPushButton(' ')
        self.closeButton.clicked.connect(self.on_click_close)
        self.closeButton.setStyleSheet("""
            background-color: #DC143C;
            border-radius: 10px;
            height: {};
            width: {};
            margin-right: 3px;
            font-weight: bold;
            color: #000;
            font-family: "Webdings";
            qproperty-text: "r";
        """.format(self.height/1.7,self.height/1.7))

        self.maxButton = QPushButton(' ')
        self.maxButton.clicked.connect(self.on_click_maximize)
        self.maxButton.setStyleSheet("""
            background-color: #32CD32;
            border-radius: 10px;
            height: {};
            width: {};
            margin-right: 3px;
            font-weight: bold;
            color: #000;
            font-family: "Webdings";
            qproperty-text: "1";
        """.format(self.height/1.7,self.height/1.7))

        self.hideButton = QPushButton(' ')
        self.hideButton.clicked.connect(self.on_click_hide)
        self.hideButton.setStyleSheet("""
            background-color: #FFFF00;
            border-radius: 10px;
            height: {};
            width: {};
            margin-right: 3px;
            font-weight: bold;
            color: #000;
            font-family: "Webdings";
            qproperty-text: "0";
        """.format(self.height/1.7,self.height/1.7))

        self.layout.addWidget(self.hideButton)
        self.layout.addWidget(self.maxButton)
        self.layout.addWidget(self.closeButton)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False
        self.maximaze = False

    def resizeEvent(self, QResizeEvent):
        super(TitleBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.move(self.mapToGlobal(self.movement))
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def on_click_close(self):
        sys.exit()

    def on_click_maximize(self):
        self.maximaze = not self.maximaze
        if self.maximaze:    self.parent.setWindowState(Qt.WindowNoState)
        if not self.maximaze:
            self.parent.setWindowState(Qt.WindowMaximized)

    def on_click_hide(self):
        self.parent.showMinimized()


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
        self.title_bar = TitleBar(self)
        #self.status_bar = StatusBar(self)
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