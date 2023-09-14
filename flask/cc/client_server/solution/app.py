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
    clients = Client.query.all()
    client_json: list[dict] = []
    for c in clients:
        servers: list[dict] = []
        for m in c.message_list:
            if m.server_object not in servers:
                servers.append(m.server_object.to_dict())
        client_dict = c.to_dict()
        client_dict["servers"] = servers
        client_json.append(client_dict)
    return make_response(jsonify(client_json), 200)


@app.post("/messages")
def post_message():
    request_json = request.get_json()
    try:
        msg = Message(
            content=request_json.get("content"),
            server_id=request_json.get("server_id"),
            client_id=request_json.get("client_id"),
        )
        db.session.add(msg)
        db.session.commit()
        msg_dict = msg.to_dict()
        msg_dict["server"] = msg.server_object.to_dict()
        msg_dict["client"] = msg.client_object.to_dict()
        del msg_dict["server_id"]
        del msg_dict["client_id"]
        return make_response(jsonify(msg_dict), 202)
    except:
        return make_response(jsonify({"error": "invalid post"}), 405)


@app.patch("/messages/<int:id>")
def patch_msg(id: int):
    msg = Message.query.filter(Message.id == id).first()
    if not msg:
        return make_response(jsonify({"error": "message not found"}), 404)
    request_json = request.get_json()
    try:
        for key in request_json:
            setattr(msg, key, request_json.get(key))
        db.session.add(msg)
        db.session.commit()
        msg_dict = msg.to_dict()
        msg_dict["server"] = msg.server_object.to_dict()
        msg_dict["client"] = msg.client_object.to_dict()
        del msg_dict["server_id"]
        del msg_dict["client_id"]
        return make_response(jsonify(msg_dict), 202)
    except ValueError:
        return make_response(jsonify({"error": "invalid patch"}), 405)


@app.delete("/messages/<int:id>")
def delete_msg(id: int):
    msg = Message.query.filter(Message.id == id).first()
    if not msg:
        return make_response(jsonify({"error": "message not found"}), 404)
    db.session.delete(msg)
    db.session.commit()
    return make_response(jsonify({}), 200)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
