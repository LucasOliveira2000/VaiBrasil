from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
from sqlalchemy import Column, DateTime, String, func


class FonteModel(SQLModel, table=True):
    __tablename__ = "fonte"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    nome: str = Field(sa_column=Column(String(255), nullable=False))
    url: str = Field(sa_column=Column(String(500), nullable=False))
    ativo: bool = Field(default=True, nulllable=False)
    created_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False
        )
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),
            onupdate=func.now(),
            nullable=False
        )
    )