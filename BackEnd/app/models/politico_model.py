from sqlmodel import Column, Field, SQLModel, DateTime, func
from typing import Optional
from datetime import datetime

class Politico(SQLModel, table=True):
    __tablename__ = "politicos"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    crawler_id: int = Field(foreign_key="crawlers.id", nullable=False, index=True)
    nome: str = Field(max_length=255, nullable=False)
    partido: str = Field(max_length=100, nullable=False)
    email: str | None = Field(max_length=255, nullable=True)
    telefone: str | None = Field(max_length=20, nullable=True)
    endereco: str | None = Field(max_length=255, nullable=True)
    data_nascimento: datetime | None = Field(nullable=True)
    foto_url: str | None = Field(max_length=255, nullable=True)
    foto_path_sistema: str | None = Field(max_length=255, nullable=True)
    situacao: str | None = Field(max_length=50, nullable=True)
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
    