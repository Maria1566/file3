# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def start(self):
        points=0
        if self.radioButton_2.isChecked():
            points+=2
        if self.radioButton_3.isChecked():
            points+=0
        if self.radioButton.isChecked():
            points+=0
        if self.radioButton_5.isChecked():
            points+=0
        if self.radioButton_6.isChecked():
            points+=2
        if self.radioButton_4.isChecked():
            points+=0
        if self.radioButton_8.isChecked():
            points+=2
        if self.radioButton_7.isChecked():
            points+=0
        if self.radioButton_9.isChecked():
            points+=0
        if self.radioButton_11.isChecked():
            points+=0
        if self.radioButton_13.isChecked():
            points+=0
        if self.radioButton_12.isChecked():
            points+=0
        if self.radioButton_10.isChecked():
            points+=2
        if self.radioButton_16.isChecked():
            points+=2
        if self.radioButton_15.isChecked():
            points+=0
        if self.radioButton_14.isChecked():
            points+=0
        if points == 0:
            self.label_8.setText("это даже картинки недостойно... ")
        if points == 2:
            self.label_8.setText("очень плохо") 
            self.label_7.setPixmap(QtGui.QPixmap("очень плохо.jpg"))
        if points == 4 :
            self.label_8.setText("ну так себе... ") 
            self.label_7.setPixmap(QtGui.QPixmap("ну так себе.jpg"))
        if points == 6 :
            self.label_8.setText("не плохо ") 
            self.label_7.setPixmap(QtGui.QPixmap("не плохо.jpg"))
        if points == 8 :
            self.label_8.setText("молодец") 
            self.label_7.setPixmap(QtGui.QPixmap("молодец5.jpg"))  
        if points == 10 :
            self.label_8.setText("да ты Експерт") 
            self.label_7.setPixmap(QtGui.QPixmap("эксперт.jpg"))  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 401, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 501, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 471, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 481, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 260, 411, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_5 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 330, 331, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 370, 461, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_8 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout_3.addWidget(self.radioButton_8)
        self.radioButton_7 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.horizontalLayout_3.addWidget(self.radioButton_7)
        self.radioButton_9 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setObjectName("radioButton_9")
        self.horizontalLayout_3.addWidget(self.radioButton_9)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 490, 541, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 530, 571, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_11 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.horizontalLayout_4.addWidget(self.radioButton_11)
        self.radioButton_13 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setObjectName("radioButton_13")
        self.horizontalLayout_4.addWidget(self.radioButton_13)
        self.radioButton_12 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.horizontalLayout_4.addWidget(self.radioButton_12)
        self.radioButton_10 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.horizontalLayout_4.addWidget(self.radioButton_10)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 650, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 690, 561, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_16 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_16.setFont(font)
        self.radioButton_16.setObjectName("radioButton_16")
        self.horizontalLayout_5.addWidget(self.radioButton_16)
        self.radioButton_15 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setObjectName("radioButton_15")
        self.horizontalLayout_5.addWidget(self.radioButton_15)
        self.radioButton_14 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setObjectName("radioButton_14")
        self.horizontalLayout_5.addWidget(self.radioButton_14)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 800, 281, 31))
        self.pushButton.clicked.connect(self.start)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(530, 60, 251, 371))
        self.label_7.setMinimumSize(QtCore.QSize(251, 0))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(""))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(600, 450, 171, 20))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Тест на знание мультфильмов Диснея "))
        self.label_2.setText(_translate("MainWindow", "1. Как зовут сына Корля-Льва Муфасы в мультфильме \"Король лев\" ?"))
        self.radioButton_3.setText(_translate("MainWindow", "Лимбо"))
        self.radioButton_2.setText(_translate("MainWindow", "Симба"))
        self.radioButton.setText(_translate("MainWindow", "Дамбо"))
        self.label_3.setText(_translate("MainWindow", "2. Сколько у Золушки сводных сестер ?"))
        self.radioButton_5.setText(_translate("MainWindow", " 1 "))
        self.radioButton_6.setText(_translate("MainWindow", " 2 "))
        self.radioButton_4.setText(_translate("MainWindow", " 3 "))
        self.label_4.setText(_translate("MainWindow", "3. Как переводиться фраза \"Акуна матата\" ?"))
        self.radioButton_8.setText(_translate("MainWindow", " \"Без  забот\" "))
        self.radioButton_7.setText(_translate("MainWindow", " \"Не сдавайся\""))
        self.radioButton_9.setText(_translate("MainWindow", "\"Не унывай\""))
        self.label_5.setText(_translate("MainWindow", "4. В кого превращается Джафар во время финальной битвы с Аладдином ?"))
        self.radioButton_11.setText(_translate("MainWindow", "В скорпиона "))
        self.radioButton_13.setText(_translate("MainWindow", "В дракона"))
        self.radioButton_12.setText(_translate("MainWindow", "В Джинна"))
        self.radioButton_10.setText(_translate("MainWindow", "В змея"))
        self.label_6.setText(_translate("MainWindow", "5. Кто является лучшим другом Гуфи ?  "))
        self.radioButton_16.setText(_translate("MainWindow", "Дональд Дак "))
        self.radioButton_15.setText(_translate("MainWindow", "Плуто "))
        self.radioButton_14.setText(_translate("MainWindow", "Микки-Маус"))
        self.pushButton.setText(_translate("MainWindow", "ГОТОВО"))
        self.label_8.setText(_translate(" MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
