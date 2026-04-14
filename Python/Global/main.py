# var: int = 10
#
# def func() -> None:
#     print(var)
#
#     def func2() -> None:
#         inner_var = 1
#         print(var)
#
#         def func3() -> None:

number: int = 0

def change_number() -> None:
    global number
    number = 10

# print(number)
# change_number()
# print(number)

def inner_func() -> None:
    global number
    number = 10