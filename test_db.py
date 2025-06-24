import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True)

async def test_connection():
    try:
        async with engine.begin() as conn:
            await conn.execute("SELECT 1")
            print("✅ Conexão com o banco de dados bem-sucedida!")
    except Exception as e:
        print("❌ Erro ao conectar ao banco de dados:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())
