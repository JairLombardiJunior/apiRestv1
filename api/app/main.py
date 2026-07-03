from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import clientes, encomendas

# Cria as tabelas do banco de dados ao iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Amazon Delivery Tracking System API")

# Configuração de CORS para permitir chamadas do Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas isoladas
app.include_router(clientes.router)
app.include_router(encomendas.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API logística do Amazon Delivery System"}