from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    endereco = Column(String)

    # Relacionamento: Um cliente tem várias encomendas
    encomendas = relationship("Encomenda", back_populates="dono", cascade="all, delete-orphan")

class Encomenda(Base):
    __tablename__ = "encomendas"

    id = Column(Integer, primary_key=True, index=True)
    codigo_rastreio = Column(String, unique=True, index=True)
    produto = Column(String)
    peso = Column(Float)
    status = Column(String, default="Pendente") # Pendente, Em Trânsito, Entregue
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    # Relacionamento: A encomenda pertence a um cliente
    dono = relationship("Cliente", back_populates="encomendas")