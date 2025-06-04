# scripts/enrichment/enrich_reviews.py
import pandas as pd
import psycopg2
from langdetect import detect
from deep_translator import GoogleTranslator
from transformers import pipeline
from hashlib import md5
from psycopg2.extras import execute_values

# Connexion 2 : lire la vue clean_reviews
conn2 = psycopg2.connect(
    dbname="review_db",
    user="postgres",
    password="dafa",
    host="localhost",
    port=5432
)

df = pd.read_sql("SELECT * FROM clean_reviews", conn2)
conn2.close()

# Enrichissement
def generate_key(row):
    return md5((str(row['review_text']).lower() + str(row['review_date']) + str(row['address'])).encode()).hexdigest()

def detect_language(text):
    try: return detect(text)
    except: return "unknown"

def translate_to_english(text):
    try: return GoogleTranslator(source='auto', target='en').translate(text)
    except: return ""

sentiment_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
def classify_sentiment(text):
    try:
        score = int(sentiment_model(text[:512])[0]['label'][0])
        return "Positive" if score >= 4 else "Neutral" if score == 3 else "Negative"
    except:
        return "unknown"

df["review_key"] = df.apply(generate_key, axis=1)
df["language"] = df["review_text"].apply(detect_language)
df["translated_review"] = df["review_text"].apply(translate_to_english)
df["sentiment"] = df["translated_review"].apply(classify_sentiment)

df_sentiment = df[["review_key", "language", "sentiment"]]

# Ajout dans enrich_reviews.py (suite)

conn3 = psycopg2.connect(
    dbname="review_db",
    user="postgres",
    password="dafa",
    host="localhost",
    port=5432
)

with conn3.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_lang (
           review_key TEXT,
            language TEXT,
            sentiment TEXT
        );
    """)
    conn3.commit()
    # Insérer les données
    execute_values(
        cur,
        "INSERT INTO sentiment_lang (review_key, language, sentiment) VALUES %s",
        df_sentiment.values.tolist()
    )
    conn3.commit()
conn3.close()

print("✅ Table sentiment_lang insérée avec succès.")
