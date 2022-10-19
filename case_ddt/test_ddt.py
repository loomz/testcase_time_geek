import pytest
from common.common_read_file import CommonReadFile


@pytest.mark.parametrize("name,email,pwd,pwd_,result", CommonReadFile().get_data_json('case_ddt/test_json.json'))
def test_json(name, email, pwd, pwd_, result):
    print("name=%s, email=%s, pwd=%s, pwd_=%s, result=%s" % (name, email, pwd, pwd_, result))
    if result == "True":
        assert pwd == pwd_
    else:
        assert pwd != pwd_


@pytest.mark.parametrize("name", CommonReadFile().get_data_json('case_ddt/test_json2.json'))
def test_json2(name):
    print("name=%s" % name)


@pytest.mark.parametrize('name, age, gender, birth', CommonReadFile().get_data_csv('case_ddt/test_csv.csv'))
def test_csv(name, age, gender, birth):
    print("name=%s, age=%s, gender=%s, birth=%s" % (name, age, gender, birth))


@pytest.mark.parametrize("username,age,pwd,pwd_,result", CommonReadFile().get_data_yaml('case_ddt/test_yaml.yaml'))
def test_yaml(username, age, pwd, pwd_, result):
    print("username=%s, age=%s, pwd=%s, pwd_=%s, result=%s" % (username, age, pwd, pwd_, result))
    if result == "True":
        assert pwd == pwd_
    else:
        assert pwd != pwd_

@pytest.mark.parametrize("username", CommonReadFile().get_data_yaml('case_ddt/test_yaml2.yaml'))
def test_yaml2(username):
    print("username=%s" % username)