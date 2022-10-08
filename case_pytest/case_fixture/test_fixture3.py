import pytest

@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 7
    return(a, b)



@pytest.fixture(scope="class")
def test_02():
    print("你是第二执行")


@pytest.mark.usefixtures("test_02")
@pytest.mark.usefixtures("test_01")
class TesNum:
    def test_03(self, test_01):
        a = test_01[0]
        b = test_01[1]
        assert a < b
        print("断言成功")

if __name__ == '__main__':
    pytest.main(['-sv', 'test_fixture3.py'])