import pandas as pd

#load csv
df = pd.read_csv('./Airbnb_Open_Data.csv')

#remove the "$" and remove the thousand ","
df['price'] = df['price'].str.replace('$', '').str.replace(',', '')
df['service fee'] = df['service fee'].str.replace('$', '').str.replace(',', '')

#make it numeric
df['price'] = pd.to_numeric(df['price'])
df['service fee'] = pd.to_numeric(df['service fee'])

#display the first rows
def display_first_rows():
    print("\n**************************************************************************************")
    print("Here are the first 5 rows:")
    print("\n**************************************************************************************")
    print(df.head())
    print("\n**************************************************************************************")

#statistics of columns
def display_column_statistics():
    print("\n**************************************************************************************")
    print("Columns in the dataset:")
    print(df.columns)
    print("\n**************************************************************************************")
    column_name = input("\nStatistic summary of the following column: ")
    if column_name in df.columns:
        print("\n**************************************************************************************")
        print("Summary statistics for '{}':".format(column_name))
        print(df[column_name].describe())
        print("\n**************************************************************************************")
    else:
        print("Invalid column name. Please enter a valid column name.")

#main function for explorers
def explore_dataset():
    while True:
        print("\nWhat are your wishes?\n")
        print("1. Show first rows")
        print("2. Show statistical summary for a column")
        print("3. Exit")
        choice = input("Choose wise: ")

        if choice == '1':
            display_first_rows()
        elif choice == '2':
            display_column_statistics()
        elif choice == '3':
            print("Thanks for your time, good bye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

#call dora the explorer
explore_dataset()