# https://mp.weixin.qq.com/s?__biz=MzAwMzY3MTU3Nw==&mid=2650528928&idx=1&sn=152d6e4fb9913b5dee3f73050758ab8f&chksm=8338efd6b44f66c0b82975276dc5f39214966797051b55c3177147e95c259ce0c6fdb5e4bfc6&scene=178&cur_album_id=1744510599146831878#rd

# !/usr/bin/env python
# !coding:utf-8
import pytest
import requests
import json


def readJson():
    return json.load(open('login.json', 'r'))['item']


def readJson2():
    return json.load(open('login2.json', 'r'))


@pytest.mark.parametrize('data', readJson())
def test_json_login(data):
    r = requests.post(
        url=data['request']['url'],
        json=data['request']['body'])
    assert r.json() == data['response'][0]


if __name__ == '__main__':
    pytest.main(["-s", "-v", "test_json_login.py"])
