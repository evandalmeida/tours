#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Client, Server, Message  # import your models here!

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)


@app.get("/")
def index():
    return "client/server"


@app.get("/clients")
def get_clients():
    return {}


@app.post("/messages")
def post_message():
    return {}


@app.patch("/messages/<int:id>")
def patch_msg(id: int):
    return {}


@app.delete("/messages/<int:id>")
def delete_msg(id: int):
    return {}


if __name__ == "__main__":
    app.run(port=5555, debug=True)
