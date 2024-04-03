import pymysql

class Professor:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS Professor (
                id INT NOT NULL NOT NULL AUTO_INCREMENT,
                name VARCHAR(35) NOT NULL,
                major VARCHAR(35) NOT NULL,
                email VARCHAR(35) NOT NULL,
                PRIMARY KEY (id)
            );
        """

        self.cur.execute(sql)
        self.db.commit()

    def get(self):
        sql = """
            SELECT * FROM professor
        """

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def select_by_name(self, dto):
        sql = """
            SELECT * FROM professor WHERE name = '{0}' AND major = '{1}'
        """.format(dto.name, dto.major)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, dto):
        sql = """
            INSERT INTO professor (name, major, email) VALUES('{0}', '{1}', '{2}')
        """.format(dto.name, dto.major, dto.email)
        self.cur.execute(sql)
        self.db.commit()