#!/usr/bin/env python
# !coding:utf-8
import pytest
import requests
import csv
import json


def readCsv():
    data = list()
    with open('login.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            print("\nitem=%s" % item)
            data.append(item)
    return data


@pytest.mark.parametrize('data', readCsv())
def test_csv_login(data):
    print("\ndata=%s" % data)
    print("\ndata0=%s" % data[0])
    print("\ndata1=%s" % data[1])
    print("\ndata2=%s" % data[2])
    r = requests.post(
        url=data[0],
        json=json.loads(data[1]))
    assert r.json() == json.loads(data[2])


if __name__ == '__main__':
    pytest.main("-sv", "test.csv_login.py")