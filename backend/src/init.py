"""
Инициализация клиента CoinMarketCap API.

Импортирует настройки и создает экземпляр `CMCHTTPClient` с базовым URL и API-ключом
из файла конфигурации `.env`.

Сущности
========

- cmc_client : CMCHTTPClient
    Готовый к использованию асинхронный HTTP-клиент для обращения к CoinMarketCap API.

Зависимости
===========

- src.config.settings : объект настроек, предоставляющий API-ключ.
- src.http_client.CMCHTTPClient : клиент CoinMarketCap API.

Пример использования
====================

.. code-block:: python

    from src.cmc import cmc_client

    listings = await cmc_client.get_listings()
    bitcoin = await cmc_client.get_currency(1)
"""

from src.config import settings
from src.http_client import CMCHTTPClient

cmc_client = CMCHTTPClient(base_url="https://pro-api.coinmarketcap.com", api_key=settings.CMC_APY_KEY)
