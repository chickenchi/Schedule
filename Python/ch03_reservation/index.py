from flask import Flask
from controllers.reservation_controller import reservation

app = Flask(__name__)

app.register_blueprint(reservation)

if __name__ == '__main__' :
    app.run(debug = True)