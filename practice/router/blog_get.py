from router.blog_post import required_functionality
from fastapi import APIRouter, Depends
from typing import Optional
from enum import Enum

router = APIRouter(prefix='/blog', tags=['Blog'])



class BlogType(str, Enum):
    short: 'short'
    story: 'story'
    howto: 'howto'


@router.get('/type/{type}')
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@router.get('/all', tags=['blog'], summary="Retrieve all blogs", description="This api call simulates fetching all blogs.")
def get_all_blog(page=1, page_size: Optional[int]=None, req_parameter: dict = Depends(required_functionality)):
    return {"message": "All {page_size} blogs on page {page}.", "req": req_parameter}


@router.get("/{id}/comments/{comment_id}", tags=['Comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {"message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"}


@router.get('/{id}')
def get_blog(id: int):
    return {"detail": f"Blog with id {id}"}

