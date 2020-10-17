import os
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/passages', methods=['GET', 'POST'])
def passages():
    passage_dir = 'data/passages'

    if request.method == 'GET':
        files = os.listdir(passage_dir)
        return jsonify({
            'files': files
        })

    elif request.method == 'POST':
        f = request.files['passage_file']
        save_path = f'{passage_dir}/passage-{get_now_str()}.csv'
        f.save(save_path)
        return 'success'


@app.route('/api/trajectories', methods=['GET', 'POST'])
def trajectories():
    trajectory_dir = 'data/trajectories'

    if request.method == 'GET':
        files = os.listdir(trajectory_dir)
        return jsonify({
            'files': files
        })

    elif request.method == 'POST':
        f = request.files['trajectory_file']
        save_path = f'{trajectory_dir}/trajectory-{get_now_str()}.csv'
        f.save(save_path)
        return 'success'


def get_now_str():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d-%H-%M-%S')


if __name__ == '__main__':
    app.run()
