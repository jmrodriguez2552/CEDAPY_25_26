import pytest

@pytest.fixture
def numbers():
    return [1, 2, 3,]

@pytest.fixture
def add_number(numbers):
   numbers.append(4)

@pytest.fixture
def add_another_number(numbers):
    numbers.append(99)

def test_numbers(numbers, add_number):
    assert numbers == [1, 2, 3, 4]

def test_numbers_again(numbers, add_another_number):
    assert numbers == [1, 2, 3, 99]
