from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.models import Todo
from schemas.schemas import TodoCreate, TodoUpdate

def get_todos(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Todo).filter(Todo.owner_id == user_id).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int, user_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == user_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

def create_todo(db: Session, todo: TodoCreate, user_id: int):
    db_todo = Todo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: TodoUpdate, user_id: int):
    db_todo = get_todo(db, todo_id, user_id)
    for key, value in todo.dict(exclude_unset=True).items():
        setattr(db_todo, key, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int, user_id: int):
    todo = get_todo(db, todo_id, user_id)
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully"}