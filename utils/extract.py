import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetching_content(url):
    HEADERS = {"User-Agent": "Chrome/96.0.4664.110"}
    try:
        session = requests.Session()
        response = session.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.content
    except Exception as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None

def extract_products_data(products):
    try:
        title = products.find('h3', class_='product-title').text.strip()
    except AttributeError:
        title = "No title found"

    try:
        price_element = products.find('div', class_='price-container')
        price = price_element.find('span', class_='price').text.strip() if price_element else "Price unavailable"
    except AttributeError:
        price = "Price not available"