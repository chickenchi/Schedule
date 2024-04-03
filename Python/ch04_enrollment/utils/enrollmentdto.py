class EnrollmentDTO:
    def __init__(self, student_id, lecture_id):
        self._student_id = student_id
        self._lecture_id = lecture_id
    
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def lecture_id(self):
        return self._lecture_id