from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HistoryDTO:
    prompt_instruction: str
    last_count_messages: int
    history: dict


@dataclass(frozen=True, slots=True)
class NewsDTO:
    pass
