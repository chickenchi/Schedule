import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        print("connect ok")

    def add(self, task):
        sql = "insert into todo(task) values('{0}')".format(task['name'])
        self.cur.execute(sql)
        self.db.commit()

    def delete(self, index):
        sql = "delete from todo where id = ('{0}')".format(index)
        self.cur.execute(sql)
        self.db.commit()