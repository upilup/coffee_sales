# Coffee Sales Dashboard Project
## Objective
Tujuan dari project ini adalah membangun pipeline data yang mampu mengolah transaksi penjualan kopi mulai dari tahap preprocessing hingga visualisasi. Dengan adanya dashboard interaktif di Kibana, pemilik bisnis dapat:
- Memahami pola penjualan kopi secara lebih mendalam (menu favorit, tren bulanan, dan jam ramai).  
- Mengidentifikasi perilaku pelanggan berdasarkan waktu konsumsi dan metode pembayaran.  
- Menghasilkan **business insight** yang dapat digunakan untuk merancang strategi promosi, meningkatkan penjualan, serta menjaga loyalitas pelanggan.  

## Repository Outline
1. README.md                                        - Gambaran umum project
2. P2M3_Muhammad_Luthfi_Alfatih_DDL.txt             - DDL untuk pembuatan tabel database PostgreSQL
3. P2M3_Muhammad_Luthfi_Alfatih_DAG.py              - File Airflow DAG untuk ETL pipeline
4. P2M3_Muhammad_Luthfi_Alfatih_data_raw.csv        - Dataset mentah penjualan kopi
5. P2M3_Muhammad_Luthfi_Alfatih_data_clean.csv      - Dataset hasil preprocessing
6. P2M3_Muhammad_Luthfi_Alfatih_GX.ipynb            - Notebook eksplorasi dan preprocessing data
7. description.md                                   - Deskripsi singkat project

## Problem Background
Bisnis kedai kopi perlu memahami pola penjualan mereka, mulai dari menu favorit, metode pembayaran, hingga jam ramai pelanggan. Data transaksi sering kali tidak langsung siap digunakan, sehingga dibutuhkan proses ETL (Extract, Transform, Load) agar data dapat divisualisasikan dan menghasilkan insight yang mendukung strategi bisnis.

## Project Output
- ETL Pipeline menggunakan Airflow untuk memproses data dari CSV -> PostgreSQL -> Elasticsearch.
- Dashboard interaktif di Kibana yang menampilkan:
    - Menu kopi terlaris
    - Tren penjualan bulanan
    - Distribusi transaksi berdasarkan waktu
    - Metode pembayaran pelanggan

## Data
- Sumber: [Coffee Sales Dataset - Kaggle](https://www.kaggle.com/datasets/navjotkaushal/coffee-sales-dataset)
- Jumlah: ±1.5K baris transaksi penjualan kopi
- Fitur utama: `coffee_name`, `money`, `date`, `hour_of_day`, `cash_type`, `month_name`
- Karakteristik: Tidak mengandung _missing values_ & tipe data tidak konsisten -> dilakukan preprocessing (cleaning, konversi tipe data, composite key).

## Method
- ETL Process: Data mentah -> Preprocessing -> Load ke PostgreSQL -> Index ke Elasticsearch -> Visualisasi di Kibana.
- Analisis: Exploratory Data Analysis (EDA) dan visualisasi untuk menemukan pola penjualan.
- Business Insight: Rekomendasi strategi promosi (contoh: diskon untuk menu dengan penjualan rendah, promo bundling pada jam sepi).

## Stacks
- Bahasa: Python
- Tools: PostgreSQL, Airflow, Elasticsearch, Kibana
- Libraries Python: `pandas`, `psycopg2`, `elasticsearch`

## Reference
- [Dataset Coffee Sales](https://www.kaggle.com/datasets/navjotkaushal/coffee-sales-dataset)
- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Elasticsearch Documentation](https://www.elastic.co/docs/get-started/)
- [Kibana Documentation](https://www.elastic.co/docs/get-started/the-stack)

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)