"""Utils to setup, teardown services
"""


from aiohttp import ClientSession
from cachetools import TTLCache

CLIENT_SESSION: ClientSession
CACHE_MOVIES: TTLCache


async def start_up():
    """bootstrap services before the api server starts
    """

    print("Creating client sessions and movies cache")
    global CLIENT_SESSION
    CLIENT_SESSION = ClientSession()

    global CACHE_MOVIES
    CACHE_MOVIES = TTLCache(maxsize=10, ttl=60)


async def shut_down():
    """Teardown services gracefully
    """
    print("Graceful shut down")
    global CLIENT_SESSION
    await CLIENT_SESSION.close()
    global CACHE_MOVIES
    CACHE_MOVIES.clear()


def update_cache(movies: dict):
    global CACHE_MOVIES
    CACHE_MOVIES["movies"] = movies
    print("Updating cache")


def get_cache(key: str):
    global CACHE_MOVIES
    return CACHE_MOVIES[key]
