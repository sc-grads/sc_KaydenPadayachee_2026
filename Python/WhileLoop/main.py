

# important to know i because it will later turn to false once it gets to the end
import time


connected: bool = True

while connected:
    print('Using internet...')
    time.sleep(5)
    connected = False

print('Connection ended')


#new askes for user input

while True:
    user_input: str = input('You:')

    if user_input == 'Hello':
        print('Bot: Hey there!')
    else:
        print('Bot: Yes, that is interesting!')
