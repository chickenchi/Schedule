from models.restaurant_db import Restaurant

class RestaurantService:
    def __init__(self):
        self.restaurant = Restaurant()

    def get_tasks(self):
        return self.restaurant.get()