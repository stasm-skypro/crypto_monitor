# CryptoTracker

Приложение для отображения актуальной информации о криптовалютах.

## Технологии

- **Бэкенд:** FastAPI  
  Зависимости: `aiohttp`, `async-lru`, `pydantic-settings`
- **Фронтенд:** React + Vite

## Структура проекта

* backend/     # FastAPI-приложение

  * .env.example

* frontend/    # React-приложение

* README.md

## Запуск проекта

### ⚙️ Локально

#### Backend

```bash
cd backend
uvicorn src.main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

#### 🐳 Через Docker

```bash
docker-compose up --build
```

•	Бэкенд (FastAPI/docs): http://localhost:8000/docs/

•	Фронт доступен по адресу: http://localhost:5173/

## API

### GET /currencies

Получает список всех криптовалют.

Возвращает:

```json
[
  {
    "id": 1,
    "name": "Bitcoin",
    ...
  },
  ...
]
```

### GET /currencies/{currency_id}

Получает информацию о конкретной криптовалюте по её идентификатору.

Параметры:
	•	currency_id: int — ID валюты в CoinMarketCap.

Возвращает:

```json
{
  "id": 1,
  "name": "Bitcoin",
  "quote": {
    "USD": {
      "price": 12345.67,
      ...
    }
  }
}
```

## Переменные окружения

Создайте файл .env в корне backend/ на основе .env.example.

```
CMC_APY_KEY=coinmarketcap_api_key
```