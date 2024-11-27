from bson import ObjectId
from fastapi import FastAPI, Depends, Response, Request
from fastapi.responses import RedirectResponse
from src.api.auth.hashing import Hash
from src.api.auth.models import User
from src.api.auth.oauth import get_current_user
from src.api.auth.jwttoken import create_access_token

from src.database import user_collection


app = FastAPI()


@app.post('/register')
async def create_user(request: User):
    hashed_pass = Hash.bcrypt(request.password)
    user_object = dict(request)
    user_object["password"] = hashed_pass
    user = user_collection.insert_one(user_object)
    return {"res": "created"}


@app.get("/profile")
async def read_profile(username: ObjectId = Depends(get_current_user)):
    return {"message": f"Welcome {username}!"}


@app.post('/login')
async def login(user: User, response: Response):
    token_data = {"sub": user.username}
    token = create_access_token(token_data)

    response.set_cookie(key="access_token", value=token, httponly=True, secure=True, samesite="lax")

    return {"message": "Login successful"}


@app.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logout successful"}


@app.get('/')
async def redirect_to_docs(request: Request):
    return RedirectResponse(f'{request.url}docs')