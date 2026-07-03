from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Schemas para Encomenda
class EncomendaBase(BaseModel):
    codigo_rastreio: str
    produto: str
    peso: float
    status: Optional[str] = "Pendente"

class EncomendaCreate(EncomendaBase):
    cliente_id: int

class EncomendaResponse(EncomendaBase):
    id: int
    cliente_id: int

    class Config:
        from_attributes = True

# Schemas para Cliente
class ClienteBase(BaseModel):
    nome: str
    email: str
    endereco: str

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    encomendas: List[EncomendaResponse] = []

    class Config:
        from_attributes = True