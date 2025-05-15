import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()  # Carrega variáveis do arquivo .env

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://samueldavi:13791379@localhost/api_toutxalpha"
)

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()
