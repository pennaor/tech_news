import pytest
from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501

mocked_news = [
    {
        "_id": {
            "$oid": "1"
        },
        "title": "Não deixe para depois: Python é a linguagem mais quente",
        "reading_time": 4,
        "url": "",
        "writer": "",
        "summary": "",
        "timestamp": "",
        "category": ""
    },
    {
        "_id": {
            "$oid": "2"
        },
        "title": "Selenium, BeautifulSoup ou Parsel? Entenda as diferenças",
        "reading_time": 3,
        "url": "",
        "writer": "",
        "summary": "",
        "timestamp": "",
        "category": ""
    },
    {
        "_id": {
            "$oid": "3"
        },
        "title": "Pytest + Faker: a combinação poderosa dos testes!",
        "reading_time": 10,
        "url": "",
        "writer": "",
        "summary": "",
        "timestamp": "",
        "category": ""
    },
    {
        "_id": {
            "$oid": "4"
        },
        "title": "FastAPI e Flask: frameworks para APIs em Python",
        "reading_time": 15,
        "url": "",
        "writer": "",
        "summary": "",
        "timestamp": "",
        "category": ""
    },
    {
        "_id": {
            "$oid": "5"
        },
        "title": "A biblioteca Pandas e o sucesso da linguagem Python",
        "reading_time": 12,
        "url": "",
        "writer": "",
        "summary": "",
        "timestamp": "",
        "category": ""
    },
]

expected_result = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "Não deixe para depois: Python é a linguagem mais quente",
                    4,
                ),
                (
                    "Selenium, BeautifulSoup ou Parsel? Entenda as diferenças",
                    3,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "Pytest + Faker: a combinação poderosa dos testes!",
                    10,
                )
            ],
        },
    ],
    "unreadable": [
        ("FastAPI e Flask: frameworks para APIs em Python", 15),
        ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
    ],
}


def test_reading_plan_group_news():
    with pytest.raises(
        ValueError,
        match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)

    with patch.object(ReadingPlanService, '_db_news_proxy') as db_news_proxy:
        db_news_proxy.return_value = mocked_news
        result = ReadingPlanService.group_news_for_available_time(10)
        assert result == expected_result
