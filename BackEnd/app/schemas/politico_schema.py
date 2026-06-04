from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class PoliticoSchema(BaseModel):
    crawler_id: int
    nome: str
    partido: str
    email: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    data_nascimento: Optional[datetime] = None
    foto_url: Optional[str] = None
    foto_path_sistema: Optional[str] = None
    situacao: Optional[str] = None
    ativo: bool = True


class PoliticoCreateSchema(PoliticoSchema):
    pass


class PoliticoUpdateSchema(BaseModel):
    crawler_id: Optional[int] = None
    nome: Optional[str] = None
    partido: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    data_nascimento: Optional[datetime] = None
    foto_url: Optional[str] = None
    foto_path_sistema: Optional[str] = None
    situacao: Optional[str] = None
    ativo: Optional[bool] = None


class PoliticoResponseSchema(PoliticoSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
