from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from typing import Generator
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./cars.db')

connect_args = {'check_same_thread': False}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    feature=True,
    echo=True
)


