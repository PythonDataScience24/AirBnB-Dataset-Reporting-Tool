"""
This module provides classes and functions for exploring and analyzing an airbnb dataset.
It provides the user 4 different functionalities.
1. Show first rows
2. Choose which rows to show
3. Show statistical summary for a column
4. Show cost information by neighborhood and room type
"""
import pandas as pd


class FirstRowsDisplay:
    """
    Class for displaying first 5 rows of a dataframe
    """

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_first_rows(self):
        """
        Method to display first 5 rows of a dataframe
        """
        print_separator()
        print("Here are the first 5 rows:")
        print_separator()
        print(self.data_frame.head())
        print_separator()


class ColumnStatistics:
    """
    Class for displaying column statistics of a specific column
    """

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_column_statistics(self):
        """
        Method to display column statistics of a specific column
        """
        print_separator()
        print("Columns in the dataset:")
        print(self.data_frame.columns)
        print_separator()
        column_name = input("\nStatistic summary of the following column: ")
        if column_name in self.data_frame.columns:
            print_separator()
            print(f"Summary statistics for '{column_name}':")
            print(self.data_frame[column_name].describe())
            print_separator()
        else:
            print("Column not found.")


class SpecificRowsDisplay:
    """
    Class to display specific rows of the dataframe.
    """

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_specific_rows(self):
        """
        Method to display specific rows of the data frame.
        The user can enter the first and last row (excluded) that he wants to see.
        """
        print_separator()
        print("Enter the row numbers you want to see:")
        try:
            start = int(input("Start row: "))
            if start < 0 or start >= len(self.data_frame):
                print("Invalid start row. Please enter a valid row number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

        try:
            end = int(input("End row: "))
            if end < 0 or end >= len(self.data_frame):
                print("Invalid end row. Please enter a valid row number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

        print_separator()
        print(self.data_frame[start:end])
        print_separator()


class NeighborhoodAnalyzer:
    """
    Class to get information, using the neighborhood and room type.
    """

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_neighborhood_info(self, neighborhood, room_type):
        """
        Method to display information, using the neighborhood and room
        :param neighborhood:
        :param room_type:
        :return:
        """
        filtered_data = self.data_frame[(self.data_frame['neighbourhood'] == neighborhood)
                                        & (self.data_frame['room type'] == room_type)]
        if filtered_data.empty:
            return None

        max_cost = filtered_data['price'].max()
        min_cost = filtered_data['price'].min()
        median_cost = filtered_data['price'].median()
        return {
            'neighborhood': neighborhood,
            'room type': room_type,
            'max_cost': max_cost,
            'min_cost': min_cost,
            'median_cost': median_cost
        }


# Load csv file
df = pd.read_csv('./Airbnb_Open_Data.csv')

# Remove the "$" and remove the thousand ","
df['price'].replace({r'\$': '', ',': ''}, regex=True, inplace=True)
df['service fee'].replace({r'\$': '', ',': ''}, regex=True, inplace=True)

# Make it numeric
df['price'] = pd.to_numeric(df['price'])
df['service fee'] = pd.to_numeric(df['service fee'])


def print_separator():
    """
    Method used to print a separator line
    :return:
    """
    print("-" * 40)


def get_neighborhoods():
    """
    Getter for the neighborhoods
    """
    return df['neighbourhood'].unique()


def get_room_types():
    """
    Getter for the room types
    """
    return df['room type'].unique()


# main function for explorers
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
        print("5. Exit")
        choice = input("Choose wise: ")

        if choice == '1':
            first_rows_display = FirstRowsDisplay(df)
            first_rows_display.display_first_rows()
        elif choice == '2':
            specific_rows_display = SpecificRowsDisplay(df)
            specific_rows_display.display_specific_rows()
        elif choice == '3':
            column_stats = ColumnStatistics(df)
            column_stats.display_column_statistics()
        elif choice == '4':
            print(df['neighbourhood'])
            neighborhood = input("Enter neighborhood: ")
            print(df['room type'])
            neighborhood_analyzer = NeighborhoodAnalyzer(df)  # using the class the class
            room_type = input("Enter room type: ")
            cost_info = neighborhood_analyzer.display_neighborhood_info(neighborhood, room_type)
            if cost_info:
                print_separator()
                print("Cost Information:")
                print("Neighborhood:", cost_info['neighborhood'])
                print("Room Type:", cost_info['room type'])
                print("Max Cost:", cost_info['max_cost'])
                print("Min Cost:", cost_info['min_cost'])
                print("Median Cost:", cost_info['median_cost'])
                print_separator()
            else:
                print("No data found for the given neighborhood and room type.")
        elif choice == '5':
            print("Thanks for your time, good bye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


# call dora the explorer
explore_dataset()
