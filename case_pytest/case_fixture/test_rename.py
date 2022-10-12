import pytest

# test_rename.py

@pytest.fixture(params=[
    ('redis', '6379'),
    ('elasticsearch', '9200'),
    ('wangmin', '1000')
])
def param(request):
    return request.param

@pytest.fixture(autouse=True)
def db(param):
    print('\nSucceed to connect %s:%s' % param)

    yield

    print('\nSucceed to close %s:%s' % param)


def test_api():
    assert 1 == 1