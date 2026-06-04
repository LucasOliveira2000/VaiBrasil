from typing import Optional
from sqlmodel import Column, Field, SQLModel, String, DateTime, func
from datetime import datetime

class FonteModel(SQLModel, table=True):
    __tablename__ = "fontes"

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    nome: str = Field(sa_column=Column(String(255), nullable=False))
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