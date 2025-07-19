# ETL Data Pipeline - Fashion Studio

## Summary

Project ini merupakan implementasi pipeline ETL (Extract, Transform, Load) yang dibangun untuk mengumpulkan, memproses, dan menyimpan data produk fashion dari website Fashion Studio Dicoding. Pipeline ini mengotomatisasi proses pengumpulan data produk fashion meliputi informasi nama produk, rating, ukuran, gender, dan jumlah warna yang tersedia.

Pipeline ETL ini dirancang untuk memberikan solusi end-to-end dalam pengelolaan data, mulai dari ekstraksi data melalui web scraping, transformasi data untuk standardisasi format, hingga loading data ke berbagai destination storage seperti Google Sheets, PostgreSQL database, dan file CSV untuk kebutuhan analisis lebih lanjut.

## Fitur Utama

- **Extract**: Web scraping otomatis dari situs Fashion Studio Dicoding
- **Transform**: Pembersihan dan standardisasi format data
- **Load**: Multi-destination loading (Google Sheets, PostgreSQL, CSV)
- **Scheduling**: Support untuk menjalankan pipeline secara terjadwal
- **Error Handling**: Robust error handling dan retry mechanism
- **Logging**: Comprehensive logging untuk monitoring pipeline
- **Data Validation**: Validasi kualitas data sebelum loading

## Arsitektur Pipeline

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   EXTRACT   │    │ TRANSFORM   │    │    LOAD     │
│             │    │             │    │             │
│ Web Scraping│───▶│Data Cleaning│───▶│Google Sheets│
│ Fashion     │    │Standardize  │    │PostgreSQL   │
│ Studio Site │    │Validation   │    │CSV Files    │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Instalasi

### Requirements

Pastikan Anda memiliki Python 3.8 atau versi yang lebih baru.

### Membuat Virtual Environment

```bash
# Membuat virtual environment
python -m venv etl-env

# Aktivasi virtual environment
# Windows
etl-env\Scripts\activate

# macOS/Linux
source etl-env/bin/activate
```

### Install Dependencies

```bash
# Install dari requirements.txt
pip install -r requirements.txt

# Atau install manual
pip install requests beautifulsoup4 pandas sqlalchemy psycopg2-binary gspread oauth2client python-dotenv schedule logging
```

### Clone Repository

```bash
git clone https://github.com/umartils/Sentimen-Analisis-Random-Forest.git
cd etl-pipeline-fashion-studio
```

### Setup Environment Variables

Buat file `.env` di root directory:

```env
# PostgreSQL Configuration
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=fashion_db
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password

# Google Sheets Configuration
GOOGLE_SHEETS_CREDENTIALS_FILE=credentials.json
GOOGLE_SHEETS_ID=your_sheet_id

# Scraping Configuration
FASHION_STUDIO_URL=https://fashion-studio.dicoding.dev/
REQUEST_DELAY=1
MAX_RETRIES=3
```

### Setup Google Sheets API

1. Buat project di Google Cloud Console
2. Enable Google Sheets API
3. Buat Service Account dan download credentials JSON
4. Simpan file credentials sebagai `credentials.json`
5. Share Google Sheets dengan service account email

## Struktur Project

```
etl-pipeline-fashion-studio/
├── src/
│   ├── extractors/
│   │   ├── __init__.py
│   │   └── fashion_scraper.py
│   ├── transformers/
│   │   ├── __init__.py
│   │   └── data_transformer.py
│   ├── loaders/
│   │   ├── __init__.py
│   │   ├── csv_loader.py
│   │   ├── postgres_loader.py
│   │   └── gsheets_loader.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── logger.py
│   └── pipeline.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
├── logs/
├── config/
│   └── credentials.json
├── notebooks/
│   └── data_exploration.ipynb
├── tests/
├── requirements.txt
├── main.py
├── .env.example
└── README.md
```

## Data Source

### Informasi Website Target

Pipeline ini melakukan scraping data dari **Fashion Studio Dicoding** yang tersedia di https://fashion-studio.dicoding.dev/. Website ini menampilkan katalog produk fashion dengan informasi:

- **Nama Produk**: T-shirt, Hoodie, Pants, Jacket, Crewneck, Outerwear
- **Rating**: Skala 1-5 bintang
- **Jumlah Warna**: Variasi warna yang tersedia
- **Ukuran**: S, M, L, XL, XXL
- **Gender**: Men, Women, Unisex
- **Harga**: Jika tersedia

### Struktur Data yang Diekstrak

```python
{
    "product_name": "T-shirt 2",
    "rating": 3.9,
    "colors_available": 3,
    "size": "M",
    "gender": "Women",
    "price": "Price Unavailable",
    "scraped_at": "2025-07-19 10:30:00"
}
```

