# Solution to find the number is divisible by 13 using lamba and filter function

l = [39, 48, 26, 98, 33, 66, 87]

result = list(filter(lambda x : x % 13 == 0, l))

print("The numbers divisible by 13 are:- ", result)