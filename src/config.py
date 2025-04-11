from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

print(settings.DATABASE_URL)
