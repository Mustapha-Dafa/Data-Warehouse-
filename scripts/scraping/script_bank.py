from serpapi import GoogleSearch
from urllib.parse import urlsplit, parse_qsl
import pandas as pd
import json
import time 

def run_scrape_banks():
  API_Key = "37c31189900ccd53d770037c6b684bc2515666333d064844fa6e23c7eb643536"
  params = {
    "api_key": API_Key,
    "engine": "google_maps",
    "ll": "@33.9700232,-6.9396649,12z",
    "q": "bank",
    "type":"search",
  }

  #existing_data_ids={}

  search = GoogleSearch(params)

  local_place_results = []

  page_num = 0

  while True:
      page_num += 1
      results = search.get_dict()
      time.sleep(2)

      if  "error" not in results:
        
          for result in results.get("local_results"):
            
            data_id = result.get("data_id")
            #if data_id not in existing_data_ids:
              # existing_data_ids.add(data_id)
                
            print(f"Extracting data from {result.get('title')}")
            local_place_results.append({
                "page_num": page_num,
                "place_name": result.get("title"),
                "rating": result.get("rating"),
                "reviews": result.get("reviews"),
                "place_id": result.get("place_id"),
                "data_id": result.get("data_id"),
                "address": result.get("address"),
                "phone": result.get("phone"),
                "website": result.get("website"),
                "reviews_link": result.get("reviews_link"),
                "photos_link": result.get("photos_link"),
                "gps_coordinates": result.get("gps_coordinates"),
                "thumbnail": result.get("thumbnail")
                # many other types of data
              })
      else:
          print(results["error"] + " Or there's no results to be extracted.")

      if "next" in results.get("serpapi_pagination", {}):
              search.params_dict.update(dict(parse_qsl(urlsplit(results["serpapi_pagination"]["next"]).query)))
      else:
          break

  unique_local_place_results = pd.DataFrame(local_place_results).astype(str).drop_duplicates().to_dict("records")
  print("le nombre d'agence bancire scrapé est :",len(unique_local_place_results))

  with open("data/banks1.json", "w", encoding="utf-8") as json_file:
    json.dump(unique_local_place_results, json_file, indent=4, ensure_ascii=False)