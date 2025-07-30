from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from core.security import create_access_token
from core.config import settings
from api.services.auth import authenticate_user, create_user
from schemas.schemas import Token, UserCreate, LoginRequest
from database import get_db

router = APIRouter(tags=["auth"])

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: LoginRequest, db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)