import os


def index(passage_path: str) -> dict:
    return {
        'files': os.listdir(passage_path)
    }
