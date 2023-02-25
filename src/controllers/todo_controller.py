from flask_restful import Resource

from src.services.todo import ITodoServices


class TodoController(Resource):

    def __init__(
        self,
        todoServices: ITodoServices,
    ):
        self.create = todoServices['create']
        self.get_all = todoServices['getAll']

    def get(self, *args, **kwargs):
        return self.get_all.execute()

    def post(self, *args, **kwargs):
        return self.create.execute()
