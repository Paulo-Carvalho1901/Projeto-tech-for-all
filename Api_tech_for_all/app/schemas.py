from pydantic import BaseModel, Field, field_validator
from typing import Optional
from decimal import Decimal
import datetime

# Ano atual automaticamente
CURRENT_YEAR = datetime.date.today().year


# gt = greater than ⇒ maior que zero
class CarBase(BaseModel):
    marca: str = Field(..., max_length=100, example="Volkswagen")
    modelo: str = Field(..., max_length=100, example="Golf GTI")
    ano: int = Field(..., example=2020)
    preco: Decimal = Field(..., gt=0, example="55999.90")
    cor: Optional[str] = Field(None, max_length=50, example="Preto")
    disponivel: Optional[bool] = Field(True)

    @field_validator("ano")
    def validar_ano(cls, ano):
        if ano < 1886 or ano > CURRENT_YEAR:
            raise ValueError(f"O ano deve estar entre 1886 e {CURRENT_YEAR}.")
        return ano


class CarCreate(CarBase):
    pass


class CarUpdate(BaseModel):
    marca: Optional[str] = Field(None, max_length=100)
    modelo: Optional[str] = Field(None, max_length=100)
    ano: Optional[int] = None
    preco: Optional[Decimal] = Field(None, gt=0)
    cor: Optional[str] = Field(None, max_length=50)
    disponivel: Optional[bool] = None

    @field_validator("ano")
    def validar_ano(cls, ano):
        if ano is None:
            return ano
        if ano < 1886 or ano > CURRENT_YEAR:
            raise ValueError(f"O ano deve estar entre 1886 e {CURRENT_YEAR}.")
        return ano


class CarOut(CarBase):
    id_carro: int

    model_config = {
        "from_attributes": True
    }


class CarDeleteResponse(BaseModel):
    message: str
    car: CarOut
    