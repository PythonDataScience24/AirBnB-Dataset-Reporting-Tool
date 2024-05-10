"""
This module provides classes and functions to make visualisations of an airbnb dataset.
It provides the user the following functionalities:

1. Visualize cost information by room type
2. Visualize cost information by neighborhood
3. Visualize cost information by rating

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import file_utils as fu
import load_and_fix_data as lf

# Load data
df = lf.LoadAndFixData()

def roomtype_selector():
    """
    Method to select the room type
    """
    fu.print_separator()
    print("Room types available:")
    fu.print_separator()
    print(df['room type'].unique())
    room_type = input("Enter room type: ")
    return room_type

def neighborhood_selector():
    """
    Method to select the neighborhood
    """
    fu.print_separator()
    print("Neighborhoods available:")
    fu.print_separator()
    print(df['neighbourhood'].unique())
    neighborhood = input("Enter neighborhood: ")
    return neighborhood

def visualisation_by_room_type(room_type):
    """
    Method to visualize the cost information by room type
    """
    fu.print_separator()
    print("Cost information by room type:")
    fu.print_separator()
    sns.set_theme(style="whitegrid")
    sns.barplot(x='room type', y='price', data=df[df['room type'] == room_type])
    plt.show()

def visualisation_by_neighborhood(neighborhood):
    """
    Method to visualize the cost information by neighborhood
    """
    fu.print_separator()
    print("Cost information by neighborhood:")
    fu.print_separator()
    sns.set_theme(style="whitegrid")
    sns.barplot(x='neighbourhood', y='price', data=df[df['neighbourhood'] == neighborhood])
    plt.show()

def visualisation_by_rating():
    """
    Method to visualize the cost information by rating
    """
    fu.print_separator()
    print("Cost information by rating:")
    fu.print_separator()
    sns.set_theme(style="whitegrid")
    sns.barplot(x='rating', y='price', data=df)
    plt.show()
