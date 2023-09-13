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
    return {}


@app.get("/students/<int:id>")
def get_student_by_id(id: int):
    return {}


@app.get("/students/<int:id>/courses")
def get_courses_for_student(id: int):
    return {}


@app.patch("/students/<int:id>")
def patch_student(id: int):
    return {}


@app.delete("/students/<int:id>")
def delete_student(id: int):
    return {}


@app.post("/students/<int:id>/enrollments")
def enroll_student(id: int):
    return {}


@app.post("/students")
def post_students():
    return {}


if __name__ == "__main__":
    app.run(port=5555, debug=True)
