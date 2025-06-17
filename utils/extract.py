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
        return response.contents
    except Exception as e:
        print(f"Terjadi kesalahan ketika melakukan requests terhadap {url}: {e}")
        return None