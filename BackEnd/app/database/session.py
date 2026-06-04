from sqlmodel import Session
from app.database.engine import engine
from typing import Generator

def get_db() -> Generator[Session, None, None]:
    """Dependency para obter sessão do banco de dados"""
    with Session(engine) as session:
        yield session