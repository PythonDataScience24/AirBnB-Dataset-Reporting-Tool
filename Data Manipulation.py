import pandas as pd

#class to get the information using the neighborhood and room type
class NeighborhoodAnalyzer:
    def __init__(self, data_frame):
        self.df = data_frame

    def display_neighborhood_info(self, neighborhood, room_type):
        filtered_data = self.df[(self.df['neighbourhood'] == neighborhood) & (self.df['room type'] == room_type)]
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
#load csv
df = pd.read_csv('./Airbnb_Open_Data.csv')

#remove the "$" and remove the thousand ","
df['price'].replace({'\$': '', ',': ''}, regex=True, inplace=True)
df['service fee'].replace({'\$': '', ',': ''}, regex=True, inplace=True)

#make it numeric
df['price'] = pd.to_numeric(df['price'])
df['service fee'] = pd.to_numeric(df['service fee'])


def print_separator():
    print("-" * 40)
    
def display_first_rows(df):
    print_separator()
    print("Here are the first 5 rows:")
    print_separator()
    print(df.head())
    print_separator()

#Get valid start and end row numbers from the user and display the rows in between
def display_specific_rows(df):
    print_separator()
    print("Enter the row numbers you want to see:")
    try:
        start = int(input("Start row: "))
        if start < 0 or start >= len(df):
            print("Invalid start row. Please enter a valid row number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    try:
        end = int(input("End row: "))
        if end < 0 or end >= len(df):
            print("Invalid end row. Please enter a valid row number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    print_separator()
    print(df[start:end])
    print_separator()

def display_column_statistics(df):
    print_separator()
    print("Columns in the dataset:")
    print(df.columns)
    print_separator()
    column_name = input("\nStatistic summary of the following column: ")
    if column_name in df.columns:
        print_separator()
        print("Summary statistics for '{}':".format(column_name))
        print(df[column_name].describe())
        print_separator()
    else:
        print("Column not found.")

def get_neighborhoods(self):
    return self.df['neighbourhood'].unique()

def get_room_types(self):
    return self.df['room type'].unique()

def display_neighborhood_info(neighborhood, room_type):
    filtered_data = df[(df['neighbourhood'] == neighborhood) & (df['room type'] == room_type)]
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


#main function for explorers
def explore_dataset():
    while True:
        print("\nWhat are your wishes?\n")
        print("1. Show first rows")
        print("2. Choose which rows you want to see")
        print("3. Show statistical summary for a column")
        print("4. Show cost information by neighborhood and room type")
        print("5. Exit")
        choice = input("Choose wise: ")

        if choice == '1':
            display_first_rows(df)
        elif choice == '2':
            display_specific_rows(df)
        elif choice == '3':
            display_column_statistics(df)
        elif choice == '4':
            print(df['neighbourhood'])
            neighborhood = input("Enter neighborhood: ")
            print(df['room type'])
            neighborhood_analyzer = NeighborhoodAnalyzer(df) #using the class the class
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

#call dora the explorer
explore_dataset()



