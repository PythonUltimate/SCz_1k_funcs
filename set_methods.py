# set methods

var_set = {1, 4, None, 'ala', True}

my_set = {1, 4, 6, 7, 3, 8, 14, 46, 79}
my_set_2 = {1, 4, 5, 6, 7, 10, 15, 79}
my_set_3 = {1, 4, 96}

some_list = [2, 3, 5, 3, 4, 2, 1, 5]


def add_to_set(set, elem):
    set.add(elem)
    return set


def clear_set(set):
    set.clear()
    return set


def make_set_copy(set):
    b = set.copy()
    return b


def get_difference(set, set2):
    return set.difference(set2)


def leave_only_unique(set, set2):
    set.difference_update(set2)
    return set


def discard_elem(set):
    set.discard(1)
    return set


def get_intersection(set, set2):
    new = set.intersection(set2)
    return new


def get_intersection_from_many_sets(set, set2, set3):
    new = set.intersection(set2, set3)
    return new


def make_intersection_update(set, set2):
    set.intersection_update(set2)
    return set


def make_intersection_update_from_many_sets(set, set2, set3):
    set.intersection_update(set2, set3)
    return set


def check_if_disjoint(set, set2):
    return set.isdisjoint(set2)


def check_if_subset(set, set2):
    return set.issubset(set2)


def check_is_superset(set, set2):
    return set.issuperset(set2)


def remove_random_item(set):
    return set.pop()


def remove_specific_item(set, item):
    set.remove(item)
    return set


def get_diff_items(set, set2):
    return set.symmetric_difference(set2)


def update_with_diff_items(set, set2):
    set.symmetric_difference_update(set2)
    return set


def make_union_of_sets(set, set2):
    return set.union(set2)


def make_union_of_many_sets(set, set2, set3):
    return set.union(set2, set3)


def update_with_set(set, set2):
    set.update(set2)
    return set


def update_with_many_sets(set, set2, set3):
    set.update(set2, set3)
    return set


def get_len_of_set(set):
    return len(set)


def eliminate_duplicated_from_list(some_list):
    return list(set(some_list))


def check_if_item_in_set(set, item):
    return item in set


def check_types_set(set):
    for item in set:
        print(type(item))


def check_falsy_items(set):
    for item in set:
        print(bool(item))


s = check_falsy_items(var_set)
print(s)
