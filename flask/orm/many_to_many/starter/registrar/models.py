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
    __tablename__ = "student_table"





class Enrollment(db.Model, SerializerMixin):
    __tablename__ = "enrollment_table"







class Course(db.Model, SerializerMixin):
    __tablename__ = "course_table"



