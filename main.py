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
    
    if data:
        # TRANSFORM DATA
        print(f"Melakukan transformasi data...")
        df_clean = clean_data(data)
        df_clean = convert_currency(df_clean, exchange_rate=16000)
        print(df_clean.head())
        print(df_clean.info())
        print("Selesai melakukan transformasi data")
        print("==============================================")
        # LOAD DATA
        load_data_to_csv(df_clean, 'products.csv')
        load_data_to_postgresql(
            df_clean,
            'postgresql://umar:umar123@localhost:5432/productsdb', 
            'fashion_data'
            )
        load_data_to_google_sheet(
            service_file_path,
            spreadsheet_id,
            sheet_name, df_clean
            )
        print("==============================================")
    else:
        print("Tidak ada data yang berhasil di-scrape")