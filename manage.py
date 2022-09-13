from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QFileDialog
app = QApplication([])

def PICTURE():
    # # self.img_path: Path = QFileDialog.getExistingDirectory(self.vmd, "local image dir selection")
    # QString_file_path = QFileDialog::getExistingDirectory(this,"home/user/h2/img","./");
    # if(file_path.isEmpty())
    # {
    #     return;
    # }else{
    #     qDebug() << file_path << endl;
    # }

window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('图片查看')

textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("请输入")
textEdit.move(10,25)
textEdit.resize(300,350)

button = QPushButton('插入图片', window)
button.move(380,80)
button.clicked.connect(self.PICTURE)


window.show()

app.exec_()