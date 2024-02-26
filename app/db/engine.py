from sqlmodel import create_engine

from app.config import get_settings
from app.models import User, UserCreate  # noqa: F401

settings = get_settings()

engine = create_engine(
    f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}@{settings.postgres_server}/{settings.postgres_db}"
)
