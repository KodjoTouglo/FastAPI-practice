from fastapi import status, HTTPException
from database.models import DbArticle
from schemas import ArticleBase
from sqlalchemy.orm.session import Session



def create_article(db: Session, request: ArticleBase):
    article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Article with id {id} does not exist.")
    return article


def get_articles(db: Session):
    return db.query(DbArticle).all()


def update_article_by_id(db: Session, id: int, request: ArticleBase):
    article = db.query(DbArticle).filter(DbArticle.id == id)
    article.update({
       DbArticle.title: request.title,
       DbArticle.content: request.content,
       DbArticle.published: request.published,
       DbArticle.user_id : request.user_id
    })
    db.commit()
    if not article:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
       detail=f"Article with id {id} does not exist.")
    return article
