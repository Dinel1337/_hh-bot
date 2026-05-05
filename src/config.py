from pydantic_settings import BaseSettings, SettingsConfigDict

DEBUG = True

class Settings(BaseSettings):
    BOT_TOKEN: str = ""
    PARSER_SERVICE_URL: str = "http://localhost:8000"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    SEARCH_QUERY: str = "fastapi python"
    CHECK_INTERVAL_MINUTES: int = 5

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")