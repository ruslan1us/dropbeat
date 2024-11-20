from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from src.config import DB_PASS, DB_USER


uri = f"mongodb+srv://{DB_USER}:{DB_PASS}@dropbeat.rzh0z.mongodb.net/?retryWrites=true&w=majority&appName=dropbeat"

client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

db = client.dropbeat

song_collection = db['dropbeat_test']
