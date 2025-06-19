import unittest
import pandas as pd
from unittest.mock import patch, MagicMock
import os
from utils.load import load_data_to_csv, load_data_to_postgresql, load_data_to_google_sheet

class TestLoadFunctions(unittest.TestCase):
    def setUp(self):
        # Sample DataFrame for testing
        self.test_data = pd.DataFrame({
            'Title': ['Product 1', 'Product 2'],
            'Price': [1600000.0, 2400000.0],
            'Rating': [4.5, 4.0],
            'Colors': [2, 3],
            'Size': ['SML', 'ML'],
            'Gender': ['Male', 'Female']
        })
        self.test_filename = 'test_fashion_data.csv'