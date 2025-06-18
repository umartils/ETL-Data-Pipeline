import pandas as pd
from sqlalchemy import create_engine
import pygsheets

def load_data_to_csv(data, filename):
    """Load data to CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data berhasil disimpan di {filename}")

def load_data_to_postgresql(data, db_url, table_name):
    """Load data to PostgreSQL database."""
    try:
        engine = create_engine(db_url)
        data.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',
            index=False
        )
        print(f"Data berhasil disimpan di PostgreSQL!")
    
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data: {e}")