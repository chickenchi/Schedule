class CourseDTO:
    def __init__(self, name, credit):
        self._name = name
        self._credit = credit
    
    @property
    def name(self):
        return self._name
    
    @property
    def credit(self):
        return self._credit
