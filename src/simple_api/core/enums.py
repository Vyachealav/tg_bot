from dataclasses import dataclass
from enum import IntEnum, StrEnum


class StatusCode(IntEnum):
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


class HTTPMethod(StrEnum):
    GET = 'GET'
    POST = 'POST'


@dataclass(frozen=True, slots=True)
class Response:
    code: int | StatusCode
    data: dict | str

    def __str__(self):
        return f'{self.code}: {self.data}'

    def __dict__(self):
        return {'code': int(self.code), 'body': self.data}
