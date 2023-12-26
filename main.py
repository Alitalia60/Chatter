import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel

from message import Ui_Form as UI_Message
from main_window import Ui_MainWindow as UI_Main


class Message(QMainWindow):
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.ui_message = UI_Message()
        self.ui_message.setupUi(self)
        print(self.ui_message)
        # self.ui_message.show()
        # self.ui_message.lbl_message.setText(self.text)


class Chatter(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui_main = UI_Main()
        self.ui_main.setupUi(self)
        # self.ui.show()
        self.ui_main.btn_send.clicked.connect(self.send_message)

    def send_message(self):
        # print(type(self.ui_main.sa_messages.children()))
        # print(type(self.ui_main.vl_message_list.children()))
        for item in self.ui_main.sa_messages.children():
        # for item in self.ui_main.vl_message_list.children():
            print(item.objectName())
        # message = Message('New message widget')
        # message = QLabel(self.ui_main)
        # self.ui_main.vl_message_list.addWidget(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    chatter = Chatter()
    chatter.show()
    sys.exit(app.exec())
