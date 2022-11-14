## String methods in Python

# first_name = input('What is your first name? ')
# last_name = input('Wht is your last name? ')
txt = 'Zyrafy wchodza do szafy\nPawiany wchodza na sciany'
txt1 = 'Zyrafy wchodza do szafy'
txt2 = 'Pawiany wchodza na sciany'


def concatenate(first_name, last_name):
    return first_name + last_name


def make_upper_case(first_name, last_name):
    return (first_name + last_name).upper()


def make_lower_case(first_name, last_name):
    return (first_name + last_name).lower()


def get_initials_upper_case(first_name, last_name):
    return (first_name[0] + last_name[0]).upper()


def get_initials_lower_case(first_name, last_name):
    return (first_name[0] + last_name[0]).lower()


def get_full_name(first_name, last_name):
    return " ".join([first_name.capitalize(), last_name.capitalize()])


def get_full_name_upper(first_name, last_name):
    return " ".join([first_name.upper(), last_name.upper()])


def get_full_name_lower(first_name, last_name):
    return " ".join([first_name.lower(), last_name.lower()])


def create_email(first_name, last_name):
    return ".".join([first_name.lower(), last_name.lower()]) + '@email.com'


def create_short_email(first_name, last_name):
    return ".".join([first_name[0].lower(), last_name.lower()]) + '@email.com'


def fill_name_to_10_chars(last_name):
    return last_name.zfill(10)


def create_email_10_chars(first_name, last_name):
    return ".".join([first_name.lower(), last_name.lower()]).zfill(10) + '@email.com'


def change_a_to_at(first_name):
    change = {65: 64, 97: 64}
    return first_name.translate(change)


def strip_inputs(first_name, last_name):
    return first_name.strip(), last_name.strip()


def rstrip_inputs(first_name, last_name):
    return first_name.rstrip(), last_name.rstrip()


def lstrip_inputs(first_name, last_name):
    return first_name.lstrip(), last_name.rstrip()


def inner_strip_inputs(first_name, last_name):
    return first_name.rstrip(), last_name.lstrip()


def check_if_starts_with_letter(first_name, letter):
    return first_name.startswith(letter)


def check_if_ends_with_letter(first_name, letter):
    return first_name.endswith(letter)


def split_them_lines(txt):
    return txt.splitlines()


def split_txt_space(txt):
    return txt.split()


def split_txt_a(txt):
    return txt.split('a')


def split_txt_a_occurencies(txt, occur):
    return txt.split('a', occur)


def rsplit_txt_space_occur(txt, occur):
    return txt.rsplit(" ", occur)


def partition_txt(txt, match):
    return txt.partition(match)


def rpartition_txt(txt, match):
    return txt.rpartition(match)


def partition_email(fn, match):
    return fn.partition(match)


def rjust_first_name(first_name):
    return first_name.rjust(20)


def rjust_first_name_x(first_name):
    return first_name.rjust(20, 'x')


def ljust_first_name(first_name, last_name):
    return first_name.ljust(30) + last_name


def separate_full_name(first_name, last_name):
    return first_name.ljust(5) + last_name.rjust(5)


def index_of_a(first_name, last_name, sign):
    return (first_name + last_name).index(sign)


def rindex_of_a(first_name, last_name, sign):
    return (first_name + last_name).rindex(sign)


def find_a(txt, sign):
    return (txt).find(sign)


def rfind_a(txt, sign):
    return (txt).rfind(sign)


def replace_a_with_at(fn, sign):
    return fn.replace(sign, "@")


def replace_szafy_with_elo(txt, sign, new_sign):
    return txt.replace(sign, new_sign)


def replace_first_occurence(txt, sign, new_sign, occur):
    return txt.replace(sign, new_sign, occur)


def join_items_with_space(txt1, txt2):
    return " ".join([txt1, txt2])


def join_items_with_nextline(txt1, txt2):
    return "\n".join([txt1, txt2])


def join_items_with_xox(txt1, txt2):
    return '  xox  '.join((txt1, txt2))


def check_if_txt_upper(txt1):
    return txt1.isupper()


def check_if_txt_capitalized(txt):
    return txt.istitle()


def check_if_all_spaces(txt):
    return txt.isspace()


def check_if_is_printable(txt):
    return txt.isprintable()


def check_if_all_are_numeric(txt):
    return txt.isnumeric()


def check_if_txt_lower(txt):
    return txt.islower()


def check_if_identifier(txt):
    return txt.isidentifier()


def check_if_txt_digits(txt):
    return txt.isdigit()


def check_if_all_decimals(txt):
    return txt.isdecimal()


print(check_if_all_decimals('123a'))

print(dir(str))
