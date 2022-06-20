import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect("cinema.db3")
        self.table_name = "actors"

    def create(self, first_name: str, last_name: str):
        self._connection.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self):
        actor_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )

        return [Actor(*row) for row in actor_cursor]

    def update(self, updated_id: int, new_first_name: str, new_last_name: str):
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ?"
            "WHERE id = ?",
            (new_first_name, new_last_name, updated_id)
        )
        self._connection.commit()

    def delete(self, deleted_id: int):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (deleted_id,)
        )
        self._connection.commit()