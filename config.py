from pydantic import BaseSettings
from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url : str = ""

    class Config:
        env_file= ".env"

# @lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for : {settings.env_name}")
    return Settings