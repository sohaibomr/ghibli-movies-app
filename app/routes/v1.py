"""App routes
"""
from app.utils import common
from fastapi import APIRouter

V1 = APIRouter()
@V1.get("/movies/")
def get_movies():
    """Returns all the movies with it's people.
    """
    return common.get_cache("movies")
