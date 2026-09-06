import json
from pathlib import Path

file_path = Path(__file__).parent / "init_values.json"


with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data)
    print(data["refresh_token"])