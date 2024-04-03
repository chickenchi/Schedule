from models.student_db import Student

class StudentService:
    def __init__(self):
        self.student = Student()

    def get(self):
        return [{'id':s[0], 'number':s[1], 'name':s[2], 'gender':s[3]} for s in self.student.get()]
    
    def add(self, dto):
        self.check_duplication(dto)
        self.student.add(dto)

    def check_duplication(self, dto):
        results = self.student.select_by_number(dto)

        for c in results:
            if c[1] == dto.name:
                raise Exception('이미 있는 학번입니다.')