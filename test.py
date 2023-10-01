import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class SideWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button = QPushButton('Close Side Window', self)
        button.clicked.connect(self.close)
        layout.addWidget(button)
        self.setLayout(layout)
        self.setWindowTitle('Side Window')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Main Window')

        # إنشاء زر لفتح النافذة الجانبية
        side_button = QPushButton('Open Side Window', self)
        side_button.clicked.connect(self.openSideWindow)
        self.setCentralWidget(side_button)

    def openSideWindow(self):
        self.side_window = SideWindow()
        self.side_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
