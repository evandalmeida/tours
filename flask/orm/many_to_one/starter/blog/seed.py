from faker import Faker
from models import User, Blog, Tag, BlogTag
from random import choice, randint
from models import db
from app import app

fake = Faker()


def create_users() -> list[User]:
    users = []
    for _ in range(10):
        users.append(User(name=fake.name()))
    return users


def create_blogs(users: list[User]) -> list[Blog]:
    blogs = []
    for _ in range(10):
        random_user = choice(users)
        blogs.append(
            Blog(user_id=random_user.id, content=fake.text(), title=fake.sentence())
        )
    return blogs


def create_tags() -> list[Tag]:
    tags = []
    for _ in range(0, 30):
        tag = Tag(text=fake.sentence().split()[0])
        tags.append(tag)

    return tags


with app.app_context():
    User.query.delete()
    Blog.query.delete()
    Tag.query.delete()
    BlogTag.query.delete()
    db.session.commit()
    users = create_users()

    db.session.add_all(users)
    db.session.commit()
    blogs = create_blogs(users)

    db.session.add_all(blogs)

    db.session.commit()

    tags = create_tags()
    print(len(tags))
    db.session.add_all(tags)
    db.session.commit()

    blog_tags = []
    for blog in blogs:
        for _ in range(0, 3):
            blog_tags.append(BlogTag(blog_id=blog.id, tag_id=choice(tags).id))
    db.session.add_all(blog_tags)

    db.session.commit()
    # import ipdb; ipdb.set_trace()
    print()
