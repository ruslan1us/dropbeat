from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from src.api.routers.auth_router import auth_router
from src.api.routers.song_router import song_router
from src.database import create_indexes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_indexes()
    yield

app = FastAPI(
    lifespan=lifespan
)


app.include_router(auth_router)
app.include_router(song_router)


@app.get('/')
async def redirect_to_docs(request: Request):
    return RedirectResponse(f'{request.url}docs')