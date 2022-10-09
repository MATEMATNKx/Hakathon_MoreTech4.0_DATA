from enum import Enum
from pydantic import BaseModel, Field


class Item(BaseModel):

    req: str = Field(
        'бизнес',
        description='Ключевая фраза по которой будут парситься новости'
    )