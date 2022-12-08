# os and sys modules for python
import os


def get_current_working_directory():
    return os.getcwd()


def change_current_working_directory(path):
    os.chdir(path)
    return os.getcwd()


def create_directory(path):
    os.mkdir(path)


def create_intermediate_directories(path):
    os.makedirs(path)


def print_files_and_dirs():
    return os.listdir()


def print_files_and_dir_in_path(path):
    return os.listdir(path)


def remove_file(path):
    os.remove(path)


def remove_directory(path):
    os.rmdir(path)


def get_name_of_operating_system():
    return os.name


def check_if_exists(file):
    return os.path.exists(file)


def get_size_of_file(file):
    return os.path.getsize(file)


def get_basename(path):
    return os.path.basename(path)

def get_dirname(path):
    return os.path.dirname(path)

def chech_if_path_absolute(path):
    return os.path.isabs(path)


def check_if_path_exists(path):
    return os.path.isdir(path)


def check_if_file_exists(path):
    return os.path.isfile(path)

def normalize_path(path):
    return os.path.normpath(path)

def split_path(path):
    return os.path.split(path)

x = split_path('/home/saek/projects/SCz_1k_funcs/count_funcs.py')
print(x)
