from flask import Flask
from flask_restful import Api
from src.controllers import providerControllers
from src.services import providerServices 

def create_server(name: str):
    server = Flask(name)
    api = Api(server)

    services = providerServices()
    controllers = providerControllers(services)

    api.add_resource(controllers['todo'], '/todo')

    return server