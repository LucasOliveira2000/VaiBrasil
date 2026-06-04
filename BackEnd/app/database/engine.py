from sqlmodel import create_engine
from app.core.config import config

engine = create_engine(
    config.DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=config.APP_ENV
)

