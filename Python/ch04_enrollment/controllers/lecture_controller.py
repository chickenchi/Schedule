from flask import render_template, request, redirect, url_for, Blueprint, jsonify, make_response
from services.lecture_service import LectureService
from services.professor_service import ProfessorService
from services.course_service import CourseService
from utils.lecturedto import LectureDTO

lecture_blueprint = Blueprint('lecture', __name__)
lecture_service = LectureService()
professor_service = ProfessorService()
course_service = CourseService()

@lecture_blueprint.route('/lecture_management', methods=["GET", "POST"])
def lecture_management():
    if request.method == "GET":
        professors = professor_service.get()
        courses = course_service.get()
        lectures = lecture_service.get()
        return render_template('lecture_management.html', professors=professors, courses=courses, lectures=lectures)
    else:
        lecturedto = LectureDTO(request.form['professor_id'], request.form['course_id'], request.form['day'], request.form['start_time'])
        lecture_service.add(lecturedto)
        return redirect(url_for('lecture.lecture_management'))
    
@lecture_blueprint.route('/api/lecture_list')
def lecture_list():
    lectures = lecture_service.get()
    print(lectures)
    return build_actual_response(jsonify(lectures))
    
@lecture_blueprint.route('/api/lecture_list_student/<id>')
def lecture_list_student(id):
    lectures = lecture_service.get_student(id)
    print(lectures)
    return build_actual_response(jsonify(lectures))

@lecture_blueprint.route('/api/lecture_list_professor/<id>')
def lecture_list_professor(id):
    lectures = lecture_service.get_professor(id)
    print(lectures)
    return build_actual_response(jsonify(lectures))

def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
