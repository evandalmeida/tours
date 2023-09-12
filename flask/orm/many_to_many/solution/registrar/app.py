from flask import make_response, jsonify, request, g
from shared import app, db
from models import Student, Course, Enrollment
from sqlalchemy.sql.expression import func


@app.route("/")
def root():
    return "<h1>Registrar</h1>"


@app.get("/students")
def get_students():
    students = Student.query.all()
    data = [student.to_dict() for student in students]
    return make_response(jsonify(data), 200)


@app.get("/students/<int:id>")
def get_student_by_id(id: int):
    student = Student.query.filter(Student.id == id).first()
    if not student:
        make_response(jsonify({"error": f"id {id} not found"}), 404)
    return make_response(jsonify(student.to_dict()), 200)


@app.get("/students/<int:id>/courses")
def get_courses_for_student(id: int):
    student = Student.query.filter(Student.id == id).first()
    if not student:
        make_response(jsonify({"error": f"id {id} not found"}), 404)
    courses = [e.course for e in student.enrollments]
    data = [course.to_dict() for course in courses]
    return make_response(jsonify(data), 200)


@app.patch("/students/<int:id>")
def patch_student(id: int):
    student = Student.query.filter(Student.id == id).first()
    if not student:
        make_response(jsonify({"error": f"id {id} not found"}), 404)
    request_data = request.get_json()
    for key in request_data:
        setattr(student, key, request_data[key])
    db.session.add(student)
    db.session.commit()
    return make_response(jsonify(student.to_dict()), 200)


@app.delete("/students/<int:id>")
def delete_student(id: int):
    student = Student.query.filter(Student.id == id).first()
    if not student:
        make_response(jsonify({"error": f"id {id} not found"}), 404)
    db.session.delete(student)
    db.session.commit()

    return make_response(jsonify({}), 200)


@app.post("/students/<int:id>/enrollments")
def enroll_student(id: int):
    student = Student.query.filter(Student.id == id).first()
    request_data = request.get_json()
    course = Course.query.filter(Course.id == request_data["course_id"]).first()
    if not student:
        make_response(jsonify({"error": f"id {id} not found"}), 404)
    if not course:
        make_response(jsonify({"error": f"id {id} not found"}), 404)
    enrollment = Enrollment(student_id=student.id, course_id=course.id, term="F2023")
    db.session.add(enrollment)
    db.session.commit()
    return make_response(jsonify(enrollment.to_dict()), 201)


@app.post("/students")
def post_students():
    data = request.get_json()

    student = Student(
        fname=data["fname"], lname=data["lname"], grad_year=data["grad_year"]
    )

    db.session.add(student)
    db.session.commit()

    return make_response(jsonify(student.to_dict()), 201)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
