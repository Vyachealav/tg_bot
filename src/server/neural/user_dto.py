from dataclasses import dataclass
from datetime import datetime

structure = dataclass(frozen=True, slots=True)


@structure
class HistoryByTimeDTO:
    start: datetime
    end: datetime


@structure
class HistoryBySizeDTO:
    """Количество последних сообщений"""

    size: int


@structure
class NewsBySizeDTO:
    size: str
