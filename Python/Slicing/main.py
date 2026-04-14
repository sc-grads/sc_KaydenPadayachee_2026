# numbers: list[int] = [1, 2, 3, 4, 5, 6]
# # print(numbers[0:3])
# # print(numbers[3:6])
# print(numbers[0:4:2])


# dont loop and modify
people: list[str] = ['Anna', 'Bob', 'Chris', 'David', 'Fred']
new_people: list[str] = []

for person in people:
    print(f'- {person}, {people.index(person)}')

    if person == 'Bob':
        print(f'Removing: {person}')
        continue

    new_people.append(person)

print(new_people)