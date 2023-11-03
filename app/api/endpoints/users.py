from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from sqlalchemy.orm import Session


router = APIRouter()


@router.get(
    path="/",
    response_model=Account,
    status_code=status.HTTP_200_OK,
    summary="Get current account",
)
async def read_user_me(
        db: Session = Depends(dependency.get_db),
        current_user: Accounts = Depends(dependency.get_current_user)
) -> Any:
    """
    Get current account.
    """
    return current_user

