'''
json.load：表示读取文件，返回python对象
json.dump：表示写入文件，文件为json字符串格式，无返回
json.dumps：将python中的字典类型转换为字符串类型，返回json字符串 [dict→str]
json.loads：将json字符串转换为字典类型，返回python对象 [str→dict]
load和dump处理的主要是 文件
loads和dumps处理的是 字符串
https://blog.csdn.net/qq_45859826/article/details/124158012
'''

import json


# json.dumps：将python中的字典类型转换为字符串类型，返回json字符串 [dict→str]
def test_dumps():
    data = {
        'fruit': 'apple',
        'vegetable': 'cabbage'
    }
    print(data, type(data))

    data = json.dumps(data)  # dict转json
    print(data, type(data))


# json.loads：将json字符串转换为字典类型，返回python对象 [str→dict]
def test_loads():
    data = """{
    "fruit": "apple",
    "vegetable": "cabbage"
    }"""
    # 一般此时data为request.text返回值
    print(data, type(data))
    data = json.loads(data)
    print(data, type(data))



# json.dump：表示写入文件，文件为json字符串格式，无返回
def test_dump():
    data = "wyt"
    with open('../case_pytest/b.json', 'w') as f:
        json.dump(data, f)

    with open('../case_pytest/b.json', 'r', encoding='utf-8') as f:
        f_str = json.load(f)
        print(f_str, type(f_str))


def test_dump_dict():
    data = {
        'fruit': 'apple',
        'vegetable': 'cabbage'
    }
    with open('../case_pytest/b.json', 'w') as f:
        json.dump(data, f)

    with open('../case_pytest/b.json', 'r', encoding='utf-8') as f:
        f_str = json.load(f)
        print(f_str, type(f_str))

# json.load：表示读取文件，返回python对象
def test_load():
    with open('../case_pytest/a.json', 'r', encoding='utf-8') as f:
        f_str = json.load(f)
        print(f_str, type(f_str))