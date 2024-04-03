from models.course_db import Course

class CourseService:
    def __init__(self):
        self.course = Course()

    def get(self):
        return [{'id':s[0], 'name':s[1], 'credit':s[2]} for s in self.course.get()]
    
    def add(self, dto):
        self.check_duplication(dto)
        self.course.add(dto)

    def check_duplication(self, dto):
        results = self.course.select_by_name(dto)

        for c in results:
            if c[1] == dto.name and c[2] == dto.professor:
                raise Exception('이미 등록된 과목입니다.')