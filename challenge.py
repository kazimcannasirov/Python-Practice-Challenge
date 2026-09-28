numbers = [12, 5, 8, 12, 3, 5, 10, 8, 7, 2]

other_list = []

add = 0

largest = 0

for number in numbers:
    if number % 2 == 0 and number not in other_list:
        other_list.append(number)

for i in other_list:
    if i > largest:
        largest = i

print(largest)

for i1 in other_list:
    add = add + i1

print(add)

print(other_list)

print(f'Count: {len(other_list)}')
print(f'Sum: {add}')
print(f'Largest: {largest}')