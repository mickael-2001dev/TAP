# ITERATE OVER A RANGE
for number in range(5):
    print(number)

print("---------------")

for number in range(2, 5):
    print(number)

print("---------------------")
# ITERATE OVER A SEQUENCE
sequence = ['One', 'Two', 'Five', 'Nine']

for value in sequence:
    print(value)

# Iterations

print("---------------------")

people = ['Jonas', 'Julio', 'Mike', 'Mez']
for position, person in enumerate(people):
    print(position, person)

#zip fuction
print("---------------------")
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']

for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)



print("---------------------")
people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']

for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)


print("---------------------")
# WHILE

n = 5
numbers = []

while n > 0:
    numbers.append(n)
    n = n -1

print(numbers)