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

    return jsonify({"response": val})


@app.route('/versions', methods=['GET', 'POST'])
def api_load_versions() -> Response:
    return jsonify({"response": load_version_history("")})


@app.route('/save-version', methods=['POST'])
def api_save_version() -> Response:
    data = request.data.decode('utf-8')

    return jsonify({"response": save_version("", "", "")})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)