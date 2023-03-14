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

expected = {
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


@patch.object(ReadingPlanService, '_db_news_proxy', return_value=mocked_news)
def test_reading_plan_group_news(_mock):
    with pytest.raises(
        ValueError,
        match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-1)

    result = ReadingPlanService.group_news_for_available_time(10)
    # assert len(result) == 2

    # readable = result.get("readable")
    # assert type(readable) == list
    # assert len(readable) == 2
    # assert type(readable[0]) == dict
    # assert type(readable[1]) == dict
    # assert len(readable[0]) == 2
    # assert len(readable[1]) == 2

    # chosen_news_readble_0 = readable[0].get("chosen_news")
    # assert type(chosen_news_readble_0) == list

    # unfilled_time_readable_0 = readable[0].get("unfilled_time")
    # assert unfilled_time_readable_0 == 3
    # unfilled_time_readable_1 = readable[1].get("unfilled_time")
    # assert unfilled_time_readable_1 == 0

    # unreadable = result.get("unreadable")
    # assert type(unreadable) == list
    # assert len(unreadable) == 2
    # assert type(unreadable[0]) == tuple
    # assert type(unreadable[1]) == tuple
    # assert len(unreadable[0]) == 2
    # assert len(unreadable[1]) == 2

    assert result == expected
