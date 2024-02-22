from sqlmodel import create_engine, SQLModel, Session, select

from app.db.crud.users import create_user
from app.models import User, UserCreate  # noqa: F401


# todo get the database url from the env
engine = create_engine("postgresql+psycopg2://postgres:postgres@postgres/app")

SQLModel.metadata.create_all(bind=engine)

session = Session(engine)

EMAIL = "test@gmail.com"
PASSWORD = "test"


def create_first_superuser():
    with session:
        super_user = session.exec(select(User).where(User.email == EMAIL)).first()

        if not super_user:
            super_user = UserCreate(
                email=EMAIL,
                password=PASSWORD,
            )
            create_user(session, super_user)


create_first_superuser()

# todo figure out how to create tabels during runtime
# maybe use alembic
