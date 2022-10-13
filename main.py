import pytest


if __name__ == '__main__':
    # 跑所有测试用例
    #pytest.main(['-sv'])

    # 执行某目录的测试用例
    # pytest.main(['-sv', "case_pytest/case_fixture"])
    pytest.main(['-sv', "case_pytest/case_fixture2/"])

    # 执行某一个文件
    # pytest.main(['-sv', "case_wx/wx_test.py"])
    #pytest.main(['-sv', "--setup-show", "case_pytest/case_fixture/test_postcode.py"])


    # 执行某一个测试用例的方法
    # pytest.main(['-sv', "case_ddt/test_ddt.py::test_yaml"])

    # 执行某种标志测试用例
    # pytest.main(['-sv',  "-m my_skip1"])

    # 执行不是这个标志的所有测试用例
    # pytest.main(['-sv',  "-m not my_skip1"])
