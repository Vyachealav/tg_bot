from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from server.db.config import settings


async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    pool_pre_ping = True,
)

async_session_factory = async_sessionmaker(async_engine)

class Base(DeclarativeBase):
    pass
