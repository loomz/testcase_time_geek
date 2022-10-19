# 官方文档https://learning-pytest.readthedocs.io/zh/latest/doc/fixture/intro.html

import pytest

'''
@pytest.fixture(scope='session', autouse=True)
def fixture_session():
    print('\n测试所有用例开始session####################')
    yield
    print('\n测试所有用例结束session####################')


@pytest.fixture(scope='function', autouse=True)
def fixture_function():
    print('\n function每个测试用例开始####################')
    yield
    print('\n function每个测试用例结束####################')


@pytest.fixture(scope='module', autouse=True)
def fixture_module():
    print('\n 每个模块测试用例开始module===================>')
    yield
    print('\n 每个模块测试用例结束module===================>')


@pytest.fixture(scope='class', autouse=True)
def fixture_class():
    print('\n 每个模块测试用例开始class===================>')
    yield
    print('\n 每个模块测试用例结束class===================>')


'''

@pytest.fixture(scope='session', name='lg')
def login_and_loginout():
    print("\n登录xxxxxx，获取token...")
    token = '9999999'
    yield token
    print('\n退出登录####################')



