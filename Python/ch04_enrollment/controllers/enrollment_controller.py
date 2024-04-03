from flask import render_template, request, redirect, url_for, Blueprint
from services.enrollment_service import EnrollmentService
from services.student_service import StudentService
from services.lecture_service import LectureService
from utils.enrollmentdto import EnrollmentDTO

enrollment_blueprint = Blueprint('enrollment', __name__)
enrollment_service = EnrollmentService()
lectures_service = LectureService()
student_service = StudentService()

@enrollment_blueprint.route('/')
def index():
    return render_template('index.html')

@enrollment_blueprint.route('/enrollment_management')
def enrollment_management():
    enrollments = enrollment_service.get()
    students = student_service.get()
    lectures = lectures_service.get_name()
    return render_template('enrollment_management.html', enrollments=enrollments, lectures=lectures, students=students)
    
@enrollment_blueprint.route('/register_enrollment', methods = ['POST'])
def register_enrollment():
    dto = EnrollmentDTO(student_id=request.form['student_id'], lecture_id=request.form['lecture_id'])
    enrollment_service.add(dto)
    return redirect(url_for('enrollment.enrollment_management'))

@enrollment_blueprint.route('/cancel_enrollment', methods = ['POST'])
def cancel_enrollment():
    enrollment_service.delete(request.form['enrollment_id'])
    return redirect(url_for('enrollment.enrollment_management'))