from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy import engine
from router import  blog_get, blog_post, user, article, product, file
from auth import authentication
from database import models
from database.db import engine


app = FastAPI()

app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)



@app.get('/hello')
def index():
    return 'Hello world !'

models.Base.metadata.create_all(engine)

app.mount("/media", StaticFiles(directory="media"), name="media")