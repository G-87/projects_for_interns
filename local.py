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


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        widget = QWidget()
        layout = QVBoxLayout()
        self.resize(1000,600)

        self.btn_select = QPushButton("打开文件")
        self.view = QGraphicsView()
        layout.addWidget(self.view)
        layout.addWidget(self.btn_select)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.btn_select.clicked.connect(self.clicked)

    def clicked(self):
        scene = QGraphicsScene()
        
        files,flietype = QFileDialog.getOpenFileNames(self.btn_select,'All Files(*);TeXt Files(*.jepg)')
        for pixpath in files:
            print(pixpath)
            # file = files[0]
        # file.setPixmap(pixmap)
        # pix_img = QtGui.QPixmap()
        # label = QWidget.QLabel()
        # label.setMaximumSize(50,50)
        # label.setPixmap(pix_img)

            pixmap = QPixmap(str(pixpath))

            item = QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
        
            scene.addLine(10,0,0,0)
        # scene.addLine(0,0, 200,200)  # 画线
        # read files and get images
        self.view.setScene(scene)
        view.setScene(scene)

class CellImageText(QWidget):

    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()
        
        

    def initUI(self):
        self.setWindowTitle("picture")
        self.resize(1600, 900)
        layout = QHBoxLayout()
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
       
# class QSSLoader:

#     def __init__(self):
#         pass

#     @staticmethod
#     def read_qss_file(qss_file_name):
#         with open(qss_file_name,'r',encoding='UTF-8') as file:
#             return file.read()




if __name__ == "__main__":
    app = QApplication()
    window = MyMainWindow()
    # style_file = './style.qss'
    # style_sheet = QSSLoader.read_qss_file(style_file)
    # window.setStyleSheet(style_sheet)
    window.show()
    app.exec()
