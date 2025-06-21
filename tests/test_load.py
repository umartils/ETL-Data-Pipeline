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

    def tearDown(self):
        # Clean up test CSV file if it exists
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_load_data_to_csv(self):
        # Test CSV file creation
        load_data_to_csv(self.test_data, self.test_filename)

        # Verify file exists
        self.assertTrue(os.path.exists(self.test_filename))

        # Verify content
        loaded_df = pd.read_csv(self.test_filename)
        pd.testing.assert_frame_equal(loaded_df, self.test_data)

    @patch('utils.load.create_engine')
    def test_load_data_to_postgresql(self, mock_create_engine):
        # Mock SQLAlchemy engine and connection
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        mock_connection = MagicMock()
        mock_engine.connect.return_value.__enter__.return_value = mock_connection

        # Test successful database load
        load_data_to_postgresql(
            self.test_data,
            'postgresql://test:test@localhost:5432/testdb',
            'test_table'
        )

        # Verify create_engine was called with correct URL
        mock_create_engine.assert_called_once_with(
            'postgresql://test:test@localhost:5432/testdb'
        )

        # Test database error handling
        mock_create_engine.side_effect = Exception("Database connection error")
        load_data_to_postgresql(
            self.test_data,
            'postgresql://invalid:invalid@localhost:5432/invaliddb',
            'test_table'
        )