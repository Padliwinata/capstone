import psycopg2
from psycopg2 import sql
from psycopg2.extensions import connection

class Role:
    def __init__(self, role_id, name) -> None:
        self.role_id = role_id
        self.name = name

class User:
    def __init__(self, user_id, username, password_hash, email, role_id, created_at=None) -> None:
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.role_id = role_id
        self.created_at = created_at

class UserRepository:
    def __init__(self, connection: connection) -> None:
        self.connection = connection

    def create_user(self, user: User):
        with self.connection.cursor() as cursor:
            insert_query = sql.SQL(
                "INSERT INTO users (username, password_hash, email, role_id, created_at)"
                "VALUES ({}, {}, {}, {}, {})"
            ).format(
                sql.Literal(user.username),
                sql.Literal(user.password_hash),
                sql.Literal(user.email),
                sql.Literal(user.role_id),
                sql.Literal(user.created_at) if user.created_at else sql.SQL("NOW()")
            )
            cursor.execute(insert_query)
    
    
