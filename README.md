# Customer Feedback Analysis Platform for Moroccan Banks

A comprehensive data pipeline that collects, processes, analyzes, and visualizes customer reviews about Moroccan banks using modern data engineering tools and natural language processing.

## 📋 Project Overview

This project implements an end-to-end data pipeline that:
- Scrapes customer reviews from Google Maps using SerpAPI
- Cleans and standardizes data using SQL and DBT
- Applies NLP techniques for language detection, translation, and sentiment analysis
- Stores processed data in a PostgreSQL data warehouse
- Creates interactive visualizations in Power BI
- Automates the entire workflow using Apache Airflow

## 🎯 Project Goals

- **Data Collection**: Automated scraping of customer reviews from Google Maps
- **Data Processing**: Clean, standardize, and enrich review data
- **NLP Analysis**: 
  - Automatic language detection
  - Translation to English for standardization
  - Sentiment classification (Positive, Negative, Neutral)
- **Data Warehousing**: Store processed data in a structured format
- **Visualization**: Create insightful dashboards for business intelligence
- **Automation**: Monthly pipeline execution for fresh data

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Data Scraping** | SerpAPI | Google Maps review extraction |
| **Data Processing** | Python | ETL operations and NLP |
| **Database** | PostgreSQL | Data warehouse and storage |
| **Data Modeling** | DBT | Data transformation and modeling |
| **Visualization** | Power BI | Dashboards and reporting |
| **Orchestration** | Apache Airflow | Pipeline automation |
| **Containerization** | Docker | Environment management |

## 📁 Project Structure

```
project/
├── data/                           # Raw data storage
│   ├── banks.json                 # Bank information
│   └── reviews.json               # Scraped reviews
├── scripts/                       # Python scripts
│   ├── scraping/                  # Data collection
│   │   ├── script_bank.py         # Bank data scraping
│   │   └── script_reviews.py      # Review scraping
│   ├── ingestion/                 # Data loading
│   │   └── upload_raw_reviews.py  # Raw data upload
│   └── enrichment/                # NLP processing
│       └── enrich_reviews.py      # Language & sentiment analysis
├── dbt/                           # Data transformation
│   ├── dbt_project.yml           # DBT configuration
│   └── models/                   # DBT models
│       ├── staging/              # Raw data staging
│       ├── intermediate/         # Intermediate transformations
│       ├── dimensions/           # Dimension tables
│       └── marts/               # Final data marts
├── dags/                         # Airflow DAGs
│   └── monthly_reviews_pipeline.py
├── docker-compose.yaml           # Docker configuration
└── README.md                     # Project documentation
```

## 🔄 Workflow Pipeline

### 1. Data Scraping (Monthly)
```bash
# Scrape bank information
python scripts/scraping/script_bank.py

# Scrape customer reviews
python scripts/scraping/script_reviews.py
```

### 2. Data Ingestion
```bash
# Upload raw data to PostgreSQL
python scripts/ingestion/upload_raw_reviews.py
```

### 3. Data Cleaning
```bash
# Clean and standardize data using DBT
dbt run --select clean_reviews
```

### 4. NLP Enrichment
```bash
# Apply language detection, translation, and sentiment analysis
python scripts/enrichment/enrich_reviews.py
```

### 5. Data Modeling
```bash
# Create enriched dataset
dbt run --select enriched_reviews

# Build dimension tables
dbt run --select dim_bank dim_location dim_sentiment

# Create fact table
dbt run --select fact_reviews
```

### 6. Visualization
- Connect Power BI to PostgreSQL database
- Refresh reports monthly with new data

### 7. Automation
```bash
# Start Airflow with Docker
docker-compose up -d

# Monitor DAG: monthly_reviews_pipeline.py
```

## 📊 Data Model (Star Schema)

### Fact Table
- **fact_reviews**: Central table containing review metrics and foreign keys

### Dimension Tables
- **dim_bank**: Bank information and attributes
- **dim_location**: Geographic information (Rabat–Salé–Témara region)
- **dim_sentiment**: Sentiment categories and scores

> **Note**: Branch-level dimension table (dim_branch) was not implemented due to insufficient branch-specific information in the scraped data.

## 📈 Visualizations & Analytics

The Power BI dashboard includes:

- **Review Volume Analysis**: Review counts by bank and time period
- **Sentiment Trends**: Sentiment distribution over time
- **Geographic Analysis**: Sentiment mapping by agency location
- **Performance Metrics**: Average satisfaction scores per bank
- **Interactive Filters**: Bank name, date range, and sentiment categories

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL database
- Docker and Docker Compose
- Power BI Desktop
- SerpAPI account

### Installation
1. Clone the repository
2. Set up environment variables for database and API credentials
3. Install Python dependencies: `pip install -r requirements.txt`
4. Configure DBT profiles
5. Set up Airflow with Docker: `docker-compose up -d`

### Configuration
- Update database connection strings in DBT profiles
- Configure SerpAPI credentials
- Set up Power BI data source connections

## 📅 Automation Schedule

The pipeline runs monthly via Apache Airflow to:
- Collect new reviews
- Process and analyze data
- Update visualizations
- Maintain data freshness

## 🤝 Contributing

Contributions are welcome! Please read the contributing guidelines and submit pull requests for any improvements.

## 👨‍💻 Author

**Mustapha Dafa**

---

*This project demonstrates modern data engineering practices applied to customer feedback analysis in the Moroccan banking sector.*