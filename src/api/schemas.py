from bson import ObjectId

from src.database import song_collection
from src.api.models import Song, SongUpdate


def song_helper(song) -> dict:
    return {
        "id": str(song["_id"]),
        "title": song["title"],
        "author": song["author"],
        "description": song["description"],
        "length": song["length"],
        "link": song["link"]
    }


async def create_song(song_data, current_user) -> dict:
    song_data_dict = song_data.dict()
    song_data_dict['author'] = current_user
    song = await song_collection.insert_one(song_data_dict)
    new_song = await song_collection.find_one({"_id": song.inserted_id})
    return song_helper(new_song)


async def retrieve_song(id: str) -> dict:
    song = await song_collection.find_one({"_id": ObjectId(id)})
    return song_helper(song) if song else None


async def retrieve_songs():
    songs = []
    async for song in song_collection.find():
        songs.append(song_helper(song))
    return songs


async def update_song(id: str, data: SongUpdate):
    if len(data.dict(exclude_unset=True)) < 1:
        return False
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        updated_song = await song_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data.dict(exclude_unset=True)}
        )
        if updated_song:
            return True
    return False


async def delete_song(id: str):
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        await song_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False
