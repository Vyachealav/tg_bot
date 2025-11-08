import inspect
from collections.abc import Coroutine
from aiohttp import web

from src.simple_api.core import Response, HTTPMethod
from src.simple_api.router import ApiMethod, Route, Router


def transformator(handler: ApiMethod):
    sig = inspect.signature(handler)
    accepts_args = len(sig.parameters) > 0

    async def wrapped_handler(*args, **kwargs) -> web.Response:
        if accepts_args:
            resp: Response = await handler(*args, **kwargs)
        else:
            resp: Response = await handler()
        if isinstance(resp.data, str):
            return web.Response(text=resp.data, status=resp.code)
        return web.json_response(resp.data, status=resp.code, headers={'Content-Type': 'application/json'})

    return wrapped_handler


class App:
    def __init__(self):
        self._server = web.Application()
        self._runner: web.AppRunner | None = None
        self._site: web.TCPSite | None = None
        self._router = Router()

    def add_route(self, path: str, method: HTTPMethod | str):
        def decorator(handler: Coroutine):
            http_method = HTTPMethod(method) if isinstance(method, str) else method
            route = Route(path=path, method=http_method, handler=handler)
            self._router.add_route(route)
            return handler

        return decorator

    async def start(self, host: str = '127.0.0.1', port: int = 0):
        self._init_routes()
        self._runner = web.AppRunner(self._server)
        await self._runner.setup()
        self._site = web.TCPSite(self._runner, host=host, port=port)
        await self._site.start()

    async def shutdown(self):
        if self._site is not None:
            await self._site.stop()
            self._site = None
        if self._runner is not None:
            await self._runner.cleanup()
            self._runner = None

    def _init_routes(self):
        for route in self._router.get_routes():
            self._server.router.add_route(route.method, route.path, transformator(route.handler))
