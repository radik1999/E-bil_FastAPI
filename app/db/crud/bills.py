from sqlmodel import select

from app.api.deps import SessionDep, CurrentUser
from app.models import Bill


def get_db_bills(session: SessionDep, user: CurrentUser):
    query = select(Bill).where(Bill.owner_id == user.id)
    bills = session.exec(query).all()
    return bills
