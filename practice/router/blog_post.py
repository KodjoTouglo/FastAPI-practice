from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List, Dict

router = APIRouter(prefix='/blog', tags=['Blog'])



class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    NbrComments: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key': 'value'}
    image: Optional[Image] = None

@router.post('/new')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    blog.title
    return {
            'id': id,
            'data': blog,
            'version': version
            }


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int, comment_id: int = Query(None,
                        title='Id of the comment',
                        description='Some description for comment_id',
                        alias='commentId',
                        deprecated=True
                    ),
                    content: str = Body(..., min_lenght=10,
                        max_lenght=50,
                        regex='^[a-z\s]*$'),
                    v: Optional[List[str]] = Query(['1.0', '2.0', '3.0']) 
                ):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version': v
    }

def required_functionality():
    return {"message": "Learning FastAPI"}