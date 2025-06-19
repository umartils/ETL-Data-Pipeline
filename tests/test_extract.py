import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from utils.extract import fetching_content, extract_products_data, products_scraping

class TestExtractFunctions(unittest.TestCase):
    def setUp(self):
        # Sample HTML for testing
        self.sample_html = '''
        <div class="collection-card">
            <h3 class="product-title">Test Product</h3>
            <div class="price-container">
                <span class="price">$100</span>
            </div>
            <p style="font-size: 14px; color: #777;">4.5</p>
            <p style="font-size: 14px; color: #777;">Red, Blue</p>
            <p style="font-size: 14px; color: #777;">S, M, L</p>
            <p style="font-size: 14px; color: #777;">Male</p>
        </div>
        '''

    def test_fetching_content(self):
        with patch('requests.Session') as mock_session:
            # Test successful request
            mock_response = MagicMock()
            mock_response.content = b"Test content"
            mock_session.return_value.get.return_value = mock_response
            
            result = fetching_content('https://test-url.com')
            self.assertEqual(result, b"Test content")

            # Test failed request
            mock_session.return_value.get.side_effect = Exception("Connection error")
            result = fetching_content('https://invalid-url.com')
            self.assertIsNone(result)