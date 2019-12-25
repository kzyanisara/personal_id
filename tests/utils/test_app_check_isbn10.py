from utils.check_isbn10 import is_valid


def test_is_valid():
    assert True == is_valid('1218651032')
    assert True == is_valid('0130674826')
    assert False == is_valid('0131482314')
    assert False == is_valid('0321721330')
