import requests
import time


def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent", "Fake user-agent"},
            timeout=3,
        )
        response.raise_for_status()
        return response.text
    except (requests.HTTPError, requests.Timeout):
        return None
    finally:
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
