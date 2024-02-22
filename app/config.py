import secrets
from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    algorithm: str
    access_token_expire_minutes: int
    secret_key: str = secrets.token_urlsafe(32)

    postgres_user: str
    postgres_password: str
    postgres_db: str

    first_user_email: str
    first_user_password: str

    model_config = SettingsConfigDict(env_file="../.env")


@cache
def get_settings():
    return Settings()
