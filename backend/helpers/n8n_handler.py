from pathlib import Path

import requests as re
from dotenv import load_dotenv

import os

load_dotenv(dotenv_path=Path(__file__).parent / ".env")


def test_prompt(prompt: str):
    payload = {"prompt": prompt}

    call = re.post(os.getenv('TEST_PROMPT') or '', json=payload)

    return call.json()