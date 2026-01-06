from sqlalchemy import Column, Integer, String, Boolean, Numeric
from .db import Base

class Carro(Base):
    __tablename__ = 'carros'

    id_carro = Column(Integer, primary_key=True, autoincrement=True, index=True)
    marca = Column(String(100), nullable=False, index=True)
    modelo = Column(String(100), nullable=False, index=True)
    ano = Column(Integer, nullable=False)
    preco = Column(Numeric(12, 2), nullable=False)
    cor = Column(String(50), nullable=True)
    disponivel = Column(Boolean, nullable=True, default=True)
    
    def __repr__(self):
        return f"<Carro id={self.id_carro}, marca={self.marca}, modelo={self.modelo}>"
    

# Exemplo de de como fazer de outra forma:


# from sqlalchemy.orm import Mapped, mapped_column

# class Carro(Base):
#     __tablename__ = "carros"

#     id_carro: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     marca: Mapped[str] = mapped_column(String(100), index=True)
#     modelo: Mapped[str] = mapped_column(String(100), index=True)
#     ano: Mapped[int]
#     preco: Mapped[Decimal] = mapped_column(Numeric(12, 2))
#     cor: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
#     disponivel: Mapped[bool] = mapped_column(Boolean, server_default=text('true'), nullable=False)
