import sys
from pathlib import Path
from pprint import pprint

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from utils.ai_assistant import get_ai_runtime_status
from utils.kis_client import get_runtime_status


def main() -> None:
    print("[KIS]")
    pprint(get_runtime_status())

    print("\n[OpenAI]")
    pprint(get_ai_runtime_status())


if __name__ == "__main__":
    main()
