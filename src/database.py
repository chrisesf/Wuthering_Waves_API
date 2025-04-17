from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config import settings

# URL do banco de dados
DATABASE_URL = settings.DATABASE_URL

# Criação da engine assíncrona
engine = create_async_engine(DATABASE_URL, echo=True)

# Sessão assíncrona (usada nos endpoints via Depends)
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,  # Evita o expirar automático, útil para o uso assíncrono
)

# Base de todos os modelos
Base = declarative_base()


# Função para obter a sessão assíncrona no FastAPI
async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        return session  # Retorna diretamente a sessão
