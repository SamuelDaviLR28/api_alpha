from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Obter a URL do banco de dados e corrigir para asyncpg
DB_URL = os.getenv("DATABASE_URL")

if DB_URL is None:
    raise ValueError("DATABASE_URL não encontrado no .env")

# Verificar se a URL está corretamente configurada para asyncpg
if not DB_URL.startswith("postgresql+asyncpg://"):
    DB_URL = DB_URL.replace("postgresql://", "postgresql+asyncpg://")

# Criar o engine assíncrono com configurações otimizadas
engine = create_async_engine(DB_URL, echo=True, future=True)

# Criar a sessão local corretamente
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Criar a base declarativa
Base = declarative_base()
