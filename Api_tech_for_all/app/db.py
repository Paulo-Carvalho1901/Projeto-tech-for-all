# Importes necessarios
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
import os

# String de conexao
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./cars.db')

"""
{'check_same_thread': False}

Esse dicionário é passado como argumento extra para a conexão com SQLite.
Por quê?

O SQLite, por padrão, não permite que a mesma conexão seja usada por múltiplas threads.
check_same_thread=False desativa essa verificação, permitindo que a conexão seja 
compartilhada entre threads (útil em aplicações web, como FastAPI).


DATABASE_URL = "postgresql://user:password@localhost:5432/banco"
connect_args = {}  # porque não é SQLite
engine = create_engine(DATABASE_URL, connect_args=connect_args)
"""
connect_args = {'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {}


# engine de conexao comunicação com banco
engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    future=True,
    echo=True
)

"""
Exemplo do future
O parâmetro future=True no create_engine do SQLAlchemy significa:
Ativar o modo “future” introduzido no SQLAlchemy 1.4.
Esse modo faz com que a API se comporte de forma mais próxima à versão 2.0 (que é a versão moderna do SQLAlchemy).

sem:
result = session.execute("SELECT * FROM cars")
rows = result.fetchall()  # comportamento antigo

com:
result = session.execute(text("SELECT * FROM cars"))
rows = result.all()  # comportamento moderno
"""
