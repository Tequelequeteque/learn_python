from typing import TypedDict
from src.controllers.todo_controller import TodoController
from src.services import IServices

IControllers = TypedDict('IControllers', {'todo': TodoController})

def providerControllers(services:IServices) -> IControllers:
    return {
        'todo': TodoController(services['todo']['create']),
    }