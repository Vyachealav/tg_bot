# Переменные
DEEPSEEK_MODEL ?= deepseek-r1:1.5b

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
clean: ## Очистить неиспользуемые ресурсы, но сохранить Ollama модели
	docker-compose down           # останавливает и удаляет контейнеры и сети
	docker system prune -f        # удаляет неиспользуемые образы, сети, кэш сборки

clean-all: ## Полная очистка (включая volumes)
	docker-compose down -v --remove-orphans
	docker system prune -af
	docker volume prune -f


deepseek: ## Загрузить DeepSeek модель
	docker-compose exec ollama ollama pull $(DEEPSEEK_MODEL)

ollama-run: ## Запустить модель DeepSeek
	docker-compose exec ollama ollama run $(DEEPSEEK_MODEL)

ollama-up: ## Запустить только Ollama
	docker-compose up -d ollama

ollama-down: ## Остановить только Ollama
	docker-compose stop ollama

.PHONY: help all up down restart logs clean