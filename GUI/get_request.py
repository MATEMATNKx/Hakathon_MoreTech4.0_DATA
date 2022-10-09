import requests
from schemas_req import Item
from Enum import URLS


#функция для запроса новостей в приложение
def get_news_by_key(key_word):
    #key_word = 'Бизнес'
    user = Item(req = f'{key_word}')
    response = requests.put(
        URLS.BASE_URL.value,
        json= dict(user),
    )

    return response.json()


