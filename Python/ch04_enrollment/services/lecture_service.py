from models.lecture_db import Lecture

class LectureService:
    def __init__(self):
        self.lecture = Lecture()

    def get(self):
        return [{'course_name':e[0], 'professor_name':e[1], 'professor_major':e[2], 'credit':e[3], 'day':e[4], 'start_time':str(e[5]), 'end_time':str(e[6])} for e in self.lecture.get()]
    
    def get_name(self):
        return [{'name':e[0], 'professor':e[1], 'course_id':e[2], 'lecture_id':e[3]} for e in self.lecture.get_name()]
    
    def get_student(self, id):
        return [{'course_name':e[0], 'professor_name':e[1], 'professor_major':e[2], 'credit':e[3], 'day':e[4], 'start_time':str(e[5]), 'end_time':str(e[6])} for e in self.lecture.get_student(id)]
    
    def get_professor(self, id):
        return [{'course_name':e[0], 'professor_name':e[1], 'professor_major':e[2], 'credit':e[3], 'day':e[4], 'start_time':str(e[5]), 'end_time':str(e[6])} for e in self.lecture.get_professor(id)]
    
    def add(self, dto):
        self.check_duplication(dto)
        self.lecture.add(dto)

    def check_duplication(self, dto):
        results = self.lecture.select_by_id(dto)

        for c in results:
            if c[1] == dto.professor_id and c[2] == dto.course_id:
                raise Exception('이미 있는 수업입니다.')