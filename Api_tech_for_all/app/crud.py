from sqlalchemy.orm import Session 
from app import models, schemas
from decimal import Decimal

# GET CARS
def get_cars(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    marca: str | None = None,
    preco_min: Decimal | None = None,
    preco_max: Decimal | None = None,
):


    """Lista de carros filtros opcionais"""
    query = db.query(models.Carro)

    if marca:
        query = query.filter(models.Carro.marca.ilike(f'%{marca}%'))

    if preco_min is not None:
        query = query.filter(models.Carro.preco >= preco_min)

    if preco_max is not None:
        query = query.filter(models.Carro.preco <= preco_max)

    return query.offset(skip).limit(limit).all()


# GET CAR
def get_car(db: Session, car_id: int):
    return db.query(models.Carro).filter(models.Carro.id_carro == car_id).first()


# POST CAR
def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Carro(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


# PUT CAR
def update_car(db: Session, car_id: int, data: schemas.CarCreate):
    db_car = get_car(db, car_id)
    
    if not db_car:
        return None

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(db_car, field, value)

    db.commit()
    db.refresh(db_car)
    return db_car

# DELETE CAR
def delete_car(db: Session, car_id: int):
    db_car = get_car(db, car_id)
    if not db_car:
        return None

    db.delete(db_car)
    db.commit()
    return db_car
