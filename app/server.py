"""server
"""
from fastapi import FastAPI

from app.routes import v1
from app.services import collect_movies
from app.utils import common

APP = FastAPI(on_startup=[common.start_up, collect_movies.update_movies_cache],
              on_shutdown=[common.shut_down])
APP.include_router(v1.V1, prefix="", tags=["v1"])
