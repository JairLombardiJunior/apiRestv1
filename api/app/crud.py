from sqlalchemy.orm import Session
from . import models, schemas

# Operações de Cliente
def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()

def get_clientes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(nome=cliente.nome, email=cliente.email, endereco=cliente.endereco)
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Operações de Encomenda
def create_encomenda(db: Session, encomenda: schemas.EncomendaCreate):
    db_encomenda = models.Encomenda(**encomenda.model_dump())
    db.add(db_encomenda)
    db.commit()
    db.refresh(db_encomenda)
    return db_encomenda

def get_encomendas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Encomenda).offset(skip).limit(limit).all()