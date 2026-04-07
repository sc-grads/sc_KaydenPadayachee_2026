def outer_func() -> None:
    name: str = ''
    value: int = 0

    def inner_func() -> None:
        nonlocal value, name
        name = 'Tom'
        value = 100

        inner_func()
        print(name, value)

# outer_func()