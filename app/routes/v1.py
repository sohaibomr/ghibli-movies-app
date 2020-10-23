"""App routes
"""
from app.utils import common
from fastapi import APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

TEMPLATES = Jinja2Templates(directory="templates")
V1 = APIRouter()
@V1.get("/movies/", status_code=status.HTTP_200_OK)
def get_movies(request: Request, response: Response):
    """Returns all the movies with it's people.
    """
    movies, is_latest = common.get_movies_cache()

    if movies is None:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"msg": "Somethings wrong, please retry in few seconds"}
    return TEMPLATES.TemplateResponse("movies.html", {'request': request, "movies": movies, "is_latest": is_latest})
