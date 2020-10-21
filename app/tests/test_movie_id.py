import pytest
from app.services.collect_movies import get_movie_id


def test_parse_movie_id():
    url = "https://ghibliapi.herokuapp.com/films/030555b3-4c92-4fce-93fb-e70c3ae3df8b"
    actual_id = get_movie_id(url)
    expected_id = "030555b3-4c92-4fce-93fb-e70c3ae3df8b"
    assert actual_id == expected_id
