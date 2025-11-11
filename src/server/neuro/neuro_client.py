import aiohttp
from http import HTTPStatus

from server.core.abstract import NeuralClientBase
from server.core.user_dto import HistoryByTimeDTO, HistoryBySizeDTO
from server.core.abstract import MessageDBBase

from neuro import MODEL, PROMPT_INSTRUCTION

import types
from typing import Self


class NeuralClient(NeuralClientBase):
    def __init__(self, base_url: str, db: MessageDBBase) -> None:
        self.base_url = base_url.rstrip('/')
        self.db = db
        self._session = None

    async def __aenter__(self) -> Self:
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: types.TracebackType | None,
    ) -> None:
        if self._session:
            await self._session.close()
            self._session = None

    async def get_rephrase_history_by_time(self, datetime: HistoryByTimeDTO) -> str:
        history = await self.db.get_history_by_time(datetime.datetime)
        return await self._rephrase_history(history)

    async def get_rephrase_history_by_size(self, size: HistoryBySizeDTO) -> str:
        history = await self.db.get_history_by_size(size.size)
        return await self._rephrase_history(history)

    async def _rephrase_history(self, history: list) -> str:
        """идея history - имя_отправителя/сообщение"""
        summarize_messages = '; '.join(history)
        prompt = f'{PROMPT_INSTRUCTION}: {summarize_messages}'
        return await self._generate(prompt)

    async def _generate(self, prompt: str, stream: bool = False) -> str:
        payload = {
            'model': MODEL,
            'prompt': prompt,
            'stream': stream,
        }
        data = await self._post('/api/generate', payload)
        return data.get('response', 'No response generated')

    async def _post(self, endpoint: str, payload: dict) -> dict:
        if not self._session:
            raise RuntimeError('Session not initialized')

        url = f'{self.base_url}/{endpoint.lstrip("/")}'
        async with self._session.post(url, json=payload) as response:
            if response.status == HTTPStatus.OK:
                return await response.json()
            raise ValueError(f'API error: {response.status} - {await response.text()}')
