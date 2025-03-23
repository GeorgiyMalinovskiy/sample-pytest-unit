import pytest

from ingredient import Ingredient

TEST_DATA = [
    ('Тип', 'Название', '100'),
    (100, 100, 100),
    ('Соус', 'Кетчуп', '50'),
    ('Котлета', 'Говяжья', '200')
]

@pytest.fixture(params=TEST_DATA)
def with_ingredient(request):
    return Ingredient(*request.param)

def test_get_name(with_ingredient):
    assert with_ingredient.get_name() == with_ingredient.name

def test_get_price(with_ingredient):
    assert with_ingredient.get_price() == with_ingredient.price

def test_get_type(with_ingredient):
    assert with_ingredient.get_type() == with_ingredient.type
