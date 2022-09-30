import pytest
import sys


@pytest.fixture(scope="module", autouse=True)
def conn_db():
    print("连接数据库")
    yield
    print("关闭数据库")


@pytest.fixture(scope="function", autouse=True)
def yield_function():
    print("yield_function start...")
    # print("fun = %s" % sys._getframe().f_code.co_name)
    yield
    print("yield_function end...")


def test_create_user():
    print("test_create_user")


def test_function():
    print(" test_function..")
