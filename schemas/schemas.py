from enum import Enum
from pydantic import BaseModel, Field


class Item(BaseModel):

    req: str = Field(
        ...,
        description='Ключевая фраза по которой будут парситься новости'
    )

class Result(BaseModel):
    title: str = Field(
        ...,
        description='Заголовок'
    )
    text: str = Field(
        ...,
        description='текст'
    )