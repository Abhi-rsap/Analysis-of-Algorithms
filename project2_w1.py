from PyQt5 import QtCore, QtGui, QtWidgets
from project2_w2 import Ui_MainWindow2
from greedy import text_and_run

import networkx as nx
import matplotlib.pyplot as plt


class Ui_MainWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def create_Graph(self):
        g= nx.Graph()
        with open('input.txt') as f:
                for line in f:
                        line = line.strip()
                        l = line.split(" ")
                        u = int(l[0])
                        v = int(l[1])
                        g.add_edge(u,v)
        color_map = []
        for node in g:
                color_map.append('green')
        nx.draw(g,with_labels=True,node_color = color_map)
        plt.savefig("graph1.png")
        plt.clf()
        return g

    def result(self,v_list,g):
        color_map = []
        for node in g:
                color_map.append('blue')  
        
        for i in v_list:
                color_map[i-1] = 'red'
        nx.draw(g, node_color=color_map, with_labels=True)
        plt.savefig("Vertex_output.png")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 611)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.NodeLinksEB = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("node links"))
        self.NodeLinksEB.setGeometry(QtCore.QRect(130, 450, 93, 28))
        self.NodeLinksEB.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NodeLinksEB.setFont(font)
        self.NodeLinksEB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NodeLinksEB.setStyleSheet("background-color: rgb(81, 204, 44);\n"
"color: rgb(255, 255, 255);")
        self.NodeLinksEB.setDefault(False)
        self.NodeLinksEB.setObjectName("NodeLinksEB")
        self.graphViewer = QtWidgets.QLabel(self.centralwidget)
        self.graphViewer.setGeometry(QtCore.QRect(550, 10, 641, 551))
        self.graphViewer.setText("")
        self.graphViewer.setPixmap(QtGui.QPixmap("graph0.png"))
        self.graphViewer.setScaledContents(True)
        self.graphViewer.setObjectName("graphViewer")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 511, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.FirstContinue = QtWidgets.QPushButton(self.centralwidget)
        self.FirstContinue.clicked.connect(self.openWindow)
        self.FirstContinue.setGeometry(QtCore.QRect(170, 510, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.FirstContinue.setFont(font)
        self.FirstContinue.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.FirstContinue.setObjectName("FirstContinue")
        self.NoOfNodesCB = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("clear NoOfNodesTB"))
        self.NoOfNodesCB.setGeometry(QtCore.QRect(270, 200, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NoOfNodesCB.setFont(font)
        self.NoOfNodesCB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NoOfNodesCB.setStyleSheet("background-color: rgb(255, 65, 68);\n"
"color: rgb(255, 255, 255);")
        self.NoOfNodesCB.setObjectName("NoOfNodesCB")
        self.NoOfNodesEB = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("no of nodes"))
        self.NoOfNodesEB.setGeometry(QtCore.QRect(130, 200, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NoOfNodesEB.setFont(font)
        self.NoOfNodesEB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NoOfNodesEB.setStyleSheet("background-color: rgb(81, 204, 44);\n"
"color: rgb(255, 255, 255);")
        self.NoOfNodesEB.setObjectName("NoOfNodesEB")
        self.NodeLinksTB = QtWidgets.QTextEdit(self.centralwidget)
        self.NodeLinksTB.setGeometry(QtCore.QRect(50, 310, 451, 111))
        self.NodeLinksTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NodeLinksTB.setObjectName("NodeLinksTB")
        self.NodeLinksCB = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("clear NodeLinksTB"))
        self.NodeLinksCB.setGeometry(QtCore.QRect(270, 450, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NodeLinksCB.setFont(font)
        self.NodeLinksCB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NodeLinksCB.setMouseTracking(True)
        self.NodeLinksCB.setStyleSheet("background-color: rgb(255, 65, 68);\n"
"color: rgb(255, 255, 255);")
        self.NodeLinksCB.setObjectName("NodeLinksCB")
        self.NoOfNodesTB = QtWidgets.QLineEdit(self.centralwidget)
        self.NoOfNodesTB.setGeometry(QtCore.QRect(300, 140, 191, 31))
        self.NoOfNodesTB.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NoOfNodesTB.setObjectName("NoOfNodesTB")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 270, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 26))
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
        self.NodeLinksEB.setText(_translate("MainWindow", "Enter"))
        self.label.setText(_translate("MainWindow", "Network Monitoring Optimizer"))
        self.FirstContinue.setText(_translate("MainWindow", "Continue"))
        self.NoOfNodesCB.setText(_translate("MainWindow", "Clear"))
        self.NoOfNodesEB.setText(_translate("MainWindow", "Enter"))
        self.NodeLinksCB.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "Enter Number of Nodes    :"))
        self.label_3.setText(_translate("MainWindow", "Enter Node Links :"))

    def press_it(self, pressed):
        if pressed == "no of nodes":
            non = self.NoOfNodesTB.text()
            print(non)

        elif pressed == "node links":
                nodelinks = self.NodeLinksTB.toPlainText()
                print(nodelinks)
                with open('input.txt', 'w') as f:
                        f.write(nodelinks)
                gr = self.create_Graph()
                print("grrr",gr.nodes())
                self.graphViewer.setPixmap(QtGui.QPixmap("graph1.png"))

                vertex_cover = text_and_run(gr)
                print(vertex_cover, len(vertex_cover))

                self.result(vertex_cover,gr)

                with open('output.txt', 'w') as f:
                        for i in vertex_cover :

                            f.write(str(i)+" ")

        elif pressed == "clear NodeLinksTB":
                self.NodeLinksTB.setText("")

        elif pressed == "clear NoOfNodesTB":
                self.NoOfNodesTB.setText("")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
