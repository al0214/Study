import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

from PyQt5 import uic
form_class = uic.loadUiType("MyWindow.ui")[0]
# Qt Designer의 결과물인 mywindow.ui 파일은 파이썬 코드와 같은 디렉터리에 위치해야한다
# uic 모듈의 loadUiType() 메서드는 Qt Designer의 결과물인 mywindow.ui 파일을 읽어서 파이썬 클래스 코드를 만듭니다.

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        # super().__init__을 쓰는 이유는 모 클래스에 정의된 초기화자를 명시적으로 호출하기위해서 사용합니다.
        
        self.setupUi(self)
        # setupUi()는 form_class에 정의된 메서드로 Qt Designer에서 만든 클래스들을 초기화합니다.
        
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

# 설명
# Qt Designer를 사용하여 위젯을 생성하더라도 위젯의 이벤트를 처리할 수 있습니다. 
# 다만 Qt Designer에서 위젯의 이름을 확인하는 과정이 필요합니다.