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
    
    def test_convert_currency(self):
        # Create test DataFrame
        df = pd.DataFrame({
            'Price': [100.0, 200.0, 300.0],
            'Title': ['Product 1', 'Product 2', 'Product 3']
        })
        
        # Test first conversion
        df_converted1 = convert_currency(df.copy(), 16000)
        self.assertEqual(df_converted1['Price'].iloc[0], 100.0 * 16000)
        
        # Test second conversion with fresh DataFrame
        df_converted2 = convert_currency(df.copy(), 15000)
        self.assertEqual(df_converted2['Price'].iloc[0], 100.0 * 15000)

    def test_edge_cases(self):
        # Test with empty data
        empty_data = []
        df_empty = clean_data(empty_data)
        self.assertTrue(df_empty.empty)
        
        # Test with missing values
        data_with_missing = [
            {
                'Title': 'Test Product',
                'Price': None,
                'Rating': None,
                'Colors': None,
                'Size': None,
                'Gender': None,
                'Time': '2024-05-08T10:00:00'
            }
        ]
        df_missing = clean_data(data_with_missing)
        self.assertTrue(df_missing.empty)
        
    def test_error_handling(self):
        # Test invalid data types
        invalid_data = [
            {
                'Title': None,
                'Price': None,
                'Rating': None,
                'Colors': None,
                'Size': None,
                'Gender': None,
                'Time': None
            }
        ]
        
        df_result = clean_data(invalid_data)
        self.assertIsInstance(df_result, pd.DataFrame)
        
        # Test invalid exchange rate
        result = convert_currency(pd.DataFrame(), -1)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)

        # Test invalid input type
        result = convert_currency("not a dataframe", 1000)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)