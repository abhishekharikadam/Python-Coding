# Program to count the Number of Each Vowel using Dictionary

a = "Harry Potter and the Prisoner of Azkaban"

vowels = "aeiou"

a = a.casefold()
print(a)

count = {}.fromkeys(vowels, 0)

for char in a:
    if char in count:
        count[char] += 1

print(count)