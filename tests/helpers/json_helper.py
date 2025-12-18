import json
from pathlib import Path
from typing import Any, Dict


def load_json_from_file(filepath: str) -> Dict[str, Any]:
    try:
        base_dir = Path(__file__).resolve().parent.parent
        with open(base_dir / filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"JSON file not found: {filepath}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Malformed JSON {filepath}: {e}")
