import json
import pytest


def get_data_json(file_json):
    with open(file_json, encoding="utf-8") as f:
        lit = []
        keys = json.load(f)
        for key in keys:
            lit.append(tuple(key.values()))
        return lit


@pytest.mark.parametrize("name,email,pwd,pwd_", get_data_json('testE.json'))
def test_case( name, email, pwd, pwd_):
    assert pwd == pwd_


if __name__ == '__main__':
    pytest.main(['-sv', 'testEnorll_json.py'])
