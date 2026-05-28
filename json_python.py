import json

json_data = """
{
  "name": "Ivan",
  "age": 30,
  "price": 30.55,
  "is_student": true,
  "courses": [
    "Python",
    "API Testing",
    "QA Automation",
    {
      "name": "Alice"
    }
  ],
  "address": {
    "city": "Moscow",
    "zip": "101000"
  }
}
"""

parsed_data = json.loads(json_data)

print(parsed_data, type(parsed_data))
print(parsed_data['name'])
print(parsed_data['courses'])

data = {
    'name': 'Maria',
    'age': 25,
    'is_student': True,
}

json_string = json.dumps(data, indent=4)

print(json_string, type(json_data))

with open("json_example.json", "r", encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data, type(read_data))

with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
