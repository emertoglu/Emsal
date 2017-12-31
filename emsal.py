from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        print(QApplication.screens())
        self.ayarlar()
        self.mainEmsal()
        self.set_layout()

    def ayarlar(self):
        self.resize(800, 600)
        self.setWindowTitle("Emsal")
        
    def mainEmsal(self):
        self.ongosterim = QLabel()
        self.ongosterim.setPixmap(self.preview_screen.scaled(750,550, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.btn_emsali_kaydet = QPushButton("Emsal'i Kaydet")
        self.btn_yeni_emsal = QPushButton("Yeni Emsal Al")

        self.btn_emsali_kaydet.clicked.connect(self.emsali_kaydet)
        self.btn_yeni_emsal.clicked.connect(self.yeni_emsal)

    def set_layout(self):
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.ongosterim, 0, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.btn_emsali_kaydet, 2,0, alignment=Qt.AlignLeft)
        self.layout.addWidget(self.btn_yeni_emsal, 2, 0, alignment=Qt.AlignRight)
        self.setLayout(self.layout)

    def emsali_kaydet(self):
        img, _ = QFileDialog.getSaveFileName(self,"Emsal - Seyahatname", filter="PNG(*.png);; JPEG(*.jpg)")
        if img[-3:] == "png":
            self.preview_screen.save(img, "png")
        elif img[-3:] == "jpg":
            self.preview_screen.save(img, "jpg")
        exit
    def yeni_emsal(self):
        self.hide()
        sure = 1000
        QTimer.singleShot(sure, self.emsal_al)

    def emsal_al(self):
        self.preview_screen = QApplication.primaryScreen().grabWindow(0)
        self.ongosterim.setPixmap(self.preview_screen.scaled(750,550, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.show()


root = QApplication(sys.argv)
app = MainWindow()
app.show()
sys.exit(root.exec_())
