"""
This module,provides utility functions for handling and manipulating 
data for the AirBnB Dataset Reporting Tool.
"""
import pandas as pd
import load_and_fix_data as lf

# Load data
df = lf.LoadAndFixData()

def print_separator():
    """
    Method used to print a separator line
    """
    print("-" * 100)

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
