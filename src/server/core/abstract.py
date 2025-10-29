from abc import ABC, abstractmethod


class NeuralClientBase(ABC):
    @abstractmethod
    async def _generate(self) -> str:
        pass


class MessageDBBase(ABC):
    @abstractmethod
    async def save_messages(self) -> None:
        pass

    @abstractmethod
    async def load_messages(self):
        pass

    @abstractmethod
    async def get_messages_by_size(self):
        pass
