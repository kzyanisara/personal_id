from utils.check_pid import is_valid, is_bkk


def test_is_valid():
    assert True == is_valid('1234567890121')
    assert True == is_valid('1101401427542')
    assert True == is_valid('3800900689681')
    assert False == is_valid('1101401427552')


def test_is_bkk():
    assert False == is_bkk('3800900689681')
    assert True == is_bkk('1101401427542')
