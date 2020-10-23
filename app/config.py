from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Settings class to maintain/access configurations across the app.
    """
    log_level: str = Field(default="info", env="LOG_LEVEL")
    app_host: str = Field(default="127.0.0.1", env="APP_HOST")
    app_port: int = Field(default=8000, env="APP_PORT")
    movies_url: str = Field(
        default="https://ghibliapi.herokuapp.com/films", env="MOVIES_URL")
    people_url: str = Field(
        default="https://ghibliapi.herokuapp.com/people", env="PEOPLE_URL")


SETTINGS = Settings(_env_file=".env")
