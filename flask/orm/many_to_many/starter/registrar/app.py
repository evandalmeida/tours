from flask import Flask

from flask_migrate import Migrate
from flask import make_response, jsonify, request, g
from models import Student, Course, Enrollment, db
from sqlalchemy.sql.expression import func


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

migrate = Migrate(app, db)

db.init_app(app)

@app.route("/")
def root():
    return "<h1>Registrar</h1>"


@app.get("/students")
def get_students():
    students = Student.query.all()
    response = [s.to_dict() for s in students]
    return make_response(jsonify(response), 200)


@app.get("/students/<int:id>")
def get_student_by_id(id: int):
    return {}


@app.get("/students/<int:id>/courses")
def get_courses_for_student(id: int):
    return {}


@app.patch("/students/<int:id>")
def patch_student(id: int):

    data = request.json
    
    try:
        student = Student.query.filter(Student.id == id).first()
 
        for key in data:
            setattr(student, key, data[key])

        db.session.add(student)
        db.session.commit()
        
        return make_response(jsonify(student.to_dict), 201)


    except Exception as e:
        print(e)

        return make_response(jsonify({'error':'bad'}), 405)


@app.delete("/students/<int:id>")
def delete_student(id: int):


    return {}


@app.post("/students/<int:id>/enrollments")
def enroll_student(id: int):

    data = request.json

    try:
        student_enrollement = Student(id=data.get('id'), enrollement_list=data.get('enrollement_list'))

        db.session.add(student_enrollement)
        db.session.commit()
        return make_response(jsonify(student_enrollement.to_dict()), 203)

    except Exception as e:
        print(e)
        return make_response(jsonify({'error':'student not enrolled'}), 405 )


@app.post("/students")
def post_students():

    data = request.json

    try:
        student = Student(fnmae=data.get('fname'), lname=data.get('lname'), grad_year=data.get('grad_year'))
        db.session.add(student)
        db.session.commit()
        return make_response(jsonify(student.to_dict()), 201)
    
    except Exception as e:
        print(e)
        return make_response(jsonify({'error':'bad student post'}), 405)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
