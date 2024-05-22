"""
This module provides an Interface to interact with the airbnb dataset.

The options to explore the data are as follows:
1. Show first rows
2. Choose which rows you want to see
3. Show statistical summary for a column
4. Show cost information by neighborhood and room type

The options to visualize the data are as follows:
1. Visualize cost information by room type
2. Visualize cost information by neighborhood
3. Visualize cost information by rating
"""
import Interface_data_manipulation as Idm
import Interface_data_visualisation as Idv
import file_utils as fu


def user_interface():
    """
    Method to interact with the airbnb dataset by providing a menu-driven
    interface to interact with various functionalities.
    """
    while True:
        print("\nWhat are your wishes?\n")
        print("1. Explore the dataset")
        print("2. Visualize the dataset")
        print("3. Exit")
        choice = input("\nChoose wise: ")
        fu.print_separator()
        if choice == '1':
            Idm.explore_dataset()
        elif choice == '2':
            Idv.visualize_dataset()
        elif choice == '3':
            print("Thanks for your time, bye.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the user interface
user_interface()
