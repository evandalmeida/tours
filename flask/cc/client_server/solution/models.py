from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Server(db.Model):
    __tablename__ = "server_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    message_list = db.relationship(
        "Message", back_populates="server_object", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {"id": self.id, "name": self.name}

    @validates("name")
    def validate_name(self, key, name):
        uppers_set = set(string.ascii_uppercase)
        name_set = set(name)
        if not name.isupper() and len(name_set - uppers_set) > 0:
            raise ValueError("Server names must be upper case")
        return name


class Message(db.Model):
    __tablename__ = "message_table"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    server_id = db.Column(db.Integer, db.ForeignKey("server_table.id"), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("client_table.id"), nullable=False)

    server_object = db.relationship("Server", back_populates="message_list")
    client_object = db.relationship("Client", back_populates="message_list")

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "server_id": self.server_id,
            "client_id": self.client_id,
        }


class Client(db.Model):
    __tablename__ = "client_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    message_list = db.relationship(
        "Message", back_populates="client_object", cascade="all, delete-orphan"
    )

    @validates("name")
    def validate_name(self, key, name):
        if len(name) < 5 and len(name) > 15:
            raise ValueError
        return name

    def to_dict(self):
        return {"id": self.id, "name": self.name}
