from sqlalchemy import Column, Integer, String, Numeric, Boolean
from .db import Base


class Carro():
    __tablename__ = 'carros'

    id_carro = Column(Integer, primary_key=True, autoincrement=True, index=True)
    marca = Column(String(100), nullable=False, index=True)
    modelo = Column(String(100), nullable=False, index=True)
    ano = Column(Integer, nullable=False)
    preco = Column(Numeric(12, 2), nullable=False)
    cor = Column(String(50), nullable=True)
    disponivel = Column(Boolean, nullable=True, default=True)
