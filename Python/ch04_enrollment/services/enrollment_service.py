from models.enrollment_db import Enrollment

class EnrollmentService:
    def __init__(self):
        self.enrollment = Enrollment()

    def get(self):
        return [{'enrollment_id':s[0], 'student_number':s[1], 'student_name':s[2], 'course_name':s[3], 'professor':s[4], 'credit':s[5]} for s in self.enrollment.get()]

    def add(self, dto):
        self.check_duplication(dto)
        self.enrollment.add(dto)

    def check_duplication(self, dto):
        results = self.enrollment.select_by_id(dto)

        for c in results:
            if c[1] == dto.student_id and c[2] == dto.lecture_id:
                raise Exception('이미 등록되어 있습니다.')
            
    def delete(self, enrollment_id):
        self.enrollment.delete(enrollment_id)