"""
This module provides classes and functions for exploring and analyzing an airbnb dataset.
It provides the user 4 different functionalities.
1. Show first rows
2. Choose which rows to show
3. Show statistical summary for a column
4. Show cost information by neighborhood and room type
"""
import file_utils as fu
import load_and_fix_data as lf

# Load data
loader = lf.LoadAndFixData()
df = loader.load_and_fix_data()

class FirstRowsDisplay: # pylint: disable=too-few-public-methods
    """
    Class for displaying first 5 rows of a dataframe
    """
    def __init__(self, data_frame):
        """
        Initializes an instance of the DataManipulation class.
        """
        self.data_frame = data_frame

    def display_first_rows(self):
        """
        Method to display first 5 rows of a dataframe
        """
        fu.print_separator()
        print("Here are the first 5 rows:")
        fu.print_separator()
        print(self.data_frame.head())
        fu.print_separator()


class ColumnStatistics: # pylint: disable=too-few-public-methods
    """
    Class for displaying column statistics of a specific column
    """

    def __init__(self, data_frame):
        """
        Initializes an instance of the DataManipulation class.
        """
        self.data_frame = data_frame

    def display_column_statistics(self):
        """
        Method to display column statistics of a specific column
        """
        fu.print_separator()
        print("Columns in the dataset:")
        print(df.columns.unique())

        fu.print_separator()
        column_name = input("\nStatistic summary of the following column: ")
        if column_name in self.data_frame.columns:
            fu.print_separator()
            print(f"Summary statistics for '{column_name}':")
            print(self.data_frame[column_name].describe())
            fu.print_separator()
        else:
            print("Column not found.")
            fu.print_separator()


class SpecificRowsDisplay: # pylint: disable=too-few-public-methods
    """
    Class to display specific rows of the dataframe.
    """

    def __init__(self, data_frame):
        """
        Initializes an instance of the DataManipulation class.
        """
        self.data_frame = data_frame

    def display_specific_rows(self):
        """
        Method to display specific rows of the data frame.
        The user can enter the first and last row (excluded) that he wants to see.
        """
        fu.print_separator()
        print("Enter the row numbers you want to see: (number must be between 0 and {})".format(len(self.data_frame)))
        #print("Enter the row numbers you want to see:")
        try:
            start = int(input("Start row: "))
            if start < 0 or start >= len(self.data_frame):
                print("Invalid start row. Please enter a valid row number.")
                fu.print_separator()
                return
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            fu.print_separator()
            return

        try:
            end = int(input("End row: "))
            if end < 0 or end >= len(self.data_frame):
                print("Invalid end row. Please enter a valid row number.")
                fu.print_separator()
                return
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            fu.print_separator()
            return


        fu.print_separator()
        print(self.data_frame[start:end+1])
        fu.print_separator()


class NeighborhoodAnalyzer: # pylint: disable=too-few-public-methods
    """
    Class to get information, using the neighborhood and room type.
    """

    def __init__(self, data_frame):
        """
        Initializes an instance of the DataManipulation class.
        """
        self.data_frame = data_frame

    def display_neighborhood_info(self):
        """
        Method to display information about the neighborhood and room
        """
        fu.print_separator()
        print("Neighborhoods to select from: ")
        print(df['neighbourhood'].unique())

        fu.print_separator()
        neighborhood = input("Choose a neighborhood: ")

        fu.print_separator()
        print(df['room type'].unique())

        fu.print_separator()
        room_type = input("Choose a room type: ")

        filtered_data = self.data_frame[(self.data_frame['neighbourhood'] == neighborhood)
                                        & (self.data_frame['room type'] == room_type)]
        if filtered_data.empty:
            print("No data found for the given neighborhood and room type.")
            fu.print_separator()
        else:
            max_cost = filtered_data['price'].max()
            min_cost = filtered_data['price'].min()
            median_cost = filtered_data['price'].median()

            fu.print_separator()
            print("Cost Information:")
            print("Neighborhood:", neighborhood)
            print("Room Type:", room_type)
            print("Max Cost:", max_cost)
            print("Min Cost:", min_cost)
            print("Median Cost:", median_cost)
            fu.print_separator()