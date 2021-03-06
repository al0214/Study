import sys
from time import struct_time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from anyio import current_time

import pykorbit

form_class = uic.loadUiType("myWindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)
        
    def inquiry(self):
        current_time = QTime.currentTime()
        string_time = current_time.toString("hh:mm:ss")
        self.statusBar().showMessage(string_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price)) 

        
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()