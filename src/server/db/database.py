from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator

from src.server.db.config import settings


async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    pool_pre_ping=True,
)

async_session_factory = async_sessionmaker(async_engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


class Base(DeclarativeBase):
    pass
