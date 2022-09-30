import pytest


@pytest.mark.xfail
def test_xfail():
    assert 1 == 2


@pytest.mark.skip
def test_skip():
    print("测试自定skip")


def test_append():
    li2 = ['a', 'b', 'c']
    li2.append(['d', 'e', 'f'])
    print("append>>>>=%s" % li2)


@pytest.mark.my_skip
def test_skip2():
    print("测试自定义mark")


@pytest.mark.my_skip1
def test_skip3():
    print("测试自定义mark11===test_skip3")
