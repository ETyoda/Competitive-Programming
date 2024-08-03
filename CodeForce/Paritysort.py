def parity_sort(arr):
    evens = [x for x in arr if x % 2 == 0]
    odds = [x for x in arr if x % 2 != 0]
    return evens + odds

# Example usage:
arr = [3, 1, 2, 4, 7, 8, 6, 5]
sorted_arr = parity_sort(arr)
print(sorted_arr)
