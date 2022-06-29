# 설명
# 위젯에 정의된 이벤트를 시그널(signal)이라고 부르고 
# 이벤트가 발생할 때 호출되는 함수나 메서드를 슬롯(slot)이라고 부릅니다

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *

class MySignal(QObject):
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()