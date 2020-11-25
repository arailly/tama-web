from typing import List, Dict
import os
import datetime
import pandas as pd
from lib.mapmatching.TAMA.main import MapMatching
from copy import copy, deepcopy


passage_dir = 'data/passages'
trajectory_dir = 'data/trajectories'


def get_now_str():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d-%H-%M-%S')


def get_passage_files():
    return os.listdir(passage_dir)


def upload_passage_file(file):
    save_name = f'passage-{get_now_str()}.csv'
    save_path = f'{passage_dir}/{save_name}'
    file.save(save_path)
    return save_name


def get_trajectory_files():
    return os.listdir(trajectory_dir)


def get_new_trajectory_path():
    save_name = f'trajectory-{get_now_str()}.csv'
    save_path = f'{trajectory_dir}/{save_name}'
    return save_path


def upload_trajectory_file(file):
    save_name = f'trajectory-{get_now_str()}.csv'
    save_path = f'{trajectory_dir}/{save_name}'
    file.save(save_path)
    return save_name


class Data:
    def __init__(self):
        self.df = None
        self.path = ''

    def load(self, path: str, **kwargs):
        self.path = path
        self.df = pd.read_csv(path, **kwargs)

    def to_dict(self, orient='dict'):
        return self.df.to_dict(orient=orient)

    def save(self, path):
        self.df.to_csv(path, index=False)


class Passage(Data):
    def __init__(self):
        super().__init__()
        self.filename = ''

    def load(self, file: str, **kwargs):
        self.filename = file
        super(Passage, self).load(f'{passage_dir}/{file}')


class Trajectory(Data):
    def __init__(self):
        super().__init__()
        self.filename = ''

    def load(self, file: str, **kwargs):
        self.filename = file
        super(Trajectory, self).load(f'{trajectory_dir}/{file}')


def map_matching(passage: Passage, trajectory: Trajectory) -> Trajectory:
    # convert passage coordinate
    passage_dict = passage.to_dict('list')
    links = list(map(
        lambda x: [x[0:2], x[2:4]],
        zip(
            passage_dict['xbegin'],
            passage_dict['ybegin'],
            passage_dict['xend'],
            passage_dict['yend'],
        )
    ))

    # convert trajectory coordinate
    trajectory_dict = trajectory.to_dict('list')
    m = MapMatching(
        x=trajectory_dict['x'],
        y=trajectory_dict['y'],
        links=links
    )

    res = m.point_to_curve()

    # convert map matching result into Trajectory class
    xs = list(map(lambda x: x[0], res))
    ys = list(map(lambda x: x[1], res))

    modified = deepcopy(trajectory)
    modified.df.x = xs
    modified.df.y = ys

    return modified
