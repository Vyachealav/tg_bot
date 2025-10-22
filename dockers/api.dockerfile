FROM python:3.13-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

WORKDIR /app

COPY pyproject.toml uv.lock ./

# Устанавливаем зависимости с помощью uv
RUN uv sync --frozen --no-dev

# Копируем исходный код
COPY . .

# Создаем пользователя для безопасности
RUN useradd --create-home --shell /bin/bash app && chown -R app:app /app
USER app

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"

# Команда по умолчанию
CMD ["python", "scripts/api_startup.py"]
