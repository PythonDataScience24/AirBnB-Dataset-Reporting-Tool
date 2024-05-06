import pandas as pd


class AirbnbDataExplorer:
    """
    Creating a class for the data exploring
    """
    def __init__(self, data_path):
        """
        Constructor to initialize the AirbnbDataExplorer class.
        :param data_path: Path to the CSV file containing Airbnb data.
        """
        self.df = pd.read_csv(data_path)
        self.clean_data()

    def clean_data(self):
        """
        Method used to clean the dataset
        """
        self.df['price'] = pd.to_numeric(self.df['price'].replace({'\$': '', ',': ''}, regex=True))
        self.df['service fee'] = pd.to_numeric(self.df['service fee'].replace({'\$': '', ',': ''}, regex=True))

    def print_separator(self):
        """
        Method used to print a seperator line.
        """
        print("-" * 40)

    def display_first_rows(self):
        """
        Method used to display the first 5 rows of the dataset
        """
        self.print_separator()
        print("Here are the first 5 rows:")
        self.print_separator()
        print(self.df.head())
        self.print_separator()

    def display_specific_rows(self):
        """
        Method used to display specific rows of the dataset
        """
        self.print_separator()
        print("Enter the row numbers you want to see:")
        try:
            start = int(input("Start row: "))
            if start < 0 or start >= len(self.df):
                print("Invalid start row. Please enter a valid row number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

        try:
            end = int(input("End row: "))
            if end < 0 or end >= len(self.df):
                print("Invalid end row. Please enter a valid row number.")
                return
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

        self.print_separator()
        print(self.df[start:end])
        self.print_separator()

    def display_column_statistics(self):
        """
        Method to display statistical summary for a specified column of the dataset.
        """
        self.print_separator()
        print("Columns in the dataset:")
        print(self.df.columns)
        self.print_separator()
        column_name = input("\nStatistic summary of the following column: ")
        if column_name in self.df.columns:
            self.print_separator()
            print("Summary statistics for '{}':".format(column_name))
            print(self.df[column_name].describe())
            self.print_separator()
        else:
            print("Column not found.")

    def get_neighborhoods(self):
        """
        Method to get unique neighborhoods from the dataset.
        """
        return self.df['neighbourhood'].unique()

    def get_room_types(self):
        """
        Method to get unique room types from the dataset.
        :return:
        """
        return self.df['room type'].unique()

    def display_neighborhood_info(self):
        """
        Method to display cost information by neighborhood and room type.
        :return:
        """
        neighborhood = input("Enter neighborhood: ")
        room_type = input("Enter room type: ")
        filtered_data = self.df[(self.df['neighbourhood'] == neighborhood) & (self.df['room type'] == room_type)]
        if filtered_data.empty:
            print("No data found for the given neighborhood and room type.")
            return

        max_cost = filtered_data['price'].max()
        min_cost = filtered_data['price'].min()
        median_cost = filtered_data['price'].median()

        self.print_separator()
        print("Cost Information:")
        print("Neighborhood:", neighborhood)
        print("Room Type:", room_type)
        print("Max Cost:", max_cost)
        print("Min Cost:", min_cost)
        print("Median Cost:", median_cost)
        self.print_separator()

    def explore_dataset(self):
        """
        Method to explore the dataset by providing a menu-driven interface to interact with various functionalities.
        """
        while True:
            print("\nWhat are your wishes?\n")
            print("1. Show first rows")
            print("2. Choose which rows you want to see")
            print("3. Show statistical summary for a column")
            print("4. Show cost information by neighborhood and room type")
            print("5. Exit")
            choice = input("Choose wisely: ")

            if choice == '1':
                self.display_first_rows()
            elif choice == '2':
                self.display_specific_rows()
            elif choice == '3':
                self.display_column_statistics()
            elif choice == '4':
                self.display_neighborhood_info()
            elif choice == '5':
                print("Thanks for your time, good bye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

# Usage:
explorer = AirbnbDataExplorer('./Airbnb_Open_Data.csv')
explorer.explore_dataset()
