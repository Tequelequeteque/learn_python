from flask_restful import Resource

from src.services.todo.create import CreateTodoService

class TodoController(Resource):
    __name__ = 'TodoController'

    def __init__(self, create_todo: CreateTodoService):
        self.create_todo = create_todo

    def get(self):
        return self.create_todo.execute()