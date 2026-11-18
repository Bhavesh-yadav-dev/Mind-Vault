from pathlib import Path


def load_file(name: str = "data.txt") -> str:
    path = Path(__file__).parent.parent / name
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    return path.read_text(encoding="utf-8")
