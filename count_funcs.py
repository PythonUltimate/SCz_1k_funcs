
files = [
    'quik_maffs.py',
    'basic_economics.py',
    'converters.py',
    'string_methods.py',
    'builtins.py',
    'list_methods.py',
    'dict_methods.py',
    'tuple_methods.py',
    'set_methods.py',
    'datetime_funcs.py',
    'numpy_examples.py',
    'os_sys_modues.py',
]

counter = 0

for file in files:
    with open(file) as file_:
        data = file_.read()
        occurences = data.count('def')
        counter += occurences
        print(f'Number of functions in {file}: {occurences}')

print(f'Functions total: {counter}')

