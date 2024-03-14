from typing import Annotated

from fastapi import APIRouter, Body

from app.api.deps import CurrentUser, SessionDep
from app.db.crud.bills import get_db_bills
from app.db.crud.products import get_products
from app.models import BillCreate, Bill

router = APIRouter()


@router.post("/")
async def create_bill(session: SessionDep, user: CurrentUser, bill: Annotated[BillCreate, Body()]):
    products = get_products(session, bill.products)
    bill = Bill.model_validate(
        bill, update={"owner_id": user.id, "products": products, "payment": bill.payment.model_dump()}
    )
    session.add(bill)
    session.commit()

    return {"message": "Bill created successfully"}


@router.get("/", response_model=list[Bill])
async def get_bills(session: SessionDep, user: CurrentUser):
    bills = get_db_bills(session, user)
    return bills
