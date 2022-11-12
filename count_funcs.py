
files = ['funcs_100.py', 'funcs_200.py']

counter = 0

for file in files:
    with open(file) as file_:
        data = file_.read()
        occurences = data.count('def')
        counter += occurences
        print(f'Number of functions in {file}: {occurences}')

print(f'Functions total: {counter}')

