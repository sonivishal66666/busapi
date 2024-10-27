# app/database.py
import motor.motor_asyncio
from pydantic import BaseSettings

class Settings(BaseSettings):
    mongodb_uri: str
    database_name: str

    class Config:
        env_file = ".env"

settings = Settings()

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
database = client[settings.database_name]
blog_collection = database.get_collection("blogs")
