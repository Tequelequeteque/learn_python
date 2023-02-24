from typing import TypedDict

from src.services.todo.create import CreateTodoService
from src.services.todo.get_all import GetAllTodoService

ITodoServices = TypedDict(
    'ITodoServices',
    {
        'getAll': GetAllTodoService,
        'create': CreateTodoService,
    }
)


def providerTodoService() -> ITodoServices:
    return {
        'getAll': GetAllTodoService(),
        'create': CreateTodoService(),
    }
