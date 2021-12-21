# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 691)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.knnResult = QtWidgets.QLabel(self.centralwidget)
        self.knnResult.setGeometry(QtCore.QRect(170, 340, 91, 131))
        font = QtGui.QFont()
        font.setPointSize(43)
        self.knnResult.setFont(font)
        self.knnResult.setObjectName("knnResult")
        self.k_label = QtWidgets.QLabel(self.centralwidget)
        self.k_label.setGeometry(QtCore.QRect(91, 50, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.k_label.setFont(font)
        self.k_label.setObjectName("k_label")
        self.kSlider = QtWidgets.QSlider(self.centralwidget)
        self.kSlider.setGeometry(QtCore.QRect(90, 90, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kSlider.setFont(font)
        self.kSlider.setOrientation(QtCore.Qt.Horizontal)
        self.kSlider.setObjectName("kSlider")
        self.trainningSlider = QtWidgets.QSlider(self.centralwidget)
        self.trainningSlider.setGeometry(QtCore.QRect(90, 170, 471, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trainningSlider.setFont(font)
        self.trainningSlider.setOrientation(QtCore.Qt.Horizontal)
        self.trainningSlider.setObjectName("trainningSlider")
        self.k_value = QtWidgets.QSpinBox(self.centralwidget)
        self.k_value.setGeometry(QtCore.QRect(220, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.k_value.setFont(font)
        self.k_value.setObjectName("k_value")
        self.trainning_value = QtWidgets.QSpinBox(self.centralwidget)
        self.trainning_value.setGeometry(QtCore.QRect(220, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.trainning_value.setFont(font)
        self.trainning_value.setObjectName("trainning_value")
        self.selectImage = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.selectImage.setGeometry(QtCore.QRect(90, 490, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Thin")
        font.setPointSize(13)
        font.setKerning(False)
        self.selectImage.setFont(font)
        self.selectImage.setObjectName("selectImage")
        self.trainninglabel = QtWidgets.QLabel(self.centralwidget)
        self.trainninglabel.setGeometry(QtCore.QRect(90, 130, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        self.trainninglabel.setFont(font)
        self.trainninglabel.setObjectName("trainninglabel")
        self.recognization = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.recognization.setGeometry(QtCore.QRect(90, 570, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Thin")
        font.setPointSize(13)
        self.recognization.setFont(font)
        self.recognization.setObjectName("recognization")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-160, 240, 1171, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(110, 260, 471, 51))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.ResultLabel = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResultLabel.setFont(font)
        self.ResultLabel.setObjectName("ResultLabel")
        self.DataInputLabel = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DataInputLabel.setFont(font)
        self.DataInputLabel.setObjectName("DataInputLabel")
        self.clear = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(90, 530, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Thin")
        font.setPointSize(13)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.DataArea = QtWidgets.QLabel(self.centralwidget)
        self.DataArea.setGeometry(QtCore.QRect(330, 320, 261, 261))
        self.DataArea.setMouseTracking(False)
        self.DataArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DataArea.setFrameShape(QtWidgets.QFrame.Box)
        self.DataArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.DataArea.setLineWidth(4)
        self.DataArea.setMidLineWidth(0)
        self.DataArea.setText("")
        self.DataArea.setObjectName("DataArea")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 320, 261, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.Area_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.Area_Layout.setContentsMargins(0, 0, 0, 0)
        self.Area_Layout.setSpacing(0)
        self.Area_Layout.setObjectName("dArea_Layout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 23))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(11)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuInput = QtWidgets.QMenu(self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuMethod = QtWidgets.QMenu(self.menubar)
        self.menuMethod.setObjectName("menuMethod")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action1_MNIT_random_selection = QtWidgets.QAction(MainWindow)
        self.action1_MNIT_random_selection.setObjectName("action1_MNIT_random_selection")
        self.action2_Mouse = QtWidgets.QAction(MainWindow)
        self.action2_Mouse.setObjectName("action2_Mouse")
        self.actionD22 = QtWidgets.QAction(MainWindow)
        self.actionD22.setObjectName("actionD22")
        self.actionD23 = QtWidgets.QAction(MainWindow)
        self.actionD23.setObjectName("actionD23")
        self.menuInput.addAction(self.action1_MNIT_random_selection)
        self.menuInput.addAction(self.action2_Mouse)
        self.menuMethod.addAction(self.actionD22)
        self.menuMethod.addAction(self.actionD23)
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuMethod.menuAction())

        self.retranslateUi(MainWindow)
        self.kSlider.valueChanged['int'].connect(self.k_value.setValue) # type: ignore
        self.trainningSlider.valueChanged['int'].connect(self.trainning_value.setValue) # type: ignore
        self.action1_MNIT_random_selection.triggered['bool'].connect(self.selectImage.setDisabled) # type: ignore
        self.action2_Mouse.triggered['bool'].connect(self.selectImage.setEnabled) # type: ignore
        #buttons
        self.selectImage.clicked.connect(MainWindow.selectImage_callback)
        self.clear.clicked.connect(MainWindow.clear_callback)
        self.recognization.clicked.connect(MainWindow.recognization_callback)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.knnResult.setText(_translate("MainWindow", "9"))
        self.k_label.setText(_translate("MainWindow", "K - neighbors:"))
        self.selectImage.setText(_translate("MainWindow", "Random image"))
        self.selectImage.setDescription(_translate("MainWindow", "Extract a img from MNIST"))
        self.trainninglabel.setText(_translate("MainWindow", "Trainning size:"))
        self.recognization.setText(_translate("MainWindow", "Recognization"))
        self.ResultLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Result : </span></p></body></html>"))
        self.DataInputLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Data input area:</span></p></body></html>"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))
        self.menuMethod.setTitle(_translate("MainWindow", "Method"))
        self.action1_MNIT_random_selection.setText(_translate("MainWindow", "1: MNIT"))
        self.action2_Mouse.setText(_translate("MainWindow", "2:Mouse"))
        self.actionD22.setText(_translate("MainWindow", "D22"))
        self.actionD23.setText(_translate("MainWindow", "D23"))
