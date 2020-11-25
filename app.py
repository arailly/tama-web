import os
from flask import Flask, request, jsonify, render_template, send_file
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
    # load passage
    passage = h.Passage()
    passage_file = request.args.get('passage')
    passage.load(passage_file)

    # load trajectory
    trajectory = h.Trajectory()
    trajectory_file = request.args.get('trajectory')
    trajectory.load(trajectory_file)

    # map matching
    modified = h.map_matching(passage, trajectory)
    save_name = trajectory.path.replace('trajectories', 'modified')
    modified.save(save_name)

    return render_template(
        'result.html',
        passage=passage.to_dict('index'),
        trajectory=trajectory.to_dict('index'),
        modified=modified.to_dict('index')
    )


@app.route('/api/passages', methods=['GET', 'POST'])
def api_passages():
    if request.method == 'GET':
        return jsonify({
            'files': h.get_passage_files()
        })

    elif request.method == 'POST':
        f = request.files['passage']
        h.upload_passage_file(f)
        return jsonify({
            'message': 'success'
        })


@app.route('/api/trajectories', methods=['GET', 'POST'])
def api_trajectories():
    if request.method == 'GET':
        return jsonify({
            'files': h.get_trajectory_files()
        })

    elif request.method == 'POST':
        try:
            trajectory = request.json['trajectory']
            path = h.get_new_trajectory_path()

            with open(path, 'w') as f:
                f.write(trajectory)

            return jsonify({
                'message': 'success'
            })

        except Exception as e:
            return jsonify({
                'message': e
            }), 400


@app.route('/data/<path:path>')
def download_data(path):
    return send_file(
        filename_or_fp=f'data/{path}',
        mimetype='text/plain',
        as_attachment=True,
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
