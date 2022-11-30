import json
import os

from list_methods import arr_num, arr_words, mixed_arr
from dict_methods import person, values, keys


def convert_list_to_json(var):
    x = json.dumps(var)
    return x


def convert_dict_to_json(var):
    x = json.dumps(var)
    return x


def convert_dict_to_json_indent(var, ind):
    x = json.dumps(var, indent=ind)
    return x


def convert_dict_to_json_separator(var, sep):
    x = json.dumps(var, separators=sep)
    return x


def convert_dict_to_json_order(var):
    x = json.dumps(var, sort_keys=True)
    return x


def convert_from_json(var):
    y = json.loads(var)
    return y


def open_file_to_read(file):
    f = open(file)
    print(f.read())
    f.close()


def open_file_to_read_chars(file, num):
    f = open(file)
    print(f.read(num))
    f.close()


def open_file_readline(file):
    f = open(file)
    print(f.readline())
    f.close()


def open_file_2_readline(file):
    f = open(file)
    print(f.readline())
    print(f.readline())
    f.close()


def open_file_loop_lines(file):
    f = open(file)
    for line in f:
        print(line)
    f.close()


def append_line_to_file(file, line):
    f = open(file, 'a')
    f.write(line)
    f.close()
    f = open(file)
    print(f.read())
    f.close()

def overwrite_file(file, text):
    f = open(file, 'w')
    f.write(text)
    f.close()
    f = open(file)
    print(f.read())
    f.close()

def create_open_file(filename, text):
    f = open(filename, 'x')
    f.write(text)
    f.close()
    f = open(filename)
    print(f.read())
    f.close()


def delete_file(file):
    os.remove(file)


v = delete_file('new_file.txt')
print(v)
