import pymysql

class PostDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        print("connect ok")

    def get(self):
        sql = "SELECT * FROM posts"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def call(self, index):
        sql = "SELECT * FROM posts WHERE id = {0}".format(index) # .format('안뇽')
        self.cur.execute(sql)
        result = self.cur.fetchall()
        print(result)
        return result

    def add(self, posts):
        sql = "INSERT INTO posts(title, content, author) VALUES('{0}', '{1}', '{2}')".format(posts['title'], posts['content'], posts['author'])
        self.cur.execute(sql)
        self.db.commit()

    def delete(self, index):
        sql = "DELETE FROM posts WHERE id = {0}".format(index)
        self.cur.execute(sql)
        self.db.commit()

    def revision(self, posts, index):
        print(posts['title'], posts['content'], posts['author'])
        sql = "UPDATE posts SET title = '{0}', content = '{1}', author = '{2}' WHERE id = {3}".format(posts['title'], posts['content'], posts['author'], index)
        self.cur.execute(sql)
        self.db.commit()
        
# get 함수 정의(select * from where)