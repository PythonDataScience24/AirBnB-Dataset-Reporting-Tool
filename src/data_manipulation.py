"""
This module provides classes and functions for exploring and analyzing an airbnb dataset.
It provides the user 4 different functionalities.
1. Show first rows
2. Choose which rows to show
3. Show statistical summary for a column
4. Show cost information by neighborhood and room type
"""


class FirstRowsDisplay:
    """
    Class for displaying first 5 rows of a dataframe
    """
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_first_rows(self):
        import file_utils as fu
        """
        Method to display first 5 rows of a dataframe
        """
        fu.print_separator()
        print("Here are the first 5 rows:")
        fu.print_separator()
        print(self.data_frame.head())
        fu.print_separator()


class ColumnStatistics:
    """
    Class for displaying column statistics of a specific column
    """

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_column_statistics(self):
        import file_utils as fu
        """
        Method to display column statistics of a specific column
        """
        fu.print_separator()
        print("Columns in the dataset:")
        print(self.data_frame.columns)
        fu.print_separator()
        column_name = input("\nStatistic summary of the following column: ")
        if column_name in self.data_frame.columns:
            fu.print_separator()
            print(f"Summary statistics for '{column_name}':")
            print(self.data_frame[column_name].describe())
            fu.print_separator()
        else:
            print("Column not found.")


class SpecificRowsDisplay:
    """
    Class to display specific rows of the dataframe.
    """

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_specific_rows(self):
        import file_utils as fu
        """
        Method to display specific rows of the data frame.
        The user can enter the first and last row (excluded) that he wants to see.
        """
        fu.print_separator()
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

        fu.print_separator()
        print(self.data_frame[start:end])
        fu.print_separator()


class NeighborhoodAnalyzer:
    """
    Class to get information, using the neighborhood and room type.
    """

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def display_neighborhood_info(self, neighborhood, room_type):
        import file_utils as fu
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
