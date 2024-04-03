from models.professor_db import Professor

class ProfessorService:
    def __init__(self):
        self.professor = Professor()

    def get(self):
        return [{'id':s[0], 'name':s[1], 'major':s[2], 'email':s[3]} for s in self.professor.get()]
    
    def add(self, dto):
        self.check_duplication(dto)
        self.professor.add(dto)

    def check_duplication(self, dto):
        results = self.professor.select_by_name(dto)

        for c in results:
            if c[1] == dto.name and c[2] == dto.major:
                raise Exception('이미 있는 이름과 전공입니다.')