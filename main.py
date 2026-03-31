from flask import Flask, render_template
from flask_cors import CORS
from helpers.n8n_handler import is_n8n_flow_online, test_prompt

app = Flask(__name__)
CORS(app)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/n8n-is-online')
def n8n_is_online():
    return is_n8n_flow_online()

@app.route('/test-prompt')
def test_prompt():
    return test_prompt()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)