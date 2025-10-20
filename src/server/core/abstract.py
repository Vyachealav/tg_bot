from abc import ABC, abstractmethod
from core.user_dto import HistoryDTO, NewsDTO

class NeuralClientBase(ABC):
    @abstractmethod
    async def get_rephrase_history(self, history_dto: HistoryDTO) -> str:
        """Отправляем историю пользователя и prompt в нейронку, получаем переформулированный ответ"""
        pass

    @abstractmethod
    async def get_generate_news(self, news_dto: NewsDTO) -> str:
        """Отправляем size и prompt, получаем рандомную историю о ЯПС"""
        pass


class UserDBBase(ABC):
    @abstractmethod
    async def save_messages(self) -> None:
        pass

    @abstractmethod
    async def load_messages(self):
        pass

    @abstractmethod
    async def get_messages_by_size(self):
        pass
