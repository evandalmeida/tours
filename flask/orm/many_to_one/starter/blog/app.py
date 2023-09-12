from flask import make_response, jsonify, request, g
from flask import Flask
from models import db, User, Blog
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
migrate = Migrate(app, db)
db.init_app(app)

@app.route("/")
def root():
    return "<h1>Simple blog site</h1>"





@app.get("/users")
def get_users():
    users = User.query.all() #const = table_name.queay.all(all_contents)
    response = [u.to_dict() for u in users] #list comprehension, FOR LOOP
    return make_response(jsonify(response), 200)


@app.post("/users")
def post_user():
    data = request.json
    new_user = User(name = data.get('name'))
    db.session.add(new_user)
    db.session.commit()
    return make_response(jsonify(new_user.to_dict()), 200)


@app.get("/users/<int:id>")
def get_user_by_id(id: int):
    user = User.query.filter(User.id == id).first()
    if not user:
        return make_response(jsonify({"ERROR": "YOU'RE NOT A USER"}), 404)
    return make_response(jsonify(user.to_dict()), 200)


@app.get("/users/<int:id>/blogs")
def get_blogs_for_user(id: int):
    return {}


@app.post("/users/<int:id>/blogs")
def post_blog_for_user(id: int):







    return {}


@app.get("/blogs/<int:id>")
def get_blog_by_id(id: int):
    return {}


@app.patch("/blogs/<int:id>")
def patch_blog(id: int):
    return {}


@app.patch("/users/<int:id>")
def patch_user(id: int):
    return {}


@app.delete("/blogs/<int:id>")
def delete_blog(id: int):
    return {}


@app.delete("/users/<int:id>")
def delete_user(id: int):
    return {}




if __name__ == "__main__":
    app.run(port=5555, debug=True)
