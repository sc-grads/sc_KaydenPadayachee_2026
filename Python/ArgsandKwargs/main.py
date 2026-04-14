#*args
def add(*args: int) -> int:
    print(args)
    return sum(args)

print(add(1, 2, 3))


#Kwargs
def pin_postion(**kwargs: int) -> None:
    print(kwargs)

pin_postion(x=10, y=20)

def func(*args: str, **kwargs: int) -> None:
    print(args)
    print(kwargs)

func('a','b',default=20, a=1, b=2)