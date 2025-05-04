from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "saYit API"
    API_V1_STR: str = "/api/v1"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER","sayit_user")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD","safe1234")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST","localhost")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB","sayit_db")

    DATABASE_URI: Optional[PostgresDsn] = None

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}/{self.POSTGRES_DB}"
    
    SECRET_KEY: str = os.getenv("SECRET_KEY","safe1234")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        case_sensitive = True

settings = Settings()