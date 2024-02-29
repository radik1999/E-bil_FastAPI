from datetime import datetime

from pydantic import EmailStr
from sqlmodel import SQLModel, Field, AutoString, Relationship, JSON, Column

from app.constants import PymentType


class UserBase(SQLModel):
    email: EmailStr = Field(unique=True, index=True, sa_type=AutoString)
    full_name: str | None = None


class User(UserBase, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str

    bills: list["Bill"] = Relationship(back_populates="owner")


class UserOut(UserBase):
    id: int


class UserCreate(UserBase):
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(SQLModel):
    sub: int | None = None


class BillsProducts(SQLModel, table=True):
    __tablename__ = "bills_products"

    bill_id: int | None = Field(default=None, foreign_key="bills.id", primary_key=True)
    product_id: int | None = Field(default=None, foreign_key="products.id", primary_key=True)


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    amount: float

    bills: list["Bill"] = Relationship(back_populates="products", link_model=BillsProducts)


class Payment(SQLModel):
    type: PymentType
    amount: float


class Bill(SQLModel, table=True):
    __tablename__ = "bills"

    id: int | None = Field(default=None, primary_key=True)
    total: float
    rest: float
    created_at: datetime = Field(default=datetime.now())

    products: list[Product] = Relationship(back_populates="bills", link_model=BillsProducts)

    payment_json: dict = Field(sa_column=Column("payment", JSON))

    @property
    def payment(self):
        return Payment.model_validate(self.payment_json)

    @payment.setter
    def payment(self, value):
        self.payment_json = value.json()

    owner_id: int = Field(foreign_key="users.id")
    owner: User = Relationship(back_populates="bills")
