import pytest

@pytest.fixture
def box():
    return []

@pytest.fixture
def add_a(box):
    box.append('a')
    return box

def test_box(add_a, box):
    assert box == ['a']
