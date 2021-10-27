from fastapi import APIRouter, Depends
from schemas import ArticleBase, ShowArticle
from sqlalchemy.orm import Session
from typing import List
from schemas import UserBase
from database import db_article
from database.db import get_db
from auth.auth_user import get_current_user


router = APIRouter(prefix='/article', tags=['Article'])


@router.post('/create', response_model=ShowArticle)
def create_article(request: ArticleBase, db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return db_article.create_article(db, request)


@router.get('/all',  response_model=List[ShowArticle])
def get_all_article(db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return db_article.get_articles(db)


@router.get('/get/{id}') #,response_model=ShowArticle )
def get_article_by_id(id: int, db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return {
        "data": db_article.get_article(db, id),
        "current_user": current_user  
    }


@router.put('/update/{id}')
def update_article_by_id():
    pass
    