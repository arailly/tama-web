import os


def index(passage_dir: str) -> dict:
    return {
        'files': os.listdir(passage_dir)
    }
