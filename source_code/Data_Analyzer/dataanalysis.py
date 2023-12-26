# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataanalysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 850)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 544, 763))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 18pt;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setStyleSheet("font: 16pt;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font: 18pt;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setStyleSheet("")
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("font: 18pt;")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setStyleSheet("font: 16pt;")
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 543, 763))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.frame_6)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setMinimumSize(QtCore.QSize(50, 20))
        self.radioButton_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.radioButton_2.setStyleSheet("font: 12pt;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setStyleSheet("font: 12pt;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.frame_6)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.addWidget(self.scrollArea_2, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_data = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_data.setStyleSheet("")
        self.menuOpen_data.setObjectName("menuOpen_data")
        self.menuRe_analysis = QtWidgets.QMenu(self.menubar)
        self.menuRe_analysis.setObjectName("menuRe_analysis")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_project = QtWidgets.QAction(MainWindow)
        self.actionOpen_project.setObjectName("actionOpen_project")
        self.actionExport_results = QtWidgets.QAction(MainWindow)
        self.actionExport_results.setObjectName("actionExport_results")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionmzML = QtWidgets.QAction(MainWindow)
        self.actionmzML.setObjectName("actionmzML")
        self.actioncdf = QtWidgets.QAction(MainWindow)
        self.actioncdf.setObjectName("actioncdf")
        self.actionIdentification = QtWidgets.QAction(MainWindow)
        self.actionIdentification.setObjectName("actionIdentification")
        self.actionmzML_2 = QtWidgets.QAction(MainWindow)
        self.actionmzML_2.setObjectName("actionmzML_2")
        self.actioncdf_2 = QtWidgets.QAction(MainWindow)
        self.actioncdf_2.setObjectName("actioncdf_2")
        self.actionAll_processing = QtWidgets.QAction(MainWindow)
        self.actionAll_processing.setObjectName("actionAll_processing")
        self.menuOpen_data.addAction(self.actionmzML)
        self.menuOpen_data.addAction(self.actioncdf)
        self.menuFile.addAction(self.menuOpen_data.menuAction())
        self.menuFile.addAction(self.actionOpen_project)
        self.menuFile.addAction(self.actionExport_results)
        self.menuFile.addAction(self.actionExit)
        self.menuRe_analysis.addAction(self.actionAll_processing)
        self.menuRe_analysis.addAction(self.actionIdentification)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRe_analysis.menuAction())

        self.retranslateUi(MainWindow)
        self.actionmzML.triggered.connect(MainWindow.open_data_mzML) # type: ignore
        self.actioncdf.triggered.connect(MainWindow.open_data_cdf) # type: ignore
        self.actionExit.triggered.connect(MainWindow.close) # type: ignore
        self.radioButton.clicked['bool'].connect(MainWindow.check_qualitative_group) # type: ignore
        self.comboBox_2.activated['QString'].connect(MainWindow.chooseRTinfo) # type: ignore
        self.spinBox.valueChanged['int'].connect(MainWindow.min_ion_num) # type: ignore
        self.actionOpen_project.triggered.connect(MainWindow.open_project) # type: ignore
        self.actionIdentification.triggered.connect(MainWindow.identification) # type: ignore
        self.actionExport_results.triggered.connect(MainWindow.save) # type: ignore
        self.actionAll_processing.triggered.connect(MainWindow.all_processing) # type: ignore
        self.radioButton_2.clicked['bool'].connect(MainWindow.ischange) # type: ignore
        self.pushButton.clicked.connect(MainWindow.export_msp) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataAnalyzer-WTV"))
        self.label.setText(_translate("MainWindow", "RT unit:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "s"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "min"))
        self.label_2.setText(_translate("MainWindow", "Only show identified component:"))
        self.label_3.setText(_translate("MainWindow", "Component ions number filter:"))
        self.radioButton_2.setText(_translate("MainWindow", "Spectra comparison"))
        self.pushButton.setText(_translate("MainWindow", "Export spectra"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_data.setTitle(_translate("MainWindow", "Open data"))
        self.menuRe_analysis.setTitle(_translate("MainWindow", "Re-analysis"))
        self.actionOpen_project.setText(_translate("MainWindow", "Open project"))
        self.actionExport_results.setText(_translate("MainWindow", "Export results"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionmzML.setText(_translate("MainWindow", "mzML"))
        self.actioncdf.setText(_translate("MainWindow", "cdf"))
        self.actionIdentification.setText(_translate("MainWindow", "Identification"))
        self.actionmzML_2.setText(_translate("MainWindow", "mzML"))
        self.actioncdf_2.setText(_translate("MainWindow", "cdf"))
        self.actionAll_processing.setText(_translate("MainWindow", "All processing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
