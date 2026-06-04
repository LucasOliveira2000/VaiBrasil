from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class FonteSchema(BaseModel):
    nome: str
    ativo: bool = True


class FonteCreateSchema(FonteSchema):
    pass


class FonteUpdateSchema(BaseModel):
    nome: Optional[str] = None
    ativo: Optional[bool] = None


class FonteResponseSchema(FonteSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
