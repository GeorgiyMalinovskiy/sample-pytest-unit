import pytest
from burger import Burger
from bun import Bun
from ingredient import Ingredient

TEST_DATA = {
    'BUN': ("Тестовая булочка", 101),
    'INGREDIENT': ("Тип", "Название", 100)
}

@pytest.fixture
def with_burger():
    return Burger()

@pytest.fixture
def with_bun_burger(with_burger):
    with_burger.set_buns(Bun(*TEST_DATA['BUN']))
    return with_burger

@pytest.fixture
def with_bun_ingredient_burger(with_bun_burger):
    with_bun_burger.add_ingredient(Ingredient(*TEST_DATA['INGREDIENT']))
    return with_bun_burger

def test_set_buns(with_burger):
    with_burger.set_buns(Bun(*TEST_DATA['BUN']))
    test_name = TEST_DATA['BUN'][0]
    test_price = TEST_DATA['BUN'][1]
    assert with_burger.bun.get_name() == test_name and with_burger.bun.get_price() == test_price

def test_add_ingredient(with_bun_burger):
    ingredient = Ingredient(*TEST_DATA['INGREDIENT'])
    with_bun_burger.add_ingredient(ingredient)
    new_ingredient = with_bun_burger.ingredients[0]
    test_type = TEST_DATA['INGREDIENT'][0]
    test_name = TEST_DATA['INGREDIENT'][1]
    test_price = TEST_DATA['INGREDIENT'][2]
    assert new_ingredient.get_type() == test_type and new_ingredient.get_name() == test_name and new_ingredient.get_price() == test_price

def test_remove_ingredient(with_bun_ingredient_burger):
    with_bun_ingredient_burger.remove_ingredient(0)
    assert len(with_bun_ingredient_burger.ingredients) == 0

def test_move_ingredient(with_bun_ingredient_burger):
    TEST_INGREDIENT = ('Тип1', 'Название1', 200)
    ingredient = Ingredient(*TEST_INGREDIENT)
    with_bun_ingredient_burger.add_ingredient(ingredient)
    with_bun_ingredient_burger.move_ingredient(1,0)
    assert with_bun_ingredient_burger.ingredients[0].get_name() ==  TEST_INGREDIENT[1]

def test_get_price(with_bun_ingredient_burger):
    test_bun_price = TEST_DATA['BUN'][1]
    test_ingredient_price = TEST_DATA['INGREDIENT'][2]
    assert with_bun_ingredient_burger.get_price() == (test_bun_price * 2) + test_ingredient_price

def test_get_receipt(with_bun_ingredient_burger):
    test_ingredient = with_bun_ingredient_burger.ingredients[0]
    test_bun = with_bun_ingredient_burger.bun
    receipt_lines = with_bun_ingredient_burger.get_receipt().split('/n')
    assert test_bun.get_name() in receipt_lines[0]
    assert test_bun.get_name() in receipt_lines[0]
    assert test_bun.get_name() in receipt_lines[0]