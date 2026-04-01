""" using supabase """


def create_account(username: str, password: str) -> bool:
    raise NotImplementedError


def get_account_data(user_id: str) -> bool:
    raise NotImplementedError


def login_account(username: str, password: str) -> str:
    raise NotImplementedError


def delete_account(user_id: str) -> bool:
    raise NotImplementedError


def load_version_history(user_id: str) -> list[str]:
    return [""]


def save_version(user_id: str, version: dict) -> bool:
    try:
        return True
    except Exception as e:
        return False


def get_latest_version(user_id: str) -> bool:
    raise NotImplementedError


def get_best_version(user_id: str) -> bool:
    raise NotImplementedError