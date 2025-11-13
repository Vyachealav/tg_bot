from dataclasses import dataclass


@dataclass
class NeuralConfig:
    model: str
    prompt_instruction: str

    @classmethod
    def load(cls):
        "Загружаем конфигурацию и .env"
        pass
