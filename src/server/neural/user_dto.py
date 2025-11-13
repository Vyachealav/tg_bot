from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class HistoryByTimeDTO:
    start: datetime
    end: datetime


@dataclass(frozen=True, slots=True)
class HistoryBySizeDTO:
    size: int


@dataclass(frozen=True, slots=True)
class NewsBySizeDTO:
    size: str
