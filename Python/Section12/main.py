numbers: list[int] = list(range(1, 21))
print(numbers)

def is_even(number: int) -> bool:
    return number % 2 == 0

even_numbers: filter = filter(lambda n: n % 2 == 0, numbers)
print(even_numbers)
print(list(even_numbers))

#map
numbers: list[int] = [1, 2, 3, 4, 5]

def double(number: int) -> int:
    return number * 2

# doubled: map = map(lambda n: n * 2, numbers)
# print(doubled)
# print(list(doubled))

doubled: list[int] = [double(n) for n in numbers]
print(doubled)

#sorted

numbers: list[int] = [1, 10, 5, 3]
sorted_numbers: list[int] = sorted(numbers)
print(sorted_numbers)

people: list[str] = ['Mario,','James', 'Anna']