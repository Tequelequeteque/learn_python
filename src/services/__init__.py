from typing import TypedDict
from src.services.todo import ITodoService, providerTodoService

IServices = TypedDict('IServices', {'todo': ITodoService})

def providerServices() -> IServices:
    return {
            'todo': providerTodoService()
        }
    