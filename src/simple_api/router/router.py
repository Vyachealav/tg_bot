from dataclasses import dataclass
from collections.abc import Coroutine
from typing import Any, TypeAlias

from src.simple_api.core import HTTPMethod, Response

ApiMethod: TypeAlias = Coroutine[Any, Any, Response]


@dataclass(frozen=True, slots=True)
class Route:
    path: str
    method: HTTPMethod
    handler: ApiMethod

    def __str__(self):
        return f'{self.path}: {self.method}'


class Router:
    def __init__(self):
        self.routes = []

    def add_route(self, route: Route) -> None:
        self.routes.append(route)

    def get_routes(self) -> list[Route]:
        return self.routes
