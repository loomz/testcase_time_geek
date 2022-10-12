import  pytest

@pytest.fixture()
def db():
    print('\n 数据库连接成功')

    yield

    print('\n 数据库关闭')


def search_user(user_id):
    d = {
        '001': 'xiaoming'
    }
    return d[user_id]


def test_search(db):
    assert search_user('001') == 'xiaoming'
