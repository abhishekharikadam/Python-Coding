# Program to remove 0 from the list and append that to the last

numbers = [1, 2, 3, 4, 0, 8, 9, 0, 6]

for num in numbers:
    if num == 00:
        numbers.remove(num)
        numbers.append(num)
print(numbers)