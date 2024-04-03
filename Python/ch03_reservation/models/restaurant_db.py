import pymysql

class Restaurant:
    def __init__(self):

        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS restaurant (
                id INT AUTO_INCREMENT,
                name VARCHAR(45) NOT NULL,
                address VARCHAR(45) NOT NULL,
                phone VARCHAR(45) NOT NULL,
                PRIMARY KEY (id)
            )
        """

        self.cur.execute(sql)
        self.db.commit()

        sql = """
            INSERT INTO restaurant(name, address, phone)
            select '컴포즈', '강서구', '051-111-1111'
            FROM dual
            WHERE NOT EXISTS (
                SELECT * FROM restaurant
                WHERE name = '컴포즈' and address = '강서구' and phone = '051-111-1111'
            )
        """

        self.cur.execute(sql)
    def get(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()

        sql = """SELECT * FROM restaurant;"""

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result