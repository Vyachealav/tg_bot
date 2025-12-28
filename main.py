# from src.server.db.orm import AsyncORM
# from src.server.db.config import settings
# import asyncio

import uvicorn
from fastapi import FastAPI

from src.server.api.routers.messages import router

app = FastAPI(title='малая')

app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app='main:app', reload=True)

# async def main():
#     print(settings.database_url_asyncpg)
#     await AsyncORM.create_tables()


# asyncio.run(main())
