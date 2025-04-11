import asyncio
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Ajusta o path pra importar dos módulos do projeto
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importa config e Base
from src.config import settings
from src.database import Base

# Importa todos os models aqui!
from src.resonators.models import Resonator
from src.factions.models import Faction

# Config Alembic
config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """Executa as migrações no modo offline (gera o SQL sem aplicar)."""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Executa as migrações no modo online (conecta no banco e aplica)."""
    connectable = create_async_engine(settings.DATABASE_URL, future=True)

    async with connectable.connect() as async_conn:

        def do_migrations(sync_conn):
            context.configure(
                connection=sync_conn,
                target_metadata=target_metadata,
                compare_type=True,
                compare_server_default=True,
            )
            with context.begin_transaction():
                context.run_migrations()

        await async_conn.run_sync(do_migrations)


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
