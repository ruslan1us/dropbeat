from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from src.api.routers.auth_router import auth_router


app = FastAPI()


app.include_router(auth_router)


@app.get('/')
async def redirect_to_docs(request: Request):
    return RedirectResponse(f'{request.url}docs')