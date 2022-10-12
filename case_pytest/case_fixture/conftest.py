import pytest

# conftest.py


def pytest_addoption(parser):
    parser.addoption('--host', action='store',
                     help='host of db')
    parser.addoption('--port', action='store', default='8888',
                     help='port of db')


@pytest.fixture
def config(request):
    return request.config


# test_config.py

def test_option2(config):
    print('host: %s' % config.getoption('host'))
    print('port: %s' % config.getoption('port'))