from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

class UI(QWidget):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("addHostgui.ui", self)

        def okBtn(self):
            unit = self.findChild(QLineEdit, "unitET")
            ip = self.findChild(QLineEdit, "ipET")
            division = self.findChild(QLineEdit, "divisionET")
            commander = self.findChild(QLineEdit, "commanderET")

            with open("tableInfo.txt", "a", encoding='utf-8') as myfile:
                myfile.write(division.text() + "," + unit.text() + "," + commander.text() + "," + ip.text() + "\n")

        ok = self.findChild(QPushButton, "okBTN")
        ok.clicked.connect(okBtn)

        self.show()

app = QApplication(sys.argv)
window = UI()
app.exec_()