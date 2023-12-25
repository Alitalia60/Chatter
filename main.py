import sys
from PyQt6.QtWidgets import QApplication, QWidget

from message import Ui_Form as UI_Message
from main_window import Ui_Form as UI_Main


class Message(QWidget):
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.ui_message = UI_Message()
        self.ui_message.setupUi(self)
        print(self.ui_message)
        # self.ui_message.show()
        # self.ui_message.lbl_message.setText(self.text)


class Chatter(QWidget):

    def __init__(self):
        super().__init__()

        self.ui_main = UI_Main()
        self.ui_main.setupUi(self)
        # self.ui.show()
        self.ui_main.btn_send.clicked.connect(self.send_message)

    def send_message(self):
        print('Message send')
        message = Message('New message widget')
        # message.show()

        # message_item = QLabel(self.ui.sa_message_list_content)
        # message_item.setText('New message')

        self.ui_main.vl_message_list.addWidget(message)
        # message_item.show()
        # QScrollArea()
        # self.ui.message_list.


if __name__ == '__main__':
    app = QApplication(sys.argv)

    chatter = Chatter()
    chatter.show()
    sys.exit(app.exec())
