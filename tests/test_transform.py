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
    def test_clean_data(self):
        # Test clean_data function
        df_cleaned = clean_data(self.test_data)
        
        # Test data type conversions
        self.assertTrue(df_cleaned['Rating'].dtype == float)
        self.assertTrue(df_cleaned['Colors'].dtype == int)
        self.assertTrue(df_cleaned['Price'].dtype == float)
        
        # Test data cleaning
        self.assertEqual(df_cleaned['Rating'].iloc[0], 4.5)
        self.assertEqual(df_cleaned['Colors'].iloc[0], 2)
        self.assertEqual(df_cleaned['Price'].iloc[0], 120.50)
        
        # Test string cleaning
        self.assertEqual(df_cleaned['Size'].iloc[0], 'SML')
        self.assertEqual(df_cleaned['Gender'].iloc[0], 'Male')
        
        # Test filtering
        self.assertTrue(len(df_cleaned) < len(self.test_data))
        self.assertTrue('Unknown Product' not in df_cleaned['Title'].values)