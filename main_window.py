# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 420)
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 641, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(parent=self.layoutWidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 283, 375))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sa_message_list = QtWidgets.QScrollArea(parent=self.layoutWidget)
        self.sa_message_list.setWidgetResizable(True)
        self.sa_message_list.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.sa_message_list.setObjectName("sa_message_list")
        self.sa_message_list_content = QtWidgets.QWidget()
        self.sa_message_list_content.setGeometry(QtCore.QRect(0, 0, 340, 265))
        self.sa_message_list_content.setObjectName("sa_message_list_content")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.sa_message_list_content)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 321, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vl_message_list = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vl_message_list.setContentsMargins(0, 0, 0, 0)
        self.vl_message_list.setObjectName("vl_message_list")
        self.sa_message_list.setWidget(self.sa_message_list_content)
        self.verticalLayout_2.addWidget(self.sa_message_list)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.te_message = QtWidgets.QTextEdit(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_message.sizePolicy().hasHeightForWidth())
        self.te_message.setSizePolicy(sizePolicy)
        self.te_message.setMinimumSize(QtCore.QSize(0, 25))
        self.te_message.setMaximumSize(QtCore.QSize(16777215, 100))
        self.te_message.setBaseSize(QtCore.QSize(0, 30))
        self.te_message.setObjectName("te_message")
        self.horizontalLayout.addWidget(self.te_message)
        self.btn_send = QtWidgets.QPushButton(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_send.sizePolicy().hasHeightForWidth())
        self.btn_send.setSizePolicy(sizePolicy)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout.addWidget(self.btn_send)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_send.setText(_translate("Form", "send"))