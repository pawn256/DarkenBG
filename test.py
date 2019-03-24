import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#import sip
 
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTransparentForInput | Qt.WindowStaysOnTopHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setAttribute(Qt.WA_TransparentForMouseEvents)
 
        self.setGeometry(0, 0, 5000,5000)
        self.setWindowTitle('QCheckBox')
        self.setWindowOpacity(0.8)
        p = self.palette()
        p.setColor(self.backgroundRole(),QColor("#000"))
        self.setPalette(p)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    #main_window.show()
    main_window.showFullScreen()
    sys.exit(app.exec_())
