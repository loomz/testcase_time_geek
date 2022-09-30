import pytest


@pytest.mark.xfail
def test_xfail():
    assert 1 == 2

def test_extend():
    li = ['a', 'b', 'c']
    li.extend(['d', 'e', 'f'])
    print("extend>>>>=%s" % li)


def test_append():
    li2 = ['a', 'b', 'c']
    li2.append(['d', 'e', 'f'])
    print("append>>>>=%s" % li2)


def test_insert():
    li3 = ['a', 'b', 'c']
    li3.insert(1, 'wangmin')
    print("insert>>>>>=%s" % li3)



'''
if __name__ == '__main__':
    pytest.main(['-sv', 'testcase_array.py'])
'''