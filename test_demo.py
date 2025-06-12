import pytest


@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')

@pytest.fixture()
def  num ():
    print('Начало теста')
    yield
    print('\nКонец теста')





def test_demo1(num):
    assert 1 == 1


def test_demo2(before_after):
    assert 2 == 2