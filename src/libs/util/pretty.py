import json
from typing import Dict


def pretty(js: Dict) -> str:
    return json.dumps(js, indent=2)
