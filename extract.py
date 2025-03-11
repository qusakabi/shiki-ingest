import requests

def fetch_anime():
    """
    Fetches data about popular anime from the Shikimori API.

    Uses the Shikimori API to retrieve a list of anime sorted by popularity.
    By default, it returns 20 anime.

    Returns:
        list: A list of dictionaries containing anime data. Each dictionary includes
              information such as ID, title, rating, number of episodes, and status.
              In case of a request error, an empty list is returned.

    Raises:
        requests.exceptions.RequestException: Logs an error if the API request fails.
    """
    url = "https://shikimori.one/api/animes"
    params = {
        "limit": 20,
        "order": "popularity"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Referer": "https://shikimori.one/",
        "Accept": "application/json",
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return []
