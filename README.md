# 📊 Customer Feedback Analysis Platform for Moroccan Banks

This project is a full data pipeline that collects, cleans, analyzes, and visualizes customer reviews about Moroccan banks using tools like Python, PostgreSQL, DBT, Airflow, and Power BI.

---

## 🧠 Goal of the Project

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

## 🛠 Tools Used

- **SerpAPI** – For scraping Google Maps data.
- **Python** – For data loading, NLP, translation, and sentiment analysis.
- **PostgreSQL** – Main database.
- **DBT** – For data cleaning and modeling (star schema).
- **Power BI** – For dashboard and reporting.
- **Apache Airflow (Docker)** – For automation and scheduling.

---

## 📁 Project Structure

