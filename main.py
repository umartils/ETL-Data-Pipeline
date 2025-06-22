from utils.extract import products_scraping
from utils.transform import clean_data, convert_currency
from utils.load import load_data_to_csv, load_data_to_postgresql, load_data_to_google_sheet

def main():
    """Fungsi utama untuk keseluruhan proses scraping."""
    BASE_URL = 'https://fashion-studio.dicoding.dev/{}'
    print(f"Melakukan scraping data...")
    data = products_scraping(
        base_url=BASE_URL,
        start_page=1,
        end_page=50,
        delay=2
    )
    print("Selesai melakukan scraping data")
    service_file_path = 'google-sheets-api.json'
    spreadsheet_id = '1GtjDqHlkCwU45KwIs8GAjel3hBxSymzNOERdcnR8OyY'
    sheet_name = 'Sheet1'