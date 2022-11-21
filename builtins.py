## Built in methods
import math
import statistics

iterable = ['ala', 'elo', 'nictam', '   ', '123']
numeric_iterable = [45, 9, 62, 79, 3, 14]


class Elo:
    elo = 'tam'
    heja = 'bye'
    age = 90


class Ola(Elo):
    trele = 'morele'


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


def turn_into_float(num):
    return float(num)


def format_into_percent(num):
    return format(num, '%')


def format_into_decimal(num):
    return format(num, 'd')


def format_into_binary(num):
    return format(num, 'b')


def format_with_comma(num):
    return format(num, ',')


def format_with_underscore(num):
    return format(num, '_')


def create_frozenset(iterable):
    return frozenset(iterable)


def print_globals():
    return globals()


def make_hash(sign):
    return hash(sign)


def get_help():
    return help()


def get_hexadecimal_value(num):
    return hex(num)


def get_id_of_object(obj):
    return id(obj)


def get_some_input():
    return input('What to you want to say?')


def make_integer(num):
    return int(num)


def check_if_isinstance(obj, what):
    return isinstance(obj, what)


def check_if_subclass(obj, class_):
    return issubclass(obj, class_)


def return_iterator(iterable):
    return iter(iterable)


def get_len_of_obj(obj):
    return len(obj)


def make_list(obj):
    return list(obj)


def get_locals():
    return locals()


def map_to_id(iterable):
    new = map(id, iterable)
    for item in new:
        print(item)
    return new


def map_to_hash(iterable):
    new = map(hash, iterable)
    for item in new:
        print(item)
    return new


def map_to_square(iterable):
    new = map(lambda x: x ** 2, iterable)
    for item in new:
        print(item)
    return new


def map_to_square_root(iterable):
    new = map(math.sqrt, iterable)
    for item in new:
        print(item)
    return new


def map_to_exponential(iterable):
    new = map(math.exp, iterable)
    for item in new:
        print(item)
    return new


def map_to_factorial(iterable):
    new = map(math.factorial, iterable)
    for item in new:
        print(item)
    return new


def map_to_log(iterable):
    new = map(math.log, iterable)
    for item in new:
        print(item)
    return new


def map_to_len(iterable):
    new = map(len, iterable)
    for item in new:
        print(item)
    return new


def map_to_memoryview(iterable):
    new = map(memoryview, iterable)
    for item in new:
        print(item)
    return new


def get_min_item(iterable):
    return min(iterable)


def get_max_item(iterable):
    return max(iterable)


def create_empty_object():
    return object()


def map_to_octals(iterable):
    new = map(oct, iterable)
    for item in new:
        print(item)
    return new


def map_to_char(iterable):
    new = map(ord, iterable)
    for item in new:
        print(item)
    return new


def rise_ro_power(a, b):
    return pow(a, b)


def rise_to_power_with_modulo(a, b, c):
    return pow(a, b, c)


def print_arguments(*args):
    print(*args)


def create_sequence(num):
    x = range(num)
    return list(x)


def create_sequence_with_custom_start(start, stop):
    x = range(start, stop)
    return list(x)


def create_sequence_with_step(start, stop, step):
    x = range(start, stop, step)
    return list(x)


def get_reversed_iterator(iterable):
    new = reversed(iterable)
    for item in new:
        print(item)
    return new


def round_to_full_digit(num):
    return round(num)


def round_with_decimal_places(num, dec):
    return round(num, dec)


def create_set(args):
    return set(args)


def create_set_from_map(args):
    new_set = set(map(math.log, args))
    return new_set


def slice_list(iterable, num):
    a = slice(num)
    return iterable[a]


def slice_list_start_stop(iterable, start, stop):
    a = slice(start, stop)
    return iterable[a]


def slice_list_with_step(iterable, start, stop, step):
    a = slice(start, stop, step)
    return iterable[a]


def sort_list(iterable):
    return sorted(iterable)


def sort_list_reversed(iterable):
    return sorted(iterable, reverse=True)


def sort_list_key(iterable):
    return sorted(iterable, key=lambda x: x[-1])

x = sort_list_key(iterable)

print(x)
