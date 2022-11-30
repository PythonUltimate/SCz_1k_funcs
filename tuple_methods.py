# tuple methods


tup = (13, 57, 98, 34, 9, 2, 90)

tup2 = ('ala', 'train', 'burrito', 'riots', 'flower')


def make_list(tup):
    return list(tup)


def make_dict(tup):
    return {key: None for key in tup}


def count_signs(tup, sign):
    return tup.count(sign)


def get_methods(tup):
    return dir(tup)


def get_hash(tup):
    return hash(tup)


def get_id(tup):
    return id(tup)


def get_index_value(tup, value):
    return tup.index(value)


def get_type(tup):
    return type(tup)


def get_num_of_elems(tup):
    return len(tup)


t = get_num_of_elems(tup2)
print(t)
