import pymysql

class Student:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS student (
                id INT NOT NULL NOT NULL AUTO_INCREMENT,
                number INT NOT NULL,
                name VARCHAR(35) NOT NULL,
                gender VARCHAR(35) NOT NULL,
                PRIMARY KEY (id)
            );
        """

        self.cur.execute(sql)
        self.db.commit()

    def get(self):
        sql = """
            SELECT * FROM student
        """
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def select_by_number(self, dto):
        sql = """
            SELECT * FROM student WHERE number = {0}
        """.format(dto.number)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, dto):
        sql = """
            INSERT INTO student (number, name, gender) VALUES({0}, '{1}', '{2}')
        """.format(dto.number, dto.name, dto.gender)
        self.cur.execute(sql)
        self.db.commit()