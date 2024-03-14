from sqlmodel import Session, select

from app.models import ProductCreate, Product


def get_products(session: Session, products: list[ProductCreate]):
    return [get_product(session, product) for product in products]


def get_product(session: Session, product: ProductCreate):
    query = select(Product).where(Product.name == product.name)
    db_product = session.exec(query).first()

    return db_product or create_product(session, product)


def create_product(session: Session, product: ProductCreate):
    db_obj = Product.model_validate(product)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj
