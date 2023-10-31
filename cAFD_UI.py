from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator

class Ui_ConversorAFD(object):
    def setupUi(self, ConversorAFD):
        ConversorAFD.setObjectName("ConversorAFD")
        ConversorAFD.resize(350, 395)
        ConversorAFD.setMinimumSize(QtCore.QSize(350, 395))
        ConversorAFD.setMaximumSize(QtCore.QSize(350, 395))
        ConversorAFD.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttonStyle = ("QPushButton {\n"
"border-radius: 5px;\n"
"background-color: rgb(52, 83, 155);\n"
"padding: 8px;\n"
"color: #fff;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(38, 67, 133);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(71, 110, 201);\n"
"}\n")
        self.lineStyle = ("QLineEdit {\n"
"    border-radius:3px;\n"
"    border: 1px solid gray;\n"
"}")
        self.app_TITLE = QtWidgets.QLabel(ConversorAFD)
        self.app_TITLE.setGeometry(QtCore.QRect(10, 10, 331, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.app_TITLE.setFont(font)
        self.app_TITLE.setObjectName("app_TITLE")
        self.layoutWidget = QtWidgets.QWidget(ConversorAFD)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 350, 331, 40))
        self.layoutWidget.setObjectName("layoutWidget")
        self.box_ACTIONBUTTONS = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.box_ACTIONBUTTONS.setContentsMargins(0, 0, 0, 0)
        self.box_ACTIONBUTTONS.setObjectName("box_ACTIONBUTTONS")
        self.box_QUIT = QtWidgets.QPushButton(self.layoutWidget)
        self.box_QUIT.setFont(font)
        self.box_QUIT.setStyleSheet(self.buttonStyle)
        self.box_QUIT.setObjectName("box_QUIT")
        self.box_ACTIONBUTTONS.addWidget(self.box_QUIT)
        self.box_START = QtWidgets.QPushButton(self.layoutWidget)
        self.box_START.setFont(font)
        self.box_START.setStyleSheet(self.buttonStyle)
        self.box_START.setObjectName("box_START")
        self.box_ACTIONBUTTONS.addWidget(self.box_START)
        self.box_CNPJ_INPUT = QtWidgets.QLineEdit(ConversorAFD)
        self.box_CNPJ_INPUT.setGeometry(QtCore.QRect(10, 170, 331, 20))
        self.box_CNPJ_INPUT.setStyleSheet(self.lineStyle)
        self.box_CNPJ_INPUT.setAlignment(QtCore.Qt.AlignCenter)
        self.box_CNPJ_INPUT.setObjectName("box_CNPJ_INPUT")
        self.box_CNPJ_LABEL = QtWidgets.QLabel(ConversorAFD)
        self.box_CNPJ_LABEL.setGeometry(QtCore.QRect(10, 150, 331, 20))
        self.box_CNPJ_LABEL.setFont(font)
        self.box_CNPJ_LABEL.setObjectName("box_CNPJ_LABEL")
        self.box_MTE_LABEL = QtWidgets.QLabel(ConversorAFD)
        self.box_MTE_LABEL.setGeometry(QtCore.QRect(10, 190, 331, 20))
        self.box_MTE_LABEL.setFont(font)
        self.box_MTE_LABEL.setObjectName("box_MTE_LABEL")
        self.box_MTE_INPUT = QtWidgets.QLineEdit(ConversorAFD)
        self.box_MTE_INPUT.setGeometry(QtCore.QRect(10, 210, 331, 20))
        self.box_MTE_INPUT.setStyleSheet(self.lineStyle)
        self.box_MTE_INPUT.setAlignment(QtCore.Qt.AlignCenter)
        self.box_MTE_INPUT.setObjectName("box_MTE_INPUT")
        self.box_DATA_TITLE_2 = QtWidgets.QLabel(ConversorAFD)
        self.box_DATA_TITLE_2.setGeometry(QtCore.QRect(10, 260, 331, 16))
        self.box_DATA_TITLE_2.setFont(font)
        self.box_DATA_TITLE_2.setObjectName("box_DATA_TITLE_2")
        self.box_CNPJ_LABEL_2 = QtWidgets.QLabel(ConversorAFD)
        self.box_CNPJ_LABEL_2.setGeometry(QtCore.QRect(10, 280, 331, 16))
        self.box_CNPJ_LABEL_2.setFont(font)
        self.box_CNPJ_LABEL_2.setObjectName("box_CNPJ_LABEL_2")
        self.box_DATA_TITLE = QtWidgets.QLabel(ConversorAFD)
        self.box_DATA_TITLE.setGeometry(QtCore.QRect(10, 85, 331, 21))
        self.box_DATA_TITLE.setFont(font)
        self.box_DATA_TITLE.setObjectName("box_DATA_TITLE")
        self.box_RAZAOSOCIAL_LABEL = QtWidgets.QLabel(ConversorAFD)
        self.box_RAZAOSOCIAL_LABEL.setGeometry(QtCore.QRect(10, 110, 331, 20))
        self.box_RAZAOSOCIAL_LABEL.setFont(font)
        self.box_RAZAOSOCIAL_LABEL.setObjectName("box_RAZAOSOCIAL_LABEL")
        self.box_RAZAOSOCIAL_INPUT = QtWidgets.QLineEdit(ConversorAFD)
        self.box_RAZAOSOCIAL_INPUT.setGeometry(QtCore.QRect(10, 130, 331, 20))
        self.box_RAZAOSOCIAL_INPUT.setStyleSheet(self.lineStyle)
        self.box_RAZAOSOCIAL_INPUT.setAlignment(QtCore.Qt.AlignCenter)
        self.box_RAZAOSOCIAL_INPUT.setObjectName("box_RAZAOSOCIAL_INPUT")
        self.layoutWidget1 = QtWidgets.QWidget(ConversorAFD)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 300, 331, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.box_FILE = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.box_FILE.setContentsMargins(0, 0, 0, 0)
        self.box_FILE.setObjectName("box_FILE")
        self.box_FILE_INPUT = QtWidgets.QLineEdit(self.layoutWidget1)
        self.box_FILE_INPUT.setMaximumSize(QtCore.QSize(16777215, 30))
        self.box_FILE_INPUT.setStyleSheet(self.lineStyle)
        self.box_FILE_INPUT.setAlignment(QtCore.Qt.AlignCenter)
        self.box_FILE_INPUT.setObjectName("box_FILE_INPUT")
        self.box_FILE_INPUT.setEnabled(False)
        self.box_FILE.addWidget(self.box_FILE_INPUT)
        self.box_FILE_BUTTON = QtWidgets.QPushButton(self.layoutWidget1)
        self.box_FILE_BUTTON.setFont(font)
        self.box_FILE_BUTTON.setStyleSheet(self.buttonStyle)
        self.box_FILE_BUTTON.setObjectName("box_FILE_BUTTON")
        self.box_FILE.addWidget(self.box_FILE_BUTTON)
        self.line = QtWidgets.QFrame(ConversorAFD)
        self.line.setGeometry(QtCore.QRect(10, 230, 331, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(ConversorAFD)
        self.line_2.setGeometry(QtCore.QRect(10, 330, 331, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        rx = QRegExp("\d+")
        cnpj_rx = QRegExp("\d+")
        self.box_RAZAOSOCIAL_INPUT.setMaxLength(150)
        self.box_RAZAOSOCIAL_INPUT.setAlignment(Qt.AlignCenter)
        self.box_CNPJ_INPUT.setValidator(QRegExpValidator(cnpj_rx))
        self.box_CNPJ_INPUT.setMaxLength(14)
        self.box_CNPJ_INPUT.setAlignment(Qt.AlignCenter)
        self.box_FILE_INPUT.setAlignment(Qt.AlignCenter)
        self.box_MTE_INPUT.setValidator(QRegExpValidator(rx))
        self.box_MTE_INPUT.setMaxLength(17)
        self.box_MTE_INPUT.setAlignment(Qt.AlignCenter)

        self.retranslateUi(ConversorAFD)
        QtCore.QMetaObject.connectSlotsByName(ConversorAFD)
        ConversorAFD.setTabOrder(self.box_RAZAOSOCIAL_INPUT, self.box_CNPJ_INPUT)
        ConversorAFD.setTabOrder(self.box_CNPJ_INPUT, self.box_MTE_INPUT)
        ConversorAFD.setTabOrder(self.box_MTE_INPUT, self.box_FILE_INPUT)
        ConversorAFD.setTabOrder(self.box_FILE_INPUT, self.box_FILE_BUTTON)
        ConversorAFD.setTabOrder(self.box_FILE_BUTTON, self.box_QUIT)
        ConversorAFD.setTabOrder(self.box_QUIT, self.box_START)

    def retranslateUi(self, ConversorAFD):
        _translate = QtCore.QCoreApplication.translate
        ConversorAFD.setWindowTitle(_translate("ConversorAFD", "ConversorAFD"))
        self.app_TITLE.setText(_translate("ConversorAFD", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#34539b;\">Conversor</span><span style=\" font-size:18pt; font-weight:600; color:#34539b;\">AFD</span></p></body></html>"))
        self.box_QUIT.setText(_translate("ConversorAFD", "Sair"))
        self.box_START.setText(_translate("ConversorAFD", "Processar"))
        self.box_CNPJ_LABEL.setText(_translate("ConversorAFD", "<html><head/><body><p><span style=\" color:#34539b;\">CNPJ do Empregador</span></p></body></html>"))
        self.box_MTE_LABEL.setText(_translate("ConversorAFD", "<html><head/><body><p><span style=\" color:#34539b;\">Número de registro MTE do Relógio Ponto</span></p></body></html>"))
        self.box_DATA_TITLE_2.setText(_translate("ConversorAFD", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#34539b;\">Arquivo AFD</span></p></body></html>"))
        self.box_CNPJ_LABEL_2.setText(_translate("ConversorAFD", "<html><head/><body><p><span style=\" color:#34539b;\">Selecione o seu arquivo AFD parcial para ser processado</span></p></body></html>"))
        self.box_DATA_TITLE.setText(_translate("ConversorAFD", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#34539b;\">Dados do Empregador e do Relógio Ponto</span></p></body></html>"))
        self.box_RAZAOSOCIAL_LABEL.setText(_translate("ConversorAFD", "<html><head/><body><p><span style=\" color:#34539b;\">Razão Social do Empregador</span></p></body></html>"))
        self.box_FILE_BUTTON.setText(_translate("ConversorAFD", "Selecionar arquivo..."))
