from datetime import date
from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(new["title"], new["url"]) for new in search_news(query)]


def search_by_date(iso_date):
    try:
        timestamp = date.fromisoformat(iso_date)
    except ValueError:
        raise ValueError("Data inválida")
    query = {"timestamp": timestamp.strftime("%d/%m/%Y")}
    return [(new["title"], new["url"]) for new in search_news(query)]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
