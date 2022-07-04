import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# bull.ui 파일 로드
form_class = uic.loadUiType("bull.ui")[0]

# form_class를 상속받아 MyWindow 클래스를 정의합니다.
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()