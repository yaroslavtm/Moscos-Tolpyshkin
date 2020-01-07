import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui',self)
        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.update()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        a = random.randint(10, 250)
        self.qp.setPen(QColor(255, 255, 0))
        self.qp.drawEllipse(0, 0, a, a)
        self.qp.end()

app = QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())