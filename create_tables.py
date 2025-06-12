import asyncio
from app.database import Base, engine
from app.models import models  # Isso garante que todas as classes sejam registradas

async def create_tables():
    print("Criando tabelas no banco de dados...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    asyncio.run(create_tables())
