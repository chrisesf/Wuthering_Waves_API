import sys
import os
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import AsyncEngine
from alembic import context

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings
from src.database import Base, engine  # engine já é AsyncEngine

# Alembic Config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Alvo das migrations
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = settings.DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine  # AsyncEngine importado do database

    async def do_run_migrations(connection):
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True,  # útil pra SQLite e compat.
        )

        async with context.begin_transaction():
            await context.run_migrations()

    import asyncio

    asyncio.run(do_run_migrations(connectable.connect()))


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
