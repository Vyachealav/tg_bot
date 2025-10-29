from server.core.user_dto import HistoryDTO, NewsDTO
from server.neuro.neuro_client import NeuralClient

# OLLAMA_URL = 'http://localhost:11434'


class NeuralGenerator:
    def __init__(self, base_url) -> None:
        self._neural_client = NeuralClient(base_url)

    async def __aenter__(self):
        await self._neural_client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._neural_client.__aexit__(exc_type, exc_val, exc_tb)

    async def rephrase_history(self, history_dto: HistoryDTO) -> str:
        """Отправляем историю пользователя и prompt в нейронку, получаем переформулированный ответ"""
        return await self._neural_client.get_rephrase_history(
            history_dto.prompt_instruction,
            history_dto.history,
            history_dto.last_count_messages,
        )

    async def generate_news(self, news_dto: NewsDTO) -> str:
        """Отправляем size и prompt, и получаем рандомную историю о ЯПС"""
        pass
