import pytest

# test_postcode.py
# fixture  固件 方法名可以当参数使用
# 固件的名称默认为定义时的函数名，如果不想使用默认，可以通过 name 选项指定名称：
@pytest.fixture(scope='function',name='postcode')
def postcode9999999999999():
    print("\n测试开始------>")
    return '010'

# 一个文件代表一个module，设置成module就表示执行一个文件只会登录一次

# 如果固件的名称默认为定义时的函数名,参数名是定义函数名才可以,不然运行失败
'''
def test_postcode(postcode9999999999999):
    assert postcode9999999999999 == '010'
'''
def test_postcode2(postcode):
    assert postcode == '010'


def test_postcode3(postcode):
    assert postcode == '010'


def test_login1(lg):
    assert lg == '9999999'

