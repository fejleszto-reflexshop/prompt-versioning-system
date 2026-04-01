""" using supabase """


def create_account(username: str, password: str) -> bool:
    pass

def get_account_data(user_id: str) -> bool:
    pass


def login_account(username: str, password: str) -> str:
    pass

def delete_account(user_id: str) -> bool:
    pass


def load_version_history(user_id: str) -> list[str]:
    return [""]


def save_version(user_id: str, version: dict) -> bool:
    try:
        return True
    except Exception as e:
        return False


def get_latest_version(user_id: str) -> bool:
    pass

def get_best_version(user_id: str) -> bool:
    pass