import json


def load_test_data(file_name, key):
    f = open(f'../testdata/{file_name}')
    data = json.load(f)
    return data[key]
