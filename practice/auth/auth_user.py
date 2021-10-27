from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import get_db
from datetime import datetime, timedelta
from database import db_user 
from jose import jwt



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '71e9a1cf72e72d13ee7022a1823e818631991b56cd0581be91c1c23222c44b03'
ALGORITHME = 'HS256'
ACCESS_TOKEN_EXPIRE8MINUTES = 30



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHME)
    return encoded_jwt


def get_current_user(token: str=Depends(oauth2_scheme), db:Session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHME])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = db_user. get_user_by_username(db, username)
    if user is None:
        raise credentials_exception
    return user