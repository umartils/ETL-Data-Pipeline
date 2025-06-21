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

    def test_extract_products_data(self):
        soup = BeautifulSoup(self.sample_html, 'html.parser')
        product = soup.find('div', class_='collection-card')
        result = extract_products_data(product)

        # Test data structure
        self.assertIsInstance(result, dict)
        self.assertEqual(result['Title'], 'Test Product')
        self.assertEqual(result['Price'], '$100')
        self.assertEqual(result['Rating'], '4.5')
        self.assertEqual(result['Colors'], 'Red, Blue')
        self.assertEqual(result['Size'], 'S, M, L')
        self.assertEqual(result['Gender'], 'Male')
        self.assertIn('Time', result)
    
    @patch('utils.extract.fetching_content')
    @patch('time.sleep')
    def test_products_scraping(self, mock_sleep, mock_fetching):
        # Mock the fetching_content response
        mock_fetching.return_value = self.sample_html.encode()

        # Test with minimal parameters
        result = products_scraping(
            base_url='https://fashion-studio.dicoding.dev/page-{}',
            start_page=2,
            end_page=3,
            delay=0
        )

        # Verify results
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)
        self.assertIsInstance(result[0], dict)
        
        # Verify correct number of calls
        self.assertEqual(mock_fetching.call_count, 2)
        self.assertEqual(mock_sleep.call_count, 2)