import requests
from bs4 import BeautifulSoup
import json


def get_first_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.2.1495 Yowser/2.5 Safari/537.36"
    }
    url = "https://ria.ru"

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("articles_cards_tag", class_="articles_cards_class")

    news_dict = {}

    for article in articles_cards:
        article_title = article.find("article_title_tag", class_="article_title_class").text.strip()
        article_url = f'{article.get("article_url")}'
        article_date_time = article.find("article_date_time_tag", class_="article_date_time_class")
        article_id = article_url.split("/")[-1]
        article_id = article_id[:article_id]
        # print(f"{article_title} | {article_url} | {article_date_time}")

        news_dict[article_id] = {
            "article_date_time": article_date_time,
            "article_titel": article_title,
            "article_url": article_url
        }
        print(article)
        with open("news_dict.json", "w") as file:
            json.dump(news_dict, file, indent=4, ensure_ascii=False)
            print("Создание json файла")


def check_news_update():
    with open("news_dict.json", "w") as file:
        news_dict = json.load(file)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.2.1495 Yowser/2.5 Safari/537.36"
        }

        url = "https://ria.ru/"
        r = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")
        articles_cards = soup.find_all("a", class_="cell-list__item-link color-font-hover-only")

        for article in articles_cards:
            article_title = article.find("article_title_tag", class_="article_title_class").text.strip()
            article_url = f'{article.get("article_url")}'
            article_date_time = article.find("article_date_time_tag", class_="article_date_time_class")

            article_id = article_url.split("/")[-1]
            article_id = article_id[:article_id]

            if article_id in news_dict:
                continue
            else:
                article_title = article.find("article_title_tag", class_="article_title_class").text.strip()
                article_url = f'{article.get("article_url")}'
                article_date_time = article.find("article_date_time_tag", class_="article_date_time_class")
                news_dict[article_id] = {
                    "article_date_time": article_date_time,
                    "article_titel": article_title,
                    "article_url": article_url
                }



