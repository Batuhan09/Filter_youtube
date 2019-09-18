import sqlite3 as sql

class baglanti():
    def __init__(self):
        self.adres = r"D:\Chrome extension\Chrome extension\yasaklar.db"

    def veriEkle(self,yasak):
        try:
            import sqlite3
            db = sqlite3.connect(self.adres)
            cursor = db.cursor()
            cursor.execute("""insert into YASAKLAR (ALANLAR) values("{}")""".format(yasak))
            db.commit()
            return 1
        except:
            return 0
        finally:
            db.close()
    def veriGuncelle(self,yasak,ID):
        try:
            import sqlite3
            db = sqlite3.connect(self.adres)
            cursor = db.cursor()
            cursor.execute("""update yasaklar set ID = {0},ALANLAR = {1}""".format(ID,yasak))
            db.commit()
            return 1 
        except:
            return 0
        finally:
            db.close()
    def veriSil(self,ID):
        try:
            import sqlite3
            db = sqlite3.connect(self.adres)
            cursor = db.cursor()
            cursor.execute("""delete from yasaklar where İD = {}""".format(ID))
            db.commit()
            return 1 
        except:
            return 0 
        finally:
            db.close()
    def tabloGetir(self):
        
        import sqlite3
        db = sqlite3.connect(self.adres)
        cursor = db.cursor()
        cursor.execute("""select * from yasaklar """)
        return cursor.fetchall()
       