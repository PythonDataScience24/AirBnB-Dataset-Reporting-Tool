"""
This module provides classes and functions to make visualisations of an airbnb dataset.
It provides the user the following functionalities:

1. Visualize cost information by room type
2. Visualize cost information by neighborhood
3. Visualize cost information by rating

"""
import matplotlib.pyplot as plt
import seaborn as sns
import file_utils as fu
import load_and_fix_data as lf

# Load data
loader = lf.LoadAndFixData()
df = loader.load_and_fix_data()

def roomtype_selector(neighborhood):
    """
    Method to select the room type
    """
    print("Room types available:")
    room_types = df[df['neighbourhood'] == neighborhood]['room type'].unique()
    print(room_types)
    fu.print_separator()
    room_type = input("Enter room type: ")
    while room_type not in room_types:
        print("Invalid room type. Please enter a room type from the list.")
        room_type = input("Enter room type: ")
    return room_type

def neighborhood_selector():
    """
    Method to select the neighborhood
    """
    print("Neighborhoods available:")
    print(df['neighbourhood'].unique())
    fu.print_separator()
    neighborhood = input("Enter neighborhood: ")
    return neighborhood

def visualisation_by_room_type(room_type, neighbourhood):
    """
    Method to visualize the cost information by room type for a chosen neighbourhood
    """
    print("Cost information by room type:")
    sns.set_theme(style="whitegrid")
    sns.barplot(x='room type', y='price', data=df[(df['room type'] == room_type) & (df['neighbourhood'] == neighbourhood)])
    plt.title(f'Cost Information for {neighbourhood}')
    plt.show()
    fu.print_separator()

def visualisation_by_neighborhood(neighbourhood):
    """
    Method to visualize the cost information by neighbourhood
    """
    print("Cost information by neighbourhood:")
    sns.set_theme(style="whitegrid")
    sns.barplot(x='neighbourhood', y='price', data=df[df['neighbourhood'] == neighbourhood])
    plt.title(f'Cost Information for {neighbourhood}')
    plt.show()
    fu.print_separator()

def visualisation_by_rating(neighbourhood):
    """
    Method to visualize the cost information by rating for a chosen room type and neighbourhood
    """
    print("Cost information by rating:")
    sns.set_theme(style="whitegrid")
    sns.barplot(x='review rate number', y='price', data=df[(df['neighbourhood'] == neighbourhood)])
    plt.title(f'Rating Information for {neighbourhood}')
    plt.show()
    fu.print_separator()
