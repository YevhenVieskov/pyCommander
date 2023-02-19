#platform == linux, darwin, win32, cygwin 
from sys import platform
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter, QIcon, QKeySequence  
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
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
    QMenuBar,
    QToolBar,
    QLabel,
)

initWidth = 1024
initHeigh = 768

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

'''
button = QtWidgets.QPushButton("Закрыть окно", window)
button.setFixedSize(150, 30)
button.move(75, 20)
button.setToolTip("Это всплывающая подсказка для кнопки")
button.setToolTipDuration(3000)
window.setToolTip("Это всплывающая подсказка для окна")
button.setToolTipDuration(5000)
button.setWhatsThis("Это справка для кнопки")
window.setWhatsThis("Это справка для окна")
button.clicked.connect(QtWidgets.qApp.quit)
'''

#paths to icons 
#File
change_attributes_icon = 'pyCommander/icons/menu/file/change_attributes.png'
pack_icon = 'pyCommander/icons/menu/file/pack.png'
unpack_specific_file_icon = 'pyCommander/icons/menu/file/unpack_specific_file.png'
test_archives_icon = 'pyCommander/icons/menu/file/test_archives.png'
compare_by_content_icon = 'pyCommander/icons/menu/file/compare_by_content.png'
associate_with_icon = ''
internal_association_icon = ''  
properties_icon = ''
calculate_occupied_space_icon = ''
multi_rename_tool_icon = 'pyCommander/icons/menu/file/multy_rename_tool.png'
edit_comment_icon = ''
print_file_icon = ''
split_file_icon = 'pyCommander/icons/menu/file/split_file.png'
combine_file_icon = 'pyCommander/icons/menu/file/combine_file.png'
encode_file_icon = 'pyCommander/icons/menu/file/encode_file.png'
decode_file_icon = 'pyCommander/icons/menu/file/decode_file.png'
create_check_sum_icon = ''
verify_check_sum_icon = 'pyCommander/icons/menu/file/verify_checksum.png'
exit_program_icon = ''
print_file_list_icon ='pyCommander/icons/menu/file/file_list.png'

#menuitemstext
#File
change_attributes_text = '&Change Attributes' 
pack_text = '&Pack...'
unpack_specific_file_text = '&Unpack Specific Files...'
test_archives_text = '&Test Archive(s)'
compare_by_content_text = '&Compare By Content'
associate_with_text = '&Associate with...'
internal_association_text = '&Internal Associations (pyCommander only)...'    
properties_text = '&Properties'
calculate_occupied_space_text = '&Calculate Occupied Space...'
multi_rename_tool_text = '&Multi-Rename Tool...'
edit_comment_text = '&Edit Comment...'
print_file_text = '&Print'
split_file_text = '&Split File...'
combine_file_text = '&Combine File...'
encode_file_text = '&Encode File (MIME,UU,XXE)...'
decode_file_text = '&Decode File (MIME,UU,XXE,BinHex)...'
create_check_sum_text = '&Create Checksum Files (CR32,MD5,SHA1)'
verify_check_sum_text = '&Verify Checksums (from checksum files)'
exit_program_text = '&Exit'
print_file_list_text = '&File list...'
print_file_list_with_subdir_text = '&File list with subdir...'
print_file_contents_text = '&File contents...'

#menu items shortcuts
#File
change_attributes_shortcut = ''
pack_shortcut = 'Alt+F5'
unpack_specific_file_shortcut = 'Alt+F9'
test_archives_shortcut = 'Alt+Shift+F9'
compare_by_content_shortcut = ''
associate_with_shortcut = ''
internal_association_shortcut = ''    
properties_shortcut = 'Alt+Enter'
calculate_occupied_space_shortcut = 'Ctrl+L'
multi_rename_tool_shortcut = 'Ctrl+M'
edit_comment_shortcut = 'Ctrl+Z'
print_file_shortcut = ''
split_file_shortcut = ''
combine_file_shortcut = ''
encode_file_shortcut = ''
decode_file_shortcut = ''
create_check_sum_shortcut = ''
verify_check_sum_shortcut = ''
exit_program_shortcut = 'Alt+F4'

#trigger functionsy
#File
def change_attributes():
    pass
def pack():
    pass
def unpack_specific_file():
    pass
def test_archives():
    pass
def compare_by_content():
    pass
def associate_with():
    pass
def internal_association():
    pass
def properties():
    pass
def calculate_occupied_space():
    pass
def multi_rename_tool():
    pass
def edit_comment():
    pass
def print_file():
    pass
def split_file():
    pass
def combine_file():
    pass
def encode_file():
    pass
def decode_file():
    pass
def create_check_sum():
    pass
def verify_check_sum():
    pass
def exit_program():
    pass

#action classes
class customAction(QAction):    
        
        def __init__(self, iname, name, scut, parent):
            icon = QIcon(iname)            
            super(customAction, self).__init__(icon, name, parent)
            self.setShortcut(scut)
            self.setStatusTip(name)
            self.triggered.connect(change_attributes)

class FileManagerActions:
    pass


'''class exitAction(QAction):

    def __init__(self, parent):
        super(exitAction, self).__init__(QIcon('exit.png'), '&Exit', parent)
        self.setShortcut('Ctrl+Q')
        self.setStatusTip('Exit application')
        self.triggered.connect(parent.quit)
'''


