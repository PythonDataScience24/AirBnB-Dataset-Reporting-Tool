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

def roomtype_selector():
    """
    Method to select the room type
    """
    print("Room types available:")
    print(df['room type'].unique())
    fu.print_separator()
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

def visualisation_by_room_type(room_type):
    """
    Method to visualize the cost information by room type
    """
    print("Cost information by room type:")
    sns.set_theme(style="whitegrid")
    sns.barplot(x='room type', y='price', data=df[df['room type'] == room_type])
    plt.show()
    fu.print_separator()

def visualisation_by_neighborhood(neighborhood):
    """
    Method to visualize the cost information by neighborhood
    """
    print("Cost information by neighborhood:")
    sns.set_theme(style="whitegrid")
    sns.barplot(x='neighbourhood', y='price', data=df[df['neighbourhood'] == neighborhood])
    plt.show()
    fu.print_separator()

def visualisation_by_rating():
    """
    Method to visualize the cost information by rating
    """
    print("Cost information by rating:")
    sns.set_theme(style="whitegrid")
    sns.barplot(x='rating', y='price', data=df)
    plt.show()
    fu.print_separator()
