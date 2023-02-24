from flask_restful import Resource

from src.services.todo.create import CreateTodoService
from src.services.todo.get_all import GetAllTodoService


class TodoController(Resource):

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        self.create = kwargs['create']
        self.get_all = kwargs['getAll']

    def get(self, *args, **kwargs):
        return self.get_all.execute()

    def post(self, *args, **kwargs):
        return self.create.execute()
