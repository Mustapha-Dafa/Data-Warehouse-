from serpapi import GoogleSearch
import json 
from urllib.parse import urlsplit, parse_qsl
import os 
import sys
import time
from datetime import datetime

def run_scrape_reviews():
    # Vérification que banks.json existe
    if not os.path.exists("data/banks1.json"):
        print("You must run script_bank file before.")
        sys.exit()
        
    with open("data/banks1.json", "r", encoding="utf-8") as json_file:
        result_bank = json.load(json_file)


    API_Key = "37c31189900ccd53d770037c6b684bc2515666333d064844fa6e23c7eb643536"
    reviews_all = []

    try:
        for i in range(1):  # Tu peux élargir à range(len(result_bank)) plus tard
            data_id = result_bank[i]["data_id"]
            place_name = result_bank[i]["place_name"]
            address = result_bank[i]["address"]
            #reviews_all.append(place_name)
            #reviews_all.append(address)
            
            print(f"\n Scraping reviews for: {place_name}")

            page_num = 0
            next_page_token = None

            while True:
                page_num += 1

                params = {
                    "api_key": API_Key,
                    "engine": "google_maps_reviews",
                    "data_id": data_id,
                    "hl": "fr"
                }

                if next_page_token:
                    params["next_page_token"] = next_page_token

                search = GoogleSearch(params)
                results = search.get_dict()

                if "error" in results:
                    print(f"Error on page {page_num}: {results['error']}")
                    break

                reviews = results.get("reviews", [])
                if not reviews:
                    print("No more reviews.")
                    break

                print(f"✓ Page {page_num} - {len(reviews)} reviews extracted.")

                for review in reviews:
                    reviews_all.append({
                        "bank_name": place_name,
                        "location": address,
                        "review text": review.get("snippet"),
                        "rating": review.get("rating"),
                        "review_date": datetime.fromisoformat(review.get("iso_date").replace("Z", "")).date().isoformat() if review.get("iso_date") else None
                        
                    })

                # Gérer la pagination
                pagination = results.get("serpapi_pagination", {})
                next_page_token = pagination.get("next_page_token")

                if not next_page_token:
                    break  # Fin de pagination

                time.sleep(2)  # Attente pour éviter d'être bloqué par SerpAPI

    finally:
        # Sauvegarde même si le script est interrompu
        os.makedirs("data", exist_ok=True)
        with open("data/reviews_test.json", "w", encoding="utf-8") as f:
            json.dump(reviews_all, f, indent=4, ensure_ascii=False)

        print(f"\nDonnées sauvegardées. Total: {len(reviews_all)} avis.")
