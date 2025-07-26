"""
Маршруты для работы с криптовалютами через CoinMarketCap API.

Определяет два эндпоинта:
- `/currencies` — получить список всех доступных криптовалют;
- `/currencies/{currency_id}` — получить информацию о конкретной валюте по ID.

Маршруты используют клиента `cmc_client`, основанного на CoinMarketCap HTTP API.

Маршруты
========

- GET `/currencies`
    Возвращает список актуальных криптовалют.

- GET `/currencies/{currency_id}`
    Возвращает информацию о криптовалюте по заданному идентификатору.

Зависимости
===========

- cmc_client : CMCHTTPClient
    Асинхронный HTTP-клиент, импортированный из `src.init`, взаимодействующий с CoinMarketCap API.
"""

from fastapi import APIRouter

from src.init import cmc_client

router = APIRouter(prefix="/currencies", tags=["currencies"])


@router.get("")
async def get_currencies() -> list:
    """
    Получает список всех криптовалют.

    Возвращает
    ----------
    list
        Список криптовалют, полученных с помощью CoinMarketCap API.
    """
    return await cmc_client.get_listings()


@router.get("/{currency_id}")
async def get_currency(currency_id: int) -> dict:
    """
    Получает информацию о конкретной криптовалюте по её идентификатору.

    Параметры
    ----------
    currency_id : int
        Идентификатор криптовалюты в CoinMarketCap.

    Возвращает
    ----------
    dict
        Информация о криптовалюте.
    """
    return await cmc_client.get_currency(currency_id)
