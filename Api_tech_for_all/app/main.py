from fastapi import FastAPI
from .db import engine, Base
from .routers import cars
import logging

# Cria tabelas automaticamente (útil para desenvolvimento com SQLite)
Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)


app = FastAPI(
    title="API Concessionária do PAPI, os melhores preços da região!",
    description="API REST para cadastro, consulta, atualização e exclusão de carros (SQLite + FastAPI).",
    version="1.0.0",
)

# incluir rotas
app.include_router(cars.router)

# raiz simples
@app.get("/", tags=["root"])
def read_root():
    return {"msg": "API Concessionária - visite /docs para a documentação Swagger UI"}

# configurar logger básico
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
