import pytest
from database import Database
from bun import Bun
from ingredient import Ingredient

@pytest.fixture
def with_database():
    return Database()

def test_available_buns(with_database):
    buns = with_database.available_buns()
    assert len(buns) == 3
    for bun in buns:
        assert isinstance(bun, Bun)
        assert bun.get_name() != ""
        assert bun.get_price() > 0

def test_available_ingredients(with_database):
    ingredients = with_database.available_ingredients()
    assert len(ingredients) == 6
    for ingredient in ingredients:
        assert isinstance(ingredient, Ingredient)
        assert ingredient.get_name() != ""
        assert ingredient.get_type() != ""
        assert ingredient.get_price() > 0
