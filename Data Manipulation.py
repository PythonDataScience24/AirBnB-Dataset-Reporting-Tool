import pandas as pd

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

#main function for explorers
def explore_dataset():
    while True:
        print("\nWhat are your wishes?\n")
        print("1. Show first rows")
        print("2. Choose which rows you want to see")
        print("3. Show statistical summary for a column")
        print("4. Exit")
        choice = input("Choose wise: ")

        if choice == '1':
            display_first_rows(df)
        elif choice == '2':
            display_specific_rows(df)
        elif choice == '3':
            display_column_statistics(df)
        elif choice == '4':
            print("Thanks for your time, good bye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#call dora the explorer
explore_dataset()