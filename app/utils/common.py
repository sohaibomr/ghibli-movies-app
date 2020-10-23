"""Utils to setup, teardown services
"""

import logging
from threading import Lock

from aiohttp import ClientSession, ClientTimeout
from app.services import collect_movies
from cachetools import LRUCache

LOGGER = logging.getLogger("collect_movies")
CLIENT_SESSION: ClientSession
CACHE_MOVIES: LRUCache
LOCK = Lock()


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
        with LOCK:
            CACHE_MOVIES[key] = movies
            CACHE_MOVIES["is_latest"] = success
        LOGGER.info("Updated cache with latest movies results")
    elif success is False:
        with LOCK:
            CACHE_MOVIES["is_latest"] = success
        LOGGER.warning("Failed to Update cache with latest movies results")


def get_movies_cache():
    global CACHE_MOVIES
    with LOCK:
        movies = CACHE_MOVIES.get("movies")
        is_latest = CACHE_MOVIES.get("is_latest")
    return movies, is_latest