class ButtomToolbar(QWidget):

    def __init__(self, parent):
        super(ButtomToolbar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        #self._createActions()
        #self.menu_bar = QMenuBar()
        #self.menu_file = self.menu_bar.addMenu("&Files")
        # Create a QHBoxLayout instance
        layout = QHBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"), 1)
        layout.addWidget(QPushButton("Right-Most"), 2)
        # Set the layout on the application's window
        self.setLayout(layout)



class MenuBar(QWidget):

    def __init__(self, parent):
        super(MenuBar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        #self._createActions()
        self.menu_bar = QMenuBar()
        self.menu_file = self.menu_bar.addMenu("&Files")
        
        #to fuction _createActions 
        
                
        
        self.change_attributes_action = \
            customAction(change_attributes_icon, change_attributes_text,
                         change_attributes_shortcut , self)       
        self.pack_action = \
            customAction(pack_icon, pack_text,
                         pack_shortcut , self) 
        self.unpack_specific_file_action = \
            customAction(unpack_specific_file_icon, unpack_specific_file_text,
                         unpack_specific_file_shortcut , self) 
        self.test_archives_action = \
            customAction(test_archives_icon, test_archives_text,
                         test_archives_shortcut , self)
        self.compare_by_content_action  = \
            customAction(compare_by_content_icon, compare_by_content_text,
                         compare_by_content_shortcut , self)
        self.associate_with_action = \
            customAction(associate_with_icon, associate_with_text,
                         associate_with_shortcut , self)
        self.internal_association_action = \
            customAction(internal_association_icon, internal_association_text,
                         internal_association_shortcut , self)
        self.properties_action  = \
            customAction(properties_icon, properties_text,
                         properties_shortcut , self)
        self.calculate_occupied_space_action = \
            customAction(calculate_occupied_space_icon, calculate_occupied_space_text,
                         calculate_occupied_space_shortcut , self)
        self.multi_rename_tool_action = \
            customAction(multi_rename_tool_icon, multi_rename_tool_text,
                         multi_rename_tool_shortcut , self)
        self.edit_comment_action = \
            customAction(edit_comment_icon, edit_comment_text,
                         edit_comment_shortcut , self)
        self.print_file_action = \
            customAction(print_file_icon, print_file_text,
                         print_file_shortcut , self)
        self.split_file_action = \
            customAction(split_file_icon, split_file_text,
                         split_file_shortcut , self)
        self.combine_file_action = \
            customAction(combine_file_icon, combine_file_text,
                         combine_file_shortcut , self)
        self.encode_file_action  = \
            customAction(encode_file_icon, encode_file_text,
                         encode_file_shortcut , self)
        self.decode_file_action  =  \
            customAction(decode_file_icon, decode_file_text,
                         decode_file_shortcut , self)
        self.create_check_sum_action  = \
            customAction(create_check_sum_icon, create_check_sum_text,
                         create_check_sum_shortcut , self)
        self.verify_check_sum_action  = \
            customAction(verify_check_sum_icon, verify_check_sum_text,
                         verify_check_sum_shortcut , self)
        #self.exit_action = exitAction(self)
      
        self.menu_file_change_attributes = self.menu_file.addAction(self.change_attributes_action)
        self.menu_file_pack = self.menu_file.addAction(self.pack_action)
        self.menu_file_unpack_specific_file = self.menu_file.addAction(self.unpack_specific_file_action)
        self.menu_file_test_archives = self.menu_file.addAction(self.test_archives_action)
        self.menu_file_associate_with = self.menu_file.addAction(self.associate_with_action)
        self.menu_file_internal_association = self.menu_file.addAction(self.internal_association_action)
        self.menu_file_properties = self.menu_file.addAction(self.properties_action)
        self.menu_file_calculate_occupied_space = self.menu_file.addAction(self.calculate_occupied_space_action)
        self.menu_file_multi_rename_tool = self.menu_file.addAction(self.multi_rename_tool_action)
        self.menu_file_edit_comment = self.menu_file.addAction(self.edit_comment_action)
        self.menu_file_print_file = self.menu_file.addAction(self.print_file_action)
        self.menu_file.addSeparator()
        self.menu_file_split_file = self.menu_file.addAction(self.split_file_action)
        self.menu_file_combine_file = self.menu_file.addAction(self.combine_file_action)
        self.menu_file_encode_file = self.menu_file.addAction(self.encode_file_action)
        self.menu_file_decode_file = self.menu_file.addAction(self.decode_file_action)
        self.menu_file_create_check_sum = self.menu_file.addAction(self.create_check_sum_action )
        self.menu_file_verify_check_sum = self.menu_file.addAction(self.verify_check_sum_action)
        #self.menu_file_exit_program = self.menu_file.addAction(self.exit_program_action)
        

        self.menu_mark = self.menu_bar.addMenu("&Mark")
        self.menu_commands = self.menu_bar.addMenu("&Commands")
        self.menu_net = self.menu_bar.addMenu("&Net")
        self.menu_show = self.menu_bar.addMenu("&Show")
        self.menu_configuration = self.menu_bar.addMenu("&Configuration")
        self.menu_start = self.menu_bar.addMenu("&Start")

        self.layout.addWidget(self.menu_bar)
        self.setLayout(self.layout)

    def _createActions(self):
        pass
        
        

class StatusBar(QWidget):
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

class MainToolBar(QWidget):

    def __init__(self, parent):
        super(MainToolBar, self).__init__()
        self.parent = parent
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        #self._createActions()
        self.main_toolbar = QToolBar('Main')  
        self.main_toolbar.setIconSize(QSize(30, 30))  
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.main_toolbar)
        
        


class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("pyCommander")
        self.resize(1024, 768)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.title_bar = MenuBar(self)
        self.status_bar = StatusBar(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title_bar)
        self.layout.addWidget(self.status_bar)
        self.centralWidget.setLayout(self.layout)

        '''self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.title_bar)
        self.layout.addStretch(1)
        self.layout.addWidget(self.status_bar)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)'''

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
