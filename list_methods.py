## List methods in Python

import copy
import math
import random
import statistics
from functools import reduce

arr_num = [23, 87, 4, 70, 5, 9, -32, 87]
arr_words = ['ala', 'wszy', 'kromka', 'nic', 'trelemorele']
mixed_arr = [45, 'panda', 65, 'heja', 2, -9, 'trele', 'scikit']
tup = (1, 4, 'robot', 'elo')


def append_elem_to_list(arr1, elem):
    arr1.append(elem)
    return arr1


def appen_list_to_list(arr1, arr2):
    arr1.append(arr2)
    return arr1


def append_listelems_to_list(arr1, arr2):
    for elem in arr2:
        arr1.append(elem)
    return arr1


def clear_list(arr):
    arr.clear()
    return arr


def copy_list(arr):
    arr2 = arr.copy()
    return arr, arr2


def copy_list_check_id(arr):
    arr2 = arr.copy()
    print(id(arr))
    print(id(arr2))
    return arr2


def deep_copy_list(arr):
    arr2 = copy.deepcopy(arr)
    print(id(arr))
    print(id(arr2))
    return arr


def count_elems_in_list(arr, sign):
    return arr.count(sign)


def count_sign_within_elems(arr, sign):
    counter = 0
    for elem in arr:
        for sign in elem:
            counter += 1
    return counter


def count_if_sign_within_elems(arr, sign):
    counter = 0
    for elem in arr:
        if sign in elem:
            counter += 1
    return counter


def extend_list_with_list(arr1, arr2):
    arr1.extend(arr2)
    return arr1


def extend_list_with_tuple(arr, tuple):
    arr.extend(tuple)
    return arr


def get_index_of_value(arr, value):
    return arr.index(value)


def insert_elem_at_pos(arr, pos, elem):
    arr.insert(pos, elem)
    return arr  # zfill


def get_pop_last_elem(arr):
    return arr.pop()


def get_pop_elem_at_pos(arr, pos):
    return arr.pop(pos)


def remove_value_from_list(arr, value):
    arr.remove(value)
    return (arr)


def reverse_list(arr):
    arr.reverse()
    return arr


def sort_list_asc(arr):
    arr.sort()
    return arr


def sort_list_desc(arr):
    arr.sort(reverse=True)
    return arr


def sort_list_custom(arr):
    arr.sort(key=lambda x: len(x))
    return arr


def sort_list_custom_reverse(arr):
    arr.sort(reverse=True, key=lambda x: len(x))
    return arr


def eliminate_duplicates(arr):
    arr2 = []
    for elem in arr:
        if elem not in arr2:
            arr2.append(elem)
    return arr2


def make_abs_values(arr):
    return [abs(elem) for elem in arr]


def concatenate_list_items(arr):
    sentence = ''
    for elem in arr:
        sentence += elem
    return sentence


def get_sum_list(arr):
    counter = 0
    for elem in arr:
        counter += elem
    return counter


def get_number_of_elems(arr):
    return len(arr) + 1


def get_first_letters(arr):
    return list(map(lambda x: x[0], arr))


def make_all_upper(arr):
    return list(map(lambda x: x.upper(), arr))


def make_all_lower(arr):
    return list(map(lambda x: x.lower(), arr))


def reverse_all_elems(arr):
    return list(map(lambda x: x[::-1], arr))


def capitalize_all_elems(arr):
    return list(map(lambda x: x.capitalize(), arr))


def map_to_length(arr):
    return list(map(lambda x: len(x), arr))


def check_falsy(arr):
    return all(arr)


def join_arr_to_string(arr):
    return " ".join(arr)


def replace_ala(arr):
    return list(map(lambda x: x.replace('ala', 'ola'), arr))


def get_elems_start_a(arr):
    return list(filter(lambda x: bool(x), map(lambda x: x.startswith('a'), arr)))


def zfill_all_elems(arr):
    return list(map(lambda x: x.zfill(10), arr))


def get_positive_values(arr):
    return list(filter(lambda x: x >= 0, arr))


def get_negative_values(arr):
    return list(filter(lambda x: x < 0, arr))


def get_highest_value(arr):
    return max(arr)


def get_highest_val_2(arr):
    value = arr[0]
    for elem in arr[1:]:
        if elem > value:
            value = elem
    return value


def get_lowest_value(arr):
    return min(arr)


def get_lowest_val_2(arr):
    value = arr[0]
    for elem in arr[1:]:
        if elem < value:
            value = elem
    return value


def multiply_all_values(arr):
    return reduce(lambda x, y: x * y, arr)


