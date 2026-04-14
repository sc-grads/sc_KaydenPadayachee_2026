users: dict = {1 :'Bob', 2: 'Luigi'}
empty: dict = {}
print(users)
print(empty)

print(users[2])

#Dictionary inside another
weather: dict = {'time': '12:00',
                 'weather': {'morning': 'rain','evening': 'more rain'}}

print(weather['time'])
print(weather['weather'])
print(weather['weather']['morning'])

#key value pairs
users[3] = 'Mario'
print(users)
users[1]  = 'James'

users.pop(2)
print(users)