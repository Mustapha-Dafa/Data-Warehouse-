from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'monthly_reviews_pipeline',
    default_args=default_args,
    schedule_interval='@monthly',
    catchup=False,
    description='Pipeline mensuel de scraping, NLP et modélisation',
    tags=['nlp', 'dbt', 'pipeline'],
) as dag:

    # Étape 1 - Scraper les banques
    scrape_banks = BashOperator(
        task_id='scrape_banks',
        bash_command='python /path/to/projet/scripts/scraping/script_bank.py'
    )

    # Étape 2 - Scraper les avis (append)
    scrape_reviews = BashOperator(
        task_id='scrape_reviews',
        bash_command='python /path/to/projet/scripts/scraping/script_reviews.py'
    )

    # Étape 3 - Upload vers PostgreSQL
    upload_data = BashOperator(
        task_id='upload_reviews',
        bash_command='python /path/to/projet/scripts/ingestion/upload_raw_reviews.py'
    )

    # Étape 4 - Nettoyage avec DBT
    dbt_clean = BashOperator(
        task_id='dbt_clean',
        bash_command='cd /path/to/projet/dbt && dbt run --select clean_reviews'
    )

    # Étape 5 - Enrichissement NLP
    enrich_nlp = BashOperator(
        task_id='enrich_reviews',
        bash_command='python /path/to/projet/scripts/enrichment/enrich_reviews.py'
    )

    # Étape 6 - Jointure enrichie
    dbt_enriched = BashOperator(
        task_id='dbt_enriched',
        bash_command='cd /path/to/projet/dbt && dbt run --select enriched_reviews'
    )

    # Étape 7 - Dimensions
    dbt_dimensions = BashOperator(
        task_id='dbt_dimensions',
        bash_command='cd /path/to/projet/dbt && dbt run --select dim_bank dim_location dim_sentiment'
    )

    # Étape 8 - Table de faits
    dbt_fact = BashOperator(
        task_id='dbt_fact_reviews',
        bash_command='cd /path/to/projet/dbt && dbt run --select fact_reviews'
    )

    # Dépendances
    scrape_banks >> scrape_reviews >> upload_data >> dbt_clean
    dbt_clean >> enrich_nlp >> dbt_enriched >> dbt_dimensions >> dbt_fact
