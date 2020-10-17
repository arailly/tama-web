from typing import List, Dict
import datetime
import pandas as pd


def get_now_str():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d-%H-%M-%S')


class Passage:
    def __init__(self):
        self.df = None

    def load(self, path: str, **kwargs):
        self.df = pd.read_csv(path, **kwargs)

    def to_json(self) -> List[Dict]:
        return self.df.to_dict(orient='index')
