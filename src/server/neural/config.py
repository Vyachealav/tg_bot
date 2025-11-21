import os
from dotenv import load_dotenv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class NeuralConfig:
    model: str
    prompt_instruction: str

    @classmethod
    def load(cls):
        "Загружаем конфигурацию из .env"
        root = Path(__file__).resolve().parents[3]
        env_path = root / 'env' / '.env'

        load_dotenv(env_path)

        return cls(
            model=os.getenv('MODEL'),
            prompt_instruction=os.getenv('PROMPT_INSTRUCTION'),
        )
