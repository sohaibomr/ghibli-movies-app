"""service to collect all movies
"""
from app.utils import common
from fastapi_utils.tasks import repeat_every


@repeat_every(seconds=50, wait_first=False, raise_exceptions=True)
async def get_movies_people():
    """Calls the ghibli server, collect movies and it's people, and saves in a cache.

    Returns:
        [type]: [description]
    """
    print("Loading cache...")
    movies = None
    peoples = None
    cahce = {}
    async with common.CLIENT_SESSION.get("https://ghibliapi.herokuapp.com/films") as response:
        movies = await response.json()

    async with common.CLIENT_SESSION.get("https://ghibliapi.herokuapp.com/people") as response:
        peoples = await response.json()
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
            film_id = movie.split("/")[-1]
            cahce[film_id]["people"].append(people)
    common.update_cache(cahce)
