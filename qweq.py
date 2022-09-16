import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.Qt import *
from socket import if_nameindex
import sys
import os
import cv2 as cv
import numpy as np
from pathlib import Path
from os import path,walk
from PySide6.QtWidgets import QHBoxLayout,QApplication,QPushButton,QWidget,QSpacerItem,QSizePolicy,QVBoxLayout,QGraphicsScene, QGraphicsView,QMessageBox,QFileDialog, QMainWindow,  QGraphicsPixmapItem
from PySide6 import QtWidgets
from PySide6.QtGui import QPixmap,QImage



class CellImageText(QWidget):

    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()
        
        

    def initUI(self):
        self.setWindowTitle("picture")
        self.resize(1600, 900)
        layout = QHBoxLayout()
        style = QStyleOptionTab()
        # self.style.setIconSize(300,200)
        self.tableWidget = QTableWidget()

        # self.tableWidget.setIconSize(QSize(300, 200))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)


        self.tableWidget.setHorizontalHeaderLabels(['1', '2', '3', '4','5'])

        
        for i in range(5):
            self.tableWidget.setColumnWidth(i, 400)

        
        for i in range(5):
            self.tableWidget.setRowHeight(i, 400)

        for k in range(15):
            i = k // 5 #行
            j = k % 5 #列
            item = QTableWidgetItem()
            item.setIcon(QIcon("/home/user/h2/img/50.jpeg"))
            # item.setIconSize(QSize(300,200)
            self.tableWidget.setItem(i, j, item)

        layout.addWidget(self.tableWidget)
        self.setLayout(layout)


# button = QPushButton()
# button.clicked.connect(self.initUI) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = CellImageText()
    main.show()

    sys.exit(app.exec())