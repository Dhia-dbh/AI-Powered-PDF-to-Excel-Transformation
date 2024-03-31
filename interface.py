from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from main import convert_all_imgs


def play():
    path=windows.lineEdit.text()
    convert_all_imgs(path)
    pass



app= QApplication([])
windows= loadUi("pdftocsv.ui")
windows.show()
windows.commandLinkButton.clicked.connect(play)
app.exec_()
