import pytest

@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 7
    return(a, b)


@pytest.mark.usefixtures("test_01")
class TestNum:
    def test_03(self, test_01):
        a = test_01[0]
        b = test_01[1]
        assert a < b
        print("断言成功")


