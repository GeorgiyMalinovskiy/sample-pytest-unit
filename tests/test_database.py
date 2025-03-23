import pytest
from database import Database

@pytest.fixture
def with_database():
    return Database()

def test_available_buns(with_database):
    assert len(with_database.available_buns()) == 3

def test_available_ingredients(with_database):
    assert len(with_database.available_ingredients()) == 6
