#!/usr/bin/env python
# !coding:utf-8
import pytest
import requests
import yaml
import json


def readYaml():
    with open('login.yaml', 'r') as f:
        return list(yaml.safe_load_all(f))


@pytest.mark.parametrize('data', readYaml())
def test_login(data):
    r = requests.post(
        url=data['url'],
        json=json.loads(data['body']))
    assert r.json() == json.loads(data['expect'])

