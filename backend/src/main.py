"""
Инициализация FastAPI-приложения.

Настраивает:
- маршруты через `router`,
- CORS-политику для взаимодействия с фронтендом (например, Vite на порту 5173).

Сущности
========

- app : FastAPI
    Основное приложение FastAPI, экспортируемое для запуска сервера.

CORS
====

Разрешены следующие источники (origins):
- http://localhost:5173
- http://127.0.0.1:5173
- http://localhost:3000
- http://127.0.0.1:3000

Параметры CORS:
- allow_credentials=True
- allow_methods=["*"]
- allow_headers=["*"]

Зависимости
===========

- `src.router.router` — объект маршрутизатора с определёнными эндпоинтами.

Пример использования
====================

.. code-block:: bash

    uvicorn src.main:app --reload

или через `python main.py` (если модульный запуск настроен).
"""

from fastapi import FastAPI
from src.router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)

origins = [
    "http://localhost:5173",  # Для локальной разработки фронтенда
    "http://127.0.0.1:5173",  # Для локальной разработки фронтенда
    "http://localhost:3000",  # Для доступа к фронтенду через localhost (порт 3000, где Nginx)
    "http://127.0.0.1:3000",  # Для доступа к фронтенду через localhost (порт 3000, где Nginx)
    "http://backend:8000",    # 💡 Для связи фронтенда с бэкендом внутри Docker сети
]   

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
