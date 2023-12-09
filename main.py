# Importações
import os
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from ui_main import Ui_MainWindow
import sys

# Definindo classe | Botão open
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("FS - File Organizer")
        appIcon = QIcon("img/logo.png")
        self.setWindowIcon(appIcon)
    
        self.file = ''

        self.btn_open.clicked.connect(self.open_path)
        self.btn_organize.clicked.connect(self.organizer)
    
    # Configurando o botão de path (Open)
    def open_path(self):
        self.file = QFileDialog.getExistingDirectory(self, str("Seus Arquivos"), '/home', QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        self.txt_path.setText(self.file)
        self.file = str(self.file)
    
    # Configurando a funcionalidade para organizar (Organizer)
    def organizer(self):
        path = self.file
        files = os.listdir(path)

        for file in files:
            filename, extension = os.path.splitext(file)
            extension = extension[1:]
            if os.path.exists(path + '/' + extension):
                shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

            else:
                os.makedirs(path + '/' + extension)
                shutil.move(path + '/' + file, path + '/' + extension)

        # Mensagem de sucesso na operação
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Arquivos organizados com sucesso!")
        msg.exec_()

# Executando a Interface
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()