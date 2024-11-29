from src.api.auth.jwttoken import create_access_token
from src.database import user_collection
from src.api.auth.hashing import Hash


async def create_user(user):
    hashed_pass = Hash.bcrypt(user.password)
    user_object = dict(user)
    user_object["password"] = hashed_pass
    user = await user_collection.insert_one(user_object)


async def login(user, response):
    token_data = {"sub": user.username}
    token = create_access_token(token_data)

    response.set_cookie(key="access_token", value=token, httponly=True, secure=True, samesite="lax")

