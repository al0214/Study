import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() # super().__init__을 쓰는 이유는 모 클래스에 정의된 초기화자를 명시적으로 호출하기위해서 사용합니다.
        self.setGeometry(100, 200, 300, 400)
     #  x축 위치, y축 위치, 윈도우의 너비, 윈도우의 높이
     
        self.setWindowTitle("PyQt")
     #  윈도우 타이틀바의 텍스트를 변경하는 메서드이다.
     
        self.setWindowIcon(QIcon("icon.png"))
    #   윈도우 타이틀바의 아이콘을 변경하는 메소드이다

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()