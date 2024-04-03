import pymysql

class Shop:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        print("connect ok")

    def a(self):
        1