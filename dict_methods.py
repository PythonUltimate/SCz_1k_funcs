## dict methods
from random import random

person = {
    'name': 'rysiek',
    'age': 56,
    'job': 'plumber',
    'married': True,
    'kids': 3,
    'happy': False
}

other_dict = {
    'elo': 'tam',
    'kasia': 'masia'
}

keys = ('band', 'album', 'single', 'price')
values_0 = 0
values = ('siekiera', 'nowa aleksandria', 'ludzie wschodu', 90)


def clear_dict(dict):
    dict.clear()
    return dict


def copy_dict(dict):
    new_dict = dict.copy()
    return new_dict


def create_empty_dict(keys):
    new_dict = dict.fromkeys(keys)
    return new_dict


def create_dict_with_0_vals(keys, values):
    new_dict = dict.fromkeys(keys, values)
    return new_dict


def create_dict_with_new_values(keys, values):
    new_dict = dict.fromkeys(keys, values)
    return new_dict


def get_value_from_dict(dict, value):
    return dict.get(value)


def get_value_from_dict_with_default(dict, value, default):
    return dict.get(value, default)


def get_dict_items(dict):
    return dict.items()


def get_dict_keys(dict):
    return dict.keys()


def get_dict_values(dict):
    return dict.values()


def pop_item_from_dict(dict, item):
    dict.pop(item)
    return dict


def pop_item_from_dict_default_value(dict, item, default):
    return dict.pop(item, default)


def pop_last_item(dict):
    return dict.popitem()


def set_default_value(dict, key, value):
    dict.setdefault(key, value)
    return dict


def update_dict(dict, other_dict):
    dict.update(other_dict)
    return dict


def make_list_from_keys(dict):
    return list(dict.keys())


def make_list_from_values(dict):
    return list(dict.values())


def make_list_from_items(dict):
    return list(dict.items())


def get_len_of_dict(dict):
    return len(dict)


def add_items_to_dict(dict, key, value):
    dict[key] = value
    return dict


def get_one_value(dict, key):
    return dict[key]


def change_value(dict, key, value):
    dict.update({key: value})
    return dict


def change_value_2(dict, key, value):
    dict[key] = value
    return dict


def delete_key_value(dict, key):
    del dict[key]
    return dict


def make_all_values_upper(dict):
    for key, value in dict.items():
        if isinstance(value, str):
            dict[key] = value.upper()
    return dict


def make_all_values_capitalized(dict):
    for key, value in dict.items():
        if isinstance(value, str):
            dict[key] = value.capitalize()
    return dict


def map_values_to_upper(dict):
    return {key: value.upper() for key, value in dict.items() if isinstance(value, str)}


def map_all_integers(dict):
    return {key: value for key, value in dict.items() if isinstance(value, int)}


def change_age_to_old(dict):
    return {key: ('old' if value > 40 else 'young') for key, value in dict.items() if isinstance(value, int)}


def generate_dict_from_range(num):
    return {key: None for key in range(num)}


def generate_dict_with_string_values(amount):
    return {key: 'elo' for key in range(amount)}


def generate_dict_with_powers(amount):
    return {key: key ** 2 for key in range(amount)}


d = generate_dict_with_powers(10)

print(d)

# filter, map
