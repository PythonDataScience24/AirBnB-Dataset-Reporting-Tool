"""
Module to explore the dataset by providing various
options to visualize the data:

1. Visualize cost information by room type
2. Visualize cost information by neighborhood
3. Visualize cost information by rating
"""
import pandas as pd
import data_visualisation as dv

# Load data
df = pd.read_csv('data/Airbnb_Open_Data.csv')

def visualize_dataset():

    print("\nWhat are your wishes?\n")

    while True:
        print("\nWhat are your wishes?\n")
        print("1. Visualize cost information by room type")
        print("2. Visualize cost information by neighborhood")
        print("3. Visualize cost information by rating")
        print("4. Back to main menu")
        choice = input("Choose wise: ")

        if choice == '1':
            print("Please enter the room type you want to visualize:")
            room_type = dv.roomtype_selector()
            dv.visualisation_by_room_type(room_type)
        elif choice == '2':
            print("Please enter the neighborhood you want to visualize:")
            neighborhood = dv.neighborhood_selector()
            dv.visualisation_by_neighborhood(neighborhood) 
        elif choice == '3':
            dv.visualisation_by_rating()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
