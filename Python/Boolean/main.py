is_connected: bool = True
has_money: bool = False

print(10 > 5)

print(int(True))
print(int(False))

if is_connected:
    print('Is there internet!')

#List
my_list: list = [1, True, 'true', [1,2,3]]

people: list[str] = ['Bob', 'Alice', 'Tom']
print(people[0])
#or you want to print the list
print('Original', people)

# Append
people.append('Jeremy')
print(people)


#Remoove
people.remove('Bob')
print(people)
#pop
people.pop()
print(people)

people[0] = 'Kaydne'
print(people)

people.insert(1, "Timothy")
print(people)

#clear

people.clear()
print(people)
