import asyncio
import time

import pytest
from app import config, server
from app.services import collect_movies
from app.utils import common


@pytest.mark.asyncio
async def test_movies_collection():
    """Tests if movies are fetched and processed successfully
    """
    await common.start_up()
    movies, is_latest = await collect_movies.collect_movies_info(
        config.SETTINGS.movies_url, config.SETTINGS.people_url)

    await common.shut_down()
    assert movies is not None
    assert is_latest is True


@pytest.mark.asyncio
async def test_movies_collection_invalid_url():
    """this serves as a negative testcase, to check that movies collection fails given wrong url or connection or timeouts error
    """
    await common.start_up()
    movies, is_latest = await collect_movies.collect_movies_info(
        "x.x.x.x", "x.x.x.x")

    await common.shut_down()
    assert is_latest is False
    assert movies is None
