import unittest
import pandas as pd
from utils.transform import clean_data, convert_currency

class TestTransformFunctions(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.test_data = [
            {
                'Title': 'Test Product 1',
                'Price': '$120.50',
                'Rating': '4.5 stars',
                'Colors': '2 colors',
                'Size': 'Size: S,M,L',
                'Gender': 'Gender: Male',
                'Time': '2024-05-08T10:00:00'
            },
            {
                'Title': 'Test Product 2',
                'Price': '$0',
                'Rating': 'No rating',
                'Colors': 'No colors',
                'Size': 'Size: XL',
                'Gender': 'Gender: Female',
                'Time': '2024-05-08T10:00:00'
            },
            {
                'Title': 'Unknown Product',
                'Price': '$50.00',
                'Rating': '3.0 stars',
                'Colors': '1 color',
                'Size': 'Size: M',
                'Gender': 'Gender: Unisex',
                'Time': '2024-05-08T10:00:00'
            }
        ]