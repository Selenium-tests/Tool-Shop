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


def load_main_menu_dropdown_list_testdata():
    source = load_test_data(FileNames.LINKS, JSONKeys.MAIN_MENU_DROPDOWN_LIST)
    return [(item['partial_selector'], item['expected_url']) for item in source]


def load_credentials_testdata(key):
    source = load_test_data(FileNames.CREDENTIALS, key)
    return [(item['email'], item['password']) for item in source]