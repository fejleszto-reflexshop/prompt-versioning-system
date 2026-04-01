from flask import Flask, jsonify, request, Response
from flask_cors import CORS

from backend.helpers.n8n_handler import test_prompt

from backend.helpers.db_handler import *

app = Flask(__name__)
CORS(app)

@app.route('/test-prompt', methods=['GET', 'POST'])
def api_test_prompt() -> Response:
    evaluate: dict = test_prompt('prompt for comparing two strings')[0]
    res: dict = evaluate.get('text', {})
    score: float | int = sum([res['scores'][key] for key in res['scores']])

    return jsonify({"response": res, "score": score})


@app.route('/new-acc', methods=['POST'])
def api_new_acc() -> Response:
    username: str = str(request.args.get('username'))
    password: str = str(request.args.get('password'))

    val: bool = create_account(username, password)

    return jsonify({"is_created": val})


@app.route('/login', methods=['GET'])
def api_login() -> Response:
    username: str = str(request.args.get('username'))
    password: str = str(request.args.get('password'))

    access_token: str = login_account(username, password)

    return jsonify({"access_token": access_token})


@app.route('/delete-acc', methods=['DELETE'])
def api_delete_acc() -> Response:
    username: str = str(request.args.get('username'))

    val: bool = delete_account(username)

    return jsonify({"is_deleted": val})


@app.route('/versions', methods=['GET'])
def api_load_versions() -> Response:
    user = request.args.get('u') or ""

    return jsonify({"versions": load_version_history(user)})


@app.route('/save-version', methods=['POST'])
def api_save_version() -> Response:
    user = request.args.get('u') or ""

    version: dict = {"v": "", "p": "", "n": "", "s": ""}

    return jsonify({"response": save_version(user, version)})


@app.route('/latest-version', methods=['GET'])
def api_latest_version() -> Response:
    user = request.args.get('u') or ""

    return jsonify({"latest_version": get_latest_version(user)})


@app.route('/best-version', methods=['GET'])
def api_best_version() -> Response:
    user = request.args.get('u') or ""

    return jsonify({"best_version": get_best_version(user)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)