import json

json_data = '{"name":"Hasan", "age": 20}'
print(type(json_data))

load_json_data = json.loads(json_data)

print(type(load_json_data))

print(load_json_data["name"])


dump_json = {
    "country": "Bangladesh",
    "city": "Dhaka"
}

dumps = json.dumps(dump_json)

print(dumps)
