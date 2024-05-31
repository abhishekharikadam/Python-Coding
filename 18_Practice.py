nums = range(0, 200)

def is_even(num):
    for i in range(2, num):
        if (num % i) == 0:
            return True
        return False

evens = list(filter(is_even, nums))
print(evens)