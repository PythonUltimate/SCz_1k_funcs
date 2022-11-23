## List methods in Python

import copy

arr_num = [23, 87, 4, 70, 5, 9, -32, 87]
arr_words = ['ala', 'wszy', 'kromka', 'nic', 'trelemorele']
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
    return arr


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


l = get_number_of_elems(arr_num)

print(l)
