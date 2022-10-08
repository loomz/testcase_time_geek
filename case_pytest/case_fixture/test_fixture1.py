import pytest

@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 7
    return(a, b)


class TesNum:
    def test_02(self, test_01):
        a = test_01[0]
        b = test_01[1]
        assert a < b
        print("断言成功")

