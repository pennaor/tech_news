import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    page = Selector(text=html_content)
    links = page.css("a.cs-overlay-link::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    page = Selector(text=html_content)
    link = page.css("a.next.page-numbers::attr(href)").get()
    return link


# Requisito 4
def scrape_news(html_content):
    new = dict()
    page = Selector(text=html_content)

    new["url"] = page.css("link[rel*=canonical]::attr(href)").get(default="")

    new["timestamp"] = page.css("li.meta-date::text").get(default="")

    new["writer"] = page.css("span.author a.url.fn.n::text").get(default="")

    new["category"] = page.css("a.category-style span.label::text").get()

    reading_time_text = page.css("li.meta-reading-time::text").get(default="0")
    new["reading_time"] = int(reading_time_text.split()[0])

    raw_title = page.css("h1.entry-title::text").get(default="")
    new["title"] = raw_title.replace("\xa0", "").strip()

    paragraph_element = page.css("div.entry-content p")[0]
    paragraph_substrings = paragraph_element.css("*::text").getall()
    unstriped_summary = ""
    for substring in paragraph_substrings:
        unstriped_summary += substring.replace("\xa0", "")
    new["summary"] = unstriped_summary.strip()

    return new


# Requisito 5
def get_tech_news(amount):
    URL = "https://blog.betrybe.com"
    news = []

    while URL:
        news_page = fetch(URL)
        news_links = scrape_updates(news_page)
        URL = scrape_next_page_link(news_page)
        for link in news_links:
            if len(news) >= amount:
                URL = ""
                break
            new_page = fetch(link)
            new = scrape_news(new_page)
            news.append(new)

    create_news(news)
    return news
