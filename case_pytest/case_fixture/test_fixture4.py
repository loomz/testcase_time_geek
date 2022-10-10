import pytest

@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 6
    return(a, b)


@pytest.fixture(scope="class")
def test_02():
    print("你是第二执行")


@pytest.mark.usefixtures("test_02")
class TestNum:
    def test_03(self, test_01):
        a = test_01[0]
        b = test_01[1]
        assert a == b
        print("断言成功")


