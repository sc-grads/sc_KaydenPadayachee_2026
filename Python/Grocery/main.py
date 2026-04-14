import sys

def welcome_message() -> None:
    print('Welcome shoppers')
    print('Enter:')
    print('--------------------------')
    print('1 - Add a product')
    print('2 - Remove product')
    print('3 - Show all products')
    print('0 - Exit')
    print('--------------------------')


def add_item(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f'{item} added to the shoppers list')


def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f'{item} removed from the shoppers list')
    except ValueError:
        print(f'NO "{item}" found in: {groceries}')

def display(groceries: list[str]) -> None:
    print('____LIST_______')
    for i, item in enumerate(groceries, 1):
        print(f'{i}. {item.capitalize()}')

    print('_' * 10)

def is_an_option(text: str) -> bool:
    return text in ['1', '2', '3','0']

def main() -> None:
    groceries: list[str] = []

    welcome_message()
    while True:
        user_input: str = input('Choose: ').lower()

        if not is_an_option(user_input):
            print('Please choose a valid option...')
            continue

        if user_input == '1':
            new_item: str = input('What item would you like to add? >> ').lower()
            add_item(new_item, groceries)
        elif user_input == '2':
            item_to_removed: str = input('What item would you like to remove? >> ').lower()
            remove_item(item_to_removed, groceries)
        elif user_input == '3':
            display(groceries)
        elif user_input == '0':
            print('Exiting...')
            sys.exit()






if __name__ == '__main__':
    main()

