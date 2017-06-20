from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class HelloWorld(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QGridLayout()

        self.hello_label = QLabel("Hello Yang lets play mobile legends!")
        self.line_edit = QLineEdit()
        self.close_button = QPushButton("Close")

        layout.addWidget(self.hello_label, 0, 0)
        layout.addWidget(self.line_edit, 1, 0)
        layout.addWidget(self.close_button, 2, 1)

        self.setLayout(layout)

        self.close_button.clicked.connect(self.close)
        self.line_edit.textChanged.connect(self.changeTextLabel)

    def changeTextLabel(self, text):
        self.hello_label.setText(text)

app = QApplication(sys.argv)
dialog = HelloWorld()
dialog.show()
app.exec_()