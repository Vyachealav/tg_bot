from aiohttp import ClientSession
import pytest_asyncio

from src.simple_api.app.app import App

HOST = 'http://127.0.0.1:8080'


@pytest_asyncio.fixture(scope='session')
async def app():
    app = App()
    # Не стартуем, чтобы обновлять роутинг
    yield app
    if app._runner is not None:
        await app.shutdown()


@pytest_asyncio.fixture(scope='function')
async def session() -> ClientSession:
    async with ClientSession(base_url=HOST) as session:
        yield session


@pytest_asyncio.fixture
async def client(session: ClientSession):
    async def request(
        method: str,
        endpoint: str = '/',
        params: dict | None = None,
    ):
        return await session.request(method, endpoint, **(params or {}))

    return request
