# PyQt5 import
import sys
from PyQt5.QtWidgets import *
# QtWidgets 모듈에는 GUI 프로그래밍을 위한 여러 클래스가 이미 정의되어 있습니다.

 # QApplication 객체 생성
app = QApplication(sys.argv)  

# 라벨을 창에 입력      
label = QLabel("Hello")

# QLabel 클래스에 대한 객체를 생성하고 show() 메서드를 호출
label.show()

# 버튼을 창에 입력
btn = QPushButton("Btn")
btn.show()

# 이벤트 루프 호출
app.exec_()             


# 설명
# 이벤트 루프란?
# GUI 프로그램에서는 'X' 버튼을 누를 때까지 종료되지 않고 계속 실행되려면 for나 while가 같은 '루프'가 필요한데 그것을 명칭하는 것