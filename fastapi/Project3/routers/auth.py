from fastapi import APIRouter, Depends
from typing import Annotated
from pydantic import BaseModel, Field
from models import Users
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import SessionLocal
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import timedelta, datetime, timezone
from http.client import HTTPException

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

SECRET_KEY = '84d9b42b4649fcc01d9b947c2b3549217a8b4646e52e411d88ecc2b05e8df919'
ALGORITHM = 'HS256'

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

class UserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role :str

class Token(BaseModel):
    access_token: str
    token_type: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username==username).first()
    if not user:
        return False

    if not bcrypt_context.verify(password, user.hashed_password):
        return False

    return user

def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):

    encode = {"sub": username, "id": user_id, "role": role}
    expires = datetime.now(tz=timezone.utc) + expires_delta
    encode.update({"exp":expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        user_role: str = payload.get("role")
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could not validate user.")
        return {"username":username, "id":user_id, "user_role": user_role}
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate user.")


@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, 
                      create_user_request: UserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        is_active=True
    )
    db.add(create_user_model)
    db.commit()


@router.post("/token",response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not validate user.")

    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    
    return {"access_token":token, "token_type":"bearer"}