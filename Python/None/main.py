no_value: None = None
print(no_value)
print(type(no_value))

users: dict = {1: 'Mario', 2: 'Luigi'}
print(users.get(3))


possible_user: str | None = users.get(3)
possible_user: str | None = users.get(2)
print(possible_user)
