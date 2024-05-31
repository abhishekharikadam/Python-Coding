def merge_array(arrayA, arrayB):
    # Merge arrayA and arrayB
    # Remove duplicates
    # sort list in ascending order
    return sorted(set(arrayA + arrayB))


a = [1, 2, 3, 5, 8, 9]
b = [1, 4, 6, 10, 7, 3]
c = merge_array(a, b)
print(c)