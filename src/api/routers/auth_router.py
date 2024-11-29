from fastapi import APIRouter, HTTPException, status, Depends, Response

from src.api.auth.models import User, Login
from src.api.auth.oauth import get_current_user
from src.api.auth.schemas import create_user, login

auth_router = APIRouter(prefix='/auth', tags=['auth'])


@auth_router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(request: User):
    await create_user(request)
    return {"res": "created"}


@auth_router.get("/profile")
async def read_profile(username: str = Depends(get_current_user)):
    return {"message": f"Welcome {username}!"}


@auth_router.post('/login')
async def login_user(user: Login, response: Response):
    await login(user=user, response=response)
    return {"message": "Login successful"}


@auth_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logout successful"}