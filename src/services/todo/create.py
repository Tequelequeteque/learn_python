class CreateTodoService:
    __name__ = 'CreateTodoService'
    # def __init__(self, todo_repository: TodoRepository):
    #     self.todo_repository = todo_repository

    def execute(self):
        return {'ok': True}, 201
