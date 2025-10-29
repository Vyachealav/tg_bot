import aiohttp
# import asyncio
# import json

from http import HTTPStatus
from server.core.abstract import NeuralClientBase


class NeuralClient(NeuralClientBase):
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self._session = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._session:
            await self._session.close()
            self._session = None

    async def _post(self, endpoint: str, payload: dict) -> dict:
        if not self._session:
            raise RuntimeError('Session not initialized')

        url = f'{self.base_url}/{endpoint.lstrip("/")}'
        async with self._session.post(url, json=payload) as response:
            if response.status == HTTPStatus.OK:
                return await response.json()
            raise ValueError(f'API error: {response.status} - {await response.text()}')

    async def _generate(self, prompt: str) -> str:
        payload = {
            'model': 'deepseek-r1:1.5b',
            'prompt': prompt,
            'stream': False,
        }
        data = await self._post('/api/generate', payload)
        return data.get('response', 'No response generated')

    async def get_rephrase_history(self, prompt_instruction: str, history: dict, last_count_messages: int) -> str:
        """идея history - имя_отправителя/сообщение"""
        summarize_prompt = self.get_summarize_history(prompt_instruction, history, last_count_messages)
        return await self._generate(summarize_prompt)

    def get_summarize_history(self, prompt_instruction: str, history: int, last_count_messages: int) -> str:
        last_messages = dict(list(history.items())[-last_count_messages:])
        summarize_messages = f'{prompt_instruction}: '
        for name, message in last_messages.items():
            summarize_messages += f'{name}:{message}; '
        return summarize_messages
