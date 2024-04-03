from models.reservation_db import Reservation

class ReservationService:
    def __init__(self):
        self.reservation = Reservation()

    def post_tasks(self, dto):
        return self.reservation.post(dto)
    
    def get_tasks(self):
        return self.reservation.get()
    
    def remove_tasks(self, index):
        return self.reservation.remove(index)