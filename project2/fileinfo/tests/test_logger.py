from unittest.mock import patch

from fileinfo.logger import Logger

# To patch the immutable method now in datetime doesn't work

# @patch('datetime.datetime.now')
# def test_log(mock_now):
#    test_now = 123
#    test_message = 'A test message'
#    mock_now.return_value = test_now

 #   test_logger = Logger()
 #   test_logger.log(test_message)
 #   assert test_logger.messages == [(test_now, test_message)]

# Solution to solve this problem:
# 1 - To patch the module datetime instead of datetime.now()
# 2 - To do this importing from the logger.py file instead of the 
#     global scope
@patch('fileinfo.logger.datetime.datetime')
def test_log(mock_datetime):
    test_now = 123
    test_message = 'A test message'
    mock_datetime.now.return_value = test_now

    test_logger = Logger()
    test_logger.log(test_message)
    assert test_logger.messages == [(test_now, test_message)]
