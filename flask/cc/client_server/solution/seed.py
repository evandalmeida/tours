#!/usr/bin/env python3

from app import app
from models import db  # models go here
from faker import Faker
from random import randint, choice, choices
from models import Client, Server, Message
import string

fake = Faker()

if __name__ == "__main__":
    with app.app_context():
        Client.query.delete()
        Message.query.delete()
        Server.query.delete()
        clients: list[Client] = []
        used_names: set[str] = set()
        for _ in range(10):
            name = fake.name()
            if name not in used_names:
                clients.append(Client(name=name))
                used_names.add(name)
        db.session.add_all(clients)
        db.session.commit()

        servers = []
        for _ in range(10):
            servers.append(Server(name="".join(choices(string.ascii_uppercase, k=5))))
        db.session.add_all(servers)
        db.session.commit()

        messages = []

        for _ in range(10):
            messages.append(
                Message(
                    content=fake.paragraph(),
                    server_id=choice(servers).id,
                    client_id=choice(clients).id,
                )
            )
        db.session.add_all(messages)
        db.session.commit()
