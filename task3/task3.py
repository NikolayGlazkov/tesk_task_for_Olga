import json

def convert_to_json_format(data):
    values_list = [{"id": key, "value": value} for key, value in data.items()]
    return {"values": values_list}

def write_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    print(f"Данные успешно записаны в {filename}")

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
    if isinstance(data, dict):
        if data.get('id') == target_id:
            return data
        for key in data:
            result = find_by_id(data[key], target_id)
            if result:
                return result


    elif isinstance(data, list):
        for item in data:
            result = find_by_id(item, target_id)
            if result:
                return result
    return None





my_dict = {}
file_value = input(f"get my file name of values.json ")
file_test = input(f"get my file name of tests.json ")
for i in extract_ids(get_json_values_data(file_value)):
    result = find_by_id(get_json_values_data(file_test), i)
   
    my_dict[i] = result["title"]


formatted_data = convert_to_json_format(my_dict)
output_filename = input(f"get my file name of 'output.json' ")
write_json_file(output_filename, formatted_data)