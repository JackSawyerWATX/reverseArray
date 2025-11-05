#!/bin/python3

def reverseArray(a):
    # Method 1: Using slicing (most Pythonic)
    return a[::-1]

# Test the function
if __name__ == '__main__':
    # Test cases
    test_arrays = [
        [1, 4, 3, 2],
        [5, 10, 15, 20, 25],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [42]
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"Test {i}:")
        print(f"Original: {arr}")
        reversed_arr = reverseArray(arr)
        print(f"Reversed: {reversed_arr}")
        print()