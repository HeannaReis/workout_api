from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://workout:workout@localhost/workout')


settings = Settings()