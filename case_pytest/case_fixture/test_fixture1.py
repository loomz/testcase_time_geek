import pytest

# 官方文档 https://docs.pytest.org/en/stable/explanation/fixtures.html#
# 官方中文文档翻译 https://learning-pytest.readthedocs.io/zh/latest/doc/fixture/intro.html

@pytest.fixture(scope="class")
def test_01():
    a = 6
    b = 7
    return(a, b)


class TestNum:
    def test_02(self, test_01):
        a = test_01[0]
        b = test_01[1]
        assert a < b
        print("断言成功")

