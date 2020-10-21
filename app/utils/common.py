"""Utils to setup, teardown services
"""

import logging

from aiohttp import ClientSession, ClientTimeout
from app.services import collect_movies
from cachetools import LRUCache

LOGGER = logging.getLogger("collect_movies")
CLIENT_SESSION: ClientSession
CACHE_MOVIES: LRUCache


async def start_up():
    """bootstrap services before the api server starts
    """

    LOGGER.info("Creating client sessions and movies cache")
    timeout = ClientTimeout(total=4)
    global CLIENT_SESSION
    CLIENT_SESSION = ClientSession(timeout=timeout)

    global CACHE_MOVIES
    CACHE_MOVIES = LRUCache(maxsize=10)


async def shut_down():
    """Teardown services gracefully
    """
    LOGGER.info("Graceful shut down")
    global CLIENT_SESSION
    await CLIENT_SESSION.close()
    global CACHE_MOVIES
    CACHE_MOVIES.clear()


def update_cache(key: str, movies: dict, success: bool):
    global CACHE_MOVIES
    if success is True:
        CACHE_MOVIES[key] = movies
        CACHE_MOVIES["is_latest"] = success
        LOGGER.info("Updated cache with latest movies results")
    elif not success:
        CACHE_MOVIES["is_latest"] = success
        LOGGER.warning("Failed to Update cache with latest movies results")


def get_movies_cache():
    global CACHE_MOVIES
    return CACHE_MOVIES.get("movies"), CACHE_MOVIES.get("is_latest")
