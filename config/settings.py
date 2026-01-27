from dotenv import load_dotenv              # Load environment variables from .env
from pydantic_settings import BaseSettings  # Base class for settings management

load_dotenv()  # Read .env and add variables to environment


class Settings(BaseSettings):
    # MongoDB connection URL
    MONGO_DB_URL: str

    # MongoDB database name
    MONGO_DB_NAME: str

    # Ollama server URL
    OLLAMA_URL: str

    # Ollama model name(s)
    OLLAMA_MODELS: str

    class Config:
        env_file = ".env"                   # Path to .env file
        env_file_encoding = "utf-8"         # Encoding of .env file
