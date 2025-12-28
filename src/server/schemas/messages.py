from pydantic import BaseModel
from datetime import datetime


class HistoryByTimeDTO(BaseModel):
    start: datetime
    end: datetime


class HistoryBySizeDTO(BaseModel):
    """Количество последних сообщений"""

    size: int


class UserMessageSchema(BaseModel):
    id: int
    username: str
    message: str
    sent_at: datetime

    class Config:
        from_attributes = True


class UserMessageSchemaAdd(BaseModel):
    username: str
    message: str
    sent_at: datetime
