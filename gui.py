#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 tutorial
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a button')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 80)

        self.setGeometry(1500, 120, 350, 800)
        self.setWindowTitle('ChatApp')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window()
    sys.exit(app.exec_())
