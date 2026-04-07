# print(.1 + .2 == .3)
# print(f'.1 + .2 == {.1 + .2}')

from math import isclose

a: float = 1.5
b: float = 2.0

print(f'{a} == {b}?' , a == b)
print(f'{a} == {b}?', isclose(a, b, abs_tol=.001))
print(f'{a} == {b}?', isclose(a, b, rel_tol=.01))
print(f'{a} == {b}?', isclose(a, b, rel_tol=.01,abs_tol=1 ))