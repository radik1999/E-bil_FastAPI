from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import get_current_user, SessionDep
from app.db.crud.users import get_user_by_email, create_user as crud_create_user
from app.models import UserOut, UserCreate

router = APIRouter()


@router.post(
    "/", dependencies=[Depends(get_current_user)], response_model=UserOut
)
def create_user(session: SessionDep, user_in: UserCreate):
    """
    Create new user.
    """
    user = get_user_by_email(session=session, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )

    user = crud_create_user(session=session, user_create=user_in)

    return user

