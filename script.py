import os
import json
import jsonschema
from jsonschema import validate


def getFiles():
    files_list = os.listdir(path='task_folder/event')
    for file_name in files_list:
        print(file_name)
        file = open(f'task_folder/event/{file_name}', 'r')
        schemaChoice(file)


def schemaChoice(file):
    data = json.load(fp=file)
    try:
        schema_file = open(f"task_folder/schema/{data.get('event')}.schema", 'r')
        schema = json.load(schema_file)
        validateJson(data, schema)
    except AttributeError:
        print('Не указана схема для валидации')
    except FileNotFoundError:
        print(f"Нет схемы с названием {data.get('event')}")


def validateJson(data, schema):
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return print(f'Найдены ошибки: {err.message}')
    return ('JSON файл валиден')


if __name__ == '__main__':
    getFiles()