def sum_all_vals(arr):
    return sum(arr)


def reduce_sum_all_vals(arr):
    return reduce(lambda x, y: x + y, arr)


def square_root_all_vals(arr):
    return list(map(lambda x: math.sqrt(abs(x)), arr))


def log__all_vals(arr):
    return list(map(lambda x: math.log(abs(x)), arr))


def filter_even_nums(arr):
    return list(filter(lambda x: x % 2 == 0, arr))


def filter_odd_nums(arr):
    return list(filter(lambda x: x % 2 != 0, arr))


def multiply_all_by_num(arr, num):
    return list(map(lambda x: x * num, arr))


def divide_all_by_num(arr, num):
    return list(map(lambda x: x / num, arr))


def power_all_to_num(arr, num):
    return list(map(lambda x: x ** num, arr))


def get_all_factorials(arr):
    return list(map(lambda x: math.factorial(abs(x)), arr))


def get_mean_arr(arr):
    return statistics.mean(arr)


def get_hmean_arr(arr):
    return statistics.harmonic_mean(arr)


def get_median_arr(arr):
    return statistics.median(arr)


def get_stdev_arr(arr):
    return statistics.stdev(arr)


def get_var_arr(arr):
    return statistics.variance((arr))


def filter_integers(arr):
    return list(filter(lambda x: isinstance(x, int), arr))


def filter_str(arr):
    return list(filter(lambda x: isinstance(x, str), arr))


def count_vovels(arr):
    counter = 0
    for letter in 'aeiouy':
        for elem in arr:
            counter += elem.count(letter)
    return counter


def count_vovels_2(arr):
    return sum(elem.count(letter) for elem in arr for letter in 'aeiouy')


def count_ints_in_arr(arr):
    return sum(1 for elem in arr if isinstance(elem, int))


def count_str_in_arr(arr):
    return sum(1 for elem in arr if isinstance(elem, str))


def make_all_str(arr):
    return list(map(lambda x: str(x), arr))


def make_all_str_and_concatenate(arr):
    return " ".join(list(map(lambda x: str(x), arr)))


def make_all_str_and_sort(arr):
    return sorted(list(map(lambda x: str(x), arr)))


def make_all_str_and_sort_reverse(arr):
    return sorted(list(map(lambda x: str(x), arr)), reverse=True)


def insert_spaces(arr):
    new_list = []
    for elem in arr:
        word = ''
        for letter in elem:
            letter += ' '
            word += letter
        new_list.append(word)
    return new_list


def eliminate_vovels(arr):
    new_list = []
    for elem in arr:
        word = ''
        for letter in elem:
            if letter in 'aeiouy':
                letter = ''
            word += letter
        new_list.append(word)
    return new_list


def make_only_ints(arr):
    return [elem if isinstance(elem, int) else len(elem) for elem in arr]


def random_choice(arr):
    return random.choice(arr)


def random_choices(arr, num):
    return random.choices(arr, k=num)


def shuffle_list(arr):
    random.shuffle(arr)
    return arr


def generate_random_int_to_list():
    return [random.randint(0, 9) for _ in range(10)]


def generate_custom_int_list(start, stop, num):
    return [random.randint(start, stop + 1) for _ in range(num)]


def get_random_elem(arr):
    return arr.pop(random.randint(0, len(arr)))


def eliminate_random_elem(arr):
    arr.pop(random.randint(0, len(arr) - 1))
    return arr


def eliminate_items_with_letter(arr, sign):
    return list(filter(lambda x: sign not in x, arr))


def eliminate_items_without_letter(arr, sign):
    return list(filter(lambda x: sign in x, arr))


def extend_list_with_random_nums(arr):
    arr.append(random.randint(0, 100))
    return arr


def extend_list_with_random_nums_x_times(arr, x):
    for i in range(0, x):
        arr.append(random.randint(0, 100))
    return arr


def russian_roulette_list(arr):
    a = random.randint(0, 6)
    if a == 0:
        arr.clear()
    else:
        arr.append(a)
    return arr


def all_modulos(arr, num):
    return list(map(lambda x: x % num, arr))


def all_floor_divisions(arr, num):
    return list(map(lambda x: x // num, arr))

def round_divisions(arr, num):
    return list(map(lambda x: round(x/num), arr))


def get_hash_of_elems(arr):
    return list(map(lambda x: hash(x), arr))


def get_id_of_elems(arr):
    return list(map(lambda x: id(x), arr))


l = get_id_of_elems(arr_words)

print(l)
