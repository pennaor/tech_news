import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_categories


def select_option():
    options = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )
    try:
        option = input(options)
        option = int(option)
        if option < 0 or option > 5:
            raise ValueError
        return option
    except ValueError:
        raise ValueError("Opção inválida")


def search_news_option():
    quantity = input("Digite quantas notícias serão buscadas:\n")
    get_tech_news(quantity)
    return True


def search_by_title_option():
    title = input("Digite o título:\n")
    print(search_by_title(title))
    return True


def search_by_date_option():
    date = input("Digite a data no formato aaaa-mm-dd:\n")
    print(search_by_date(date))
    return True


def search_category_option():
    category = input("Digite a categoria:\n")
    print(search_by_category(category))
    return True


def top_5_categories_option():
    print(top_5_categories())
    return True


def exit_menu():
    print("Encerrando script\n")
    return False


options_funcs = [
    search_news_option,
    search_by_title_option,
    search_by_date_option,
    search_category_option,
    top_5_categories_option,
    exit_menu,
]


def analyzer_menu():
    try:
        run = True
        while run:
            option = select_option()
            func = options_funcs[option]
            run = func()
    except Exception as exception:
        print(exception, file=sys.stderr)
