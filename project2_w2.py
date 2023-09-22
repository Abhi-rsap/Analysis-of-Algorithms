
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        n = ""
        with open('output.txt') as f:
                for line in f:
                        line = line.strip()
                        s = line.split(" ")
                        n = len(s)

        k = ""
        for i in s:
                k = k + str(i) + " "
        MainWindow2.resize(1208, 611)
        MainWindow2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.graphViewer2 = QtWidgets.QLabel(self.centralwidget)
        self.graphViewer2.setGeometry(QtCore.QRect(540, 0, 641, 551))
        self.graphViewer2.setText("")
        self.graphViewer2.setPixmap(QtGui.QPixmap("Vertex_output.png"))
        self.graphViewer2.setScaledContents(True)
        self.graphViewer2.setObjectName("graphViewer2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.VerSet = QtWidgets.QLabel(self.centralwidget)
        self.VerSet.setGeometry(QtCore.QRect(340, 250, 191, 31))
        self.VerSet.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.VerSet.setText(k)
        self.VerSet.setAlignment(QtCore.Qt.AlignCenter)
        self.VerSet.setObjectName("VerSet")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.MinDevices = QtWidgets.QLabel(self.centralwidget)
        self.MinDevices.setGeometry(QtCore.QRect(220, 130, 91, 31))
        self.MinDevices.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.MinDevices.setText(str(n))
        self.MinDevices.setObjectName("MinDevices")
        self.MinDevices.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 360, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(180, 410, 131, 71))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("arrow.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 26))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.label.setText(_translate("MainWindow2", "Minimum Monitering Devices required :"))
        self.label_3.setText(_translate("MainWindow2", "Vertex Cover Set   :"))
        self.label_5.setText(_translate("MainWindow2", "Vertex Cover Set Representation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
