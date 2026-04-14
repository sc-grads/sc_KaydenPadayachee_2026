age: int = 30

if age >= 21:
    print('You may enter the club')
else:
    print(' you are not allowed in')


weather: str = 'cloudy'
if weather == 'clear':
    print('Its a nice day')
elif weather == 'cloudy':
    print('The weather is terrible')
elif weather == 'rainy':
    print('What an awful day')
else:
    print('Unknown weather')

#new shorten code

number: int = 0

if number > 0:
    result: str = ' Above 0'
else:
    result: str = '0 and below'

    print(result)

result: str = ' Above 0' if number > 0 else '0 and below'
print(result)

#new
condition: bool = True
var: str = 'True' if condition else 'False'
print(var)

#
condition: bool = False
var: str = 'True' if condition else 'False'
print(var)

if condition:
    var: str = 'True'
else:
    var: str = 'False'

print(var)

