import os
from flask import Flask, request, jsonify, render_template
import helper as h

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           passage_files=h.get_passage_files(),
                           trajectory_files=h.get_trajectory_files())


@app.route('/api')
def api_index():
    return jsonify({
        'message': 'hello world'
    })


@app.route('/result')
def result():
    passage = h.Passage()
    passage_file = request.args.get('passage')
    passage.load(passage_file)
    return render_template(
        'result.html',
        passage=passage.to_json(),
    )


@app.route('/api/passages', methods=['GET', 'POST'])
def api_passages():
    if request.method == 'GET':
        return jsonify({
            'files': h.get_passage_files()
        })

    elif request.method == 'POST':
        f = request.files['passage_file']
        h.upload_passage_file(f)
        return 'success'


@app.route('/api/trajectories', methods=['GET', 'POST'])
def api_trajectories():
    if request.method == 'GET':
        return jsonify({
            'files': h.get_trajectory_files()
        })

    elif request.method == 'POST':
        f = request.files['trajectory_file']
        h.upload_trajectory_file(f)
        return 'success'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
