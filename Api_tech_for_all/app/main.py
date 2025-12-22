from fastapi import FastAPI
from .db import engine, Base
from . import models
from .routers import cars


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='API Papi concessionaria',
    description='API REST para cadastro, consulta, atualização, e exclusão',
    version='1.0.0'
)

app.include_router(cars.router)

@app.get('/', tags=['root'])
def read_root():
    return {'msg': 'API concessionaria - Visite/docs para documentação'}

# uvicorn app.main:app --reload