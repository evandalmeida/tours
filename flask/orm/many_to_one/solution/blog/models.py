from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    blogs = db.relationship("Blog", back_populates="user")

    @validates("name")
    def validate_name(self, key: str, name: str):
        if len(name) < 0:
            raise ValueError("name must be at least 1 character")
        return name

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Blog(db.Model):
    __tablename__ = "blog"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    content = db.Column(db.String)
    title = db.Column(db.String)

    user = db.relationship("User", back_populates="blogs")


    @validates('content')
    def validate_content(self, key:str, content:str):
        if len(content.split(' ')) < 5:
            raise ValueError('Blogs must be at least 5 words')
        return content

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "content": self.content,
            "title": self.title,
        }


