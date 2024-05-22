"""
This module contains the LoadAndFixData class that loads the Airbnb dataset from a csv file and fixes the data.
"""
import pandas as pd

class LoadAndFixData:
    """
    a class to fix raw data in the csv file
    """
    def __init__(self):
        self.file_path = './data/Airbnb_Open_Data.csv'

    def load_and_fix_data(self):
        """
        Load Airbnb dataset from file and fix the data
        """
        df = pd.read_csv(self.file_path)

        # Remove "$" and remove the thousand ","
        df['price'].replace({r'\$': '', ',': ''}, regex=True, inplace=True)
        df['service fee'].replace({r'\$': '', ',': ''}, regex=True, inplace=True)

        # Make it numeric
        df['price'] = pd.to_numeric(df['price'])
        df['service fee'] = pd.to_numeric(df['service fee'])

        return df

