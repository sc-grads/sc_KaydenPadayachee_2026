# def start_program(db: dict[int, str]) -> None:
#     assert db, 'Database is empty'
#
#     print('Loaded:', db)
#     print('Program started successfully')
#
# def main() -> None:
#     db1:dict[int, str] = {0: 'a', 1: 'b'}
#     start_program(db=db1)
#
#
# if __name__ == '__main__':
#     main()

#Unpacking
a,b = 5, 10

print(a, b)

a, *b, c = 'abcdef'
print(a, b, c)

*_, last = 'abcdef'
print(last)

def add(a: int, b: int) -> None:
    print(f'{a+b =}')


numbers: dict[str, int] = {'a': 5, 'b':10}
add(**numbers)