# Program to count the Number of Each Vowel using List and Dictionary Comprehension

a = "Harry Potter and the Prisoner of Azkaban"

vowels = "aeiou"

a = a.casefold()

count = {key : sum([1 for char in a if char == key]) for key in vowels}

print(count)