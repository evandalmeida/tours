from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from shared import db, metadata
import re


class Student(db.Model, SerializerMixin):
    __tablename__ = "student"
    serialize_rules = ("-enrollments",)
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    grad_year = db.Column(db.Integer)

    enrollments = db.relationship("Enrollment", back_populates="student")

    @validates("grad_year")
    def validate(self, key, grad_year):
        if grad_year < 2023:
            raise ValueError(f"{grad_year} : Invalid graduation year")
        return grad_year


class Enrollment(db.Model, SerializerMixin):
    __tablename__ = "enrollment"

    serialize_rules = ("-student.enrollments", "-course.enrollments")
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    term = db.Column(db.String)

    student = db.relationship("Student", back_populates="enrollments")
    course = db.relationship("Course", back_populates="enrollments")

    @validates("term")
    def validates_term(self, key, term):
        """
        regex breakdown:
        ^ : the match must start from the beginning of the string
        [SF] : matches the characters S or F
        [0-9] : matches the digits 0 to 9
        + : matches one or more of the previous characters (in this case [0-9])
        $ : the match must end at the end of the string
        """
        if not re.match("^[SF][0-9]+$", term):
            raise ValueError(f"{term} : term string has incorrect format")
        return term


class Course(db.Model, SerializerMixin):
    __tablename__ = "course"

    serialize_rules = ("-enrollments",)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    instructor = db.Column(db.String)
    credits = db.Column(db.Integer)

    enrollments = db.relationship("Enrollment", back_populates="course")

    @validates("title")
    def validate_title(self, key, title):
        if len(title) < 1:
            raise ValueError(f"{title} : title must be at least 1 character")
        return title
