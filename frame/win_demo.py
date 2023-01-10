# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1221, 660)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.video_label = QtWidgets.QLabel(self.centralwidget)
        self.video_label.setAutoFillBackground(False)
        self.video_label.setStyleSheet("QLabel{background-color:rgb(225, 247, 255);}")
        self.video_label.setText("")
        self.video_label.setObjectName("video_label")
        self.horizontalLayout.addWidget(self.video_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.select_video = QtWidgets.QPushButton(self.centralwidget)
        self.select_video.setObjectName("select_video")
        self.horizontalLayout_4.addWidget(self.select_video)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.select_camera = QtWidgets.QPushButton(self.centralwidget)
        self.select_camera.setObjectName("select_camera")
        self.horizontalLayout_4.addWidget(self.select_camera)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_2.addWidget(self.play_button)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.suspend_button = QtWidgets.QPushButton(self.centralwidget)
        self.suspend_button.setObjectName("suspend_button")
        self.horizontalLayout_2.addWidget(self.suspend_button)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.continue_button = QtWidgets.QPushButton(self.centralwidget)
        self.continue_button.setObjectName("continue_button")
        self.horizontalLayout_2.addWidget(self.continue_button)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.line_ch_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.line_ch_1.setObjectName("line_ch_1")
        self.horizontalLayout_7.addWidget(self.line_ch_1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout_7.addWidget(self.lineEdit_1)
        self.line_ch_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.line_ch_2.setObjectName("line_ch_2")
        self.horizontalLayout_7.addWidget(self.line_ch_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_7.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.line_ch_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.line_ch_3.setObjectName("line_ch_3")
        self.horizontalLayout_8.addWidget(self.line_ch_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_8.addWidget(self.lineEdit_3)
        self.line_ch_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.line_ch_4.setObjectName("line_ch_4")
        self.horizontalLayout_8.addWidget(self.line_ch_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_8.addWidget(self.lineEdit_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.progress_label = QtWidgets.QLabel(self.centralwidget)
        self.progress_label.setObjectName("progress_label")
        self.verticalLayout_5.addWidget(self.progress_label)
        self.fps_label = QtWidgets.QLabel(self.centralwidget)
        self.fps_label.setObjectName("fps_label")
        self.verticalLayout_5.addWidget(self.fps_label)
        self.label_line_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_line_1.setObjectName("label_line_1")
        self.verticalLayout_5.addWidget(self.label_line_1)
        self.label_line_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_line_2.setObjectName("label_line_2")
        self.verticalLayout_5.addWidget(self.label_line_2)
        self.label_line_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_line_3.setObjectName("label_line_3")
        self.verticalLayout_5.addWidget(self.label_line_3)
        self.label_line_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_line_4.setObjectName("label_line_4")
        self.verticalLayout_5.addWidget(self.label_line_4)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "行人检测"))
        self.select_video.setText(_translate("MainWindow", "选择视频"))
        self.select_camera.setText(_translate("MainWindow", "选择摄像头"))
        self.play_button.setText(_translate("MainWindow", "播放"))
        self.suspend_button.setText(_translate("MainWindow", "暂停"))
        self.continue_button.setText(_translate("MainWindow", "继续"))
        self.line_ch_1.setText(_translate("MainWindow", "线条1"))
        self.line_ch_2.setText(_translate("MainWindow", "线条2"))
        self.line_ch_3.setText(_translate("MainWindow", "线条3"))
        self.line_ch_4.setText(_translate("MainWindow", "线条4"))
        self.progress_label.setText(_translate("MainWindow", "播放进度：--/--"))
        self.fps_label.setText(_translate("MainWindow", "FPS："))
        self.label_line_1.setText(_translate("MainWindow", "线条1："))
        self.label_line_2.setText(_translate("MainWindow", "线条2："))
        self.label_line_3.setText(_translate("MainWindow", "线条3："))
        self.label_line_4.setText(_translate("MainWindow", "线条4："))
