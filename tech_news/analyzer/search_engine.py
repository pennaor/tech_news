from datetime import date
from tech_news.database import search_news


def build_search_results(news):
    return [(new["title"], new["url"]) for new in news]


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)
    return build_search_results(news)


def search_by_date(iso_date):
    try:
        timestamp = date.fromisoformat(iso_date)
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": timestamp.strftime("%d/%m/%Y")}
    news = search_news(query)
    return build_search_results(news)


def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news = search_news(query)
    return build_search_results(news)
