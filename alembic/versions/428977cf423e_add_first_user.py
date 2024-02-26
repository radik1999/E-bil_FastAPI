"""add first user

Revision ID: 428977cf423e
Revises: 4788316d93e8
Create Date: 2024-02-23 16:08:13.133524

"""
import os
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


from app.core import get_password_hash


# revision identifiers, used by Alembic.
revision: str = '428977cf423e'
down_revision: Union[str, None] = '4788316d93e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

user_table = table(
    "users",
    column("id", sa.BIGINT()),
    column("email", sa.String()),
    column("full_name", sa.String()),
    column("hashed_password", sa.String()),
)


def get_first_user_creds():
    return {
        "email": os.environ["FIRST_USER_EMAIL"],
        "full_name": "First User",
        "hashed_password": get_password_hash(os.environ["FIRST_USER_PASSWORD"]),
    }


def upgrade() -> None:
    op.bulk_insert(user_table, [get_first_user_creds()])


def downgrade() -> None:
    op.execute(f"DELETE FROM users WHERE email = '{get_first_user_creds()['email']}'")
