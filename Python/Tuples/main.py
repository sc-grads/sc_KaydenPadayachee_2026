coordinates: tuple = 1.5, 2.5
#coordinates:[0] =10
print(coordinates)

#new_tuple: tuple = ()
#print(type(new_tuple))

coordinates: tuple[float, float] = 1.5, 2.5
print(coordinates)

#Sets
elements: set = {99, True, 'Bob'}
print(elements)

#Add elements
elements.add('James')
print(elements)

#Remove elements
elements.remove('Bob')
print(elements)

#Pop
elements.pop()
print(elements)

#clear
elements.clear()
print(elements)

empty: tuple = tuple()

empty: set = set()
print(empty)
