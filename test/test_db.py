import asyncio
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from src.database import AsyncSessionLocal


async def test_connection():
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
        print("✅ Conexão com o banco de dados funcionando!")
    except SQLAlchemyError as e:
        print("❌ Erro ao conectar no banco:", str(e))


if __name__ == "__main__":
    asyncio.run(test_connection())
