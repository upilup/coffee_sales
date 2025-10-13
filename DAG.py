'''
============================================================================================================================================================================
Milestone 3

Nama  : Muhammad Luthfi Alfatih

Program ini dibuat untuk melakukan automatisasi Extract, Transform, dan Load (ETL) data dari PostgreSQL ke ElasticSearch. Adapun dataset yang dipakai adalah dataset mengenai 
penjualan kopi (Coffee Sales) dari Kaggle (Maret 2024 sampai dengan Maret 2025). Tujuan utam program ini adalah membangun pipeline data yang dapat membersihkan, mentransformasi,
dan memuat data ke ElasticSearch sehingga siap divisualisasikan di Kibana untuk menghasilkan insight terkait pola penjualan kopi.

============================================================================================================================================================================
'''

import re
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from elasticsearch import Elasticsearch

default_args= {
    'owner': 'Muhammad Luthfi Alfatih',
    'start_date': datetime(2024, 11, 1)
}

with DAG(
    'etl_csv_files',
    description='from local to postgres',
    schedule_interval='10-30/10 9 * 11 6',
    default_args=default_args, 
    catchup=False) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def extract():
        '''
        Fungsi ini digunakan untuk mengekstrak data dari PostgreSQL ke dalam format CSV.
        - Menghubungkan ke database PostgreSQL.
        - Membaca tabel `table_m3`.
        - Menyimpan hasil query ke file CSV mentah (`data_raw.csv`).

        Output:
        File CSV mentah yang berisi data original dari PostgreSQL.
        '''
        
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

        engine = create_engine(postgres_url)
        conn = engine.connect()
        
        df = pd.read_sql('SELECT * FROM table_m3', conn)
        df.to_csv('/opt/airflow/dags/P2M3_Muhammad_Luthfi_Alfatih_data_raw.csv', index=False)

        print("Success INSERT")

    @task()
    def preprocess_data():
        '''
        Fungsi ini melakukan preprocessing terhadap data mentah hasil extract.
        - Normalisasi nama kolom (lowercase, underscore, hapus simbol).
        - Konversi tipe data `date` dan `time` ke format datetime.
        - Mengisi missing values (numerik dengan mean, kategorik dengan mode).
        - Menghapus duplikat.

        Output:
        File CSV bersih (`data_clean.csv`) yang siap untuk tahap transformasi.
        '''
        df = pd.read_csv('/opt/airflow/dags/P2M3_Muhammad_Luthfi_Alfatih_data_raw.csv')
        
        # Rename columns and normalizations
        df.columns = (df.columns
                      .astype(str)                                      # Make sure all columns string
                      .str.strip()                                      # Delete whitespace start/end
                      .str.replace(r'\s+', '_', regex=True)             # space/tab -> underscore
                      .str.replace(r'[^a-zA-Z0-9]', '_', regex=True)    # Symbol (|,!,@,etc.) -> underscore
                      .str.replace(r'_+', '_', regex=True)              # Compile duplicated underscore
                      .str.strip('_')                                   # Clean underscore start/end
                      .str.lower())                                     # Convert to lowercase
        
        # Convert data types if necessary (example: ensure 'date' is datetime and 'time' is datetime.time)
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S.%f', errors='coerce').dt.floor('S').dt.time

        # Handle missing values (example: fill missing numeric values with mean & categorical with mode)
        # Numerical
        num_cols = df.select_dtypes(include=['int64', 'float64']).columns
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

        # Categorical
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if df[col].isnull().sum() > 0:
                df[col].fillna(df[col].mode()[0], inplace=True)
        
        # Remove duplicates if any
        df.drop_duplicates(inplace=True)

        print("Preprocessed data is Success")
        print(df.head())
        df.to_csv('/opt/airflow/dags/P2M3_Muhammad_Luthfi_Alfatih_data_clean.csv', index=False)

    @task()
    def transform():
        '''
        Fungsi ini menambahkan fitur baru untuk mendukung analisis data.
        - Membaca file hasil preprocessing ('data_clean.csv`).
        - Membuat kolom `transaction_id` sebagai unique identifier gabungan dari date, time, dan coffee_name.

        Output:
        File CSV hasil transformasi (`data_transformed.csv`) yang siap dimuat ke ElasticSearch.
        '''
        # Load data hasil preprocessing
        df = pd.read_csv('/opt/airflow/dags/P2M3_Muhammad_Luthfi_Alfatih_data_clean.csv')

        # Add transaction_id
        df['transaction_id'] = (
                df['date'].astype(str) + "_" +
                df['time'].astype(str) + "_" +
                df['coffee_name'].astype(str)
            )

        print("Transform data Success")
        print(df.head())

        # Save transformed file result
        df.to_csv('/opt/airflow/dags/P2M3_Muhammad_Luthfi_Alfatih_data_transformed.csv', index=False)

    @task
    def load():
        '''
        Fungsi ini bertanggungjawab untuk memuat data hasil transformasi ke ElasticSearch.
        - Membaca file (`data_transformed.csv`).
        - Mengirim setiap record ke index `coffee_sales_v2` di ElasticSearch.

        Output:
        Data berhasil diindeks di ElasticSearch dan siap divisualisasikan di Kibana.
        '''
        es = Elasticsearch("http://elasticsearch:9200")
        print(es.ping())
        # Read data file
        df = pd.read_csv("/opt/airflow/dags/P2M3_Muhammad_Luthfi_Alfatih_data_transformed.csv")

        # Send data to ElasticSearch
        for i, row in df.iterrows():
            res = es.index(index="coffee_sales_v2", id=i+1, body=row.to_json())

    start >> extract() >> preprocess_data() >> transform() >> load() >> end
