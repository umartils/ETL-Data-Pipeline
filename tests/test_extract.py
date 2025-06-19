import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from utils.extract import fetching_content, extract_products_data, products_scraping