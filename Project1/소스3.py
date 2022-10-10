import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainter
 
from vector import vector
from threading import Thread
import time
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
class CWidget(QWidget):
 
    def __init__(self):
        super().__init__()
        #위치벡터
        self.location = vector(self.width()/2, self.height()/2)
        #속도벡터
        self.velocity = vector()
        #가속도벡터
        self.acceleration = vector()
        #마우스 좌표
        self.pt = vector(self.width()/2, self.height()/2)
        self.d = 50
        self.r = self.d/2
 
        self.thread = Thread(target=self.threadFunc)
        self.bThread = False
 
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle('move')
        self.setMouseTracking(True)
        self.bThread = True
        self.thread.start()
        self.show()        
 
    def mouseMoveEvent(self, e):
        self.pt.x = e.x()
        self.pt.y = e.y()
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        rect = QRectF(self.location.x-self.r, self.location.y-self.r, self.d, self.d)
        qp.drawEllipse(rect)     
 
        self.showInfo(qp)
 
        qp.end()
 
    def showInfo(self, qp):
        pos = 'Position\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.location.x, self.location.y)
        mousepos = 'Mouse\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.pt.x, self.pt.y)
        velocity = 'Velocity\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.velocity.x, self.velocity.y)
        accel = 'Accel\t:X:{0:0.2f} Y:{1:0.2f}'.format(self.acceleration.x, self.acceleration.y)
        text = pos+'\n'+mousepos+'\n'+velocity+'\n'+accel
 
        qp.drawText(self.rect(), Qt.AlignLeft|Qt.AlignTop|Qt.TextExpandTabs, text)
 
    def threadFunc(self):
        while self.bThread:
 
            # 현재 위치에서 마우스를 향하는 벡터를 계산
            self.acceleration = self.pt - self.location
            # 벡터길이를 정규화(너무빠른 가속도때문)
            self.acceleration.normalize()
            # 적당한 벡터의 길이로 변경 (벡터곱)
            self.acceleration *= vector(0.5, 0.5)
 
            #가속도는 속도에 영향
            self.velocity += self.acceleration
            #최대 속도 제한
            self.velocity.setLimit(5)
            #속도는 위치에 영향
            self.location += self.velocity            
 
            #화면끝에 닿으면 튕기기
            if self.location.x+self.r > self.width() or self.location.x-self.r < 0:
                self.velocity.x *= -1
            if self.location.y+self.r > self.height() or self.location.y-self.r < 0:
                self.velocity.y *= -1
 
            self.update()
 
            time.sleep(0.01)
             
    def closeEvent(self, e):
        self.bThread = False
          
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())