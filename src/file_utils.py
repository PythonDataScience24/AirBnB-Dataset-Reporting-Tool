"""
This module,provides utility functions for handling and manipulating 
data for the AirBnB Dataset Reporting Tool.
"""
import pandas as pd

# Load data
df = pd.read_csv('data/Airbnb_Open_Data.csv')

def print_separator():
    """
    Method used to print a separator line
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
