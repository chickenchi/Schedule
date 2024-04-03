import pymysql

class Course:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS course (
                id INT NOT NULL AUTO_INCREMENT,
                name VARCHAR(35) NOT NULL,
                credit int NOT NULL,
                PRIMARY KEY (id)
            );
        """

        self.cur.execute(sql)
        self.db.commit()

    def get(self):
        sql = """
            SELECT * FROM course
        """

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def select_by_name(self, dto):
        sql = """
            SELECT * FROM course WHERE name = '{0}'
        """.format(dto.name)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, dto):
        sql = """
            INSERT INTO course (name, credit) VALUES('{0}', {1})
        """.format(dto.name, dto.credit)
        self.cur.execute(sql)
        self.db.commit()