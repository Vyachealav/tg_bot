from server.core.neural_generator import NeuralGenerator
from server.core.user_dto import HistoryDTO, NewsDTO


class TestNeuralGenerator:
    def test_history(self):
        generator = NeuralGenerator()
