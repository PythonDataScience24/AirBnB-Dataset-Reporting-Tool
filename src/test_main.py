"""
Testing unit for the main.py function
it provides 6 tests for 6 different inputs (3 right inputs and 3 wrong inputs)
in the mock the input is given through the side_effect (first is the input, second is to exit the interface)
it is checked whether the right functions are called by the given input or not
"""

import unittest
from unittest import mock
from src.main import user_interface


class TestUserInterface(unittest.TestCase):

    def test_explore_dataset(self):
        """
        test to check if the input "1" leads to the dataset exploring
        """
        with mock.patch('builtins.input', side_effect=['1', '3']), \
                mock.patch('Interface_data_manipulation.explore_dataset') as mock_explore, \
                mock.patch('Interface_data_visualisation.visualize_dataset') as mock_visualize:
            user_interface()
            mock_explore.assert_called_once()
            mock_visualize.assert_not_called()

    def test_visualize_dataset(self):
        """
        test to check if the input "2" leads to the dataset visualisation
        """
        with mock.patch('builtins.input', side_effect=['2', '3']), \
                mock.patch('Interface_data_manipulation.explore_dataset') as mock_explore, \
                mock.patch('Interface_data_visualisation.visualize_dataset') as mock_visualize:
            user_interface()
            mock_visualize.assert_called_once()
            mock_explore.assert_not_called()

    def test_exit(self):
        """
        test to check if the input "3" leads to exiting the program
        """
        with mock.patch('builtins.input', side_effect=['3']), \
                mock.patch('builtins.print') as mock_print, \
                mock.patch('Interface_data_manipulation.explore_dataset') as mock_explore, \
                mock.patch('Interface_data_visualisation.visualize_dataset') as mock_visualize:
            user_interface()
            mock_print.assert_called_with("Thanks for your time, bye.")
            mock_visualize.assert_not_called()
            mock_explore.assert_not_called()

    def test_invalid_choice(self):
        """
        test to check if the too high input "4" leads to an error
        """
        with mock.patch('builtins.input', side_effect=['4', '3']), \
                mock.patch('builtins.print') as mock_print, \
                mock.patch('Interface_data_manipulation.explore_dataset') as mock_explore, \
                mock.patch('Interface_data_visualisation.visualize_dataset') as mock_visualize:
            user_interface()
            mock_print.assert_any_call("Invalid choice. Please enter a valid option.")
            mock_visualize.assert_not_called()
            mock_explore.assert_not_called()

    def test_float_input(self):
        """
        test to check if the float input "3.1415" leads to an error
        """
        with mock.patch('builtins.input', side_effect=['3.1415', '3']), \
                mock.patch('builtins.print') as mock_print, \
                mock.patch('Interface_data_manipulation.explore_dataset') as mock_explore, \
                mock.patch('Interface_data_visualisation.visualize_dataset') as mock_visualize:
            user_interface()
            mock_print.assert_any_call("Invalid choice. Please enter a valid option.")
            mock_visualize.assert_not_called()
            mock_explore.assert_not_called()

    def test_string_input(self):
        """
        test to check if the string input "i am funny" leads to an error
        """
        with mock.patch('builtins.input', side_effect=['i am funny', '3']), \
                mock.patch('builtins.print') as mock_print, \
                mock.patch('Interface_data_manipulation.explore_dataset') as mock_explore, \
                mock.patch('Interface_data_visualisation.visualize_dataset') as mock_visualize:
            user_interface()
            mock_print.assert_any_call("Invalid choice. Please enter a valid option.")
            mock_visualize.assert_not_called()
            mock_explore.assert_not_called()