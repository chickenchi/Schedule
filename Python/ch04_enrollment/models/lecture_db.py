import pymysql

class Lecture:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS Lecture (
                id INT NOT NULL NOT NULL AUTO_INCREMENT,
                professor_id INT NOT NULL,
                course_id VARCHAR(35) NOT NULL,
                day VARCHAR(35) NOT NULL,
                start_time TIME NOT NULL,
                PRIMARY KEY (id)
            );
        """

        self.cur.execute(sql)
        self.db.commit()

    def get(self):
        sql = """
                SELECT c.name, p.name, p.major, c.credit, l.day, l.start_time, DATE_ADD(l.start_time, INTERVAL c.credit HOUR)
                FROM lecture l INNER JOIN professor p on l.professor_id = p.id INNER JOIN course c on l.course_id = c.id
        """

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_student(self, id):
        sql = """
                SELECT c.name, p.name, p.major, c.credit, l.day, l.start_time, DATE_ADD(l.start_time, INTERVAL c.credit HOUR)
                FROM enrollment e INNER JOIN lecture l on e.lecture_id = l.id INNER JOIN student s on e.student_id = s.id
                INNER JOIN course c on c.id = l.course_id INNER JOIN professor p on p.id = l.professor_id
                WHERE s.id = '{0}'
        """.format(id)

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_professor(self, id):
        sql = """
                SELECT c.name, p.name, p.major, c.credit, l.day, l.start_time, DATE_ADD(l.start_time, INTERVAL c.credit HOUR)
                FROM enrollment e INNER JOIN lecture l on e.lecture_id = l.id INNER JOIN student s on e.student_id = s.id
                INNER JOIN course c on c.id = l.course_id INNER JOIN professor p on p.id = l.professor_id
                WHERE p.id = '{0}'
        """.format(id)

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def get_name(self):
        sql = """
                SELECT c.name, p.name, c.id, l.id
                FROM lecture l INNER JOIN professor p on l.professor_id = p.id INNER JOIN course c on l.course_id = c.id
        """

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def select_by_id(self, dto):
        sql = """
            SELECT * FROM lecture WHERE professor_id = {0} AND course_id = {1}
        """.format(dto.professor_id, dto.course_id)

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, dto):
        sql = """
            INSERT INTO lecture (professor_id, course_id, day, start_time) VALUES({0}, {1}, '{2}', '{3}')
        """.format(dto.professor_id, dto.course_id, dto.date, dto.start_time)
        self.cur.execute(sql)
        self.db.commit()