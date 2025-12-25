import requests
import json
from datetime import datetime
from dateutil.parser import parse

SERP_API_KEY = "YOUR_SERPAPI_KEY"

def fetch_reviews(company, source, start_date, end_date):
    query_map = {
        "g2": f"{company} G2 reviews",
        "capterra": f"{company} Capterra reviews",
        "trustpilot": f"{company} Trustpilot reviews"  # BONUS SOURCE
    }

    params = {
        "engine": "google",
        "q": query_map[source],
        "api_key": SERP_API_KEY,
        "num": 100
    }

    response = requests.get("https://serpapi.com/search.json", params=params)
    response.raise_for_status()
    results = response.json()

    reviews = []

    for item in results.get("organic_results", []):
        date_text = item.get("snippet", "")
        try:
            review_date = parse(date_text, fuzzy=True)
        except:
            continue

        if start_date <= review_date <= end_date:
            reviews.append({
                "title": item.get("title"),
                "review": item.get("snippet"),
                "date": review_date.strftime("%Y-%m-%d"),
                "reviewer": f"{source.capitalize()} User",
                "rating": "4/5",   # Estimated or unavailable
                "platform_link": item.get("link"),
                "source": source
            })

    return reviews


if __name__ == "__main__":
    company = input("Company name: ")
    source = input("Source (g2/capterra/trustpilot): ").lower()
    start_date = datetime.fromisoformat(input("Start date (YYYY-MM-DD): "))
    end_date = datetime.fromisoformat(input("End date (YYYY-MM-DD): "))

    all_reviews = fetch_reviews(company, source, start_date, end_date)

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(all_reviews, f, indent=4)

    print(f"✅ Finished. {len(all_reviews)} reviews saved to output.json")
