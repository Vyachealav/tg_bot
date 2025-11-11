from abc import ABC, abstractmethod
from datetime import datetime

from core.user_dto import HistoryBySizeDTO, HistoryByTimeDTO, NewsBySizeDTO


class NeuralClientBase(ABC):
    @abstractmethod
    async def get_rephrase_history_by_time(self, datetime: HistoryByTimeDTO) -> str:
        pass

    @abstractmethod
    async def get_rephrase_history_by_size(self, size: HistoryBySizeDTO) -> str:
        pass

    @abstractmethod
    async def get_random_news(self, size: NewsBySizeDTO) -> str:
        pass


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
