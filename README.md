# My Project
Теперь можно запускать покрытие прямо через uv run:
uv run coverage run -m pytest

или, если у тебя просто тесты без pytest:
uv run coverage run your_script.py

После запуска появится файл .coverage.
Чтобы вывести отчёт в консоль:
uv run coverage report
