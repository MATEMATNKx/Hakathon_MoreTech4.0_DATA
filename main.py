from typing import Union
from fastapi import FastAPI


from analysis.analys import get_news
from test import key_word
from schemas.schemas import Item, Result


app = FastAPI()


@app.get("/")
def read_root():
    return {"Добрый день": "Дайте деняк"}



@app.put("/items/", response_model=Result)
async def update_item(item: Item):
    key_word(item.req)

    news = get_news(item.req)
    print(f'\n\n\n{news}\n\n\n')

    return news