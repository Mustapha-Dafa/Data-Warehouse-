import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Charger les données brutes
df_raw = pd.read_json("data/reviews.json")

# Connexion PostgreSQL
conn1 = psycopg2.connect(
    dbname="review_db",
    user="postgres",
    password="dafa",
    host="localhost",
    port=5432
)

with conn1.cursor() as cur:
    # Créer la table si elle n'existe pas
    cur.execute("""
        CREATE TABLE IF NOT EXISTS review (
            bank_name TEXT,
            address TEXT,
            review_text TEXT,
            rating FLOAT,
            review_date DATE
        );
    """)
    conn1.commit()

    # Insérer les données
    execute_values(
        cur,
        "INSERT INTO review (bank_name, address, review_text, rating, review_date) VALUES %s",
        df_raw.values.tolist()
    )
    conn1.commit()

conn1.close()
print("✅ Table review créée et données insérées.")
