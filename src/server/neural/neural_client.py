from ollama import AsyncClient

from src.server.neural.abstract import MessageDBBase
from src.server.neural.config import NeuralConfig
from src.server.neural.user_dto import HistoryByTimeDTO, HistoryBySizeDTO


class NeuralClient:
    def __init__(self, db: MessageDBBase, config: NeuralConfig) -> None:
        self._client = AsyncClient()
        self._db = db
        self._config = config

    async def get_rephrase_history_by_time(self, datetime: HistoryByTimeDTO) -> str:
        history = await self._db.get_history_by_time((datetime.start, datetime.end))
        return await self._rephrase_history(history)

    async def get_rephrase_history_by_size(self, size: HistoryBySizeDTO) -> str:
        history = await self._db.get_history_by_size(size.size)
        return await self._rephrase_history(history)

    async def _rephrase_history(self, history: list) -> str:
        """идея history - имя_отправителя/сообщение"""
        summarize_messages = '; '.join(history)
        prompt = f'{self._config.prompt_instruction}: {summarize_messages}'
        return await self._generate(prompt)

    async def _generate(self, prompt: str, stream: bool = False) -> str:
        data = await self._client.generate(model=self._config.model, prompt=prompt, stream=stream)
        return data.get('response', 'No respone generated')
