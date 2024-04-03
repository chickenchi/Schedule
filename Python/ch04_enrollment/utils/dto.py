class DTO:
    def __init__(self, number, name, gender):
        self._number = number
        self._name = name
        self._gender = gender

    @property
    def number(self):
        return self._number
    
    @property
    def name(self):
        return self._name
    
    @property
    def gender(self):
        return self._gender
