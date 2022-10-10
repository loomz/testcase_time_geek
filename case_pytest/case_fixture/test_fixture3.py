import pytest

@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 7
    print("one")
    return(a, b)




@pytest.fixture(scope="class")
def test_02():
    print("你是第二执行")

# 如果一个方法或者一个class用例想要同时调用多个fixture，可以使用@pytest.mark.usefixture()进行叠加。注意叠加顺序，先执行的放底层，后执行的放上层。
@pytest.mark.usefixtures("test_02")
@pytest.mark.usefixtures("test_01") # 优先执行
class TestNum:
    def test_03(self, test_01):
        a = test_01[0]
        b = test_01[1]
        assert a < b
        print("断言成功")

