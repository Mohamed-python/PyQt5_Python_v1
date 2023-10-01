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
import re
########################


class MainWindow(QMainWindow):

    def __init__(self,name,start_time,tybe_pc,time_in,user_name):
        super(MainWindow, self).__init__()
        ######################
        self.name = name
        self.start_time = start_time
        self.tybe_pc = tybe_pc
        self.time_in = time_in 
        self.user_name = user_name
        ###################################
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.tootl = 0
        self.food = ""
        
        
        self.minutes = int(self.time_in)

        self.start_timer()
        ############################

        layout = QVBoxLayout()

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
        background-color:green;
        color:#fff;
        font-size:14px;
        """
        


        self.Lb_name_pc = QLabel(f"{self.name}")
        self.Lb_name_pc.setStyleSheet(color)
        #self.lb_start_time = QLabel(f"تم البدء: {self.start_time}")
        
        self.lb_tybe_pc = QLabel(f"نوع اللعب: {self.tybe_pc}")
        self.lb_time_in = QLabel("")
        self.lb_add_time = QLabel("الوقت المضاف: 0")
        self.lb_too = QLabel("")


        self.lb_1 = QLabel("********************")
        self.bt_end = QPushButton("إنهاء")
        self.bt_end.clicked.connect(self.exit)
        self.bt_end.setStyleSheet("background-color:red;")
        


        self.bt_add_food = QPushButton("أوردر")
        self.bt_add_food.clicked.connect(self.ADD)
        self.bt_add_food.setStyleSheet(color)

        self.bt_set_Time = QPushButton("إضافة وقت")
        self.bt_set_Time.clicked.connect(self.SET_TIME)
        self.bt_set_Time.setStyleSheet(color)

        ###########################
        

        #for w in widgets:
            #layout.addWidget(w)

        layout.addWidget(self.Lb_name_pc)
        #layout.addWidget(self.lb_start_time)
        layout.addWidget(self.lb_tybe_pc)
        layout.addWidget(self.lb_time_in)
        layout.addWidget(self.lb_add_time)
        layout.addWidget(self.lb_1)
        layout.addWidget(self.lb_too)

        layout.addWidget(self.bt_set_Time)
        layout.addWidget(self.bt_add_food)
        layout.addWidget(self.bt_end)
        




        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)



    ############################################
    #time
    def start_timer(self):
        try:
            #self.minutes = int(1)
            self.remaining_time = self.minutes * 60
            self.timer.start(1000)
        except ValueError:
            self.timer_label.setText("الرجاء إدخال رقم صحيح.")

    def update_timer(self):
        #جلب الساعات وضربها
        #tootl = int(self.time_in) + 
        #########
        self.remaining_time -= 1
        self.format_time(self.remaining_time)
        self.lb_time_in.setText(f"الوقت المتبقي: {str(self.format_time(self.remaining_time))}")

        if self.remaining_time <= 0:
            self.timer.stop()
            self.lb_time_in.setText("انتهى الوقت!")
            
            self.setStyleSheet("background:red")
            self.ADD_DATA_IN_DATABESE()
            self.close()

            #QMessageBox.information(self,"تم إنهاء الوقت", "تم انتهاء الوقت وتم غلق الجهاز")
            #pygame.init()
            #pygame.mixer.music.load("end_1.mp3")  # قم بتعديل المسار إلى ملف الصوت الخاص بك
            #pygame.mixer.music.play()
            """self.win_77 = QtWidgets.QMainWindow()
            self.ui = Ui()

            self.ui.setupUi(self.win_77)
            
            self.win_77.show()
            for i in range(6):
                self.win_77.recoverItem()"""

    def format_time(self, seconds):
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02}:{secs:02}"

    ##########################################
    def exit(self): 
        print("إنهاء")
        text_info=f""""
        اسم الجهاز: {self.name}
        *******************
        وقت البدء: {self.start_time}
        *******************
        الوقف الاصلي: {self.time_in}
        *******************
        نوع اللعب: {self.tybe_pc}
        *******************

        """
        QMessageBox.information(self,"إنهاء الفاتوره", text_info)
        self.timer.stop()
        #self.lb_time_in.setText("انتهى الوقت!")
        self.ADD_DATA_IN_DATABESE()
        self.close()
        
        
        #obj = Ui()

        #name_pc = str(obj.comboBox_4.currentText())
        #print(name_pc)

            
        #self.close()
    def ADD(self):
        print("اضافه اكل")

        listt = ["ادنومي","شاي","بيبسي"]
        di = QInputDialog.getItem(self,"اضافه مشروبات","أدخل إسم المشروب",listt,0,False)
        self.food = str(di[0])
        print(di[0])




    def SET_TIME(self):
        
        self.new_time = 0
        print("اضافه وقت")
       
        print("totl>"+ str(self.tootl))
        di = QInputDialog.getInt(self,"إضافه وقت","أدخل عدد الدقائق",60,True)
        self.new_time += int(di[0])
        
        self.minutes += self.new_time
       
        self.tootl += self.new_time
        self.start_timer()
        print("totl>"+ str(self.tootl))
        
        self.lb_add_time.setText(str(f"الوقت المضاف: {str(self.tootl)}"))

        #set tootl time
        self.lb_too.setText(f"الحساب الكلي: {str(self.tootl)}")
    
    
    
    
    
    def ADD_DATA_IN_DATABESE(self):
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        #set time in var
        time_now= str(formatted_time)

        #add data in databise
        try:
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute(f"""insert into start_pc(
            person,
            name_pc,
            total,
            type_pc,
            time,
            end_time,
            food) values(
            '{self.user_name}',
            '{self.name}',
            '{str(self.tootl)}',
            '{self.tybe_pc}',
            '{self.time_in}',
            '{str(time_now)}',
            '{self.food}') """)
            #######################
            db.commit()
            db.close()
            #
            print("Don Data new pc ")

            #refresh window
            #self.close()
            

        except Exception as e:
            print(e)
        

    
##########################################################
    
            
###########################################################
###########################################################
































































#Ui_MainWindow
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        uic.loadUi('ui\\main_2.ui', self)
        self.user_name = ""
        #داله الازرار
        self.Button_DS()
        self.Pc_8_DS()
        #داله انشاء قاده البيانات
        self.create_all_db()
        #var Login
        self.time_start_user = ""
        self.var_time = 0

        self.DS_ALL()
        #set data in Login
        self.username.setText("admin")
        self.passwd.setText("admin")
        self.th_create_db()
        self.settings()
        self.hide_groupBox()
        self.show_data_settings()
        self.set_name_pc_in_combo()
        self.Live_time()
        self.deleted_items = []
        ########
        
        ########
        #self.cun: int = 0
        #self.gridLayout
        self.widg_DS()


    def DS_ALL(self):

        self.lb_info_user = self.findChild(QLabel,"label")
        self.groupBox_main_window = self.findChild(QGroupBox,"groupBox_2")
        #self.groupBox_main_window.hide()
        #
        self.tabWidget = self.findChild(QTabWidget,"tabWidget")
        self.tabWidget.hide()
        #groupBox settings
        self.groupBox_settings = self.findChild(QGroupBox,"groupBox_4")
        #groupBox Login
        self.groupBox_Login = self.findChild(QGroupBox,"groupBox")
        
        self.box_add = self.findChild(QWidget,"groupBox_5")

        #widg_1
        self.widget_1 = self.findChild(QWidget,"widget")
        self.widget_1.hide()
        
        self.widget_2 = self.findChild(QWidget,"widget_2")
        self.widget_2.hide()
        #self.widget_3 = self.findChild(QWidget,"widget_3")
        #self.widget_2.hide()

        
        

        #self.gridLayout
        #layout.addWidget(self.widget_1,0,1)
        #layout.addWidget(self.widget_2,0,2)
        #layout.addWidget(self.widget_3,0,3)
        #self.setLayout(layout)

       

        






        #Combo Box
        self.list_name_pc = []
        self.comboBox_name = self.findChild(QComboBox,"comboBox_4")

        self.comboBox_time_1 = self.findChild(QComboBox,"comboBox_7")
        
        #self.comboBox_time.addItems(item)
        
        self.comboBox_type = self.findChild(QComboBox,"comboBox_6")

        #sttings
        self.name_pc = self.findChild(QLineEdit,"lineEdit_10")
        self.type_pc = self.findChild(QLineEdit,"lineEdit_11")
        self.price_fardy_pc = self.findChild(QLineEdit,"lineEdit_12")
        self.price_zawgy_pc = self.findChild(QLineEdit,"lineEdit_13")

        #widg login
        self.widget_login = self.findChild(QWidget,"widget_5")
        self.welcome_lb =  self.label_2
        self.widget_login.hide()

        


    #جميع الازرار هنا
    def Button_DS(self):
        #الاعدادات
        self.bt_stt = self.findChild(QPushButton,"pushButton_13")
        self.bt_stt.clicked.connect(self.test)
        ###
        #bt start pc
        self.start_pc_bt = self.findChild(QPushButton,"add_pc_4")
        self.start_pc_bt.clicked.connect(self.start_pc)
        #bt start user
        self.start_user_bt = self.findChild(QPushButton,"pushButton_8")
        self.start_user_bt.clicked.connect(self.start_user)
        ####
        self.exit_bt = self.findChild(QPushButton,"pushButton_3")
        self.exit_bt.clicked.connect(self.exit_user)
        #bt login
        self.seve_bt_1 = self.findChild(QPushButton,"pushButton_17")
        self.seve_bt_1.clicked.connect(self.Login_user)

        #bt login sittings
        self.bt_add_pc = self.findChild(QPushButton,"add")
        self.bt_edit_pc = self.findChild(QPushButton,"edit")
        self.bt_delete_pc = self.findChild(QPushButton,"delete_2")
        self.save_data_pc = self.findChild(QPushButton,"pushButton")

        self.update_7 = self.findChild(QPushButton,"update")
        #self.pushButton_14 = self.findChild(QPushButton,"pushButton_14")
        self.update_7.clicked.connect(self.test_1)

        self.save_data_pc.clicked.connect(self.save_data)

        self.bt_add_pc.clicked.connect(self.show_widget_add_pc)
        self.bt_edit_pc.clicked.connect(self.show_widget_update_pc)
        self.bt_delete_pc.clicked.connect(self.show_widget_delete_pc)



        self.widget_add = self.findChild(QWidget,"widget")

        

        

       


    #داله ال8 اجهزة هنا
    def Pc_8_DS(self):
        #[جهاز رقم 1]
        self.lb_name_pc = self.findChild(QLabel,"label_6")
        self.lb_time_pc = self.findChild(QLabel,"label_12")
        self.lb_type_pc = self.findChild(QLabel,"label_13")
        self.lb_time_motabky = self.findChild(QLabel,"label_15")
        #Login
        self.username = self.findChild(QLineEdit,"lineEdit")
        self.passwd = self.findChild(QLineEdit,"lineEdit_2")


    #show widg add new pc
    def show_widget_add_pc(self):
        print("add")
        self.groupBox_3.hide()
        self.groupBox_4.hide()
        self.groupBox.show()

    # show widg update pc
    def show_widget_update_pc(self):
        print("update")
        self.groupBox.hide()
        self.groupBox_4.hide()
        self.groupBox_3.show()

    # show widg delete pc
    def show_widget_delete_pc(self):
        print("Delete")
        self.groupBox.hide()
        self.groupBox_3.hide()
        self.groupBox_4.show()


    #hide groupBox
    def hide_groupBox(self):
        self.groupBox.hide()
        self.groupBox_3.hide()
        self.groupBox_4.hide()


    def Login_user(self):


        self.widget_login.show()
        self.user_name = self.username.text()

        #set user in lb
        self.welcome_lb.setText(f"hi,{self.user_name}")

        print(self.user_name)
        #set time
        import datetime
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        #cr.execute(f"insert into user(name,time) values('{str(self.username.text())}','{str(formatted_time)}' ) ")
        #db.commit()
        #db.close()
        if self.user_name != "":

            self.groupBox_main_window.hide()








    def settings(self):
        self.table = self.widget_stt
        self.table.setRowCount(6)

        
        




    def set_name_pc_in_combo(self):
        list_name = []

        #celect data
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from new_pc order by id ")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            #print(data)
            list_name.append(data[2])
        #set data in combo
        self.comboBox_name.addItems(list_name)





    def show_data_settings(self):

        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("select * from new_pc order by id DESC")
        datas = cr.fetchall()
        for key, data in enumerate(datas):
            self.table.setRowCount(key+1)
            #print(data)
            self.table.setItem(key, 0, QTableWidgetItem(str(data[2])))
            self.table.setItem(key, 1, QTableWidgetItem(str(data[3])))
            self.table.setItem(key, 2, QTableWidgetItem(str(data[4])))
            self.table.setItem(key, 3, QTableWidgetItem(str(data[5])))
            self.table.setItem(key, 4, QTableWidgetItem(str(data[1])))









            #obj.list_comco_name_pc_from_dafa_bise.append(str(data[0]))

    def create_db_sttings(self):
        db1 = sqlite3.connect("app.db")
        db1.execute("""create table if not exists new_pc (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person VARCHAR(10) DEFAULT 'Missed',
                    name_pc Text,
                    type_pc VARCHAR(10) DEFAULT 'Missed',
                    price_hour_person1 Text,
                    price_hour_person2 Text)
                    """)
        db1.close()


        # [جدول القفل والفتح فقط]
        db2 = sqlite3.connect("app.db")
        db2.execute("""create table if not exists start_pc (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person VARCHAR(10) DEFAULT 'Missed',
                    name_pc Text,
                    total Text,
                    type_pc VARCHAR(10) DEFAULT 'Missed',
                    time Text,
                    end_time,
                    food VARCHAR(10) DEFAULT 'Missed')
                    """)
        db2.close()

    def th_create_db(self):
        th = Thread(target=self.create_db_sttings)
        th.start()


    def widg_DS(self):
        self.scrollArea = self.scrollArea
        self.Grid = QGridLayout()
        self.home_Widget = QWidget()

        self.home_Widget.setWindowTitle("PyQt5")
        self.home_Widget.setLayout(self.Grid)



    def test(self):
        #get data in ui
        get_name_in_combo = str(self.comboBox_name.currentText())
        get_Index_in_combo = str(self.comboBox_name.currentIndex())

        name_pc = str(get_name_in_combo)
        tybe_pc = str(self.comboBox_type.currentText())

        time_pc = str(self.comboBox_7.currentText())
        print(f"GGGG {time_pc}")
        


        ##########################################
        #get time now
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        #set time in var
        time_now= str(formatted_time)
        ###########################################
        
        #from test_2 import MainWindow
        # create a frame and set its properties
        #self.mm = MainWindow("1")
        #for i in range(1,4):
            #for y in range(1,3): 
                #self.Grid.addWidget(MainWindow(f"{i}"),y,i)
        

        if int(get_Index_in_combo) >= 1:
            if get_name_in_combo != "تحديدالجهاز":
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                print(self.Grid.count())
                self.deleteItem()
            """
            if "2" in get_name_in_combo:
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                print(self.Grid.count())
                self.deleteItem()
            if "3" in get_name_in_combo:
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                print(self.Grid.count())
                self.deleteItem()
            if "4" in get_name_in_combo:
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                self.deleteItem()
            if "5" in get_name_in_combo:
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                self.deleteItem()
            if "6" in get_name_in_combo:
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                self.deleteItem()
            if "7" in get_name_in_combo:
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                self.deleteItem()
            if "8" in get_name_in_combo:
                self.Grid.addWidget(MainWindow(name_pc,time_now,tybe_pc,time_pc,self.user_name),0,self.Grid.columnCount())
                self.deleteItem()
            """
        else:
            QMessageBox.critical(self,"خطأ","لم يتم تحديد جهاز للتشغيل")
            #remove item
            #self.comboBox_4.removeItem(int(get_Index_in_combo))
            #######################################
            self.home_Widget.setLayout(self.Grid)
            self.scrollArea.setWidget(self.home_Widget)
            # تمكين خاصية التمرير العمودي والأفقي
            self.scrollArea.setWidgetResizable(True)
    def deleteItem(self):
        # احذف العنصر المحدد من QComboBox وأضفه إلى القائمة المحذوفة
        current_index = self.comboBox_name.currentIndex()
        if current_index >= 0:
            deleted_item = self.comboBox_name.itemText(current_index)
            self.deleted_items.append(deleted_item)
            self.comboBox_name.removeItem(current_index)
    def recoverItem(self):
        # استرجاع العناصر المحذوفة من القائمة وإضافتها مرة أخرى إلى QComboBox
        if self.deleted_items:
            recovered_item = self.deleted_items.pop()
            self.comboBox_name.addItem(recovered_item)
        


      
        
    def get_data_2(self):
        y = self.ui.lineEdit.text()
        self.label_4.setText(y)




        




    
    ##################################################
    def test_1(self):
        print("TEST")
        #self.close()
        #self.ww = Ui()
        #self.ww.show()

        self.recoverItem()
        print(self.Grid.columnCount())
        #self.comboBox_name()
        
            

    def start_countdown1(self):
        self.countdown1.start()

    def update_countdown(self):
        self.time_left = self.time_left.addSecs(-1)  # تحديث الوقت المتبقي
        self.label.setText(self.time_left.toString())

        if self.time_left == QTime(0, 0):
            self.countdown1.stop()
            self.label.setText("انتهى الوقت!")
            #pygame.init()
            #pygame.mixer.music.load("end_1.mp3")  # قم بتعديل المسار إلى ملف الصوت الخاص بك
            #pygame.mixer.music.play()



    def Live_time(self):
        # creating a timer object
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)


    def showTime(self):
        #font = QFont('Arial', 20, QFont.Bold)
        #self.label_3.setFont(font)

        # getting current time
        current_time = QTime.currentTime()
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        # showing it to the label
        self.label_3.setText(f"الساعه الان: {label_time}")

        
    def start_pc(self):
        pass
        
        ############################################
        
        

    def start_user(self):


        self.tabWidget.show()
        self.widget_login.hide()
        self.tabWidget.setCurrentIndex(0)

        #hi

        print("Hi, " + self.user_name)
        #get time
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')

        #set time in var
        self.time_start_user = str(formatted_time)
        self.lb_info_user.setText(f"مرحباً يا {self.user_name} || تم بدء الوردية الساعه: {self.time_start_user}")

        #self.start_user_bt.hide()
        #self.box_add.show()





    

    #set Data in var

    def exit_user(self):
        print(f"log out: {self.user_name}")
        self.name_user = ""


        self.tabWidget.hide()
        self.widget_5.hide()

        # show Login window
        self.groupBox_2.show()


        #clear bt data
        self.username.setText("admin")
        self.passwd.setText("admin")

    def create_all_db(self):
        db1 = sqlite3.connect("app.db")
        db1.execute("create table if not exists user (id INTEGER PRIMARY KEY AUTOINCREMENT,name Text,time VARCHAR(10) DEFAULT 'Missed' )")
        #db1.commit()
        db1.close()
        ####
        #الاصناف
        #db2 = sqlite3.connect("db\\new_data.db")
        #db2.execute("create table if not exists product_new (id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(20) DEFAULT 'Missed', parcode_defolt integer,parcode integer(20) DEFAULT 'Missed',eladd VARCHAR(20) DEFAULT 'Missed',price VARCHAR(20) DEFAULT 'Missed',date_now VARCHAR(20) DEFAULT 'Missed')")
        #db2.commit()
        #db2.close()
        #############
        #داتا البيع
        #db3 = sqlite3.connect("db\\info_day.db")
        #db3.execute("create table if not exists product (id INTEGER PRIMARY KEY AUTOINCREMENT,name Text, price integer,el3dd Text,time Text,date_now Text)")
        #db2.commit()
        #db3.close()

###########################################################
###########################################################


    def save_data(self):
        name_pc = str(self.name_pc.text())
        type_pc = str(self.type_pc.text())
        price_fardy_pc = str(self.price_fardy_pc.text())
        price_zawgy_pc = str(self.price_zawgy_pc.text())
        if name_pc != "" and type_pc != "" and price_fardy_pc != "" and price_zawgy_pc != "":
            try:
                # add Data in connect
                db = sqlite3.connect("app.db")
                cr = db.cursor()
                cr.execute(f"""insert into new_pc(
                person,
                name_pc,
                type_pc,
                price_hour_person1,
                price_hour_person2) values(
                '{self.user_name}',
                '{name_pc}',
                '{type_pc}',
                '{price_fardy_pc}',
                '{price_zawgy_pc}') """)
                #######################
                db.commit()
                db.close()
                #
                print("Don Data new pc ")

                #refresh window
                self.close()
                w = self.show()
                self.show_data_settings()

            except Exception as e:
                print(e)
        else:
            QMessageBox.information(self,"الحقول فارقه","أدخل البيانات أولاً")

#################################
    def Time(self, duration_seconds):
        
        self.duration_seconds = duration_seconds
        self.remaining_time = duration_seconds
        self.initUI()

    def initUI(self):
        self.timerLabel = QLabel()
        self.updateTime()
        
        layout = QVBoxLayout()
        layout.addWidget(self.timerLabel)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # تحديث العرض كل ثانية
        
    def updateTime(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self.timer.stop()
            self.timerLabel.setText("انتهى الوقت!")
        else:
            minutes, seconds = divmod(self.remaining_time, 60)
            
            self.label_5.setText(f"الوقت المتبقي: {minutes} دقيقة و {seconds} ثانية")
            
            #a =  f"الوقت المتبقي: {minutes} دقيقة و {seconds} ثانية"
            
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()

