import pytest
from common_read_file import CommonReadFile


@pytest.mark.parametrize("name,email,pwd,pwd_,result", CommonReadFile().get_data_json('testE.json'))
def test_json(name, email, pwd, pwd_, result):
    if result == "True":
        assert pwd == pwd_
    else:
        assert pwd != pwd_


@pytest.mark.parametrize('name, age, gender, birth', CommonReadFile().get_data_csv('test.csv'))
def test_csv(name, age, gender, birth):
    print("name=%s, age=%s, gender=%s, birth=%s" % (name, age, gender, birth))


@pytest.mark.parametrize("username,age,pwd,pwd_,result", CommonReadFile().get_data_yaml('testdata.yaml'))
def test_yaml(username, age, pwd, pwd_, result):
    if result == "True":
        assert pwd == pwd_
    else:
        assert pwd != pwd_

if __name__ == '__main__':
    pytest.main(['-sv','test_case.py'])