from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Класс настроек приложения.

    Использует Pydantic для загрузки переменных окружения из файла `.env`.
    Предназначен для хранения конфиденциальных настроек, таких как ключи API.

    Атрибуты
    --------
    CMC_APY_KEY : str
        Ключ API для подключения к CoinMarketCap. По умолчанию — "default_or_placeholder".

    Атрибуты класса
    ---------------
    model_config : SettingsConfigDict
        Конфигурация загрузки переменных окружения. Указывает файл `.env` и его кодировку.
    """
    CMC_APY_KEY: str = "default_or_placeholder"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
