import requests as re

def is_n8n_flow_online():
    call = re.get("https://reflexshop.app.n8n.cloud/webhook-test/api/up")

    response = call.json()

    return dict(response).get("status") == 'up'


def test_prompt():
    pass