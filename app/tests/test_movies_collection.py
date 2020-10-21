import asyncio
import time

import pytest
from app import config, server
from app.services import collect_movies
from app.utils import common


@pytest.mark.asyncio
async def test_films_collection():
    await common.start_up()
    films, is_latest = await collect_movies.collect_movies_info(
        config.SETTINGS.films_url, config.SETTINGS.people_url)

    await common.shut_down()
    assert films is not None
    assert is_latest is True


@pytest.mark.asyncio
async def test_films_collection_invalid_url():
    await common.start_up()
    films, is_latest = await collect_movies.collect_movies_info(
        "x.x.x.x", "x.x.x.x")

    await common.shut_down()
    assert is_latest is False
    assert films is None
