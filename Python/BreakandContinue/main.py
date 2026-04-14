number: int = 5

while number > 0:
    number -= 1

    if number == 2:
        print('Breaks at 2')
        break

    print(number)

print('Done')


#new work delete code sbove first
while number > 0:
    number -= 1

    if number == 2:
        print('Skips 2')
        continue

    print(number)

print('Done')

#new

total: int = 0

print('Welcome to calc+! Add positive numbers, or insert "0" to exit')
while True:
    user_input: int = int(input('Enter a number: '))

    if user_input < 0:
        print('!!! Please enter positive numbers only!!!')
        continue

    if user_input == 0:
        print(f'Total: {total}')
        break
    total += user_input



