import pytest


@pytest.fixture(autouse=True)
def test1():
    print('\n开始执行function')


def testa():
    print('------用例a执行------')


class TestCase:
    def test_b(self):
        print('------用例b执行------')


if __name__ == '__main__':
    pytest.main(['-sv', 'test_fixture5.py'])