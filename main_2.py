from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QPushButton,QDialog,QLineEdit,QTimeEdit ,QMainWindow,QApplication,QLabel ,QGroupBox,QMessageBox,QWidget,QComboBox,QTableWidgetItem,QTableWidget,QTabWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5 import QtCore

#from ds import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize,QDateTime
import sqlite3
from threading import Thread
import time

import datetime
import pygame
from PyQt5.QtGui import QFont
########################
#داله الساع



###########################################################
###########################################################

#Ui_MainWindow
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        uic.loadUi('ui\\main.ui', self)
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
        self.settings()
        self.hide_groupBox()
        self.show_data_settings()
        self.set_name_pc_in_combo()
        self.Live_time()


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
        #widg_1
        self.box_add = self.findChild(QWidget,"groupBox_5")
        self.widget_1 = self.findChild(QWidget,"widget")
        self.widget_1.hide()

        self.widget_2 = self.findChild(QWidget,"widget_2")
        self.widget_2.hide()







        #Combo Box
        self.list_name_pc = []
        self.comboBox_name = self.findChild(QComboBox,"comboBox_4")

        self.comboBox_time = self.findChild(QComboBox,"comboBox_5")
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
        self.save_data_pc.clicked.connect(self.save_data)

        self.bt_add_pc.clicked.connect(self.show_widget_add_pc)
        self.bt_edit_pc.clicked.connect(self.show_widget_update_pc)
        self.bt_delete_pc.clicked.connect(self.show_widget_delete_pc)

        #self.widget_add = self.findChild(QWidget,"widget")



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

        self.th_create_db()
        




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
    def th_create_db(self):
        th = Thread(target=self.create_db_sttings)
        th.start()



    def test(self):
        pass
        

    
  
    ##################################################
    def test_1(self):
        self.countdown1 = QTimer()
        self.countdown1.setInterval(1000)  # تحديث العد كل ثانية
        self.countdown1.timeout.connect(self.update_countdown)
        
        # إنشاء عنصر العرض لعرض الوقت المتبقي
        if "1" in self.comboBox_name.currentText():
            self.label = self.label_15
        elif "2" in self.comboBox_name.currentText():
            self.label = self.label_18
        

    def start_countdown1(self):
        self.countdown1.start()

    

    
            

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
        #get info
        dt = datetime.datetime.now()
        formatted_time = dt.strftime('%H:%M')
        name_pc = str(self.comboBox_name.currentText())
        type_pc = str(self.comboBox_type.currentText())
        time_pc = str(self.comboBox_time.currentText())
        start_time = formatted_time


        if "1" in self.comboBox_name.currentText():
            self.widget_1.show()
            self.test_1()
        elif "2" in self.comboBox_name.currentText():
            self.test_1()


            
     


                

        self.show_pc(name_pc,time_pc,type_pc,start_time)


    def show_pc(self,name_pc,time_pc,type_pc,start_time):
        #self.time_left = QTime(0, 0, 5)  # 10 ثوانٍ
        #self.start_countdown()
        #اختيار الاجهزه
        if "1" in name_pc:
            self.widget_1.show()
            #self.lb_name_pc.setText(name_pc)
            self.lb_time_pc.setText(str(f"وقت البداية |  {start_time}"))
            self.lb_type_pc.setText(f"نوع الجهاز |  {type_pc}")
            #if "30" in time_pc:
            self.lb_time_motabky.setText(str(30))
            self.var_time = 5
            #self.th_time()
            self.time_left = QTime(0, 0, 30)  # 10 ثوانٍ
            self.start_countdown1()



        elif "2" in name_pc:
            print("222222222222222")
            self.widget_2.show()
            self.label_7.setText(name_pc)
            self.lb_type_pc.setText(f"{type_pc}")
            self.time_left = QTime(0, 0, 30)  # 10 ثوانٍ
            #self.start_countdown()

        else:
            pass



        ####

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





    #open_window_settings
    def open_Eta7acom(self):
        #print("open_Eta7acom")
        self.op = Settings_Playstation()
        self.op.show()

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









#######################################

class DeviceWindow(QDialog):
    def __init__(self, device_id, duration, price):
        super().__init__()
        self.setWindowTitle(f"جهاز رقم {device_id}")
        self.setModal(True)

        main_layout = QVBoxLayout(self)

        duration_label = QLabel(f"المدة (بالساعات): {duration}")
        main_layout.addWidget(duration_label)

        price_label = QLabel(f"السعر للساعة (بالدولار): {price}")
        main_layout.addWidget(price_label)

        close_button = QPushButton("إغلاق")
        close_button.clicked.connect(self.close)
        main_layout.addWidget(close_button)
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()

