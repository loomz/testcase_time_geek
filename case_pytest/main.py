import pytest

if __name__ == '__main__':
   pytest.main(['-sv', '-m not  my_skip', 'test_mark.py']) 