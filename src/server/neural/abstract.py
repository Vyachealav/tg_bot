from abc import ABC, abstractmethod
from datetime import datetime


class MessageDBBase(ABC):
    @abstractmethod
    async def save_message(self, message: str) -> None:
        """Сохраняем каждое сообщение"""
        pass

    @abstractmethod
    async def get_history_by_time(self, datetime: tuple[datetime, datetime]) -> list[str]:
        """Принимаем промежуток даты по которой получаем историю сообщений"""
        pass

    @abstractmethod
    async def get_history_by_size(self, size: int) -> list[str]:
        """Принимаем кол-во сообщений которых хотим получить"""
        pass
