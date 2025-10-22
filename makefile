# Переменные
DEEPSEEK_MODEL ?= deepseek-r1:8b

help: ## Показать справку
	@echo "Доступные команды:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

all: ## Запустить все сервисы
	docker-compose up -d --build

up: ## Запустить сервисы
	docker-compose up -d

down: ## Остановить сервисы
	docker-compose down


# Очистка
clean: ## Очистить неиспользуемые ресурсы
	docker-compose down -v
	docker system prune -f

clean-all: ## Полная очистка (включая volumes)
	docker-compose down -v --remove-orphans
	docker system prune -af
	docker volume prune -f


deepseek: ## Загрузить DeepSeek модель
	docker-compose exec ollama ollama pull $(DEEPSEEK_MODEL)

ollama-run: ## Запустить модель DeepSeek
	docker-compose exec ollama ollama run $(DEEPSEEK_MODEL)

.PHONY: help all up down restart logs clean