import json
from operator import truediv

# Загрузка JSON (парсинг)
json_data = '{"name": "Ivan", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data['name'])

# Сохранение JSON (сериализация)
data = {
    'name': 'Maria',
    'age': 25,
    'is_student': True
}
json_string = json.dumps(data, indent=4)  # Преобразуем Python-объект в JSON-строку
print(json_string)

# Чтение JSON из файла
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  # Загружаем JSON из файла
    print(data)

# Запись JSON d файл
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # Сохраняем JSON в файл