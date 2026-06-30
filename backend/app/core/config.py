from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration.

    Values are loaded from the .env file and environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ==========================================
    # Application
    # ==========================================
    app_name: str = "InventoryPro"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = True

    # ==========================================
    # API
    # ==========================================
    api_v1_prefix: str = "/api/v1"

    # ==========================================
    # Security
    # ==========================================
    secret_key: str 

    algorithm: str = "HS256"

    access_token_expire_minutes: int = 30

    refresh_token_expire_days: int = 7

    # ==========================================
    # Database
    # ==========================================
    database_url: str

    # ==========================================
    # Redis
    # ==========================================
    redis_url: str


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()   # type: ignore[call-arg]


settings = get_settings()