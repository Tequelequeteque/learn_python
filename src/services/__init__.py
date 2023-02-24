from typing import TypedDict

from src.services.todo import ITodoServices, providerTodoService

IServices = TypedDict('IServices', {'todo': ITodoServices})


def providerServices() -> IServices:
    return {
        'todo': providerTodoService()
    }
