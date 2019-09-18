import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui,QtCore
from p1 import baglanti
import requests 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
class extension(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__()
        self.veriTabani = baglanti()
        self.win = uic.loadUi(r"D:\Chrome extension\Chrome extension\STOP.ui")
        self.win.btekle.clicked.connect(self.btekleclick)
        self.liste = []
        self.liste1 = []
        self.win.show()
        self.listeDoldur()
        self.win.tbliste.itemDoubleClicked.connect(self.on_click)
        self.r = requests.get("https://www.youtube.com/watch?v=UqVMKxzXb9c")
        self.soup = bs(self.r.content,"html.parser")
        self.baslik = self.soup.find_all("title")
        self.baslik1 = self.baslik[0].text
        self.liste2 = str(self.baslik1).upper().split()
        for i in range (0,5):
            self.liste1.append(self.liste[i][1].upper())
        for item in self.liste1:
            if item in self.liste2:
                print("{} var".format(item))
            else:
                print("sorun yok")
    def btekleclick(self):
        giris = self.win.lbgiris.text()
        sonuc = self.veriTabani.veriEkle(giris)
        if sonuc == 1:
            QMessageBox.information(self,"Sonuc","Kaydedildi")
            self.listeDoldur()
        else:
            QMessageBox.information(self,"Sonuc","Kaydedilmedi")

    
    def listeDoldur(self):
        satir = 0
        self.win.tbliste.clear()
        self.win.tbliste.setColumnCount(2)
        self.liste = self.veriTabani.tabloGetir()
        self.win.tbliste.setRowCount(20)
        for a,b in self.liste:
            self.win.tbliste.setItem(satir, 0, QTableWidgetItem(str(a)))
            self.win.tbliste.setItem(satir, 1, QTableWidgetItem(str(b)))
            satir+=1
    @pyqtSlot()
    def on_click(self):
        # print(self.liste[self.win.tbliste.currentRow()])
        # alan = str(self.liste[self.win.tbliste.currentRow()][1])
        # print(alan)
        # ID = str(self.liste[self.win.tbliste.currentRow()][0])
        # print(ID)
        # self.win.lbgiris.setText(alan)
        # a = self.veriTabani.veriGuncelle(alan,ID)
        # print(a)
        ID = str(self.liste[self.win.tbliste.currentRow()][0])
        self.win.lbcikis.setText(str(ID))
        silinenKayit = self.win.lbcikis.text()
        print(silinenKayit)
        print(ID)
        if silinenKayit != "":
            print("buraya geldi")
            self.veriTabani.veriSil(int(ID))
            QMessageBox.information(self,"Sonuc","Silindi")
            self.listeDoldur()
        else:
            QMessageBox.information(self,"Sonuc","Silinemedi")
           

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = extension()
    sys.exit(app.exec_())









































if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = extension()
    sys.exit(app.exec_())