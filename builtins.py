## Built in methods

iterable = ['ala', 'elo', 'nictam', '', '123']


class Elo:
    elo = 'tam'
    heja = 'bye'
    age = 90


def make_absolute_num(num):
    return abs(num)


def check_if_iterable_true(iterable):
    return all(iterable)


def check_if_any_iterable_true(iterable):
    return any(iterable)


def make_num_binary(num):
    return bin(num)


def make_bool(object):
    return bool(object)


def create_bytearray(object):
    return bytearray(object)


def create_bytes(object):
    return bytes(object)


def check_if_callable(object):
    return callable(object)


def check_unicode_char_from_num(sign):
    return chr(sign)


def create_complex_num(num1, num2):
    return complex(num1, num2)


def delete_attribute(object, attr):
    delattr(object, attr)
    return object


def get_attribute(object, attr):
    return getattr(object, attr)


def check_if_has_attribute(object, attr):
    return hasattr(Elo, 'elo')


def set_attribute(object, attr, new_value):
    setattr(Elo, attr, new_value)
    return object


def make_dictionary(**kwargs):
    return dict(**kwargs)


def get_methods(object):
    return dir(object)


def get_division_results(num1, num2):
    return divmod(num1, num2)


def enumerate_iterable(iterable):
    return enumerate(iterable)


def evaluate_text(txt5):
    return eval(txt5)


def execute_multiline_code(txt):
    return exec(txt)


def filter_truthies(iterable):
    x = filter(lambda x: bool(x), iterable)
    for elem in x:
        print(elem)
    return x

def filter_falsies(iterable):
    x = filter(lambda x: not bool(x), iterable)
    for elem in x:
        print(elem)
    return x


def filter_if_integers(iterable):
    new_list = filter(lambda x: type(x) == int, iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_if_string(iterable):
    new_list = filter(lambda x: type(x) == str, iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_in_len_gt_3(iterable):
    new_list = filter(lambda x: len(x) > 3, iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_if_lower_only(iterable):
    new_list = filter(lambda x: x.islower(), iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_if_upper_only(iterable):
    new_list = filter(lambda x: x.isupper(), iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_if_printable(iterable):
    new_list = filter(lambda x: x.isprintable(), iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_if_identifier(iterable):
    new_list = filter(lambda x: x.isidentifier(), iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_if_digits(iterable):
    new_list = filter(lambda x: x.isdigit(), iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_if_ascii(iterable):
    new_list = filter(lambda x: x.isascii(), iterable)
    for elem in new_list:
        print(elem)
    return new_list


def filter_callable(iterable):
    new_list = filter(check_if_callable, iterable)
    for elem in new_list:
        print(elem)
    return new_list


x = filter_falsies(iterable)

print(x)
