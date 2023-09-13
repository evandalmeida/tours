from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from shared import db, metadata
import re

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)



class Student(db.Model, SerializerMixin):
    serialize_rules = ('-enrollment_list.student.object', )
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    grad_year = db.Column(db.Integer, nullable=False)

    enrollment_list = db.relationship('Enrollment', back_populates='student_object')



class Enrollment(db.Model, SerializerMixin):
    __tablename__ = "enrollments"
    serialize_rules = ('student_object.enrollment_list', 'course_object.enrollment_list')
    id = db.Column(db.Integer, primary_key=True)
    students_id = db.Column(db.Integer, db.ForeignKey("students.id"))
    courses_id = db.Column(db.Integer, db.ForeignKey("courses.id"))
    term = db.Column(db.String, nullable=False)

    student_object = db.relationship('Student', back_populates='enrollment_list')
    course_object = db.relationship('Course', back_populates='enrollment_list')


class Course(db.Model, SerializerMixin):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    instructor = db.Column(db.String)
    credits = db.Column(db.Integer)

    enrollment_list = db.relationship('Enrollment', back_populates='course_object')