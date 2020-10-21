"""service to collect all movies
"""
import logging
from asyncio import TimeoutError

from aiohttp import ServerTimeoutError
from aiohttp.client_exceptions import ClientConnectionError, InvalidURL
from aiohttp.web_exceptions import HTTPRequestTimeout
from app import config
from app.utils import common
from fastapi_utils.tasks import repeat_every

LOGGER = logging.getLogger("collect_movies")


def get_movie_id(url: str):
    return url.split("/")[-1]


async def collect_movies_info(films_url: str, people_url: str):
    """Calls the ghibli server, collect movies and it's people, and saves in a cache.

    Returns:
        dict: aggregated movies dict
    """
    LOGGER.info("Initiating movies collector and cache updating job")
    movies = None
    peoples = None
    cahce = {}

    try:
        async with common.CLIENT_SESSION.get(films_url) as response:
            movies = await response.json()

        async with common.CLIENT_SESSION.get(people_url) as response:
            peoples = await response.json()
    except (ClientConnectionError, TimeoutError, InvalidURL) as fetch_exception:
        LOGGER.warning(
            "Fetching movies to update cache failed due to exception, Will retry in 20 seconds")
        return None, False

    for movie in movies:
        movie_id = movie.get("id")
        cahce[movie_id] = {}
        for key in movie:
            if key is not "people" and key is not "id":
                cahce[movie_id][key] = movie.get(key)
        cahce[movie_id]["people"] = []

    # add people in respective movies
    for people in peoples:
        for movie in people.get("films"):
            film_id = get_movie_id(movie)
            cahce[film_id]["people"].append(people)

    LOGGER.info("Movies collection job finished")
    return cahce, True


@repeat_every(seconds=20, wait_first=False, raise_exceptions=True)
async def update_movies_cache():
    """[summary]
    """
    movies, success = await collect_movies_info(config.SETTINGS.films_url,
                                                config.SETTINGS.people_url)
    common.update_cache("movies", movies, success)
