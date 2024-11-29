from fastapi import APIRouter, HTTPException, Depends

from src.api.auth.oauth import get_current_user
from src.api.models import Song, SongResponse, SongUpdate, SongCreate
from src.api.schemas import create_song, retrieve_song, retrieve_songs, delete_song, update_song


song_router = APIRouter(
    prefix='/songs',
    tags=['songs']
)


@song_router.post("/", response_model=SongResponse)
async def add_song(song: Song, current_user: dict = Depends(get_current_user)):
    new_song = await create_song(song_data=song, current_user=current_user)
    return new_song


@song_router.get("/", response_model=list[SongResponse])
async def get_songs():
    songs = await retrieve_songs()
    return songs


@song_router.get("/{id}", response_model=SongResponse)
async def get_song(id: str):
    song = await retrieve_song(id)
    if not song:
        raise HTTPException(status_code=404, detail="Song not found")
    return song


@song_router.patch("/{id}", response_model=SongResponse)
async def update_song_data(id: str, book: SongUpdate):
    updated = await update_song(id, book)
    if not updated:
        raise HTTPException(status_code=404, detail="Song not found or no data to update")
    return await retrieve_song(id)


@song_router.delete("/{id}")
async def delete_song_data(id: str):
    deleted = await delete_song(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Song not found")
    return {"message": "Song deleted successfully"}
