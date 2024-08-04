import json
import sys

def write_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
    print(f"Данные успешно записаны в {filename}")

def read_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def update_tests_with_values(tests, values):
    values_dict = {item["id"]: item["value"] for item in values["values"]}
    
    def update_recursive(test_item):
        if 'id' in test_item and test_item['id'] in values_dict:
            test_item['value'] = values_dict[test_item['id']]
        if 'values' in test_item:
            for child in test_item['values']:
                update_recursive(child)
    
    for test in tests['tests']:
        update_recursive(test)

def main():
    if len(sys.argv) != 4:
        print("Использование: python3 task3.py values.json tests.json report.json")
        return

    values_filename = sys.argv[1]
    tests_filename = sys.argv[2]
    report_filename = sys.argv[3]

    values = read_json_file(values_filename)
    tests = read_json_file(tests_filename)

    update_tests_with_values(tests, values)

    write_json_file(report_filename, tests)

if __name__ == "__main__":
    main()
