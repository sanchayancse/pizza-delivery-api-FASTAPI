from fastapi import APIRouter, HTTPException,status
from database import Session,engine
from schemas import SignUpModel, UserResponseModel
from models import User
from werkzeug.security import generate_password_hash, check_password_hash 
auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

session = Session(bind=engine)

@auth_router.get("/")
async def hello():
    return {"message": "Hello, World!"}



@auth_router.post("/signup", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
async def signup(user:SignUpModel):
    # Implement signup logic here
    db_email=session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    db_username=session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")


    new_user=User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        isActive=user.isActive,
        isStaff=user.isStaff
    )
    session.add(new_user)
    session.commit()
    return new_user