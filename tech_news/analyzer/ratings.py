from tech_news.database import find_news


def top_5_categories():
    categories_amount = dict()

    for new in find_news():
        category = new["category"]
        if not categories_amount.get(category):
            categories_amount[category] = 1
        else:
            categories_amount[category] += 1

    alphabet_order = sorted(categories_amount.items(), key=lambda t: t[0])

    numeric_order = sorted(alphabet_order, key=lambda t: t[1], reverse=True)

    return [category for category, _ in numeric_order]
