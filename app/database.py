from dotenv import load_dotenv
from pathlib import Path
import os

# Carregar .env no módulo database
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não definido nas variáveis de ambiente (.env)")

DATABASE_URL = DATABASE_URL.strip()

# resto do seu código SQLAlchemy aqui...
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_connection():
    return SessionLocal()
