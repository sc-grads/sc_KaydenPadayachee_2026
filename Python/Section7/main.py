# print(bool([]))
# print(bool(None))
# print(bool(200))

users: dict = {1: 'Mario', 2: 'Luigi', 3: 'James'}

if users:
    for k, v in users.items():
        print(k, v, sep=': ')
else:
        print('No data found')