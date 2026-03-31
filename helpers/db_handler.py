""" using supabase """


def create_account(username: str, password: str) -> bool:
    pass

def get_account_data(user_id: str) -> bool:
    pass


def login_account(username: str, password: str) -> bool:
    pass


def load_version_history(user_id: str) -> list[str]:
    return [""]


def save_version(user_id: str, version: str, prompt: str) -> bool:
    try:
        return True
    except Exception as e:
        return False