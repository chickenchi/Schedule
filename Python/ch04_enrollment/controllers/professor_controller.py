from flask import render_template, request, redirect, url_for, Blueprint
from services.professor_service import ProfessorService
from utils.professordto import ProfessorDTO

professor_blueprint = Blueprint('professor', __name__)
professor_service = ProfessorService()

@professor_blueprint.route('/professor_management', methods=["GET", "POST"])
def professor_management():
    if request.method == "GET":
        professors = professor_service.get()
        return render_template('professor_management.html', professors=professors)
    else:
        dto = ProfessorDTO(request.form['name'], request.form['major'], request.form['email'])
        professor_service.add(dto)
        return redirect(url_for('professor.professor_management'))