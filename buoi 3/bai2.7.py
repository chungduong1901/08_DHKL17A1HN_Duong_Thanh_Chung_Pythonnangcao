import json
data = {
    "ten": "A",
    "tuoi": 35,
    "congty": "Đất Việt"
}

json_string = json.dumps(data, ensure_ascii=False)
print(json_string)
print(type(json_string))