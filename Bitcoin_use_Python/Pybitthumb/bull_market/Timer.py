import sys
import pybithumb
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

tickers = ["BTC", "ETH", "BCH", "ETC"]
# bull.ui 파일 로드
form_class = uic.loadUiType("bull.ui")[0]

# form_class를 상속받아 MyWindow 클래스를 정의합니다.
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)
        
    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)
    
    def get_market_infos(self, ticker):
        df = pybithumb.get_oclcv(ticker)
        ma5 = df['close'].rolling(window = 5).mean()
        last_ma5 = ma5[-2]
        price = pybithumb.get_current_price(ticker)
        
        state = None
        if price > last_ma5:
            state = "상승장"
        else:
            state = "하락장"
        
        return price, last_ma5, state
        

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()