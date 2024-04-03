import pymysql

class Reservation:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS reservation (
                id INT(11) AUTO_INCREMENT,
                name VARCHAR(45) NOT NULL,
                email VARCHAR(45) NOT NULL,
                phone VARCHAR(45) NOT NULL,
                num_guests INT NOT NULL,
                date_time DATETIME NOT NULL,
                restaurant_id INT NOT NULL,
                FOREIGN KEY (restaurant_id) REFERENCES restaurant (id),
                PRIMARY KEY (id)
            );
        """

        self.cur.execute(sql)
        self.db.commit()

    def post(self, dto):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = "INSERT INTO reservation(name, email, phone, num_guests, date_time, restaurant_id) VALUES('{0}', '{1}', '{2}', {3}, '{4}', '{5}')".format(dto.name, dto.email, dto.phone, dto.num_guests, dto.date_time, dto.restaurant_id)
        self.cur.execute(sql)
        self.db.commit()

    def get(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = "SELECT * FROM reservation"

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def remove(self, index):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = "DELETE FROM reservation WHERE id = {0}".format(index)
        self.cur.execute(sql)
        self.db.commit()