import pytest

@pytest.fixture
def order():
    return []

@pytest.fixture(autouse=True)
#@pytest.fixture(scope="module")
def seed(order):
    order.append('seed')


def test_validate_seed(order):
    assert order == ['seed']

def test_add_item(order):
    order.append('item')
    assert order == ['seed', 'item']


