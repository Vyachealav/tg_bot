from pydantic import BaseModel
from datetime import datetime


class HistoryByTimeDTO(BaseModel):
    start: datetime
    end: datetime


class HistoryBySizeDTO(BaseModel):
    """Количество последних сообщений"""

    size: int
