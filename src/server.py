from os import getenv

from flask import Flask
from flask_restful import Api

from src.controllers.todo_controller import TodoController
from src.repositories.database import Database
from src.services import providerServices


def create_server(name: str):
    db = Database({
        "type": getenv("DB_TYPE", "postgresql"),
        "database": getenv("DB_NAME", "postgres"),
        "host": getenv("DB_HOST", "localhost"),
        "port": int(getenv("DB_PORT", 5432)),
        "user": getenv("DB_USER", "postgres"),
        "password": getenv("DB_PASS", "postgres")
    })

    server = Flask(name)
    api = Api(server)

    services = providerServices()
    api.add_resource(
        TodoController,
        '/todo',
        resource_class_args=[services['todo']],
    )

    return server
