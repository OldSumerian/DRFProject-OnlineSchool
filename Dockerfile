# Используем базовый образ Python
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /web

# Копируем зависимости и код приложения
COPY poetry.lock pyproject.toml .

RUN python -m pip install --no-cache-dir poetry==1.4.0 \
    && poetry config virtualenvs.in-project true \
    && poetry install --without dev,test --no-interaction --no-ansi
COPY . .
