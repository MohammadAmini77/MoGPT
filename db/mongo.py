from pymongo import MongoClient       # MongoDB client library
from config.settings import Settings  # Load app settings from .env

settings = Settings()  # Initialize settings (loads DB URL and name)

# Connect to MongoDB using the URL from settings
# tz_aware=True makes datetime fields timezone-aware
_client = MongoClient(settings.MONGO_DB_URL, tz_aware=True)

# Select the database from MongoDB
_db = _client[settings.MONGO_DB_NAME]

def get_collection(name: str):
    """
    Return a MongoDB collection by name
    Example: get_collection("users") returns the 'users' collection
    """
    return _db[name]
