# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectCamera(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_SelectCamera, self).__init__()
        self.setupUi(self)
    def setupUi(self, SelectCamera):
        SelectCamera.setObjectName("SelectCamera")
        SelectCamera.resize(341, 180)
        self.OK_pushButton = QtWidgets.QPushButton(SelectCamera)
        self.OK_pushButton.setGeometry(QtCore.QRect(170, 140, 75, 23))
        self.OK_pushButton.setObjectName("OK_pushButton")
        self.cancel_pushButton = QtWidgets.QPushButton(SelectCamera)
        self.cancel_pushButton.setGeometry(QtCore.QRect(260, 140, 75, 23))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.tabWidget = QtWidgets.QTabWidget(SelectCamera)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 321, 121))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.label.setObjectName("label")
        self.url_lineEdit = QtWidgets.QLineEdit(self.tab)
        self.url_lineEdit.setGeometry(QtCore.QRect(40, 50, 241, 21))
        self.url_lineEdit.setObjectName("url_lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(20, 40, 89, 16))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 40, 89, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 40, 89, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(SelectCamera)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SelectCamera)

    def retranslateUi(self, SelectCamera):
        _translate = QtCore.QCoreApplication.translate
        SelectCamera.setWindowTitle(_translate("SelectCamera", "摄像头选择"))
        self.OK_pushButton.setText(_translate("SelectCamera", "确定"))
        self.cancel_pushButton.setText(_translate("SelectCamera", "取消"))
        self.label.setText(_translate("SelectCamera", "请输入网络摄像头URL地址："))
        self.url_lineEdit.setText(_translate("SelectCamera", "rtsp://admin:b210b210@192.168.1.64:554/11"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("SelectCamera", "网络摄像头"))
        self.radioButton.setText(_translate("SelectCamera", "接口0"))
        self.radioButton_2.setText(_translate("SelectCamera", "接口1"))
        self.radioButton_3.setText(_translate("SelectCamera", "接口2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("SelectCamera", "USB摄像头"))
