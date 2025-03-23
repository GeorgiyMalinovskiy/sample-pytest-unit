import pytest

from bun import Bun

TEST_DATA = [
    ('Булочка', '100'),
    (100, 100),
    ('Черная булочка', '150'),
    ('Белая булочка', '120')
]

@pytest.fixture(params=TEST_DATA)
def with_bun(request):
    return Bun(*request.param)

def test_get_name(with_bun):
    assert with_bun.get_name() == with_bun.name

def test_get_price(with_bun):
    assert with_bun.get_price() == with_bun.price
