import pymysql

class Enrollment:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='practice')
        self.cur = self.db.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS enrollment (
                id INT NOT NULL AUTO_INCREMENT NOT NULL,
                student_id INT NOT NULL,
                lecture_id INT NOT NULL,
                course_id INT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES student (id),
                FOREIGN KEY (lecture_id) REFERENCES lecture (id),
                UNIQUE INDEX(student_id, lecture_id),
                PRIMARY KEY (id)
            );
        """

        self.cur.execute(sql)
        self.db.commit()

    def get(self):
        sql = """
            SELECT e.id, s.number, s.name, c.name, p.name, c.credit
            FROM enrollment e INNER JOIN student s on s.id = e.student_id
                              INNER JOIN course c on c.id = e.course_id
                              INNER JOIN lecture l on l.id = e.lecture_id
                              INNER JOIN professor p on p.id = l.professor_id
        """
        
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def select_by_id(self, dto):
        sql = """
            SELECT * FROM enrollment WHERE student_id = {0} and lecture_id = {0}
        """.format(dto.student_id, dto.lecture_id)
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
    
    def add(self, dto):
        print(self.find_course_id(dto.lecture_id))
        sql = """
            INSERT INTO enrollment (student_id, lecture_id, course_id) VALUES({0}, {1}, {2})
        """.format(dto.student_id, dto.lecture_id, self.find_course_id(dto.lecture_id))
        self.cur.execute(sql)
        self.db.commit()

    def find_course_id(self, lecture_id):
        sql = """
            SELECT course_id FROM lecture WHERE id = {0}
        """.format(lecture_id)
        print(lecture_id)

        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result[0][0]

    def delete(self, enrollment_id):
        sql = """
            DELETE FROM enrollment WHERE id = {0}
        """.format(enrollment_id)
        self.cur.execute(sql)
        self.db.commit()