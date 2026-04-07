while True:
    user_input: str = input('Enter a number')

    try:
        number: float = float(user_input)
        print(f'You entered: {number}')
    except ValueError:
        print(f'The value you entered ("{user_input}" is not valid')
    except Exception as e:
        print('Program encounted a new exception')
        print(f'Type: {type(e)}')
        print(f'Error: {e}')
