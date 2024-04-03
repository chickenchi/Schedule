from flask import render_template, request, redirect, url_for, Blueprint
from services.student_service import StudentService
from utils.dto import DTO

student_blueprint = Blueprint('student', __name__)
student_service = StudentService()

@student_blueprint.route('/student_management', methods=["GET", "POST"])
def student_management():
    if request.method == "GET":
        students = student_service.get()
        return render_template('student_management.html', students=students)
    else:
        dto = DTO(request.form['number'], request.form['name'], request.form['gender'])
        students = student_service.add(dto)
        return redirect(url_for('student.student_management'))
    
    