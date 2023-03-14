from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(new["title"], new["url"]) for new in search_news(query)]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
