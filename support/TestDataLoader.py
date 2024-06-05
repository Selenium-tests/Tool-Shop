import json
from support.FileNames import FileNames
from support.JSONKeys import JSONKeys


def load_test_data(file_name, key):
    with open(f'../testdata/{file_name}', 'r') as f:
        data = json.load(f)
    return data[key]


def load_main_menu_testdata():
    source = load_test_data(FileNames.LINKS, JSONKeys.MAIN_MENU)
    return [(item['init_url'], item['partial_selector'], item['expected_url']) for item in source]


def load_dropdown_list_testdata(key):
    source = load_test_data(FileNames.LINKS, key)
    return [(item['item_partial_selector'], item['expected_url']) for item in source]


def load_array(file_name, key):
    return load_test_data(file_name, key)