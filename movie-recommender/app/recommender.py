import requests
import certifi
import os

os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxMWM1ZTk0Yjg1ZGVmYTM4NmY0Yjc4MmViMGViOTJmZiIsIm5iZiI6MTU1NzIyMzc5My41MjksInN1YiI6IjVjZDE1OTcxMGUwYTI2MmZiMzA5ZTE4NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iWmoAF5FIpGxGrNyphM34ZZ0sXYHWwp0EnAQbFZuW0I"  # Replace this with your actual token
BASE_URL = "https://api.themoviedb.org/3"

HEADERS = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "accept": "application/json"
}

def fetch_movies(start_year, end_year):
    all_movies = []
    for year in range(start_year, end_year + 1):
        print(f"Fetching movies from year: {year}")
        page = 1
        while True:
            print(f"  Requesting page {page}...")
            response = requests.get(
                f"{BASE_URL}/discover/movie",
                headers=HEADERS,
                params={
                    "language": "en-US",
                    "sort_by": "popularity.desc",
                    "primary_release_year": year,
                    "page": page
                }
            )
            if response.status_code != 200:
                print(f"  Failed: Year {year}, Page {page}, Status {response.status_code}")
                break

            data = response.json()
            results = data.get('results', [])
            if not results:
                print(f"  No more results for year {year} at page {page}")
                break

            print(f"  Fetched {len(results)} movies from page {page}")
            all_movies.extend(results)
            page += 1

            if page > data.get('total_pages', 1):
                break
    print(f"Fetched a total of {len(all_movies)} movies.")
    return all_movies

# Usage example:
movies = fetch_movies(1990, 1990)

# If you want a DataFrame:
import pandas as pd
df = pd.DataFrame(movies)
print(df.head())
print(f"Total movies fetched: {len(df)}")

# Save to CSV file
df.to_csv("movies_1990_1990.csv", index=False)
print("Saved movies to movies_1990_1990.csv")
