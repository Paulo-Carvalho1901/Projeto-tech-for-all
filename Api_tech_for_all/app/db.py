from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./cars.db')

connect_args = {'check_same_thread': False} if DATABASE_URL.startswith('sqlite') else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    future=True,
    echo=bool(os.getenv("SQL_DEBUG", False))
)


SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine,
    future=True
)


Base = declarative_base()

def get_db() -> Generator[Session, None, None]: # Generator[ YIELD , SEND , RETURN ]
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
