"""
Модуль клиента для взаимодействия с API CoinMarketCap.

Содержит классы для создания асинхронных HTTP-запросов с использованием `aiohttp`
и кешированием с помощью `async_lru`.

Классы
======

- HTTPClient
    Базовый HTTP-клиент, инициализирующий сессию с заданными заголовками и базовым URL.

- CMCHTTPClient
    Расширение `HTTPClient` с методами для получения:
    - списка криптовалют,
    - информации о конкретной валюте по её ID.

Зависимости
===========

- aiohttp
- async_lru
- pydantic_settings (через импорт настроек из `src.config`)

Пример использования
====================

.. code-block:: python

    client = CMCHTTPClient(base_url="https://pro-api.coinmarketcap.com", api_key=settings.CMC_APY_KEY)
    listings = await client.get_listings()
    btc = await client.get_currency(currency_id=1)
"""

from aiohttp import ClientSession

from async_lru import alru_cache


class HTTPClient:
    """
    Базовый HTTP-клиент для взаимодействия с API через aiohttp.

    Инициализирует сессию `ClientSession` с базовым URL и заголовками.

    Параметры
    ---------
    base_url : str
        Базовый URL для всех запросов.
    api_key : str
        Ключ API, используемый в заголовке `X-CMC_PRO_API_KEY`.
    """
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                "X-CMC_PRO_API_KEY": api_key,
            },
        )


class CMCHTTPClient(HTTPClient):
    """
    HTTP-клиент для работы с CoinMarketCap API.

    Реализует методы получения списка криптовалют и данных о конкретной валюте.

    Методы
    -------
    get_listings() -> list
        Возвращает список актуальных криптовалют с CoinMarketCap.
        Результат кешируется с помощью `async_lru`.

    get_currency(currency_id: int)
        Возвращает информацию о конкретной валюте по её ID.
        Результат кешируется с помощью `async_lru`.
    """
    @alru_cache(maxsize=128)
    async def get_listings(self) -> list:
        """
        Получает список актуальных криптовалют с CoinMarketCap.

        Возвращает
        ----------
        list
            Список криптовалют в формате ответа API.
        """
        async with self._session.get("/v1/cryptocurrency/listings/latest") as response:
            result = await response.json()
        return result["data"]

    @alru_cache(maxsize=128)
    async def get_currency(self, currency_id: int):
        """
        Получает информацию о криптовалюте по её идентификатору.

        Параметры
        ----------
        currency_id : int
            Идентификатор криптовалюты в CoinMarketCap.

        Возвращает
        ----------
        dict
            Словарь с данными о криптовалюте.
        """
        async with self._session.get("/v2/cryptocurrency/quotes/latest", params={"id": currency_id}) as response:
            result = await response.json()
        return result["data"][str(currency_id)]
