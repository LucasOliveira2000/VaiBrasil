from sqlmodel import Column, Field, SQLModel, String, DateTime, func
from typing import Optional
from datetime import datetime


class Crawler(SQLModel, table=True):
    __tablename__ = "crawlers"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    fonte_id: int = Field(foreign_key="fontes.id", nullable=False, index=True)
    nome: str = Field(max_length=255, nullable=False)
    url: str = Field(max_length=500, nullable=False)
    ativo: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False,
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )
    )