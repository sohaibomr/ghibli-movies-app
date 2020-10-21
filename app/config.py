from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    LOG_LEVEL: str = Field(default="info", env="LOG_LEVEL")
    app_host: str = Field(default="127.0.0.1", env="APP_HOST")
    app_port: int = Field(default=8000, env="APP_PORT")
    films_url: str = Field(
        default="https://ghibliapi.herokuapp.com/films", env="FILMS_URL")
    people_url: str = Field(
        default="https://ghibliapi.herokuapp.com/people", env="PEOPLE_URL")


SETTINGS = Settings()
