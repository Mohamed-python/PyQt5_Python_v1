
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setup_ui()
        self.start_timer()
    
    def setup_ui(self):
        self.label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        
    def start_timer(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)  # تحديد 1000 ميلي ثانية (1 ثانية) كفاصل زمني للإشارة
    
    def update_time(self):
        current_time = QTime.currentTime()
        time_text = current_time.toString('hh:mm:ss')
        self.label.setText(time_text)

if __name__ == '__main__':
    app = QApplication([])
    window1 = MyWindow()
    window1.show()
    
    window2 = MyWindow()
    window2.show()
    
    app.exec_()

