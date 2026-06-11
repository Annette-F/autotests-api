from jsonschema import validate, ValidationError


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

data = {
    'name': 'Mark',
    'age': 25
}

try:
    validate(instance=data, schema=schema)
    print('Данные соответствуют схеме.')
except ValidationError as e:
    print(f'Ошибка валидации {e.message}.')
