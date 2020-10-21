"""App routes
"""
from app.utils import common
from fastapi import APIRouter

V1 = APIRouter()
@V1.get("/movies/")
def get_movies():
    """Returns all the movies with it's people.
    """
    movies, is_latest = common.get_movies_cache()

    if movies is None:
        return {"code": "400"}
    return {"movies": movies, "is_latest": is_latest}
