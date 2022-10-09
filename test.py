import requests
from bs4 import BeautifulSoup
import pandas as pd



headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.2.1495 Yowser/2.5 Safari/537.36"
    }
"""
Основная функция для парсинга сайта
"""
def get(article, index):
    #print(f'Заходи в get article is {article}')
    # Парсим заголовки

    article_title = article.find('a', class_="list-item__title color-font-hover-only").text  # .strip()
    articles_href = article.find('a', class_='list-item__image', href=True)['href']


    # Извлекаем текст из новости
    href_req = requests.get(url=articles_href, headers=headers)
    soup = BeautifulSoup(href_req.text, "lxml")
    text_news = soup.find_all("div", class_="article__text")
    text = ''

    for elem in text_news:
        text += '\n' + elem.text

    news_dict = {
        "article_title": article_title,
        "article_text": text,
        "article_url": articles_href
    }

    df = pd.DataFrame(news_dict, index=[index])

    return df





"""
Основная функция для создания датасета
"""
def key_word(key):


    url = f"https://ria.ru/search/?query={key}"

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("div", class_="list-item")

    index = 0
    output = pd.DataFrame()



    # основной цикл парсера
    for article in articles_cards:
        output = output.append(get(article, index), ignore_index=True)
        index += 1

    output.to_csv(f'news_today_{key}_.csv', index=False)