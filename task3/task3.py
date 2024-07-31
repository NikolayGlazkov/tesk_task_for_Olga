"""На вход в качестве аргументов программы поступают три пути к файлу (в приложении к заданию находятся примеры этих файлов):
● values.json содержит результаты прохождения тестов с уникальными id
● tests.json содержит структуру для построения отчета на основе прошедших
тестов (вложенность может быть большей, чем в примере) 
● report.json - сюда записывается результат.
Напишите программу, которая формирует файл report.json с заполненными полями value 
для структуры tests.json на основании values.json.
Структура report.json такая же, как у tests.json, только заполнены поля “value”."""

import json
from collections import OrderedDict

def merge_to_json(filename1,filename2):
    pass

# функция для данных из value
def get_json_values_data(filename):
    with open(filename, 'r') as file:
        data = file.read()
        person_dict = json.loads(data)
        return person_dict 

def extract_ids(data, key='id'):
    ids = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                ids.append(v)
            else:
                ids.extend(extract_ids(v, key))
    elif isinstance(data, list):
        for item in data:
            ids.extend(extract_ids(item, key))
    return ids

# функция для данных из tests
def find_by_id(data, target_id):
    # Проверяем, является ли текущий элемент словарем
    if isinstance(data, dict):
        # Проверяем, есть ли у текущего словаря ключ 'id' и совпадает ли значение с искомым id
        if data.get('id') == target_id:
            return data
        # Проверяем значения всех ключей текущего словаря
        for key in data:
            result = find_by_id(data[key], target_id)
            if result:
                return result
    # Проверяем, является ли текущий элемент списком
    elif isinstance(data, list):
        # Проходим по каждому элементу списка
        for item in data:
            result = find_by_id(item, target_id)
            if result:
                return result
    # Если текущий элемент ни словарь, ни список, возвращаем None
    return None



target_id = 5321 # id для теста
result = find_by_id(get_json_values_data("tests.json"), target_id)




for i in extract_ids(get_json_values_data('values.json')):
    result = find_by_id(get_json_values_data("tests.json"), i)
    print(f"id = {i}, title = {result["title"]}")