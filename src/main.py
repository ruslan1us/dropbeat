from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Starting...')
    yield
    print('Off...')

app = FastAPI(
    title='DropBeat',
    lifespan=lifespan)


@app.get('/')
async def redirect_to_docs(request: Request):
    return RedirectResponse(f'{request.url}docs')
