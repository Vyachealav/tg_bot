from src.server.db.models import ChatMessage #noqa
from src.server.db.database import Base

from src.server.db.database import async_engine


class AsyncORM:
    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            async_engine.echo = False
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            async_engine.echo = True

    @staticmethod
    async def insert_message():
        pass

    @staticmethod
    async def select_messages():
        pass
