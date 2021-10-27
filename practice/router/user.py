from fastapi import APIRouter, Depends
from schemas import UserBase
from sqlalchemy.orm import Session
from typing import List
from database.db import get_db
from database import db_user
from schemas import ShowUser
from auth.auth_user import get_current_user



router = APIRouter(prefix='/user', tags=['User'])



@router.post('/', response_model=ShowUser)
def create_user(request: UserBase, db: Session=Depends(get_db)):
    return db_user.create_user(db,request)


@router.get('/', response_model=List[ShowUser])
def get_users(db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return db_user.get_all_users(db)


@router.get('/{id}', response_model=ShowUser)
def get_user_by_id(id: int, db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return db_user.get_user(db, id)


@router.put('/update/{id}')
def update_user_by_id(id: int, request: UserBase, db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return db_user.update_user(db, id, request)


@router.delete('/delete/{id}')
def delete_user_by_id(id: int, db:Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return db_user.delete_user(db, id)
