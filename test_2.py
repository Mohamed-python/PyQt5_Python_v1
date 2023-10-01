
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtCore

#from ds import Ui_MainWindow
import sys
#from PyQt5 import QtCore, QtGui
#from PyQt5.QtCore import QSize,QDateTime
import sqlite3
from threading import Thread
import time

import datetime
import pygame
from PyQt5.QtGui import QFont
########################



class MainWindow(QMainWindow):
    def __init__(self,name):
        super(MainWindow, self).__init__()
        self.name = name
        self.tybe_pc = ""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        layout = QVBoxLayout()
        self.minutes = 1
        widgets = [
            #QCheckBox,
            QComboBox,
            #QDateEdit,
            #QDateTimeEdit,
            #QDial,
            #QDoubleSpinBox,
            #QFontComboBox,
            #QLCDNumber,
            #QLabel(f"[جهاز رقم: {name}]"),
            #QLineEdit,
            #QProgressBar,
            #QPushButton("Hi"),
            #QRadioButton,
            #QSlider,
            #QSpinBox,
            #QTimeEdit,
        ]

        color = """
                background-color:#5f6368;
                color:#fff;
                font-size:14px;
                """     
        


        Lb_name_pc = QLabel(f"[جهاز رقم: {self.name}]")
        Lb_name_pc.setStyleSheet(color)
        lb_start_time = QLabel(f"[وقت البدايه: ]")
        lb_tybe_pc = QLabel(f"نوع الجهاز: {self.tybe_pc}")
        self.lb_time_in = QLabel("الوقت المتبقي: ")
        self.lb_time_info = QLabel("الوقت المضاف:")



        lb_1 = QLabel("********************")
        bt_end = QPushButton("إنهاء")
        bt_end.clicked.connect(self.exit)
        bt_end.setStyleSheet(color)

        bt_add_food = QPushButton("أوردر")
        bt_add_food.clicked.connect(self.ADD)
        bt_add_food.setStyleSheet(color)

        self.bt_set_Time = QPushButton("إضافة وقت")
        self.bt_set_Time.clicked.connect(self.SET_TIME)
        self.bt_set_Time.setStyleSheet(color)

        ###########################
        

        #for w in widgets:
            #layout.addWidget(w)

        layout.addWidget(Lb_name_pc)
        layout.addWidget(lb_start_time)
        layout.addWidget(lb_tybe_pc)
        layout.addWidget(self.lb_time_in)
        layout.addWidget(self.lb_time_info)
        layout.addWidget(lb_1)

        layout.addWidget(self.bt_set_Time)
        layout.addWidget(bt_add_food)
        layout.addWidget(bt_end)
        




        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
        #self.update_timer()



        self.start_timer()
    def start_timer(self):
        try:
            #self.minutes = int(1)
            self.remaining_time = self.minutes * 60
            self.timer.start(1000)
        except ValueError:
            self.timer_label.setText("الرجاء إدخال رقم صحيح.")

    def update_timer(self):
        self.remaining_time -= 1
        self.format_time(self.remaining_time)
        #self.lb_time_in.setText(str(self.format_time(self.remaining_time)))
        self.lb_time_in.setText(f"الوقت المتبقي: {str(self.format_time(self.remaining_time))}")
        #print(str(self.format_time(self.remaining_time)))

        if self.remaining_time <= 0:
            self.timer.stop()
            self.lb_time_in.setText("انتهى الوقت!")

    def format_time(self, seconds):
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02}:{secs:02}"
    def exit(self): 
        color = """
        fdsgdsgds
        gsdgdsgds
        hgdsh
        hdshfds
        hhfdshfdshfdh: hfdhfd
        hdfhfdhfdhfd: hfdhfd
        """

        print("إنهاء")
        QMessageBox.information(self,"إنهاء الفاتوره", str(self.lb_time_info.text()))

    def ADD(self): 
        print("اضافه اكل")
        listt = ["hi","LOl","RR"]
        di = QInputDialog.getItem(self,"col","enter",listt,0,False)
        print(di[0])

    def SET_TIME(self): 
        print("اضافه وقت")
        ###
        #listt = ["hi","LOl","RR"]
        #di = QInputDialog.getInt(self,"col","enter",60,False)

        #layout2 = QVBoxLayout()
        #widget2 = QWidget()
        #lb_time_in = QLabel("إضافة وقت")
    
        di = QInputDialog.getInt(self,"col","enter",60,False)
        self.lb_time_info.setText(str(f"الوقت المضاف: {di[0]}"))
        
        #layout2.addWidget(lb_time_in)

        #widget2.setLayout(layout2)
        #x = self.setCentralWidget(widget2)

        

    
#"""
app = QtWidgets.QApplication(sys.argv)
window = MainWindow("hi")
window.show()
app.exec_()
#"""
