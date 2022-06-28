import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("MyWindow.ui")[0]
# Qt Designer의 결과물인 mywindow.ui 파일은 파이썬 코드와 같은 디렉터리에 위치해야한다

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__() # super().__init__을 쓰는 이유는 모 클래스에 정의된 초기화자를 명시적으로 호출하기위해서 사용합니다.
        self.setGeometry(100, 200, 300, 400)
     #  x축 위치, y축 위치, 윈도우의 너비, 윈도우의 높이
     
        self.setWindowTitle("PyQt")
     #  윈도우 타이틀바의 텍스트를 변경하는 메서드이다.
     
        self.setWindowIcon(QIcon("icon.png"))
    #   윈도우 타이틀바의 아이콘을 변경하는 메소드이다
        
        # 이벤트 처리 코드
        btn = QPushButton("버튼1", self)
        btn.move(10, 10)
        btn.clicked.connect(self.btn_clicked)
        # 프로그래머가 직접 메서드를 호출하는 것이 아니라 이벤트 루프가 메서드를 호출하기 때문에 '콜백 함수'라고 불린다.
        
        self.setupUi(self)

    def btn_clicked(self):
        print("버튼 클릭") 


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()