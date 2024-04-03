from flask import render_template, request, redirect, url_for, Blueprint
from services.restaurant_service import RestaurantService
from services.reservation_service import ReservationService
from util.dto import ReservationFormDto

reservation = Blueprint('reservation', __name__)
restaurant_service = RestaurantService()
reservation_service = ReservationService()
@reservation.route('/', methods=["POST", "GET"])
def index():
    print("미아핑")
    if request.method == "GET":
        restaurants = restaurant_service.get_tasks()
        return render_template('index.html', restaurants=restaurants)
    else:
        dto = ReservationFormDto(request.form['restaurant_id'], request.form['name'], request.form['email'], request.form['phone'], request.form['num_guests'], request.form['date'])
        reservation_service.post_tasks(dto)
        return redirect(url_for('reservation.index'))

@reservation.route('/manage')
def manage_reservations():
        reservations = reservation_service.get_tasks()
        return render_template('manage_reservations.html', reservations=reservations)
    
@reservation.route('/cancel_reservation/<int:index>')
def remove_reservations(index):
    reservation_service.remove_tasks(index)
    return redirect(url_for('reservation.manage_reservations'))