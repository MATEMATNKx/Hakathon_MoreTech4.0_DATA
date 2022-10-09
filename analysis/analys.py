import pandas as pd
import json
from schemas.schemas import Result
import numpy as np
import matplotlib.pyplot as plt
import os


def get_news(key):
    df = pd.read_csv(f'news_today_{key}_.csv')
    result = df.to_json(orient="index")
    parsed = json.loads(result)

    #return json.dumps(parsed, indent=4)
    return Result(title = df.iloc[0,0], text = df.iloc[0,1])#value = output.tolist()[0])


