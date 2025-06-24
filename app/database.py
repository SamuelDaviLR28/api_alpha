from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Obter a URL do banco de dados
DB_URL = os.getenv("DATABASE_URL")

if DB_URL is None:
    raise ValueError("DATABASE_URL não encontrado no .env")

# Criar o engine assíncrono
engine = create_async_engine(DB_URL, echo=True)

# Criar a sessão local corretamente
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Criar a base declarativa
Base = declarative_base()
