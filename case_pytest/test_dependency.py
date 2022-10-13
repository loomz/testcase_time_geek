import pytest


@pytest.mark.dependency(name="aa")
def test_01():
    print("test_01==================")
    assert 1 == 1


@pytest.mark.dependency(depends=["aa"])
def test_02():
    print("test_02##################")


