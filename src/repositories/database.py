from typing import TypedDict

from sqlalchemy import create_engine

IDatabaseConnection = TypedDict("IDatabaseConnection", {
    "type": str,  # "postgresql"
    "database": str,  # "postgres"
    "host": str,  # "localhost"
    "port": int,  # 5432
    "user": str,  # "postgres"
    "password": str,  # "postgres"
})


class Database:
    def __init__(
        self,
        dbConnection: IDatabaseConnection
    ):
        self._engine = create_engine(
            f"{dbConnection['type']}://{dbConnection['user']}:{dbConnection['password']}@{dbConnection['host']}:{dbConnection['port']}/{dbConnection['database']}"
        )

    def get_connection(self):
        return self._engine.connect()

    def destroy(self):
        self._engine.dispose()
