import pytest


# @pytest.mark.run('last')
@pytest.mark.run(order=-1)
def test_logout():
    print("退出登录")


@pytest.mark.run(after='test_login')
def test_after_login():
    print("after_login")


def test_login():
    print("用户登录")


@pytest.mark.run(order=1)
def test_register():
    print("注册用户")

