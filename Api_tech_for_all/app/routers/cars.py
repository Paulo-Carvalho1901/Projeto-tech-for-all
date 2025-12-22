from decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/cars",
    tags=["Cars"]
)

@router.get("/", response_model=List[schemas.CarOut])
def list_car(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, gt=0, le=100),
    marca: Optional[str] = Query(None),
    preco_min: Optional[Decimal] = Query(None, ge=0),
    preco_max: Optional[Decimal] = Query(None, ge=0),
    db: Session = Depends(get_db)
):

    
    """Lista de carros com filtros opcionais"""
    return crud.get_cars(
        db,
        skip=skip,
        limit=limit,
        marca=marca,
        preco_min=preco_min,
        preco_max=preco_max,
    )

# Criar Carro
@router.post("/", response_model=schemas.CarOut, status_code=201)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db, car)

