from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class CrawlerSchema(BaseModel):
    fonte_id: int
    nome: str
    url: str
    caminho_modulo: str
    classe_nome: str
    ativo: bool = True


class CrawlerCreateSchema(CrawlerSchema):
    pass


class CrawlerUpdateSchema(BaseModel):
    fonte_id: Optional[int] = None
    nome: Optional[str] = None
    url: Optional[str] = None
    caminho_modulo: Optional[str] = None
    classe_nome: Optional[str] = None
    ativo: Optional[bool] = None


class CrawlerResponseSchema(CrawlerSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
