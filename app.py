from flask import Flask, request, jsonify
import handlers.passages as passages_handler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/passages', methods=['GET', 'POST'])
def passages():
    if request.method == 'GET':
        return jsonify(passages_handler.index())


if __name__ == '__main__':
    app.run()
