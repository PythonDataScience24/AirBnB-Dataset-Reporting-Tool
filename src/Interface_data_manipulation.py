"""
Module to explore the dataset by providing various
functions:
1. Show first rows
2. Choose which rows you want to see
3. Show statistical summary for a column
4. Show cost information by neighborhood and room type
"""
import pandas as pd
import data_manipulation as dm

# Load data
df = pd.read_csv('data/Airbnb_Open_Data.csv')

# Remove the "$" and remove the thousand ","3
df['price'].replace({r'\$': '', ',': ''}, regex=True, inplace=True)
df['service fee'].replace({r'\$': '', ',': ''}, regex=True, inplace=True)

# Make it numeric
df['price'] = pd.to_numeric(df['price'])
df['service fee'] = pd.to_numeric(df['service fee'])

def explore_dataset():
    """
    Method to explore the dataset by providing a menu-driven
    interface to interact with various functionalities.
    """
    while True:
        print("\nWhat are your wishes?\n")
        print("1. Show first rows")
        print("2. Choose which rows you want to see")
        print("3. Show statistical summary for a column")
        print("4. Show cost information by neighborhood and room type")
        print("5. Back to main menu")
        choice = input("Choose wise: ")

        if choice == '1':
            first_rows_display = dm.FirstRowsDisplay(df)
            first_rows_display.display_first_rows()
        elif choice == '2':
            specific_rows_display = dm.SpecificRowsDisplay(df)
            specific_rows_display.display_specific_rows()
        elif choice == '3':
            column_stats = dm.ColumnStatistics(df)
            column_stats.display_column_statistics()
        elif choice == '4':
            print(df['neighbourhood'])
            neighborhood = input("Enter neighborhood: ")
            print(df['room type'])
            neighborhood_analyzer = dm.NeighborhoodAnalyzer(df)  # using the class the class
            room_type = input("Enter room type: ")
            cost_info = neighborhood_analyzer.display_neighborhood_info(neighborhood, room_type)
            if cost_info:
                print("-" * 40)
                print("Cost Information:")
                print("Neighborhood:", cost_info['neighborhood'])
                print("Room Type:", cost_info['room type'])
                print("Max Cost:", cost_info['max_cost'])
                print("Min Cost:", cost_info['min_cost'])
                print("Median Cost:", cost_info['median_cost'])
                print("-" * 40)
            else:
                print("No data found for the given neighborhood and room type.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
