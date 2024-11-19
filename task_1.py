import json

def task() -> float:
    file_path = "input.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    total_sum = 0
    for item in data:
        total_sum += item["score"] * item["weight"]

    return round(total_sum, 3)

print(task())

