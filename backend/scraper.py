import requests
from bs4 import BeautifulSoup

def scrape_website(domain):
    try:
        url = f"http://{domain}" if not domain.startswith("http") else domain
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        return {
            "url": url,
            "title": soup.title.string if soup.title else "",
            "meta_description": (soup.find("meta", attrs={"name": "description"}) or {}).get("content", ""),
            "h1_tags": [h1.get_text(strip=True) for h1 in soup.find_all("h1")],
            "h2_tags": [h2.get_text(strip=True) for h2 in soup.find_all("h2")],
            "html": response.text
        }

    except Exception as e:
        print(f"❌ Scraper Error: {e}")
        return {}
