#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QMessageBox, QGridLayout, QTextEdit, \
                            QDesktopWidget
from PyQt5.QtGui import QIcon, QFont, QTextCursor

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        inputText = QTextEdit()

        logText = QTextEdit()
        logText.setReadOnly(True)
        font = logText.font()
        font.setFamily("Courier")
        font.setPointSize(10)
        logText.moveCursor(QTextCursor.End)
        sb = logText.verticalScrollBar()
        sb.setValue(sb.maximum())

        grid = QGridLayout()
        grid.addWidget(logText, 0, 0, 2, 1)
        grid.addWidget(inputText, 2, 0, 1, 1)

        self.setLayout(grid)

        self.resize(700, 400)
        self.center()
        self.setWindowTitle('ChatApp')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
