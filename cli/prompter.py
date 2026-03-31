import sys
import subprocess


def usage() -> str:
    return f"""Usage: {sys.argv[0]}"""


def start_localhost():
    p = subprocess.run(["python", "-m", "flask", "run", "../main.py"])

    return f"Visit -> http://localhost:5000/ to test your prompt. {p.returncode}"


def execution(params: list) -> int:
    return 0

def main():
    if len(sys.argv) < 2:
        return usage()
    elif len(sys.argv) == 2:
        match sys.argv[1]:
            case "test":
                return start_localhost()

    return execution(sys.argv[1:])


if __name__ == "__main__":
    print(main())