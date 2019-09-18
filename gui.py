import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5 import uic,QtGui
from proje import veriTaban
class STOP(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.win = uic.loadUi(r"D:\proje1\STOP.ui")
        self.veriTaban = veriTaban
        self.win.btekle.clicked.connect(self.btekleclick)
        self.win.tbliste.doubleClicked.connect(self.btkaldirclick)
        self.win.show()
        self.yasak = []
        self.ID = []
    def btekleclick(self):
        giris = self.win.lbgiris.text()
        self.yasak.append(giris)
        sonuc = self.veriTaban.veriEkle(self,giris)
        

        if sonuc == 1:
            QMessageBox.information(self,"Sonuç","Kaydedildi")
            self.tabloyaEkle()

    def tabloyaEkle(self):
        satir = 0
        self.win.tbliste.clear()
        self.win.tbliste.setColumnCount(2)
        self.liste = self.veriTaban.tabloGetir(self)
        self.win.tbliste.setRowCount(20)
        for item in self.yasak :
            self.win.tbliste.setItem(satir,1,QTableWidgetItem(str(item)))
            satir += 1
    @pyqtSlot()
    def btkaldirclick(self):
        print("\n")
        for currentQTableWidgetItem in self.win.tbliste.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = STOP()
    sys.exit(app.exec_())