from fastapi import APIRouter,status,Depends


auth_router = APIRouter()

@auth_router.post('/login',status_code=status.HTTP_200_OK)
async def login():
    return {"message":"login successful"}

@auth_router.post('/signup',status_code=status.HTTP_201_CREATED)
async def signup():
    return {"message":"signup successful"}