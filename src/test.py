import main

import unittest
from unittest import mock


# Test for an invalid input in the user interface.
def user_interface_test():
    with mock.patch('builtins.input', side_effect=['4', '3']), \
            mock.patch('builtins.print') as mock_print:
        main.user_interface()
        mock_print.assert_any_call("Invalid choice. Please enter a valid option.")
        mock_print.assert_any_call("Thanks for your time, bye.")
class TestAirbnbInterface(unittest.TestCase):
    def test_user_interface(self):
        user_interface_test()



if __name__ == '__main__':
    unittest.main()
