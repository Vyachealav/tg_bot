import pytest
from src.server.neural.user_dto import HistoryByTimeDTO, HistoryBySizeDTO


@pytest.mark.asyncio
async def test_get_rephrase_history_by_time(neural_client, mock_db, mock_ollama_client):
    dto = HistoryByTimeDTO(start='2025-01-01 10:00', end='"2025-01-01 20:00"')
    mock_db.get_history_by_time.return_value = ['user1/hello', 'user2/how are you?']

    result = await neural_client.get_rephrase_history_by_time(dto)

    assert result == 'mocked-answer'


@pytest.mark.asyncio
async def test_get_rephrase_history_by_size(neural_client, mock_db, mock_ollama_client):
    dto = HistoryBySizeDTO(3)
    mock_db.get_history_by_size.return_value = [
        'user1/hello',
        'user2/hi',
        'user3/amigo!',
    ]

    result = await neural_client.get_rephrase_history_by_size(dto)

    assert result == 'mocked-answer'
