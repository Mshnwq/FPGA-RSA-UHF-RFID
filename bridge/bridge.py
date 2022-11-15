from Window import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from key_gen import RSA
from RFID_Driver import RFID
from fpga_driver import FPGA
# from firebase_admin import *

import sys

class MainWindow(QMainWindow):
      
    rsa  = RSA() # create instance of RSA
    rfid = RFID() # create instance of RFID
    fpga = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # construct choice window
        self.ui = Choice_Window()
        self.ui.setupUi(self)

        self.ui.GenMode_btn.clicked.connect(self.generateMode)
        self.ui.AttMode_btn.clicked.connect(self.attemptMode)

    def generateMode(self):
        self.generateSuccess = False
        self.UARTSuccess = False
        self.dialogType = 0

        self.ui = GenMode_MainWindow()
        self.ui.setupUi(self)
        
        # establish FPGA UART comm
        #TODO
        self.ui.FPGA_btn.clicked.connect(self.establishUART)

        # Generate keys
        self.ui.genKeys_btn.clicked.connect(self.generateKeys)

        # Write Key
        self.ui.writeKey_btn.clicked.connect(self.writeKey)

        # Encrpyt the plaintext
        self.ui.encryptMsg_btn.clicked.connect(self.encrypt)

        # Upload data to backend
        # TODO
        self.ui.uploadData_btn.clicked.connect(self.sendData)

        # Clear logs
        self.ui.clearLogs_btn.clicked.connect(lambda: self.ui.logs_box.setPlainText(""))
        
        # hide buttons
        self.ui.encryptMsg_btn.setEnabled(False)
        self.ui.writeKey_btn.setEnabled(False)
        self.ui.uploadData_btn.setEnabled(False)

    def attemptMode(self):

        self.ui = AttMode_MainWindow()
        self.ui.setupUi(self)
        # self.barcode.clearData() # clear reader data
        # self.writeTagInfo() # to initalizd empty
        # self.ui.pushButton_7.clicked.connect(self.printBarcode)

    def checkBtns(self):
        if (self.ui.bit16_btn.isChecked()):
            return 16
        elif (self.ui.bit64_btn.isChecked()):
            return 64
        elif (self.ui.bit32_btn.isChecked()):
            return 32
        else:
            return 64
        
    def generateKeys(self):
        bitSize = self.checkBtns()
        self.publicKey, self.privateKey = self.rsa.generateKey(
            bitSize, window=self.ui)
        n = self.rsa.getN()
        e = self.rsa.getE()
        d = self.rsa.getD()
        self.ui.N_label_box.setText(n)
        self.ui.E_label_box.setText(e)
        self.ui.D_label_box.setText(d)
        lenN = len(n)
        lenE = len(e)
        lenD = len(d)
        privateKey = ""
        publicKey = ""
        modKey = ""
        for i in range(lenE):
            privateKey += e[i]
            if ((i+1)%20 == 0):
                privateKey += "\n"
        privateKey += ",\n"
        for i in range(lenD):
            publicKey += d[i]
            if ((i+1)%20 == 0):
                publicKey += "\n"
        publicKey += ",\n"
        for i in range(lenN):
            modKey += n[i]
            if ((i+1)%20 == 0):
                modKey += "\n"
        privateKey += modKey
        publicKey += modKey
        self.ui.Private_box.setText(privateKey)
        self.ui.Public_box.setText(publicKey)
        self.ui.writeKey_btn.setEnabled(True)
        self.generateSuccess = True
        self.ui.encryptMsg_btn.setEnabled(
            self.generateSuccess and self.UARTSuccess)
        self.ui.logs_box.append("Key Generation Success")
        self.ui.genKeys_statusText.setText("Keys Generated")
        self.ui.genKeys_statusText.setStyleSheet(
            "color: rgb(0,200,0);\nfont: bold 10px;")
        # Sorry for no comments and ugly code

    def writeKey(self):
        self.dialogType == 2

        tagData = bytearray(16)
        keyToWriteInt = self.publicKey[0]
        keyToWrite = keyToWriteInt.to_bytes(16, byteorder = 'big')

        for i in range(0, len(keyToWrite)):  
            tagData[i] = keyToWrite[i]  

        print(keyToWriteInt)
        print(keyToWrite)
        print(tagData)
        stat = self.rfid.writeKey(
            desiredDataToWrite = tagData, window=self.ui)
        if (stat == 1):
            self.ui.logs_box.append("Write Key Success")
            self.ui.writeKey_statusText.setText("Key Issued")
            self.ui.writeKey_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 14px;")
            print(f'(int) written: {keyToWriteInt}')
            # print(f'(bytes) written: {keyToWrite}')
            print(f'(hex) written: {hex(keyToWriteInt)}')
            print(f'(bin) written: {bin(keyToWriteInt)}')
            # print(keyToWrite)
            # print(tagData)
        elif stat == 0: 
            self.ui.logs_box.append("Write Key Failed")
            self.ui.writeKey_statusText.setText("Issueing Failed")
            self.ui.writeKey_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 12px;;")
        else:
            self.ui.writeKey_statusText.setText("Issueing Failed")
            self.ui.writeKey_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 12px;;")
            dialog = QMessageBox()
            dialog.setText("incorrect amount of keys in front of reader")
            dialog.setWindowTitle("Error!")
            dialog.setIcon(QMessageBox.Critical)
            dialog.setInformativeText("Place only 1 key only infront of reader")
            dialog.setStandardButtons(QMessageBox.Retry|QMessageBox.Cancel)
            dialog.buttonClicked.connect(self.dialogClicked)
            dialog.exec_()

    def dialogClicked(self, btn):
        # print(btn.text())
        if(self.dialogType == 2 and btn.text() == 'Retry'):
            self.writeKey()
        if(self.dialogType == 1 and btn.text() == 'Retry'):
            self.readKey()

    def establishUART(self):
        #TODO ABDULLAH HELP
        print("kaka")
        
        self.fpga = FPGA() # create instance of RFID

        stat = 1

        if stat == 1:
            self.ui.logs_box.append("FPGA UART Success")
            self.ui.FPGA_statusText.setText("Success")
            self.ui.FPGA_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
            self.UARTSuccess = True
            self.ui.encryptMsg_btn.setEnabled(
            self.generateSuccess and self.UARTSuccess)
        else: 
            self.ui.logs_box.append("FPGA UART Failed")
            self.ui.FPGA_statusText.setText("Failed")
            self.ui.FPGA_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")

    def encrypt(self):
    
        plainTextString = self.ui.plaintext_box.text()
        nchars = len(plainTextString)
        # string to int or long. Type depends on nchars
        plainTextInt = sum(ord(plainTextString[byte])<<8*(nchars-byte-1) for byte in range(nchars))
        print(plainTextInt)
        # plainTextHex = hex(plainTextInt)[2::]
        # print(plainTextHex)

        #encrypting # TODO
        cipherTextInt = self.fpga.encrypt_decrypt(plainTextInt, self.rsa.getE(), self.rsa.getN())
        self.cipherTextInt = cipherTextInt

        cipherTextString = ''.join(chr((cipherTextInt>>8*(nchars-byte-1))&0xFF) for byte in range(nchars))
        # int or long to string
        self.ui.ciphertext_text.setText(cipherTextString)

        stat = 1

        if stat == 1:
            self.ui.logs_box.append("FPGA UART Success")
            self.ui.encryptMsg_statusText.setText("Success")
            self.ui.encryptMsg_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
            self.ui.uploadData_btn.setEnabled(True)
        else: 
            self.ui.logs_box.append("FPGA UART Failed")
            self.ui.encryptMsg_statusText.setText("Failed")
            self.ui.encryptMsg_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")
        

    def retreiveData(self):
        #TODO
        cred = credentials.Certificate('halaqah-150f3-firebase-adminsdk-re0wk-3d667829eb.json')
        firebase_admin.initialize_app(cred, {
        "databaseURL": "https://halaqah-150f3.firebaseio.com",
        "storageBucket": "halaqah-150f3.appspot.com"
        })
    
        # Storage = storage.bucket()
        # pair = {}
        # pair["cipherTextInt"] = self.cipherTextInt
        # pair["Modulus"] = self.rsa.getN()
        
    def sendData(self):
        #TODO
        # # try:
        # Storage.child(path).download("test.wav")
        pair = {}
        pair["cipherTextInt"] = self.cipherTextInt
        pair["Modulus"] = self.rsa.getN()

        stat = self.fpga.fOpenComIndex

        if stat == 1:
            self.ui.logs_box.append("FPGA UART Success")
            self.ui.uploadData_statusText.setText("Success")
            self.ui.uploadData_statusText.setStyleSheet(
                "color: rgb(0,200,0);\nfont: bold 16px;")
        else: 
            self.ui.logs_box.append("FPGA UART Failed")
            self.ui.uploadData_statusText.setText("Failed")
            self.ui.uploadData_statusText.setStyleSheet(
                "color: rgb(250,0,0);\nfont: bold 16px;;")




if __name__ == '__main__':
    app = QApplication(sys.argv) 
    display = MainWindow()
    display.show()
    sys.exit(app.exec_())