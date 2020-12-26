import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QColor, QPainter
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.create_button.clicked.connect(self.create_circles)
        self.draw_flag = False

    def create_circles(self):
        self.draw_flag = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.draw_flag:
            self.draw(qp)
        qp.end()

    def draw(self, qp):
        for _ in range(randint(1, 10)):
            col = QColor('#FFFF00')
            qp.setPen(col)
            qp.setBrush(col)
            radius = randint(10, 100)
            qp.drawEllipse(randint(10, 500), randint(10, 500), radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
