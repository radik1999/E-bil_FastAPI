from fastapi import APIRouter

from app.api import login, users, bills

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(bills.router, prefix="/bills", tags=["bills"])
