from typing import List, Dict
import os
import datetime
import pandas as pd


passage_dir = 'data/passages'
trajectory_dir = 'data/trajectories'


def get_now_str():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d-%H-%M-%S')


def get_passage_files():
    return os.listdir(passage_dir)


def upload_passage_file(file):
    save_path = f'{passage_dir}/passage-{get_now_str()}.csv'
    file.save(save_path)


def get_trajectory_files():
    return os.listdir(trajectory_dir)


def upload_trajectory_file(file):
    save_path = f'{trajectory_dir}/trajectory-{get_now_str()}.csv'
    file.save(save_path)


class Data:
    def __init__(self):
        self.df = None

    def load(self, path: str, **kwargs):
        self.df = pd.read_csv(path, **kwargs)

    def to_json(self) -> List[Dict]:
        return self.df.to_dict(orient='index')


class Passage(Data):
    def __init__(self):
        super().__init__()

    def load(self, file: str, **kwargs):
        self.load(f'{passage_dir}/{file}')


class Trajectory(Data):
    def __init__(self):
        super().__init__()

    def load(self, file: str, **kwargs):
        self.load(f'{trajectory_dir}/{file}')
