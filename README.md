# Customer Feedback Analysis Platform for Moroccan Banks

This project is a full data pipeline that collects, cleans, analyzes, and visualizes customer reviews about Moroccan banks using tools like Python, PostgreSQL, DBT, Airflow, and Power BI.

---

## Goal of the Project

- Scrape reviews from Google Maps using SerpAPI.
- Clean and standardize the data using SQL and DBT.
- Use NLP (Natural Language Processing) to:
  - Detect language
  - Translate to English
  - Classify sentiment (Positive, Negative, Neutral)
- Store the final data in a data warehouse (PostgreSQL).
- Visualize results in Power BI dashboards.
- Automate the entire process using Apache Airflow (monthly updates).

---

## Tools Used

- **SerpAPI** – For scraping Google Maps data.
- **Python** – For data loading, NLP, translation, and sentiment analysis.
- **PostgreSQL** – Main database.
- **DBT** – For data cleaning and modeling (star schema).
- **Power BI** – For dashboard and reporting.
- **Apache Airflow (Docker)** – For automation and scheduling.

---

##  Project Structure
project/
├── data/
│ ├── banks.json
│ └── reviews.json
├── scripts/
│ ├── scraping/
│ │ ├── script_bank.py
│ │ └── script_reviews.py
│ ├── ingestion/
│ │ └── upload_raw_reviews.py
│ └── enrichment/
│ └── enrich_reviews.py
├── dbt/
│ ├── dbt_project.yml
│ └── models/
│ ├── staging/
│ ├── intermediate/
│ ├── dimensions/
│ └── marts/
├── dags/
│ └── monthly_reviews_pipeline.py
└── docker-compose.yaml

---

## ⚙️ Workflow Steps

1. **Scraping (monthly)**  
   Run:
   ```bash
   python scripts/scraping/script_bank.py
   python scripts/scraping/script_reviews.py

2. Upload raw data to PostgreSQL

python scripts/ingestion/upload_raw_reviews.py

3. Run DBT cleaning

dbt run --select clean_reviews

4. Enrichment with NLP

python scripts/enrichment/enrich_reviews.py

5. Model data in DBT

dbt run --select enriched_reviews
dbt run --select dim_bank dim_location dim_sentiment
dbt run --select fact_reviews

6. Visualize in Power BI

    Connect to PostgreSQL

    Refresh reports monthly

7. Automate with Airflow

    docker-compose up -d

    DAG: monthly_reviews_pipeline.py

Visualizations Created

    Reviews count per bank

    Sentiment trends over time

    Map of sentiment by agency (Rabat–Salé–Témara)

    Average satisfaction score per bank

    Filters: bank name, date, sentiment

 Star Schema Overview

    Fact Table: fact_reviews

    Dimensions:

        dim_bank

        dim_location

        dim_sentiment

    Note: No dim_branch table due to missing branch-level info in scraped data.

 Authors

    Mustapha Dafa

