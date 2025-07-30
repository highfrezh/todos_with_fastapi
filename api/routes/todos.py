from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.services.todos import (
    get_todos,
    get_todo,
    create_todo,
    update_todo,
    delete_todo
)
from schemas.schemas import TodoCreate, Todo, TodoUpdate
from database import get_db
from core.security import get_current_user_from_token

router = APIRouter(tags=["todos"])

@router.get("/", response_model=List[Todo])
def read_todos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user_from_token)
):
    return get_todos(db, user_id=current_user.id, skip=skip, limit=limit)

@router.post("/", response_model=Todo, status_code=201)
def create_new_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user_from_token)
):
    return create_todo(db, todo=todo, user_id=current_user.id)

@router.get("/{todo_id}", response_model=Todo)
def read_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user_from_token)
):
    return get_todo(db, todo_id=todo_id, user_id=current_user.id)

@router.put("/{todo_id}", response_model=Todo)
def update_existing_todo(
    todo_id: int,
    todo: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user_from_token)
):
    return update_todo(db, todo_id=todo_id, todo=todo, user_id=current_user.id)

@router.delete("/{todo_id}")
def delete_existing_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user_from_token)
):
    return delete_todo(db, todo_id=todo_id, user_id=current_user.id)