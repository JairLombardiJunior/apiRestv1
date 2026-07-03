from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, database

router = APIRouter(prefix="/encomendas", tags=["Encomendas"])

@router.post("/", response_model=schemas.EncomendaResponse)
def criar_encomenda(encomenda: schemas.EncomendaCreate, db: Session = Depends(database.get_db)):
    # Verifica se o cliente existe antes de associar a encomenda
    cliente = crud.get_cliente(db, cliente_id=encomenda.cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return crud.create_encomenda(db=db, encomenda=encomenda)

@router.get("/", response_model=List[schemas.EncomendaResponse])
def listar_encomendas(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_encomendas(db, skip=skip, limit=limit)