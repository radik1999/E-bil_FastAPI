from sqlmodel import create_engine, SQLModel, Session, select

from app.config import get_settings
from app.db.crud.users import create_user
from app.models import User, UserCreate  # noqa: F401

settings = get_settings()

engine = create_engine(
    f"postgresql+psycopg2://{settings.postgres_user}:{settings.postgres_password}@postgres/{settings.postgres_db}"
)
SQLModel.metadata.create_all(bind=engine)

session = Session(engine)


def create_first_user():
    with session:
        super_user = session.exec(select(User).where(User.email == settings.first_user_email)).first()

        if not super_user:
            super_user = UserCreate(
                email=settings.first_user_email,
                password=settings.first_user_password,
            )
            create_user(session, super_user)


create_first_user()

# todo figure out how to create tabels during runtime
# maybe use alembic
