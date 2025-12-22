from pydantic import BaseModel, Field, field_validator
from typing import Optional
from decimal import Decimal
import datetime


CURRENT_YEAR = datetime.date.today().year


class CarBase(BaseModel):
    marca: str = Field(..., max_length=100, examples='Toyta')
    modelo: str = Field(..., max_length=100, examples='Fusca')
    ano: int = Field(..., examples=2001)
    preco: Decimal = Field(..., gt=0, examples='60000,00')
    cor: Optional[str] = Field(None, max_length=50, examples='preto')
    disponivel: Optional[bool] = Field(True)

    @field_validator('ano')
    def validar_ano(cls, ano):
        if ano < 1982 or ano > CURRENT_YEAR:
            raise ValueError(f'O deve ser entre 1982 e {CURRENT_YEAR}')
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
        if ano < 1982 or ano > CURRENT_YEAR:
            raise ValueError(f'O deve ser entre 1982 e {CURRENT_YEAR}')


class CarOut(CarBase):
    id_carro: int

    model_config = {
        "from_attributes": True,
        "json_encoders": {
            Decimal: lambda v: str(v)  # Converte Decimal para string no JSON
        }
    }


class CarDelete(BaseModel):
    message: str
    car: CarOut