from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class GenMode_MainWindow(object):
    def setupUi(self, MainWindow):
        
        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 800
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 36
        font = QFont()
    
        # create components
        MainWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralwidget = QWidget(MainWindow)

        self.title_txt = QLabel(self.centralwidget)
        self.title_txt.setGeometry(QRect(int(WINDOW_WIDTH/1.8), 2, 300, 40))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.title_txt.setFont(font)

        self.FPGA_btn = QPushButton(self.centralwidget)
        # self.FPGA_btn.setStyleSheet("font-weight: bold")
        self.FPGA_btn.setGeometry(QRect(int(WINDOW_WIDTH/1.225), 6, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.FPGA_btn.setStyleSheet("QPushButton" 
                                    "{"
                                        "background-color: rgb(0, 0, 250);"
                                        "border-style: outset;"
                                        "border-width: 2px;"
                                        "border-radius: 10px;"
                                        "border-color: black;"
                                        "font: bold 14px;"
                                        "color: white;"
                                        "padding: 1px;"
                                    "}"
                                    "QPushButton::pressed" 
                                    "{"
                                        "background-color: rgb(0, 0, 150);"
                                        "border-style: inset;"
                                    "}"
                                    )
        # self.FPGA_btn.setStyleSheet(
            # "background-color: rgb(0, 0, 250);\nborder-style: outset;\nborder-width: 2px;\nborder-radius: 10px;\nborder-color: rgb(0, 0, 154);\nfont: bold 14px;;\npadding: 1px;")
        self.FPGA_statusBox = QGroupBox(self.centralwidget)
        self.FPGA_statusBox.setStyleSheet("color: rgb(0, 0, 250);\nfont-weight: bold;")
        self.FPGA_statusBox.setGeometry(QRect(int(WINDOW_WIDTH)-BUTTON_WIDTH-6, 6, BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.FPGA_statusBox.setFont(font)
        self.FPGA_statusText = QLabel(self.FPGA_statusBox)
        self.FPGA_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        keyGenBox_Xaxis = int(WINDOW_WIDTH/24)
        keyGenBox_Yaxis = int(WINDOW_HEIGHT/24)

        self.keyGen_groupBox = QGroupBox(self.centralwidget)
        self.keyGen_groupBox.setGeometry(QRect(keyGenBox_Xaxis, keyGenBox_Yaxis, 
                                int(WINDOW_WIDTH/4), WINDOW_HEIGHT-int(2*WINDOW_HEIGHT/24)))
        self.keyGen_groupBox.setAutoFillBackground(False)
        self.keyGen_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.keyGen_groupBox.setFont(font)
        
        self.bitSize_groupBox = QGroupBox(self.keyGen_groupBox)
        self.bitSize_groupBox.setGeometry(QRect(10, 30,
                                int(WINDOW_WIDTH/4)-20, 10+int(WINDOW_HEIGHT/24)))
        self.horizontalLayout = QHBoxLayout(self.bitSize_groupBox)

        self.bit64_btn = QRadioButton(self.bitSize_groupBox)
        self.bit64_btn.setGeometry(QRect(0, 0, 18, 18))
        self.bit64_btn.setChecked(True)
        self.horizontalLayout.addWidget(self.bit64_btn)
        self.bit32_btn = QRadioButton(self.bitSize_groupBox)
        self.bit32_btn.setGeometry(QRect(0, 0, 18, 18))
        self.horizontalLayout.addWidget(self.bit32_btn)
        self.bit16_btn = QRadioButton(self.bitSize_groupBox)
        self.bit16_btn.setGeometry(QRect(0, 0, 18, 18))
        self.horizontalLayout.addWidget(self.bit16_btn)

        self.genKeys_btn = QPushButton(self.keyGen_groupBox)
        self.genKeys_btn.setGeometry(QRect(36, int(36*2.5), BUTTON_WIDTH+6, BUTTON_HEIGHT))
        self.genKeys_statusBox = QGroupBox(self.keyGen_groupBox)
        self.genKeys_statusBox.setGeometry(QRect(int(36*4.8), int(36*2.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.genKeys_statusBox.setFont(font)
        self.genKeys_statusText = QLabel(self.genKeys_statusBox)
        self.genKeys_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        
        self.N_label = QLabel(self.keyGen_groupBox)
        self.N_label.setGeometry(QRect(36, 36*4, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.N_label_box = QLabel(self.keyGen_groupBox)
        self.N_label_box.setGeometry(QRect(36+18, 36*4, BUTTON_WIDTH*2, BUTTON_HEIGHT)) 
        self.E_label = QLabel(self.keyGen_groupBox)
        self.E_label.setGeometry(QRect(36, 36*5, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.E_label_box = QLabel(self.keyGen_groupBox)
        self.E_label_box.setGeometry(QRect(36+18, 36*5, BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.D_label = QLabel(self.keyGen_groupBox)
        self.D_label.setGeometry(QRect(36, 36*6, BUTTON_WIDTH, BUTTON_HEIGHT))
        self.D_label_box = QLabel(self.keyGen_groupBox)
        self.D_label_box.setGeometry(QRect(36+18, 36*6, BUTTON_WIDTH*2, BUTTON_HEIGHT))
        self.Private_label = QLabel(self.keyGen_groupBox)
        self.Private_label.setGeometry(QRect(36, 36*7, BUTTON_WIDTH+42, BUTTON_HEIGHT))
        self.Private_groupBox = QGroupBox(self.keyGen_groupBox)
        self.Private_groupBox.setGeometry(QRect(36, 36*8, int(36*6.5), 36*4))
        self.Private_box = QLabel(self.Private_groupBox)
        self.Private_box.setGeometry(QRect(6, 2, int(36*6.5), 36*4))
        self.Public_label = QLabel(self.keyGen_groupBox)
        self.Public_label.setGeometry(QRect(36, int(36*12.5), BUTTON_WIDTH+36, BUTTON_HEIGHT))
        self.Public_groupBox = QGroupBox(self.keyGen_groupBox)
        self.Public_groupBox.setGeometry(QRect(36, int(36*13.5), int(36*6.5), (36*5)+4))
        self.Public_box = QLabel(self.Public_groupBox)
        self.Public_box.setGeometry(QRect(6, 2, int(36*6.5), 36*5))
        font.setPointSize(5)
        font.setBold(False)
        font.setWeight(4)
        self.N_label_box.setFont(font)
        self.E_label_box.setFont(font)
        self.D_label_box.setFont(font)
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(10)
        self.Private_box.setFont(font)
        self.Public_box.setFont(font)

        self.writeKey_btn = QPushButton(self.centralwidget)
        self.writeKey_btn.setStyleSheet("font-weight: bold")
        self.writeKey_btn.setGeometry(QRect(keyGenBox_Xaxis+36, int(WINDOW_HEIGHT)-40*2, 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        self.writeKey_statusBox = QGroupBox(self.centralwidget)
        self.writeKey_statusBox.setStyleSheet("font-weight: bold")
        self.writeKey_statusBox.setGeometry(QRect(int(keyGenBox_Xaxis+36*4.8), int(WINDOW_HEIGHT)-40*2, 
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.writeKey_statusBox.setFont(font)
        self.writeKey_statusText = QLabel(self.writeKey_statusBox)
        self.writeKey_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        self.message_groupBox = QGroupBox(self.centralwidget)
        self.message_groupBox.setGeometry(QRect(int(2*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4), 
                                                int(WINDOW_HEIGHT/24), 
                                                WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)), 
                                                int(WINDOW_HEIGHT/2)+36))
        self.message_groupBox.setAutoFillBackground(False)
        self.message_groupBox.setStyleSheet("font-weight: bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(40)
        self.message_groupBox.setFont(font)

        self.plaintext_label = QLabel(self.message_groupBox)
        self.plaintext_label.setGeometry(QRect(40*3, 40, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.plaintext_label.setFont(font)
        self.plaintext_box = QLineEdit(self.message_groupBox)
        self.plaintext_box.setGeometry(QRect(40, 40*2, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))
        self.ciphertext_label = QLabel(self.message_groupBox)
        self.ciphertext_label.setGeometry(QRect(40*3, 40*5, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(40)
        self.ciphertext_label.setFont(font)
        self.ciphertext_box = QGroupBox(self.message_groupBox)
        self.ciphertext_box.setGeometry(QRect(40, 40*6, 
        WINDOW_WIDTH-(int(3*WINDOW_WIDTH/24)+ int(WINDOW_WIDTH/4)) - 40*2, 40*4))
        self.ciphertext_text = QLabel(self.ciphertext_box)
        self.ciphertext_text.setGeometry(QRect(12, 5, BUTTON_WIDTH*6, BUTTON_HEIGHT*4))

        self.encryptMsg_btn = QPushButton(self.message_groupBox)
        self.encryptMsg_btn.setStyleSheet("font-weight: bold")
        self.encryptMsg_btn.setGeometry(QRect(40*6, int(40*3.5), BUTTON_WIDTH+20, BUTTON_HEIGHT))
        self.encryptMsg_statusBox = QGroupBox(self.message_groupBox)
        self.encryptMsg_statusBox.setStyleSheet("font-weight: bold")
        self.encryptMsg_statusBox.setGeometry(QRect(40*10, int(40*3.5), BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.encryptMsg_statusBox.setFont(font)
        self.encryptMsg_statusText = QLabel(self.encryptMsg_statusBox)
        self.encryptMsg_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))
        

        self.logs_box = QTextEdit(self.centralwidget)
        self.logs_box.setGeometry(QRect(int(3.8*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4), 
                                          int(2.5*WINDOW_HEIGHT/24)+int(WINDOW_HEIGHT/2), 
                                          WINDOW_WIDTH-(int(4.8*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4)), 
                                          int(WINDOW_HEIGHT/2)-int(3.5*WINDOW_HEIGHT/24)))

        self.logs_label = QLabel(self.centralwidget)
        self.logs_label.setGeometry(QRect(int(2*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4),       
                                          int(2.5*WINDOW_HEIGHT/24)+int(WINDOW_HEIGHT/2), 
                                          BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(60)
        self.logs_label.setFont(font)

        self.uploadData_btn = QPushButton(self.centralwidget)
        self.uploadData_btn.setStyleSheet("font-weight: bold")
        self.uploadData_btn.setGeometry(QRect(int(1.4*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4),       
                                          int(4*WINDOW_HEIGHT/24)+int(WINDOW_HEIGHT/2),
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        self.uploadData_statusBox = QGroupBox(self.centralwidget)
        self.uploadData_statusBox.setStyleSheet("font-weight: bold")
        self.uploadData_statusBox.setGeometry(QRect(int(1.4*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4),       
                                          int(6*WINDOW_HEIGHT/24)+int(WINDOW_HEIGHT/2),
                                            BUTTON_WIDTH, BUTTON_HEIGHT))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(8)
        self.uploadData_statusBox.setFont(font)
        self.uploadData_statusText = QLabel(self.uploadData_statusBox)
        self.uploadData_statusText.setGeometry(QRect(12, 5, BUTTON_WIDTH, BUTTON_HEIGHT))

        self.clearLogs_btn = QPushButton(self.centralwidget)
        self.clearLogs_btn.setStyleSheet("font-weight: bold")
        self.clearLogs_btn.setGeometry(QRect(int(1.4*WINDOW_WIDTH/24)+int(WINDOW_WIDTH/4),       
                                        int(WINDOW_HEIGHT)-40*2, BUTTON_WIDTH, BUTTON_HEIGHT))



       
        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setGeometry(QRect(0, 0, 1147, 26))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        # translate text into components
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Generate Mode"))
        self.title_txt.setText(_translate("MainWindow", "Establish FPGA UART Connection"))
        self.keyGen_groupBox.setTitle(_translate("MainWindow", "Generation"))
        self.bit64_btn.setText(_translate("MainWindow", "64 bit"))
        self.bit32_btn.setText(_translate("MainWindow", "32 bit"))
        self.bit16_btn.setText(_translate("MainWindow", "16 bit"))
        self.N_label.setText(_translate("MainWindow", "N:"))
        self.N_label_box.setText(_translate("MainWindow", "---"))
        self.E_label.setText(_translate("MainWindow", "E:"))
        self.E_label_box.setText(_translate("MainWindow", "---"))
        self.D_label.setText(_translate("MainWindow", "D:"))
        self.D_label_box.setText(_translate("MainWindow", "---"))
        self.Private_label.setText(_translate("MainWindow", "Private Key Pair {E,N}"))
        # self.Private_box.setText(_translate("MainWindow", "---"))
        self.Public_label.setText(_translate("MainWindow", "Public Key Pair {D,N}"))
        # self.Public_box.setText(_translate("MainWindow", "---"))
        self.message_groupBox.setTitle(_translate("MainWindow", "Enter a message"))
        self.plaintext_label.setText(_translate("MainWindow", "PlainText"))
        self.ciphertext_label.setText(_translate("MainWindow", "CipherText"))
        # self.ciphertext_box.setText(_translate("MainWindow", "-----"))
        self.logs_label.setText(_translate("MainWindow", "Logs"))
        self.FPGA_btn.setText(_translate("MainWindow", "Connect"))
        self.FPGA_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.FPGA_statusText.setText(_translate("MainWindow", "-------------"))
        self.genKeys_btn.setText(_translate("MainWindow", "Generate Keys"))
        self.genKeys_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.genKeys_statusText.setText(_translate("MainWindow", "-------------"))
        self.writeKey_btn.setText(_translate("MainWindow", "Write Key"))
        self.writeKey_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.writeKey_statusText.setText(_translate("MainWindow", "-------------"))
        self.encryptMsg_btn.setText(_translate("MainWindow", "Encrypt Message"))
        self.encryptMsg_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.encryptMsg_statusText.setText(_translate("MainWindow", "-------------"))
        self.uploadData_btn.setText(_translate("MainWindow", "Upload Data"))
        self.uploadData_statusBox.setTitle(_translate("MainWindow", "     Status"))
        self.uploadData_statusText.setText(_translate("MainWindow", "-------------"))
        self.clearLogs_btn.setText(_translate("MainWindow", "Clear"))

        self.logs_box.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

        QMetaObject.connectSlotsByName(MainWindow)

        
class AttMode_MainWindow(object):
    def setupUi(self, MainWindow):
    
        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 800
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 40
    
        # create components
        MainWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralwidget = QWidget(MainWindow)

        self.title_txt = QLabel(self.centralwidget)
        self.title_txt.setGeometry(QRect(int(WINDOW_WIDTH/10), int(WINDOW_HEIGHT/6), 400, 40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(40)
        self.title_txt.setFont(font)

        self.GenMode_btn = QPushButton(self.centralwidget)
        self.GenMode_btn.setGeometry(QRect(int(WINDOW_WIDTH/8), int(WINDOW_HEIGHT/2), BUTTON_WIDTH, BUTTON_HEIGHT))
        self.AttMode_btn = QPushButton(self.centralwidget)
        self.AttMode_btn.setGeometry(QRect(int(WINDOW_WIDTH*5/8), int(WINDOW_HEIGHT/2), BUTTON_WIDTH, BUTTON_HEIGHT))

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(30, 30, 451, 71))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QRect(30, 330, 421, 181))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QRect(460, 330, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QRect(400, 330, 93, 28))
        self.pushButton_8.setObjectName("pushButton_6")
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setGeometry(QRect(30, 310, 131, 16))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QRect(30, 110, 421, 191))
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("font-weight: bold")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setGeometry(QRect(20, 30, 91, 16))
        self.label_2.setObjectName("label_2")
       
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1147, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # translate text into components
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Attempt Mode"))
        self.label.setText(_translate("MainWindow", "RSA Attempt"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "Logs"))
        self.groupBox.setTitle(_translate("MainWindow", "Generator"))
        self.label_2.setText(_translate("MainWindow", "Key"))
        self.pushButton_6.setText(_translate("MainWindow", "Read"))
        self.pushButton_8.setText(_translate("MainWindow", "d"))

        QMetaObject.connectSlotsByName(MainWindow)

class Choice_Window(object):
    def setupUi(self, ChoiceWindow):
       
        WINDOW_WIDTH = 400
        WINDOW_HEIGHT = 200
        BUTTON_WIDTH = 100
        BUTTON_HEIGHT = 50
    
        # create components
        ChoiceWindow.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.centralwidget = QWidget(ChoiceWindow)

        self.title_txt = QLabel(self.centralwidget)
        self.title_txt.setGeometry(QRect(int(WINDOW_WIDTH/10), int(WINDOW_HEIGHT/6), 400, 40))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(40)
        self.title_txt.setFont(font)

        self.GenMode_btn = QPushButton(self.centralwidget)
        self.GenMode_btn.setGeometry(QRect(int(WINDOW_WIDTH/8), int(WINDOW_HEIGHT/2), BUTTON_WIDTH, BUTTON_HEIGHT))
        self.AttMode_btn = QPushButton(self.centralwidget)
        self.AttMode_btn.setGeometry(QRect(int(WINDOW_WIDTH*5/8), int(WINDOW_HEIGHT/2), BUTTON_WIDTH, BUTTON_HEIGHT))

        ChoiceWindow.setCentralWidget(self.centralwidget)

        # translate text into components
        _translate = QCoreApplication.translate
        ChoiceWindow.setWindowTitle(_translate("ChoiceWindow", "RSA Encryption/Descryption"))
        self.title_txt.setText(_translate("ChoiceWindow", "Choose an Operation Mode"))
        self.GenMode_btn.setText(_translate("ChoiceWindow", "Generate Mode"))
        self.AttMode_btn.setText(_translate("ChoiceWindow", "Attempt Mode"))

        QMetaObject.connectSlotsByName(ChoiceWindow)

