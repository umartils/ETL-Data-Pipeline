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
    
    section = products.find_all('p', style="font-size: 14px; color: #777;")

    rating = section[0].text
    color = section[1].text
    size = section[2].text
    gender = section[3].text

    fashion = {
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Colors": color,
        "Size": size,
        "Gender": gender,
        "Time": datetime.now().isoformat()
    }

    return fashion
def products_scraping(base_url, start_page=1, end_page=50, delay=2):
    data = []

    for page_number in range(start_page, end_page + 1):
        # print(f"Scraping halaman {page_number}: {url}")
        if page_number == 1:
            url = base_url.rstrip('{}')
        else:
            url = base_url.format(f"page{page_number}")
        content = fetching_content(url)
        if not content:
            print(f"Gagal mengambil konten dari halaman {page_number}")
            continue

        soup = BeautifulSoup(content, "html.parser")
        elements = soup.find_all('div', class_='collection-card')

        if not elements:
            print(f"Tidak ada data ditemukan di halaman {page_number}")
            break

        for products in elements:
            fashion = extract_products_data(products)
            data.append(fashion)

        time.sleep(delay)

    return data