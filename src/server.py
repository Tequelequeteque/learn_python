from flask import Flask
from flask_restful import Api

from src.controllers.todo_controller import TodoController
from src.services import providerServices


def create_server(name: str):
    server = Flask(name)
    api = Api(server)

    services = providerServices()
    api.add_resource(
        TodoController,
        '/todo',
        resource_class_kwargs=services['todo'],
    )

    return server