## Cara Penggunaan

### 1. Menjalankan Pipeline Lengkap

```python
from src.pipeline import ETLPipeline

# Inisialisasi pipeline
pipeline = ETLPipeline()

# Jalankan pipeline lengkap
pipeline.run()
```

### 2. Menjalankan Komponen Terpisah

```python
# Extract saja
from src.extractors.fashion_scraper import FashionScraper

scraper = FashionScraper()
raw_data = scraper.extract()

# Transform saja
from src.transformers.data_transformer import DataTransformer

transformer = DataTransformer()
cleaned_data = transformer.transform(raw_data)

# Load ke destination tertentu
from src.loaders.postgres_loader import PostgresLoader

postgres_loader = PostgresLoader()
postgres_loader.load(cleaned_data)
```

### 3. Running via Command Line

```bash
# Jalankan pipeline lengkap
python main.py --mode full

# Extract saja
python main.py --mode extract

# Transform dan Load saja (dengan input file)
python main.py --mode transform-load --input data/raw/fashion_data.json

# Load ke destination tertentu
python main.py --mode load --destination postgres --input data/processed/cleaned_data.csv
```

### 4. Scheduled Pipeline

```python
import schedule
import time
from src.pipeline import ETLPipeline

def run_pipeline():
    pipeline = ETLPipeline()
    pipeline.run()

# Jadwalkan pipeline setiap hari jam 2 pagi
schedule.every().day.at("02:00").do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(60)
```

## Konfigurasi

### Scraping Configuration

```python
SCRAPING_CONFIG = {
    'base_url': 'https://fashion-studio.dicoding.dev/',
    'request_delay': 1,
    'max_retries': 3,
    'timeout': 30,
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
}
```

### Database Configuration

```python
DATABASE_CONFIG = {
    'postgres': {
        'host': 'localhost',
        'port': 5432,
        'database': 'fashion_db',
        'table': 'fashion_products'
    }
}
```

### Google Sheets Configuration

```python
GSHEETS_CONFIG = {
    'credentials_file': 'credentials.json',
    'sheet_id': 'your_google_sheet_id',
    'worksheet_name': 'Fashion_Data'
}
```

## Monitoring dan Logging

Pipeline dilengkapi dengan comprehensive logging yang mencatat:

```python
# Contoh log output
2025-07-19 10:30:00 INFO - Starting ETL Pipeline
2025-07-19 10:30:01 INFO - Extracting data from Fashion Studio
2025-07-19 10:30:15 INFO - Successfully extracted 20 products
2025-07-19 10:30:16 INFO - Starting data transformation
2025-07-19 10:30:17 INFO - Data validation completed - 20 valid records
2025-07-19 10:30:18 INFO - Loading data to PostgreSQL
2025-07-19 10:30:20 INFO - Loading data to Google Sheets
2025-07-19 10:30:25 INFO - Loading data to CSV
2025-07-19 10:30:26 INFO - ETL Pipeline completed successfully
```

## Data Quality & Validation

Pipeline mengimplementasikan validasi data meliputi:

- **Completeness**: Memastikan field wajib terisi
- **Accuracy**: Validasi format rating, ukuran, dan gender
- **Consistency**: Standardisasi nama produk dan kategori
- **Timeliness**: Penambahan timestamp untuk setiap record

## Error Handling

- **Retry Mechanism**: Auto-retry untuk failed requests
- **Graceful Degradation**: Pipeline tetap berjalan meski ada destination yang gagal
- **Error Notification**: Logging detail error untuk debugging
- **Data Recovery**: Backup data di setiap tahap pipeline

## Performance

- **Concurrent Processing**: Multi-threading untuk extract dan load
- **Batch Processing**: Efficient batch loading untuk database
- **Memory Management**: Stream processing untuk dataset besar
- **Caching**: Cache untuk avoid duplicate requests

## Troubleshooting

### Common Issues

1. **Connection Error**: Periksa koneksi internet dan status website
2. **Database Connection**: Verifikasi credentials dan database availability
3. **Google Sheets API**: Periksa service account permissions
4. **Memory Issues**: Adjust batch size untuk dataset besar

### Debugging

```bash
# Run dengan verbose logging
python main.py --mode full --verbose

# Check logs
tail -f logs/etl_pipeline.log
```

## Contributing

Kontribusi sangat diterima! Silakan fork repository dan submit pull request untuk perbaikan atau fitur baru.

## License

Project ini dilisensikan under MIT License.

## Kontak

- Repository: https://github.com/umartils/Sentimen-Analisis-Random-Forest
- Email: your.email@example.com

## Deaktivasi Virtual Environment

```bash
# Untuk venv
deactivate
```