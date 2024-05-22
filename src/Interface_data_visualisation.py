"""
Module to explore the dataset by providing various
options to visualize the data:

1. Visualize cost information by room type
2. Visualize cost information by neighborhood
3. Visualize cost information by rating
"""
import pandas as pd
import data_visualisation as dv
import load_and_fix_data as lf
import file_utils as fu

# Set the display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Load data
loader = lf.LoadAndFixData()
df = loader.load_and_fix_data()

def visualize_dataset():

    print("\nWhich neighbourhood do you want to visualize?\n")
    neighbourhood = dv.neighborhood_selector()
    print("\nWhat are your wishes?\n")

    while True:
        print("\nWhat are your wishes?\n")
        print("1. Visualize cost information by room type")
        print("2. Visualize cost information by neighborhood")
        print("3. Visualize cost information by rating")
        print("4. Explore a different neighbourhood")
        print("5. Back to main menu")
        choice = input("\nChoose wise: ")

        if choice == '1':
            fu.print_separator()
            print("Please enter the room type you want to visualize:")
            room_type = dv.roomtype_selector(neighbourhood)
            dv.visualisation_by_room_type(room_type, neighbourhood)
        elif choice == '2':
            fu.print_separator()
            dv.visualisation_by_neighborhood(neighbourhood)
        elif choice == '3':
            dv.visualisation_by_rating(neighbourhood)
        elif choice == '4':
            print("\nWhich neighbourhood do you want to visualize?\n")
            neighbourhood = dv.neighborhood_selector()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
