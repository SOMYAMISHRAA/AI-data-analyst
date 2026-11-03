from collections.abc import Generator
from sqlalchemy.engine import Connection
from app.database.connection import engine

def get_db() -> Generator[Connection,None,None]:
    with engine.connect() as connection:
        yield connection

