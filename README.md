# ☕ Coffee Sales Dashboard Project

## 📌 Introduction
This project was developed as part of **Hacktiv8 Milestone 3** by **Muhammad Luthfi Alfatih (Batch FTDS-030-HCK)**.  
The goal is to build an **automated ETL pipeline** that processes coffee sales transactions and delivers insights through an **interactive dashboard in Kibana**.  

---

## 🎯 Objectives
The main objectives of this project are:
- Automate a pipeline to process coffee sales data from **CSV → PostgreSQL → Elasticsearch → Kibana**.
- Perform **preprocessing** to clean and transform raw transactions into structured data.
- Provide **business insights** through dashboards, enabling coffee shop owners to:
  - Identify favorite menus and monthly sales trends.
  - Understand peak hours and payment method preferences.
  - Design effective promotional strategies and improve customer loyalty.

---

## 🗂 Repository Outline
├── README.md # Project documentation<br>
├── description.md # Project description<br>
├── P2M3_Muhammad_Luthfi_Alfatih_DDL.txt # PostgreSQL table creation script (DDL)<br>
├── P2M3_Muhammad_Luthfi_Alfatih_DAG.py # Airflow DAG for ETL pipeline<br>
├── P2M3_Muhammad_Luthfi_Alfatih_data_raw.csv # Raw dataset (extracted from PostgreSQL)<br>

---

## 🏪 Problem Background
Coffee shop businesses need to understand their sales patterns — from top-selling menus and customer purchase times to preferred payment methods.  
However, transactional data is often not directly ready for analysis. An **ETL (Extract, Transform, Load)** process is required to make data structured, cleaned, and ready for visualization to generate actionable insights.

---

## 🚀 Project Output
- **ETL Pipeline** with Airflow:
  - Extract raw sales data
  - Clean & preprocess data
  - Store in PostgreSQL
  - Load into Elasticsearch
- **Kibana Dashboard** displaying:
  - Best-selling coffee menu
  - Monthly sales trends
  - Customer purchase distribution by time
  - Payment method preferences

---

## 📊 Dataset
- **Source:** [Coffee Sales Dataset - Kaggle](https://www.kaggle.com/)  
- **Size:** ~1.5K rows of coffee sales transactions  
- **Key Features:**  
  - `coffee_name` (menu)  
  - `money` (sales amount)  
  - `date`, `hour_of_day`, `month_name` (time dimension)  
  - `cash_type` (payment method)  
- **Notes:**  
  - Contains no missing values  
  - Inconsistent data types → fixed during preprocessing  
  - Composite key (`transaction_id`) created for unique identification  

---

## ⚙️ Methodology
1. **ETL Process**
   - Data ingestion from CSV
   - Preprocessing: column normalization, type conversion, missing value handling, deduplication
   - Load into PostgreSQL
   - Index data into Elasticsearch
   - Dashboard building in Kibana

2. **Analysis**
   - Exploratory Data Analysis (EDA)
   - Visualizations of sales patterns and customer behavior

3. **Business Insights**
   - Promotional strategy recommendations
     - Discounts for low-selling menus  
     - Bundling promotions during off-peak hours  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Pipeline Orchestration:** Apache Airflow  
- **Database:** PostgreSQL  
- **Search Engine:** Elasticsearch  
- **Visualization:** Kibana  
- **Libraries:** `pandas`, `sqlalchemy`, `psycopg2`, `elasticsearch`  

---

## 📖 References
- [Coffee Sales Dataset - Kaggle](https://www.kaggle.com/)  
- [Apache Airflow Documentation](https://airflow.apache.org/)  
- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)  
- [Kibana Documentation](https://www.elastic.co/guide/en/kibana/current/index.html)  
- Additional references:  
  - Markdown Guide: [Basic Syntax](https://www.markdownguide.org/basic-syntax/)  
  - Example README templates  

├── P2M3_Muhammad_Luthfi_Alfatih_data_clean.csv # Cleaned dataset (after preprocessing)
├── P2M3_Muhammad_Luthfi_Alfatih_GX.ipynb # Data exploration & preprocessing notebook
└── conceptual.txt # Conceptual Q&A (NoSQL, Airflow, Great Expectations, etc.)
