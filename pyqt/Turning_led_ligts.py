"""
turn led
"""
import sys
import PyQt5

import sys
from PyQt4 import QtGui
from functools import partial


class Led(QtGui.QWidget):
    def __init__(self):
        super(Led, self).__init__()
        self.initUI()

    def initUI(self):
        btn = QtGui.QPushButton('Button', self)
        self.lbl = QtGui.QLabel(self)
        btn.resize(btn.sizeHint())
        btn.move(100, 250)
        btn.setStyleSheet("background-color: grey")
        btn.clicked.connect(partial(self.distext))

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()

    def distext(self):
        print("Button Pressed")
        self.lbl.setText("Pressed")
        self.lbl.move(50,100)
        self.lbl.resize(self.lbl.sizeHint())

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Led()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
