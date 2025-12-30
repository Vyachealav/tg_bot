import pytest
from unittest.mock import AsyncMock


# from src.server.neural.abstract import MessageDBBase
from src.server.neural.config import NeuralConfig
from src.server.neural.neural_client import NeuralClient


class MockMessageDB:
    def __init__(self):
        self.get_history_by_time = AsyncMock()
        self.get_history_by_size = AsyncMock()
        self.save_message = AsyncMock()
        self.save_messages = AsyncMock()


@pytest.fixture(autouse=True, scope='function')
def mock_db():
    return MockMessageDB()


@pytest.fixture(autouse=True, scope='function')
def config():
    return NeuralConfig(model='deepseek-r1:1.5b', prompt_instruction='Rehprase')


@pytest.fixture(autouse=True, scope='function')
def mock_ollama_client(monkeypatch):
    mock = AsyncMock()
    mock.generate = AsyncMock(return_value={'response': 'mocked-answer'})

    monkeypatch.setattr('src.server.neural.neural_client.AsyncClient', lambda: mock)
    return mock


@pytest.fixture(autouse=True, scope='function')
def neural_client(mock_db, config, mock_ollama_client):
    return NeuralClient(db=mock_db, config=config)
