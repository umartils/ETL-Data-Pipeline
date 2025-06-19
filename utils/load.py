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

def load_data_to_google_sheet(service_file_path, spreadsheet_id, sheet_name, data_df):
    """
    this function takes data_df and writes it under spreadsheet_id
    and sheet_name using your credentials under service_file_path
    """
    gc = pygsheets.authorize(service_file=service_file_path)
    sh = gc.open_by_key(spreadsheet_id)
    try:
        sh.add_worksheet(sheet_name)
    except:
        pass
    wks_write = sh.worksheet_by_title(sheet_name)
    wks_write.clear('A1',None,'*')
    wks_write.set_dataframe(data_df, (1,1), encoding='utf-8', fit=True)
    wks_write.frozen_rows = 1
    print(f"Data berhasil disimpan di Google Sheet!")