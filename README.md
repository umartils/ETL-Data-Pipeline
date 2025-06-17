# ELT Data Pipeline

## Deskripsi

Repository ini berisi mengenai project data pipeline menggunakan metode ELT (Extract, Load, Transform). Project ini menggunakan teknik scraping untuk mengambil data (Extract) dengan sumber data dari situs [Fashion Studio by Dicoding](https://fashion-studio.dicoding.dev/). Lalu data ditransformasi agar data yang disimpan bersih dan memiliki format yang sesuai sebelum data disimpan ke dalam database atau repository data. Setelah data bersih dan memiliki format yang seragam, data disimpan ke dalam Google Sheet, PostgreSQL dan file csv.

Selain berisi data pipeline, project ini juga berisi unit test untuk memastikan semua proses data pipeline ETL berjalan dengan baik tanpa ada kendala yang dapat mengganggu proses data pipeline.

## Proses Persiapan

Sebelum menjalankan project, lalu instalasi library atau package yang ada pada file `requirements.txt` menggunakan terminal pada IDE atau command prompt anda. Pastikan anda berada di direktori yang sama dengan file `requirements.txt` .

Selanjutnya lakukan perintah
```bash
pip install -r requirements.txt
```