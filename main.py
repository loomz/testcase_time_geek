import pytest
if __name__ == '__main__':
   # pytest.main(['-sv', 'testcase_mark.py'])
   # pytest.main(['-sv', '-m test_skip', 'testcase_mark.py'])
   pytest.main(['-sv', '-m my_skip', 'testcase_list.py'])