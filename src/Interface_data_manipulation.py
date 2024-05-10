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
import load_and_fix_data as lf

# Load data
loader = lf.LoadAndFixData()
df = loader.load_and_fix_data()

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
        choice = input("\nChoose wise: ")

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
            neighbor_info = dm.NeighborhoodAnalyzer(df)
            neighbor_info.display_neighborhood_info()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
