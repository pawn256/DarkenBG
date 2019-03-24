import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#import sip
 
class MainWindow(QWidget):
    def __init__(self, width=1024,height=720,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowTransparentForInput | Qt.WindowStaysOnTopHint | Qt.Tool)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setAttribute(Qt.WA_TransparentForMouseEvents)

        print width,height
        self.setGeometry(0, 0, width,height)
        self.setWindowTitle('QCheckBox')
        self.setWindowOpacity(0.8)
        p = self.palette()
        p.setColor(self.backgroundRole(),QColor("#000"))
        self.setPalette(p)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    desktop = app.desktop()
    width = desktop.width()
    height = desktop.height()
    main_window = MainWindow(width,height)
    #main_window.show()
    main_window.showFullScreen()
    sys.exit(app.exec_())
