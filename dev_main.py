from src.server.db.orm import AsyncORM
from src.server.db.config import settings
import asyncio

async def main():
    print(settings.database_url_asyncpg)
    await AsyncORM.create_tables()


asyncio.run(main())
