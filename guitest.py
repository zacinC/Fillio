import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import Qt


class FloatingButton(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Floating Button')
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 100, 100)

        button = QPushButton('Click Me', self)
        button.setGeometry(10, 10, 80, 80)
        button.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        print('Button clicked!')


# if __name__ == '__main__':
app = QApplication(sys.argv)
ex = FloatingButton()
ex.show()
sys.exit(app.exec_())
