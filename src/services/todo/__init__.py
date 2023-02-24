from typing import TypedDict
from src.services.todo.create import CreateTodoService

ITodoService = TypedDict('ITodoService', {'create': CreateTodoService})

def providerTodoService() -> ITodoService:
    return {
        'create': CreateTodoService()
    }