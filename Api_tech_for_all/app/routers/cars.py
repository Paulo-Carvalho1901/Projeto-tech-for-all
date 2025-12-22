from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/cars",
    tags=["Cars"]
)

# LISTAR CARROS
@router.get("/", response_model=List[schemas.CarOut])
def list_cars(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, gt=0, le=1000),
    marca: str | None = Query(None),
    preco_min: float | None = Query(None, ge=0),
    preco_max: float | None = Query(None, ge=0),
    db: Session = Depends(get_db),
):
    """
    Lista carros com filtros (marca e preço mínimo/máximo).
    """
    return crud.get_cars(
        db,
        skip=skip,
        limit=limit,
        marca=marca,
        preco_min=preco_min,
        preco_max=preco_max,
    )


# CRIAR CARRO
@router.post("/", response_model=schemas.CarOut, status_code=201)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db, car)
